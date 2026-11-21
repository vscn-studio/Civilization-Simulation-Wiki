"""Presentation only: preserve numeric/source expressions in expandable notes."""
import re

def player_tables(text):
    result=[]
    table_kind=None
    for line in text.splitlines():
        if line.startswith('| 指标 | 单位/尺度 | 玩家读法 |'):
            table_kind='metric'
            result.append('| 属性 | 单位 | 含义与读法 | 技术说明 |'); continue
        if line.startswith('| 状态 | 游戏说明 |'):
            table_kind='condition'
            result.append('| 状态 | 表现与应对 | 技术说明 |'); continue
        if table_kind and line.startswith('| ') and not line.startswith('| ---'):
            cells=line.strip('|').split(' | ')
            cells=[s.strip() for s in cells]
            code=re.search(r'<br><code>(.*?)</code>',cells[0])
            if code:
                cells[0]=cells[0][:code.start()]
                cells[-1]=f'标识：<code>{code.group(1)}</code><br>'+cells[-1]
            cells[-1]='<details><summary>源码与计算</summary>'+cells[-1]+'</details>'
            line='| '+' | '.join(cells)+' |'
        elif not line.startswith('|'):
            table_kind=None
        result.append(line)
    text='\n'.join(result)+'\n'
    text=text.replace('投诉','不适症状').replace('综合症','综合征').replace('walkspeed','行走速度属性')
    text=text.replace('当前 Exertion 实现','当前体力系统实现')
    text=text.replace('这份表把窗口实际使用的键与服务端生成 `PanelMetric` 的代码对照。','按 C 打开角色窗口，在下表查找属性名称。展开“技术说明”可查看取值代码。')
    text=text.replace('疾病窗口中不全是传染病。以下项目来自 `ClinicalEffects.Evaluate`，负担大于零时才加入，严重度会夹到 0–1。','疾病窗口中不全是传染病。这里也会显示失温、疲惫、出血和营养不足等身体异常。')
    text=text.replace('来源：`PinnedCharacterPanels.cs`。','窗口固定的实现见技术参考 `PinnedCharacterPanels.cs`。')
    # Localized game text can lag behind source; use the verified disease conditions.
    text=text.replace('急性感染叠加严重缺水、失血、意识低下或再次虫咬/入血暴露时出现；每 10 min 损失 5 点生命，与其他全身损伤取较强者。','候选感染处于严重症状期，并叠加严重脱水、失血或意识危险，持续达到配置时间后出现。具体条件和恢复要求见疾病百科的败血症条目。')
    return text
