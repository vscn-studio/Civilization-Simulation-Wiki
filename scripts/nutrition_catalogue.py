"""Resolve concrete food variants and recipe previews without publishing local provenance.

Static previews implement the verified Seraph composition rules. Arbitrary stack metadata,
code mod asset mutations and server-specific patch order are not claimed to be reproduced.
"""
import copy
import itertools
import json
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

RETENTION = {'calciumMg': 1, 'ironMg': 1, 'zincMg': 1, 'vitaminAUgRAE': .8,
             'vitaminCMg': .5, 'b1Mg': .7, 'b6Mg': .8, 'folateUgDFE': .7, 'b12Ug': .8}
DAILY = {'calciumMg': 1000, 'ironMg': 12, 'zincMg': 11, 'vitaminAUgRAE': 900,
         'vitaminCMg': 90, 'b1Mg': 1.2, 'b6Mg': 1.7, 'folateUgDFE': 400, 'b12Ug': 2.4}
MACROS = ('carbohydrate', 'protein', 'fat', 'fiber')
HEATED = ('raw', 'milled', 'dough', 'juice', 'ground', 'pickled', 'soaked')


def get(obj, key, default=None):
    if not isinstance(obj, dict): return default
    return next((v for k, v in obj.items() if k.lower() == key.lower()), default)


@lru_cache(maxsize=16384)
def pattern_regex(pattern):
    try:
        return re.compile(pattern[1:] if pattern.startswith('@') else
                          re.escape(pattern).replace(r'\*', '.*').replace(r'\?', '.'))
    except re.error:
        return None


def matches(code, pattern):
    regex = pattern_regex(pattern)
    return regex is not None and regex.fullmatch(code) is not None


def qualify(code, domain):
    return code if ':' in code else domain + ':' + code


def expand_variants(obj, domain, worldprops):
    base = get(obj, 'code', '')
    if not isinstance(base, str): return [], ['invalid code']
    variants = [('', {})]
    added, unresolved = [], []
    for group in get(obj, 'variantgroups', []):
        states = get(group, 'states')
        key = get(group, 'code')
        loads = get(group, 'loadFromPropertiesCombine')
        load = get(group, 'loadFromProperties', get(group, 'loadFrom'))
        if loads or load:
            states = []
            for loc in loads or [load]:
                dom, name = qualify(loc, domain).split(':', 1)
                prop = worldprops.get((dom, name), {})
                key = key or get(prop, 'code')
                states.extend(get(v, 'code') for v in get(prop, 'variants', []))
        if not key or not states or not all(isinstance(s, str) for s in states):
            unresolved.append(group)
            continue
        combine = str(get(group, 'combine', 'multiply')).lower()
        if combine == 'add':
            added.extend(('-' + s, {key: s}) for s in states)
        elif combine == 'multiply':
            if len(variants) * len(states) > 100000:
                unresolved.append(group)
                continue
            variants = [(suffix + '-' + s, dict(values, **{key: s}))
                        for suffix, values in variants for s in states]
        else:
            unresolved.append(group)  # Never silently turn selective multiplication into a cartesian product.
    if unresolved: return [], unresolved
    if added and variants == [('', {})]: variants = []
    result = []
    for suffix, values in variants + added:
        code = base + suffix
        if any(matches(code, p) for p in get(obj, 'skipVariants', [])): continue
        allow = get(obj, 'allowedVariants', [])
        if allow and not any(matches(code, p) for p in allow): continue
        result.append((code, values))
    return result, []


def merge(left, right):
    if isinstance(left, dict) and isinstance(right, dict):
        out = copy.deepcopy(left)
        for k, v in right.items():
            old = next((x for x in out if x.lower() == k.lower()), k)
            out[old] = merge(out[old], v) if old in out else copy.deepcopy(v)
        return out
    if isinstance(left, list) and isinstance(right, list): return left + copy.deepcopy(right)
    return copy.deepcopy(right)


