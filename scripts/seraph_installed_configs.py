# -*- coding: utf-8 -*-
from local_inputs import required_dir, source_dir
import json, os
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CFG = required_dir('SERAPH_MODCONFIG_DIR')
FILES=['vsslssmod.Server.json','SeraphCivilizationSimulation.json','VscnCivilizationSimulation.json','vsscpmod-privacy.json','vsscpmod-quarry-carry.json']

def flatten(v,p=''):
    if isinstance(v,dict):
        for k,x in v.items(): yield from flatten(x, f'{p}.{k}' if p else k)
    elif isinstance(v,list):
        yield p, json.dumps(v,ensure_ascii=False,separators=(',',':'))
    else: yield p, json.dumps(v,ensure_ascii=False)

lines=['# 已安装 Seraph 配置实值','',f'> 来源：`{CFG}` 中的 Seraph 配置文件。这里记录当前实例文件的实际值；源码默认值和校验范围见[完整生存配置](/admin/survival-config-full)。','', '修改前请停服、备份并在启动日志中确认校验通过。','']
for fn in FILES:
    p=CFG/fn
    if not p.exists():
        lines += [f'## `{fn}`','', '当前实例未找到该文件。','']
        continue
    try: data=json.loads(p.read_text(encoding='utf-8-sig'))
    except Exception as e:
        lines += [f'## `{fn}`','',f'解析失败：{e}','']; continue
    lines += [f'## `{fn}`','', '| 路径 | 当前值 |','| --- | --- |']
    for k,v in flatten(data):
        safe=str(v).replace('|', r'\|')
        lines.append(f'| `{k}` | `{safe}` |')
    lines.append('')
from wiki_content import write_generated
write_generated(ROOT/'docs/admin/installed-configs.md','\n'.join(lines)+'\n')
print('generated installed Seraph config values')
