# -*- coding: utf-8 -*-
"""Create a non-sensitive inventory of the installed server ModConfig files."""
import json, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = Path(os.environ.get('SERAPH_MODCONFIG_DIR', r'C:\Users\29596\AppData\Roaming\MVL\Modpack\测试服务器\Logs\服务器相关\ModConfig'))
OUT = ROOT / 'docs/admin/modconfig-inventory.md'
SENSITIVE = ('auth', 'privacy', 'player-history', 'audit', 'voice', 'redirect')

def paths(value, prefix=''):
    out=[]
    if isinstance(value, dict):
        for k,v in value.items():
            p=f'{prefix}.{k}' if prefix else str(k)
            out.append(p)
            out.extend(paths(v,p))
    elif isinstance(value, list) and value and isinstance(value[0], dict):
        out.append(prefix+'[]')
        out.extend(paths(value[0], prefix+'[]'))
    return out

rows=[]
for p in sorted(CFG.rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(CFG).as_posix()
    if p.suffix.lower() != '.json':
        rows.append((rel,'非 JSON/脚本配置','未解析'))
        continue
    try:
        data=json.loads(p.read_text(encoding='utf-8-sig'))
        keys=paths(data)
        label='敏感配置（只列文件名）' if any(x in p.name.lower() for x in SENSITIVE) else ('；'.join(keys[:30]) or '（空对象/数组）')
        if len(keys)>30: label += f'；…共 {len(keys)} 个路径'
        rows.append((rel,'JSON',label))
    except Exception as e:
        rows.append((rel,'JSON（解析失败）',str(e).splitlines()[0][:120]))

lines=['# 整合包服务器配置文件清单','',f'> 来源：`{CFG}`。本页只列文件、格式和键路径，不复制认证、地址、玩家历史、审计或语音内容；实际值请在服务器停机并备份后查看。','',f'共 **{len(rows)}** 个文件。','', '| 相对路径 | 格式 | 顶层/键路径摘要 |','| --- | --- | --- |']
for rel,kind,label in rows:
    safe=label.replace('|', r'\|')
    lines.append(f'| `{rel}` | {kind} | {safe} |')
OUT.parent.mkdir(parents=True, exist_ok=True)
from wiki_content import write_generated
write_generated(OUT,'\n'.join(lines)+'\n')
print(f'generated config files={len(rows)}')
