# -*- coding: utf-8 -*-
from local_inputs import required_dir, source_dir
"""Read installed JSON/JSON5 assets. Preserve conditions; never simulate DLL/patch load order."""
import collections, hashlib, html, itertools, json, os, re, subprocess, zipfile
from functools import lru_cache
from pathlib import Path
from wiki_content import write_generated
from public_content import public_food_data
from recipe_presentation import display_name, recipe_summary
from nutrition_catalogue import build_catalogue, expand_variants, compact_catalogue

ROOT = Path(__file__).resolve().parent.parent
GAME = required_dir('SERAPH_GAME_DIR')
PACK = required_dir('SERAPH_MODS_DIR')
SURV = source_dir('SERAPH_SURVIVAL_SOURCE', 'Seraph Living Survival Simulation')
MANIFEST = json.loads((ROOT/'scripts/inventory-manifest.json').read_text(encoding='utf-8-sig'))

def esc(value):
    return html.escape(str(value), quote=False).replace('|', '&#124;').replace('\r','').replace('\n','<br>').replace('`','&#96;').replace('{{','&#123;&#123;')

def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'))

def write(path, text):
    p = ROOT/path
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.suffix == '.md': write_generated(p,text)
    else: p.write_text(text, encoding='utf-8')

def parse_many(texts):
    p = subprocess.run(['node', str(ROOT/'scripts/parse-json5.mjs')], input=json.dumps(texts, ensure_ascii=False),
                       capture_output=True, encoding='utf-8', check=True)
    return json.loads(p.stdout)

def selected(name):
    n = '/'+name.lower().replace('\\','/')
    return n.endswith('.json') and any('/'+part+'/' in n for part in
        ['itemtypes','blocktypes','recipes','patches','lang','worldproperties','config/handbook'])

def package_files(entry):
    # Core survival documentation and its composition model must use the same current assets.
    if entry['id'] == 'vsslssmod':
        return [(f.relative_to(SURV).as_posix(), f.read_bytes())
                for f in sorted((SURV/'assets').rglob('*.json')) if selected(f.as_posix())]
    p = PACK/entry['file']
    if p.is_dir():
        return [(f.relative_to(p).as_posix(),f.read_bytes()) for f in sorted(p.rglob('*.json')) if selected(f.as_posix())]
    with zipfile.ZipFile(p) as z:
        return [(n,z.read(n)) for n in sorted(z.namelist()) if selected(n)]

def walk(value, path=''):
    yield path,value
    if isinstance(value,dict):
        for k,v in value.items(): yield from walk(v,path+'/'+str(k))
    elif isinstance(value,list):
        for i,v in enumerate(value): yield from walk(v,path+'/'+str(i))

@lru_cache(maxsize=4096)
def compiled_pattern(pattern):
    if pattern.startswith('@'):
        try: return re.compile(pattern[1:])
        except re.error: return None
    return re.compile(re.escape(pattern).replace(r'\*','.*').replace(r'\?','.'))

def match(code, pattern):
    if not pattern.startswith('@') and '*' not in pattern and '?' not in pattern: return code==pattern
    compiled=compiled_pattern(pattern)
    return compiled is not None and bool(compiled.fullmatch(code))

def translated(key, domain, langs):
    if not isinstance(key,str): return compact(key)
    if ':' in key: dom,k=key.split(':',1)
    else: dom,k=domain,key
    return langs.get((dom,k), langs.get((dom,dom+':'+k), langs.get(('game',k),key)))

def plain_rich(text):
    text=re.sub(r'<(?:br\s*/?|/?p|/?h[1-6]|/?li)[^>]*>', '\n',str(text),flags=re.I)
    # Preserve inline item references as readable codes, without rendering game markup as HTML.
    text=re.sub(r'<(?:itemstack|a)\b[^>]*(?:code|href)=["\']([^"\']+)["\'][^>]*>',r' [\1] ',text,flags=re.I)
    return html.unescape(re.sub('<[^>]+>','',text))

