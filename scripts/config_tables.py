# -*- coding: utf-8 -*-
from local_inputs import required_dir, source_dir
"""All installed configuration leaf values, with credentials and identity data redacted."""
import hashlib, html, json, os, re
from pathlib import Path
from asset_catalogue import parse_many, esc, write
ROOT=Path(__file__).resolve().parent.parent
CFG = required_dir('SERAPH_MODCONFIG_DIR')
# Never copy server authentication material or lists of real player identities into public pages.
SECRET=re.compile(r'password|passwd|secret|token|credential|authorization|privatekey|apikey|authkey|connectionstring|webhook|endpoint|serveraddress|ipaddress|\bhost\b|playeruid|playername|allowedplayers|adminuid|owneruid|whitelistedplayers',re.I)
PRIVATE_FILE=re.compile(r'auth|player.?history|audit|clientlog|identity|account',re.I)

def leaves(v,p='',hidden=False):
    hidden=hidden or bool(SECRET.search(p))
    if hidden: yield p,'已隐藏','敏感字段'; return
    if isinstance(v,dict) and v:
        for k,x in v.items(): yield from leaves(x,p+'/'+str(k))
    elif isinstance(v,list) and v:
        for i,x in enumerate(v): yield from leaves(x,p+'/'+str(i))
    else:
        typ='null' if v is None else 'boolean' if isinstance(v,bool) else 'number' if isinstance(v,(int,float)) else 'string' if isinstance(v,str) else 'array' if isinstance(v,list) else 'object'
        if isinstance(v,str) and (re.search(r'https?://|wss?://',v) or re.fullmatch(r'\d{1,3}(?:\.\d{1,3}){3}(?::\d+)?',v)):
            yield p,'已隐藏地址',typ
        else: yield p,json.dumps(v,ensure_ascii=False),typ

def main():
    files=sorted(p for p in CFG.rglob('*') if p.is_file())
    parsed=parse_many([p.read_text(encoding='utf-8-sig') for p in files])
    lines=['# 全部整合包配置表','','逐文件展开当前服务器配置快照的全部叶子字段，数组使用从 0 开始的索引。这里是文件中的实际值，不是作者默认值；没有读取到源码的字段不凭名称编造作用或取值范围。','',
           '认证字段、玩家身份列表和连接地址保留字段位置并隐藏值。配置改变后是否需要重启，应按模组加载流程判断；文明主配置的热重载不能用于其他模组。','',
           '| 配置文件 | 字段数 | 状态 |','| --- | ---: | --- |']
    total=0
    for p,result in zip(files,parsed):
        rel=p.relative_to(CFG).as_posix(); slug=hashlib.sha256(rel.encode()).hexdigest()[:12]
        rows=[] if 'error' in result else list(leaves(result['value'],hidden=bool(PRIVATE_FILE.search(rel))))
        total+=len(rows)
        lines.append(f'| [{esc(rel)}](/reference/configs/{slug}) | {len(rows)} | '+('解析失败' if 'error' in result else '完整字段表')+' |')
        body=[f'# {esc(rel)}','','[返回全部配置表](/admin/config-tables)','',f'来源：指定服务器 `ModConfig/{esc(rel)}`；路径以 `/` 分隔，数字是数组索引。','']
        if 'error' in result: body += ['解析失败：'+esc(result['error'])]
        else:
            body+=['| 字段路径 | 类型 | 当前值 |','| --- | --- | --- |']
            for key,value,typ in rows: body.append(f'| <code>{esc(key or "/")}</code> | {typ} | <code>{esc(value)}</code> |')
        body+=['','配置表没有列为默认值的内容均来自当前实例；不应直接照搬到另一个服务器。Seraph 的已核验含义、范围和生效方式见[管理员入口](/admin/)。']
        write(f'docs/reference/configs/{slug}.md','\n'.join(body)+'\n')
    write('docs/admin/config-tables.md','\n'.join(lines)+'\n')
    print(f'configuration files={len(files)}, leaf rows={total}')
if __name__=='__main__': main()
