from local_inputs import required_dir, source_dir
"""Append reproducible package evidence without touching human-authored text."""
import collections, concurrent.futures, hashlib, json, os, re, subprocess, tempfile, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACK = required_dir('SERAPH_MODS_DIR')
MANIFEST = json.loads((ROOT/'scripts/inventory-manifest.json').read_text(encoding='utf-8-sig'))
START='<!-- package-evidence:start -->'
END='<!-- package-evidence:end -->'

def escape(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|',r'\|').replace('`','')
def extract(entry):
    path=PACK/entry['file']; files={}
    if path.is_dir():
        for f in path.rglob('*'):
            if f.is_file(): files[f.relative_to(path).as_posix()]=f.read_bytes()
    else:
        with zipfile.ZipFile(path) as z:
            files={n:z.read(n) for n in z.namelist() if not n.endswith('/') and z.getinfo(n).file_size<30000000}
    buckets=collections.defaultdict(list)
    for name in files:
        n=name.lower().replace('\\','/')
        if n.endswith('.dll'): buckets['程序集'].append(name)
        elif '/recipes/' in '/'+n and n.endswith('.json'): buckets['配方定义'].append(name)
        elif '/patches/' in '/'+n and n.endswith('.json'): buckets['资产补丁'].append(name)
        elif '/blocktypes/' in '/'+n and n.endswith('.json'): buckets['方块定义'].append(name)
        elif '/itemtypes/' in '/'+n and n.endswith('.json'): buckets['物品定义'].append(name)
        elif '/entities/' in '/'+n and n.endswith('.json'): buckets['实体定义'].append(name)
        elif '/lang/' in '/'+n and n.endswith('.json'): buckets['语言资源'].append(name)
        elif 'handbook' in n and n.endswith('.json'): buckets['手册资源'].append(name)
        elif '/config/' in '/'+n and n.endswith('.json'): buckets['包内配置数据'].append(name)
        elif n.endswith(('.cs','.fs')): buckets['源码文件'].append(name)
    types=[]; failures=[]
    with tempfile.TemporaryDirectory(prefix='wiki-assemblies-') as tmp:
        for idx,name in enumerate(buckets['程序集']):
            f=Path(tmp)/(str(idx)+'.dll'); f.write_bytes(files[name]); digest=hashlib.sha256(files[name]).hexdigest()[:16]
            try:
                p=subprocess.run(['ilspycmd','-l','c',str(f)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
                if p.returncode: failures.append(name); continue
                found=[x.strip() for x in p.stdout.splitlines() if x.startswith('Class ')]
                types.append((name,digest,found))
            except (OSError,subprocess.TimeoutExpired): failures.append(name)
    lines=[START,'<details><summary>安装包技术资料与实现证据</summary>','','## 安装包实现证据','', '以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。','','| 类型 | 数量 | 包内路径示例 |','| --- | ---: | --- |']
    for category in ['源码文件','程序集','方块定义','物品定义','实体定义','配方定义','资产补丁','语言资源','手册资源','包内配置数据']:
        items=sorted(buckets[category]); examples='<br>'.join('`'+escape(v)+'`' for v in items[:12]) or '—'
        if len(items)>12: examples+='<br>另有 {} 个文件'.format(len(items)-12)
        lines.append('| {} | {} | {} |'.format(category,len(items),examples))
    if types:
        lines += ['', '### 程序集类型索引', '', '通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。','']
        for name,digest,found in types:
            lines += ['**{}**（`{}`）：{} 个类型。'.format(escape(name),digest,len(found)),'']
            if found:
                lines += ['```text','\n'.join(found[:40]),'```','']
                if len(found)>40: lines += ['其余 {} 个类型未在此列出；可按维护说明重新分析程序集。'.format(len(found)-40),'']
    if failures: lines += ['以下程序集未能解析：'+', '.join('`'+escape(f)+'`' for f in failures)+'。','']
    lines += ['类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。','','</details>',END]
    target=ROOT/'scripts/generated/package-evidence'/(entry['slug']+'.md')
    target.parent.mkdir(parents=True, exist_ok=True)
    text=target.read_text(encoding='utf-8') if target.exists() else ''
    # Remove previous generated section, retaining all other content.
    if START in text and END in text: text=text[:text.index(START)]+text[text.index(END)+len(END):]
    target.write_text(text.rstrip()+'\n\n'+'\n'.join(lines)+'\n',encoding='utf-8')
    return {'id':entry['id'],'files':sum(len(v) for v in buckets.values()),'dlls':len(buckets['程序集']),'parsed':len(types),'failed':failures}

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(extract,MANIFEST))
    (ROOT/'scripts/package-evidence.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('packages:',len(results),'assemblies:',sum(r['dlls'] for r in results),'parsed:',sum(r['parsed'] for r in results),'failed:',sum(len(r['failed']) for r in results),flush=True)