def main():
    raw=[]
    for f in sorted((GAME/'assets').rglob('*.json')):
        name='assets/'+f.relative_to(GAME/'assets').as_posix()
        if selected(name): raw.append(('game','原版',name,f.read_bytes()))
    for entry in MANIFEST:
        raw.extend((entry['slug'],entry['name'],n,b) for n,b in package_files(entry))
    parsed=[]; errors=[]
    for offset in range(0,len(raw),250):
        batch=raw[offset:offset+250]
        results=parse_many([b.decode('utf-8-sig',errors='replace') for _,_,_,b in batch])
        for (slug,name,path,b),r in zip(batch,results):
            if 'error' in r: errors.append({'mod':slug,'file':path,'error':r['error']}); continue
            parts=path.replace('\\','/').split('/')
            domain=parts[parts.index('assets')+1] if 'assets' in parts else slug
            if slug=='game' and domain in ('survival','creative'): domain='game'
            parsed.append(dict(mod=slug,modName=name,file=path,domain=domain,data=r['value'],sha256=hashlib.sha256(b).hexdigest()))
    langs={}
    for locale in ('en','zh-cn'):
        for asset in parsed:
            if asset['file'].lower().endswith('/lang/'+locale+'.json') and isinstance(asset['data'],dict):
                for k,v in asset['data'].items():
                    if not isinstance(v,str): continue
                    dom,key=k.split(':',1) if ':' in k else (asset['domain'],k)
                    langs[(dom,key)]=v
    worldprops={}
    for a in parsed:
        if '/worldproperties/' in a['file'] and isinstance(a['data'],dict):
            key=a['file'].split('/worldproperties/',1)[1][:-5]
            worldprops[(a['domain'],key)]=a['data']
    cache = ROOT/'scripts/generated/nutrition-assets.json'
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(parsed, ensure_ascii=False), encoding='utf-8')
    foods=[]; recipes=collections.defaultdict(list); manuals=collections.defaultdict(list); nutrition_patches=[]
    for a in parsed:
        data=a['data']; path=a['file']; domain=a['domain']; slug=a['mod']
        if '/recipes/' in path:
            recipes[slug].append(a)
        if '/config/handbook/' in path:
            for page in data if isinstance(data,list) else [data]:
                if not isinstance(page,dict): continue
                title=translated(page.get('title',page.get('pageCode',path)),domain,langs)
                body=translated(page.get('text',''),domain,langs)
                manuals[slug].append(dict(title=title,body=plain_rich(body),file=path,page=page))
        if '/patches/' in path:
            for pointer,value in walk(data):
                if isinstance(value,dict) and 'op' in value and re.search('nutrition|satiety|foodcategory|health',compact(value),re.I):
                    nutrition_patches.append(dict(mod=slug,file=path,pointer=pointer,patch=value))
        if not any('/'+part+'/' in path for part in ('itemtypes','blocktypes')): continue
        for objindex,obj in enumerate(data if isinstance(data,list) else [data]):
            if not isinstance(obj,dict): continue
            low={k.lower():v for k,v in obj.items()}
            base=low.get('code',Path(path).stem)
            if not isinstance(base,str): base=compact(base)
            expanded, unresolved = expand_variants(obj, domain, worldprops)
            variants = [code for code, _ in expanded]
            allcodes=[v if ':' in v else domain+':'+v for v in variants]
            typ='item' if '/itemtypes/' in path else 'block'
            for pointer,value in walk(obj):
                if not isinstance(value,dict): continue
                vals={k.lower():v for k,v in value.items()}
                if not ('satiety' in vals or 'foodcategory' in vals): continue
                condition=pointer or '/'
                codes=allcodes
                # ByType selection is recorded per branch rather than falsely resolving nested overrides.
                pieces=pointer.split('/')
                for idx,piece in enumerate(pieces[:-1]):
                    if piece.lower().endswith('bytype'):
                        pattern=pieces[idx+1]
                        codes=[c for c in codes if match(c.split(':',1)[-1],pattern) or match(c,pattern)]
                names=list(dict.fromkeys(translated(typ+'-'+c.split(':',1)[-1],c.split(':',1)[0],langs) for c in codes))
                foods.append(dict(mod=slug,modName=a['modName'],code=domain+':'+base if ':' not in base else base,
                    codes=codes,names=names,condition=condition,category=vals.get('foodcategory','—'),
                    satiety=vals.get('satiety'),health=vals.get('health'),nutrition=value,
                    file=path,unresolvedVariants=unresolved,liquidUnits=low.get('attributes',{}).get('waterTightContainerProps',{}).get('itemsPerLitre') if isinstance(low.get('attributes'),dict) else None))
    food_config=json.loads((SURV/'assets/vsslssmod/config/foods.json').read_text(encoding='utf-8-sig'))
    calibrations=food_config['Foods']
    for row in foods:
        row['calibrations']=[i for i,f in enumerate(calibrations) if any(match(c,p) for c in row['codes'] for p in f.get('Codes',[]))]
    public=ROOT/'docs/public/data'; public.mkdir(parents=True,exist_ok=True)
    calibration_names=[]
    for calibration in calibrations:
        names=[]
        for code in calibration.get('Codes',[]):
            name=display_name(code,'game',langs)
            if not name.startswith(('名称未汉化','变体材料')): names.append(name)
        calibration_names.append(list(dict.fromkeys(names)))
    payload=dict(foods=foods,calibrations=calibrations,calibrationNames=calibration_names,patches=nutrition_patches,
        counts=dict(assets=len(raw),parsed=len(parsed),errors=len(errors),foodRows=len(foods),foodMods=len({x['mod'] for x in foods}),
            recipeFiles=sum(map(len,recipes.values())),handbookPages=sum(map(len,manuals.values()))))
    write('docs/public/data/food-catalogue.json',json.dumps(public_food_data(payload),ensure_ascii=False))
    catalogue = build_catalogue(parsed, food_config, MANIFEST)
    write('docs/public/data/nutrition-catalogue.json',json.dumps(compact_catalogue(catalogue),ensure_ascii=False,separators=(',', ':')))
    print('Nutrition catalogue:', json.dumps(catalogue['counts'], ensure_ascii=False))
    write('scripts/asset-catalogue-errors.json',json.dumps(errors,ensure_ascii=False,indent=2)+'\n')
    write('scripts/asset-catalogue-manifest.json',json.dumps({k:v for k,v in payload.items() if k=='counts'},ensure_ascii=False,indent=2)+'\n')
    index=['# 整合包配方与手册资料库','','查询各模组的配方条件和手册正文。配方保留数量、网格、工具、时长、温度与变体限制；网格中的字母对应 ingredients 键，空格或下划线为空格。书中 itemstack 图片改为物品代码，正文未解析为网页脚本。','',
        '模组条件、补丁执行顺序和服务器配置可能改变可用配方，请同时核对游戏内手册。','',
        '| 模组 | 配方文件 | 手册章节 |','| --- | ---: | ---: |']
    for slug in ['game']+[e['slug'] for e in MANIFEST]:
        rec=recipes[slug]; man=manuals[slug]
        if not rec and not man: continue
        from site_catalogue import GROUPS
        titles={s.split('=',1)[0]:s.split('=',1)[1] for listing in GROUPS.values() for s in listing.split('|')}
        original_name='原版' if slug=='game' else next(e['name'] for e in MANIFEST if e['slug']==slug)
        name=titles.get(slug,original_name)
        index.append(f'| [{esc(name)}](/reference/recipes/{slug}) | {len(rec)} | {len(man)} |')
        lines=[f'# {esc(name)}：配方与手册','','[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)','',
            '配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。','']
        for i,m in enumerate(man):
            localized=bool(re.search('[\u4e00-\u9fff]',m['body']))
            title=m['title'] if re.search('[\u4e00-\u9fff]',m['title']) else f'{name}游戏内手册 {i+1}'
            lines.extend([f'## 手册 {i+1}：{esc(title)}',''])
            if not localized:
                lines += ['本章节在当前可读取语言资源中没有中文正文。相关材料和加工条件可在下方中文配方摘要查询；原文保留供核对。','','<details><summary>查看手册原文与来源</summary>','']
            lines += [f'来源：`{m["file"]}`。','', '\n\n'.join(esc(p.strip()) for p in m['body'].split('\n') if p.strip()),'']
            if not localized: lines += ['</details>','']
        lines.extend(['## 配方清单','','每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。',''])
        for a in rec:
            outputs=[]
            for pointer,v in walk(a['data']):
                if pointer.lower().endswith('/output') and isinstance(v,dict): outputs.append(v.get('code',''))
            names=[display_name(str(code),a['domain'],langs) for code in dict.fromkeys(outputs)]
            label='、'.join(dict.fromkeys(names)) or '特殊配方'
            lines.extend([f'<details><summary>{esc(label)} · {esc(Path(a["file"]).stem)}</summary>',''])
            lines.extend(recipe_summary(a['data'],a['domain'],langs))
            lines.extend(['<details><summary>技术说明：完整配方与资源路径</summary>','',f'来源：`{a["file"]}`','',
                '```json',json.dumps(a['data'],ensure_ascii=False,indent=2),'```','','</details>','','</details>',''])
        write(f'docs/reference/recipes/{slug}.md','\n'.join(lines)+'\n')
    write('docs/reference/recipes/index.md','\n'.join(index)+'\n')

if __name__=='__main__': main()