def resolve(obj, code, variants):
    if isinstance(obj, str):
        for k, v in variants.items(): obj = obj.replace('{' + k + '}', v)
        return obj
    if isinstance(obj, list): return [resolve(x, code, variants) for x in obj]
    if not isinstance(obj, dict): return obj
    out = {k: copy.deepcopy(v) for k, v in obj.items() if not k.lower().endswith('bytype')}
    for k, branches in obj.items():
        if not k.lower().endswith('bytype') or not isinstance(branches, dict): continue
        target = next((x for x in out if x.lower() == k[:-6].lower()), k[:-6])
        for pattern, value in branches.items():
            if matches(code, pattern):
                out[target] = merge(out[target], value) if target in out else copy.deepcopy(value)
                break
    return {k: resolve(v, code, variants) for k, v in out.items()}


def profile_for(code, config):
    candidates = []
    for i, profile in enumerate(config['Foods']):
        scores = [len(p) - 1 if p.endswith('*') else 10000 + len(p)
                  for p in profile['Codes'] if code.startswith(p[:-1]) if p.endswith('*')]
        scores += [10000 + len(p) for p in profile['Codes'] if code == p]
        if scores: candidates.append((max(scores), -i, profile, i))
    return max(candidates, key=lambda x: (x[0], x[1]))[2:] if candidates else (None, None)


def composition(profile, native=None, liquid=False, mapped=True, cooked=False):
    """One item or one litre, with normalization and effective micronutrient amounts."""
    p = profile
    energy = sum(p.get('Per100G', {}).get(k, 0) * factor for k, factor in
                 [('carbohydrate', 16.736), ('protein', 16.736), ('fat', 37.656)])
    portion = p.get('PortionG', 0) or (get(native, 'satiety', 0) * 418.4 / energy if energy else 0)
    mass = 1000 * p.get('Density', 1) if liquid and mapped else portion
    if mass <= 0: return None
    water = mass * p.get('WaterGPer100G', 0) / 100
    values = {k: v * mass / 100 for k, v in p.get('Per100G', {}).items() if k in MACROS}
    total = sum(values.values())
    if total > max(0, mass - water) and total:
        values = {k: v * max(0, mass - water) / total for k, v in values.items()}
    alcohol = p.get('AlcoholGPer100G', 0) or 0
    values['fiber'] = min(values.get('fiber', 0), max(0, mass - water - sum(values.get(k, 0) for k in MACROS[:3]) - alcohol * mass / 100))
    values['energy'] = sum(values.get(k, 0) * f for k, f in [('carbohydrate', 16.736), ('protein', 16.736), ('fat', 37.656)])
    values['water'] = water
    values['alcohol'] = alcohol * mass / 100
    values['sodium'] = p.get('SodiumMgPer100G', 0) * mass / 100
    values['potassium'] = p.get('PotassiumMgPer100G', 0) * mass / 100
    values['electrolytes'] = (values['sodium'] + values['potassium']) / 1000 * .8
    if not values['electrolytes']: values['electrolytes'] = p.get('Per100G', {}).get('electrolytes', 0) * mass / 100
    if mapped:
        for key, value in p.get('MicroPer100G', {}).items():
            values[key] = value * mass / 100 * p.get('MicroReserveScale', {}).get(key, 1)
            if cooked and p.get('Preparation') in HEATED: values[key] *= RETENTION.get(key, 1)
    return {'mass': mass, 'values': values}


def scale(dose, quantity):
    return {'mass': dose['mass'] * quantity, 'values': {k: v * quantity for k, v in dose['values'].items()}}


def combine(doses):
    # Unknown micronutrients stay unknown when even one ingredient is unmeasured.
    keys = set.intersection(*(set(d['values']) for d in doses))
    return {'mass': sum(d['mass'] for d in doses),
            'values': {k: sum(d['values'][k] for d in doses) for k in keys}}


def cooked_dose(row, config):
    profile = row.get('_profile')
    if not profile: return row.get('dose')
    ref = profile.get('CookedReference')
    prepared = next((p for p in config['Foods'] if ref in p['Codes']), None) if ref else None
    dose = composition(prepared or profile, row.get('_mealNative') or row.get('_native'), row['kind'] == 'liquid', row['coverage'] != 'fallback', True)
    return scale(dose, profile.get('CookedQuantityScale', 1)) if prepared and dose else dose


def readable(code, kind, langs):
    domain, path = code.split(':', 1)
    for typ in [kind, 'block' if kind == 'item' else 'item']:
        key = typ + '-' + path
        if (domain, key) in langs: return re.sub('<[^>]+>', '', langs[(domain, key)])
        # Language assets also provide wildcard item names (e.g. orientation variants).
        for (dom, pattern), text in langs.items():
            if dom == domain and '*' in pattern and matches(key, pattern): return re.sub('<[^>]+>', '', text)
    return path


