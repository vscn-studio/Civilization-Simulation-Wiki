# -*- coding: utf-8 -*-
"""Keep extraction provenance out of published pages and downloadable data."""
import re

RETIRED_PAGES = {
    'develop/source-inventory.md', 'develop/maintenance.md',
    'develop/sources/vsscsmod.md', 'develop/sources/vsscpmod.md',
    'develop/sources/vsslssmod.md',
}


def public_markdown(text):
    text = re.sub(r'<!-- package-evidence:start -->.*?<!-- package-evidence:end -->', '', text, flags=re.S)
    # These lines describe extraction locations, not infection/food origins.
    text = re.sub(r'^(?:> )?来源：[^\n]*\n?', '', text, flags=re.M)
    text = re.sub(r'^(?:> )?证据：.*?。\s*', '', text, flags=re.M)
    text = re.sub(r'<br>[\w./-]+\.cs(?::\d+)?(?=</details>)', '', text)
    text = re.sub(r'参见\s*\x60[^\x60\n]+\.cs\x60(?:[、和 ]*\x60[^\x60\n]+\.cs\x60)*。', '', text)
    text = re.sub(r'来源：\s*\x60[^\x60\n]+\.cs\x60(?:[、和 ]*\x60[^\x60\n]+\.cs\x60)*。?', '', text)
    text = re.sub(r'窗口固定的实现见技术参考 \x60[^\x60]+\x60。', '', text)
    for old, new in [
        ('技术说明与来源', '技术说明'), ('源码与计算', '标识与计算'),
        ('技术说明：完整配方与资源路径', '技术说明：完整配方'),
        ('查看手册原文与来源', '查看手册原文'),
        ('源码默认值', '默认值'), ('源码 悬停说明', '悬停说明'),
        ('源码没有为它另设', '本病未单独设置'),
        ('源码未实现的', '游戏未提供的'),
        ('手持任意原版散石（如花岗岩散石），瞄准未点燃的火塘，按住 Shift 并连续右键逐块加入，共需 12 块',
         '完成原版火塘后将其熄灭，手持一叠至少 12 块散石（如花岗岩散石），瞄准火塘按住 Shift + 右键，一次投入 12 块'),
        ('生存模拟源码 1.0.1 的中文游戏内手册', '生存模拟 1.0.1 的中文游戏内手册'),
        ('以下介绍依据源码与资源整理；实际规则可能受服务器配置影响。', '实际规则可能受服务器配置影响。'),
    ]:
        text = text.replace(old, new)
    # Configuration examples can contain local paths too; never publish a drive path.
    text = re.sub(r'(?<![\w:/])[A-Za-z]:[\\/][^\x60\n<>"|]*', '（本机目录已省略）', text)
    return re.sub(r'\n{4,}', '\n\n\n', text)


def public_food_data(payload):
    for food in payload['foods']:
        food.pop('file', None)
    for calibration in payload['calibrations']:
        calibration.pop('Source', None)
        calibration.pop('PortionBasis', None)
    payload.pop('patches', None)
    payload['counts'] = {key: payload['counts'][key] for key in ('foodRows', 'foodMods')}
    return payload
