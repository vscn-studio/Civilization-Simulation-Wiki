# -*- coding: utf-8 -*-
"""Read installed JSON/JSON5 assets. Preserve conditions; never simulate DLL/patch load order."""
import collections, hashlib, html, itertools, json, os, re, subprocess, zipfile
from functools import lru_cache
from pathlib import Path
from wiki_content import write_generated
from recipe_presentation import display_name, recipe_summary

ROOT = Path(__file__).resolve().parent.parent
GAME = Path(os.environ.get('SERAPH_GAME_DIR', r'E:\vintagestory\Vintagestory'))
PACK = Path(os.environ.get('SERAPH_MODS_DIR', r'C:\Users\29596\AppData\Roaming\MVL\Modpack\测试服务器\Mods'))
SURV = Path(os.environ.get('SERAPH_SURVIVAL_SOURCE', r'E:\vintagestory\Seraph Living Survival Simulation'))
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
            variants=[base]; unresolved=[]
            for g in low.get('variantgroups',[]):
                if not isinstance(g,dict): continue
                states=g.get('states')
                if states is None and 'loadFrom' in g:
                    load=g['loadFrom']; dom,key=load.split(':',1) if ':' in load else (domain,load)
                    states=[v.get('code') for v in worldprops.get((dom,key),{}).get('variants',[]) if isinstance(v,dict)]
                if states and all(isinstance(s,str) for s in states) and len(variants)*len(states)<=50000:
                    variants=[v+'-'+s for v in variants for s in states]
                else: unresolved.append(g)
            skip=low.get('skipvariants',[]); allow=low.get('allowedvariants',[])
            variants=[v for v in variants if not any(match(v,p) for p in skip) and (not allow or any(match(v,p) for p in allow))]
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
    calibrations=json.loads((SURV/'assets/vsslssmod/config/foods.json').read_text(encoding='utf-8-sig'))['Foods']
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
    write('docs/public/data/food-catalogue.json',json.dumps(payload,ensure_ascii=False))
    write('scripts/asset-catalogue-errors.json',json.dumps(errors,ensure_ascii=False,indent=2)+'\n')
    write('scripts/asset-catalogue-manifest.json',json.dumps({k:v for k,v in payload.items() if k=='counts'},ensure_ascii=False,indent=2)+'\n')
    index=['# 整合包配方与手册资料库','','从实际安装包读取配方定义和手册正文。配方保留数量、网格、工具、时长、温度与变体限制；网格中的字母对应 ingredients 键，空格或下划线为空格。书中 itemstack 图片改为物品代码，正文未解析为网页脚本。','',
        '原版基准为本机 `E:/vintagestory/Vintagestory/assets`。这里展示资产定义；模组条件、补丁执行顺序、脚本和服务器配置可能改变可用配方。','',
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
        if slug!='game':
            target=ROOT/f'docs/mods/entries/{slug}.md'; original=target.read_text(encoding='utf-8')
            block=f'\n<!-- reference-link:start -->\n## 材料、加工与手册正文\n\n[查阅本版本 {len(rec)} 个配方文件与 {len(man)} 个手册章节](/reference/recipes/{slug})。配方中可查投入数量、产物、工具、网格和加工条件。\n<!-- reference-link:end -->\n'
            original=re.sub(r'\n<!-- reference-link:start -->.*?<!-- reference-link:end -->\n','\n',original,flags=re.S)
            target.write_text(original.rstrip()+'\n'+block,encoding='utf-8')
    write('docs/reference/recipes/index.md','\n'.join(index)+'\n')
    lines=['# 原版与整合包食物检索','','可以按中文名称、代码、模组或营养类别搜索。展开行查看全部变体、条件及营养字段。原版饱食度与 Seraph 的克、千焦、微量营养是不同系统，不能直接换算。','',
        '本表扫描本机原版资源及整合包全部安装包，列出含 satiety/foodCategory 的资源分支；条件分支保留原样。空白表示未声明，不能当作零；同一物品可有直接食用、烹饪、液体等多行。','',
        '<FoodCatalogue />','',
        '## 查表方法','','1. 输入中文名或完整代码，选择来源模组。找不到中文名时用游戏内高级提示里的代码。\n2. 看条件路径：`nutritionProps` 是该定义的营养；`nutritionPropsByType` 还需要匹配变体；烹饪字段只在相应加工后适用。\n3. 查看命中的 Seraph 校准记录。宏量与微量字段是每 100 g，实际份量需乘 `PortionG / 100`；液体还要结合每升物品数。\n4. 混合餐、派、液体混合和运行时修改需按实际配料结算，不能把容器基础值当作整餐值。','',
        '## 数据来源与更新','','原版：`E:/vintagestory/Vintagestory/assets`；整合包：用户指定 Mods；Seraph 校准：生存源码 `assets/vsslssmod/config/foods.json`。运行 `npm run asset-catalogue` 可重建。','',
        f'本次读取 {len(raw)} 个资源，成功解析 {len(parsed)} 个；营养分支 {len(foods)} 条，涉及 {len({x["mod"] for x in foods})} 个来源。解析错误 {len(errors)} 个。','',
        '[下载完整数据（含营养补丁和校准记录）](/data/food-catalogue.json) · [查看全部配方与手册](/reference/)','',
        '## 补丁和运行时边界','','营养补丁保存在下载文件 patches 中。此表没有假装执行 DLL、JSON 补丁加载顺序和服务器世界规则；多个分支也没有强行合并为最终值。校准命中表示代码匹配，不保证发布 DLL 与当前源码校准完全一致。游戏内 Seraph 食品手册的服务端数据用于核对最终份量。']
    if errors:
        lines+=['','## 未能解析的资源','','以下文件未静默忽略；相关条目需要查看原文件或游戏运行数据。','','| 模组 | 文件 | 原因 |','| --- | --- | --- |']
        lines += [f'| {esc(e["mod"])} | {esc(e["file"])} | {esc(e["error"])} |' for e in errors]
    write('docs/guide/food-catalogue.md','\n'.join(lines)+'\n')
    print(compact(payload['counts']),flush=True)

if __name__=='__main__': main()