def patch_assets(parsed, manifest, audit=None):
    """Apply ordinary JSON asset patches with enabled/dependency checks, before variant resolution."""
    assets = {}
    for a in parsed:
        parts = a['file'].replace('\\', '/').split('/')
        if 'assets' not in parts: continue
        path = '/'.join(parts[parts.index('assets') + 2:])
        assets[a['domain'] + ':' + path] = dict(a, data=copy.deepcopy(a['data']))
    installed = {x['id'].lower() for x in manifest} | {'game', 'survival', 'creative'}
    applied, pending, skipped = 0, 0, 0
    for a in parsed:
        if '/patches/' not in a['file']: continue
        for patch in a['data'] if isinstance(a['data'], list) else [a['data']]:
            if not isinstance(patch, dict) or not isinstance(patch.get('file'), str): continue
            if patch.get('enabled') is False: continue
            deps = patch.get('dependsOn', [])
            if any((d.get('modid', '').lower() in installed) == bool(d.get('invert', False)) for d in deps):
                skipped += 1
                continue
            target = qualify(patch['file'], a['domain'])
            targets = [key for key in assets if matches(key, target)] if '*' in target else [target] if target in assets else []
            for key in targets:
                if not any(':' + part + '/' in key for part in ('itemtypes', 'blocktypes', 'worldproperties', 'recipes')): continue
                relevant = bool(re.search('nutrition|inPieProperties|variantgroups', json.dumps(patch), re.I))
                if patch.get('condition') or patch.get('dependsOnConfig'):
                    if relevant: pending += 1
                    continue
                candidate = copy.deepcopy(assets[key]['data'])
                try:
                    path = [p.replace('~1', '/').replace('~0', '~') for p in patch.get('path', '').strip('/').split('/')]
                    parent = candidate
                    for part in path[:-1]: parent = parent[int(part)] if isinstance(parent, list) else parent[part]
                    leaf = path[-1]
                    op = patch.get('op', '').lower()
                    value = copy.deepcopy(patch.get('value'))
                    if isinstance(parent, list):
                        index = len(parent) if leaf == '-' else int(leaf)
                        if op == 'add': parent.insert(index, value)
                        elif op == 'addeach': parent[index:index] = value
                        elif op == 'replace': parent[index] = value
                        elif op == 'remove': del parent[index]
                        elif op == 'addmerge':
                            if index == len(parent): parent.append(value)
                            else: parent[index] = merge(parent[index], value)
                        else: raise ValueError(op)
                    elif op in ('add', 'replace'): parent[leaf] = value
                    elif op == 'addmerge': parent[leaf] = merge(parent[leaf], value) if leaf in parent else value
                    elif op == 'remove': del parent[leaf]
                    else: raise ValueError(op)
                    assets[key]['data'] = candidate
                    if relevant: applied += 1
                except (KeyError, IndexError, ValueError, TypeError) as exc:
                    if relevant: pending += 1
                    if relevant and audit is not None: audit.append({'mod': a['mod'], 'target': key, 'patch': patch, 'error': str(exc)})
    return list(assets.values()), dict(applied=applied, pending=pending, skippedDependencies=skipped)


def build_catalogue(parsed, config, manifest):
    parsed, patch_summary = patch_assets(parsed, manifest)
    langs, worldprops = {}, {}
    for locale in ('en', 'zh-cn'):
        for a in parsed:
            if a['file'].lower().endswith('/lang/' + locale + '.json') and isinstance(a['data'], dict):
                for k, v in a['data'].items():
                    if isinstance(v, str):
                        dom, key = k.split(':', 1) if ':' in k else (a['domain'], k)
                        langs[(dom, key)] = v
    for a in parsed:
        if '/worldproperties/' in a['file'] and isinstance(a['data'], dict):
            worldprops[(a['domain'], a['file'].split('/worldproperties/', 1)[1][:-5])] = a['data']
    rows, seen, unresolved, patchmods = [], set(), [], set()
    # Make asset-defined branches explicit; patches are counted as unresolved overlays below.
    for a in parsed:
        if '/patches/' in a['file'] and re.search('nutrition|inPieProperties|variantgroups', json.dumps(a['data']), re.I): patchmods.add(a['mod'])
        kind = 'item' if '/itemtypes/' in a['file'] else 'block' if '/blocktypes/' in a['file'] else None
        if not kind: continue
        for obj in a['data'] if isinstance(a['data'], list) else [a['data']]:
            if not isinstance(obj, dict) or get(obj, 'enabled') is False: continue
            # Restrict expansion to food-bearing resources, including recipe ingredients such as dough.
            base = qualify(get(obj, 'code', ''), a['domain'])
            calibrated_family = any(code == base or code.startswith(base + '-') or
                                    (code.endswith('*') and base.startswith(code[:-1]))
                                    for p in config['Foods'] for code in p['Codes'])
            if not calibrated_family and not re.search('nutrition|inPieProperties', json.dumps(obj), re.I): continue
            variants, missing = expand_variants(obj, a['domain'], worldprops)
            if missing:
                unresolved.append(qualify(get(obj, 'code', 'unknown'), a['domain']))
                continue
            for path, variables in variants:
                code = qualify(path, a['domain'])
                if (kind, code) in seen: continue
                seen.add((kind, code))
                resolved = resolve(obj, path, variables)
                attrs = get(resolved, 'attributes', {}) or {}
                if get(get(attrs, 'handbook', {}), 'exclude') is True: continue
                creative = get(resolved, 'creativeinventory', {}) or {}
                visible = any(matches(path, pattern) for patterns in creative.values()
                              for pattern in patterns) if isinstance(creative, dict) else False
                if not visible and not get(resolved, 'creativeInventoryStacks') and not get(get(attrs, 'handbook', {}), 'include', False): continue
                native = get(resolved, 'nutritionProps')
                meal_native = get(attrs, 'nutritionPropsWhenInMeal', get(resolved, 'nutritionPropsWhenInMeal'))
                liquid = get(attrs, 'waterTightContainerProps', {}) or {}
                units = get(liquid, 'itemsPerLitre', 0)
                is_liquid = isinstance(units, (int, float)) and units > 0
                if is_liquid:
                    perlitre = get(liquid, 'nutritionPropsPerLitre')
                    if perlitre: native = perlitre
                    elif native:
                        native = dict(native)
                        native['satiety'] = get(native, 'satiety', 0) * units
                    meal_native = get(liquid, 'nutritionPropsPerLitreWhenInMeal', meal_native)
                p, index = profile_for(code, config)
                cooking_water = code == 'game:waterportion'
                if not cooking_water and any(code.startswith(x[:-1]) if x.endswith('*') else code == x for x in config.get('Exclusions', {})): continue
                if cooking_water:
                    p = dict(PortionG=1000, Density=1, WaterGPer100G=100, Preparation='liquid', Coverage='recipe',
                             Per100G={k: 0 for k in MACROS}, MicroPer100G={k: 0 for k in DAILY})
                category = get(native or meal_native, 'foodcategory', 'Unknown')
                coverage = p.get('Coverage', 'reference') if p else 'fallback'
                if p is None and get(native or meal_native, 'satiety', 0) > 0:
                    p = config.get('CategoryBaselines', {}).get(category)
                    if p is None:
                        p = {'PortionG': get(native or meal_native, 'satiety', 0) / 4, 'Per100G': {'carbohydrate': 100}, 'Preparation': 'unknown'}
                if p is None: continue
                dose = composition(p, native or meal_native, is_liquid, index is not None or cooking_water)
                if not dose: continue
                row = dict(id=kind + ':' + code, code=code, name=readable(code, kind, langs), mod=a['mod'],
                           modName=a['modName'], category=category, kind='liquid' if is_liquid else 'food',
                           preparation=p.get('Preparation', 'unknown'), coverage=coverage,
                           basis='litre' if is_liquid else 'item', edible=native is not None,
                           satiety=get(native, 'satiety'), health=get(native, 'health'),
                           profile=index, dose=dose, _profile=p, _native=native, _mealNative=meal_native,
                           _pie=get(attrs, 'inPieProperties'), _resolved=resolved)
                row['cookedDose'] = cooked_dose(row, config)
                if cooking_water:
                    row.update(name='清水（烹饪用）', edible=False, cookedDose=dose,
                               note='烹饪用水按实际升数计入质量与水分。直接饮水的水质、病原与矿物质另行处理。')
                if row['_pie']:
                    row['pie'] = dict(role=get(row['_pie'], 'partType', '').lower(),
                                      mixing=get(row['_pie'], 'allowMixing', True),
                                      mixingCodes=get(row['_pie'], 'mixingCodes', []),
                                      category=get(row['_pie'], 'foodCategory', category))
                if code.startswith('butchering:sausage-') and any(part in code for part in ('bloodsausage', 'blackpudding')):
                    row['note'] = '此处是默认配方；游戏中实际制作会记录所用配料，成品营养可能不同。'
                row['perishable'] = 'perish' in json.dumps(resolved).lower()
                rows.append(row)
    # Exact configured foods lacking nutrition-bearing JSON still include legitimate recipe inputs.
    # They are not fabricated as installed edible items; the complete profile list remains separate.
    base_rows = list(rows)
    crusts = [r for r in base_rows if get(r['_pie'], 'partType', '').lower() == 'crust']
    fillings = [r for r in base_rows if get(r['_pie'], 'partType', '').lower() == 'filling']
    for crust, filling in itertools.product(crusts, fillings):
        mix = get(filling['_pie'], 'allowMixing', True)
        mixing_codes = get(filling['_pie'], 'mixingCodes', [])
        if mix and not mixing_codes and filling['category'] in ('Unknown', 'NoNutrition'): continue
        if not mix and mixing_codes: continue
        for covered in (False, True):
            if covered and not get(crust['_pie'], 'allowMixing', True): continue
            for stage, label, level in [('raw', '生派', 0), ('partbaked', '半熟派', 1), ('baked', '烤熟派', 2), ('charred', '烤焦派', 3)]:
                dough = scale(crust['cookedDose'] if level >= 2 else crust['dose'], 4 if covered else 2)
                fill = scale(filling['cookedDose'] if level >= 2 else filling['dose'], 8)
                if level:
                    dry = max(0, dough['mass'] - dough['values']['water'])
                    limit = {1: .5, 2: .327, 3: .2}[level]
                    water = min(dough['values']['water'], dry * limit / (1 - limit))
                    dough['values']['water'] = water
                    dough['mass'] = dry + water
                dose = scale(combine([dough, fill]), .25)
                rows.append(dict(id='pie:' + crust['code'] + ':' + filling['code'] + ':' + str(int(covered)) + ':' + stage,
                    code='game:pie-' + {'baked': 'perfect'}.get(stage, stage),
                    name=filling['name'] + ' · ' + crust['name'] + ' · ' + ('带顶皮' if covered else '敞口') + label,
                    mod='game', modName='原版', ingredientMods=sorted({crust['mod'], filling['mod']}),
                    category=filling['category'], kind='pie', preparation=stage, coverage='recipe',
                    basis='slice', edible=level > 0, perishable=True, dose=dose,
                    ingredients=[{'id': crust['id'], 'code': crust['code'], 'name': crust['name'], 'quantity': 4 if covered else 2},
                                 {'id': filling['id'], 'code': filling['code'], 'name': filling['name'], 'quantity': 8}],
                    note='配料数量为整派用量；营养按四分之一派显示。'))
    by_code = {r['code']: r for r in base_rows}
    # Keep all valid cooking choices for a constrained, on-demand meal calculator.
    meal_recipes = []
    for a in parsed:
        if '/recipes/cooking/' not in a['file']: continue
        for recipe in a['data'] if isinstance(a['data'], list) else [a['data']]:
            if not isinstance(recipe, dict) or get(recipe, 'enabled') is False: continue
            if get(recipe, 'cooksInto'): continue
            roles = []
            for role in get(recipe, 'ingredients', []):
                options = {}
                for stack in get(role, 'validStacks', []):
                    pattern = qualify(get(stack, 'code', ''), a['domain'])
                    for row in base_rows:
                        if not matches(row['code'], pattern): continue
                        if not row['id'].startswith(get(stack, 'type', 'item').lower() + ':'): continue
                        # Cooking recipes specify count per ingredient slot and litres separately.
                        quantity = get(stack, 'stackSize', get(stack, 'quantity', 1))
                        if row['kind'] == 'liquid': quantity *= get(role, 'portionSizeLitres', 1)
                        if isinstance(quantity, (int, float)) and quantity > 0:
                            options[row['id']] = {'id': row['id'], 'quantity': quantity}
                roles.append(dict(code=get(role, 'code', ''), name=get(role, 'typeName', get(role, 'code', '')),
                                  min=get(role, 'minQuantity', 0), max=get(role, 'maxQuantity', 1),
                                  options=list(options.values())))
            if roles and all(r['options'] for r in roles if r['min'] > 0):
                code = qualify(get(recipe, 'code', ''), a['domain'])
                name = langs.get((a['domain'], 'mealrecipe-name-' + get(recipe, 'code', '')))
                meal_recipes.append(dict(code=code, name=name or get(recipe, 'code', ''), mod=a['mod'], roles=roles))
    for row in base_rows:
        resolved = row['_resolved']
        transitions = []
        def walk(obj, pointer=''):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    yield k, v, pointer
                    yield from walk(v, pointer + '/' + k)
            elif isinstance(obj, list):
                for v in obj: yield from walk(v, pointer)
        for key, value, pointer in walk(resolved):
            if key.lower() not in ('smeltedstack', 'groundstack', 'transitionedstack', 'resultcode', 'liquidstack', 'pressedstack'): continue
            target = get(value, 'code') if isinstance(value, dict) else value
            if not isinstance(target, str): continue
            code = qualify(target, row['code'].split(':')[0])
            if code not in by_code: continue
            action = {'smeltedstack': '加热', 'groundstack': '研磨', 'transitionedstack': '保存／转化',
                      'resultcode': '烘焙', 'liquidstack': '榨汁', 'pressedstack': '压榨残渣'}[key.lower()]
            transitions.append({'id': by_code[code]['id'], 'name': by_code[code]['name'], 'action': action})
        if transitions: row['transitions'] = list({x['id']: x for x in transitions}.values())
    for row in rows:
        for key in list(row):
            if key.startswith('_'): del row[key]
        for field in ('dose', 'cookedDose'):
            if row.get(field):
                row[field]['mass'] = round(row[field]['mass'], 8)
                row[field]['values'] = {k: round(v, 8) for k, v in row[field]['values'].items()}
    rows.sort(key=lambda r: (r['kind'], r['mod'], r['id']))
    return dict(version=1, rows=rows, mealRecipes=meal_recipes,
                counts=dict(records=len(rows), items=len(base_rows), pies=len(rows)-len(base_rows),
                            mods=len({r['mod'] for r in base_rows}), profiles=len(config['Foods']),
                            fallback=sum(r['coverage'] == 'fallback' for r in base_rows), mealRecipes=len(meal_recipes)),
                coverage=dict(unresolvedVariants=sorted(set(unresolved)), patchMods=sorted(patchmods),
                              patches=patch_summary,
                              runtime='静态食物与配方预览；服务器补丁、附加模组动态物品和实际配料元数据可能改变结果。'),
                retention=RETENTION, daily=DAILY)


def compact_catalogue(catalogue):
    """Store shared ingredients once; reconstruct the exact pie previews in the browser."""
    result = dict(catalogue)
    result['rows'] = [r for r in catalogue['rows'] if r['kind'] != 'pie']
    indexes = {r['id']: i for i, r in enumerate(result['rows'])}
    result['pieVariants'] = [[indexes[r['ingredients'][0]['id']], indexes[r['ingredients'][1]['id']],
                              int(r['ingredients'][0]['quantity'] == 4),
                              ['raw', 'partbaked', 'baked', 'charred'].index(r['preparation'])]
                             for r in catalogue['rows'] if r['kind'] == 'pie']
    return result


if __name__ == '__main__':
    from local_inputs import source_dir
    root = Path(__file__).resolve().parent.parent
    source = source_dir('SERAPH_SURVIVAL_SOURCE', 'Seraph Living Survival Simulation')
    result = build_catalogue(json.loads((root/'scripts/generated/nutrition-assets.json').read_text(encoding='utf-8')),
                             json.loads((source/'assets/vsslssmod/config/foods.json').read_text(encoding='utf-8-sig')),
                             json.loads((root/'scripts/inventory-manifest.json').read_text(encoding='utf-8')))
    (root/'docs/public/data/nutrition-catalogue.json').write_text(json.dumps(compact_catalogue(result), ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(json.dumps(result['counts'], ensure_ascii=False))
