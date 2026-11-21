# -*- coding: utf-8 -*-
"""Source-linked disease and UI reference. Hand-written explanations sit beside extracted expressions."""
import html, json, os, re
from pathlib import Path
from wiki_content import write_generated
from player_presentation import player_tables
from disease_editorial import build_diseases
ROOT=Path(__file__).resolve().parent.parent
SURV=Path(os.environ.get('SERAPH_SURVIVAL_SOURCE',r'E:\vintagestory\Seraph Living Survival Simulation'))
SRC=SURV/'src'
LANG=json.loads((SURV/'assets/vsslssmod/lang/zh-cn.json').read_text(encoding='utf-8-sig'))
def read(path): return (SRC/path).read_text(encoding='utf-8-sig')
def esc(value): return html.escape(str(value),quote=False).replace('|','&#124;').replace('\n','<br>').replace('`','&#96;').replace('{{','&#123;&#123;')
def write(path,lines):
    write_generated(ROOT/'docs'/path, player_tables('\n'.join(lines)))
def label(key): return LANG.get(key,key)

def args(text,start):
    """Balanced call arguments, preserving nested calls and quoted C# strings."""
    out=[]; begin=start; depth=0; quoted=False; escaped=False
    for i in range(start,len(text)):
        c=text[i]
        if quoted:
            if escaped: escaped=False
            elif c=='\\': escaped=True
            elif c=='"': quoted=False
            continue
        if c=='"': quoted=True
        elif c in '([{': depth+=1
        elif c in ')]}':
            if depth==0: out.append(text[begin:i].strip()); return out
            depth-=1
        elif c==',' and depth==0: out.append(text[begin:i].strip()); begin=i+1
    raise ValueError('unclosed call')

def diseases():
    source=read('Seraph.Core/Framework/Pathogens.cs')
    records=[]
    for m in re.finditer(r'new\("([^"]+)",\s*"([^"]+)",\s*ExposureRoute\.(\w+),\s*new\("[^"]+",\s*([\d.]+),\s*([\d.]+),\s*([\d.]+),\s*([\d.]+)\)\)',source):
        id,agent,route,inc,sym,rec,sev=m.groups(); records.append((id,agent,route,*[float(v)*30/3600 for v in (inc,sym,rec)],float(sev)))
    records += [('water-enteric','水源肠道病原','Ingestion',2.5,15,12.5,.6),('wound-local','局部伤口病原','OpenWound',5,30,22.5,.5)]
    specific={
      'norovirus':('诺如病毒感染','污染食物/水中携带此 ID，或手部、粪便污染进入食物。','食物中毒组；恶心系数 0.9。','停止使用污染水与食物；先稳定可用水量。症状期进食利用率大幅下降，不要只凭吃下去的份数判断已补足。'),
      'giardia':('贾第虫感染','摄入携带 giardia 的水或食物。','不属于 FoodPoisoning 组；消化效率为 1 − 有效病原负担 × 0.4；恶心系数 0.3、腹痛系数 0.4。','胃里有东西而水和能量增长缓慢时检查本病与消化倍率。保持洁净补给，给消化留时间；不能把它当成清空胃的食物中毒。'),
      'shigella':('志贺菌感染／痢疾','摄入携带 shigella 的污染物。','痢疾组；症状期固定失水分量为 0.5 × (1 − 针对此病原的缓解率) L/游戏小时，与一般肠道失水取较大值；腹痛系数 0.9。','重点追踪水量趋势、胃水和肠道容量。持续补给干净水并处理排泄物，避免仅补食物而忽视持续失水。'),
      'ecoli':('致病性大肠杆菌感染','摄入携带 ecoli 的水、食物或粪便污染。','食物中毒组；恶心系数 0.4、腹痛系数 0.7。','清洁手部、容器和饮水链；观察腹痛、胃内容物变化以及实际水量增长。'),
      'salmonella':('沙门氏菌感染','除污染来源外，FoodCatalog 对已识别的生动物肉加入 quantity × 0.08 的沙门氏菌负荷。蛋白质类别本身不等于生肉。','食物中毒组；恶心系数 0.7、腹痛系数 0.5。','处理动物肉后进行实际烹饪，核对产物状态。不能用豆类等蛋白质食品的类别推断同样感染风险。'),
      'wound-staph':('伤口葡萄球菌感染','未愈合开放伤口内的同名病原负荷，经 AdvanceWounds 推进。','发热组；也是败血症候选病原。','先按压/包扎控制失血，再清洁伤口并减少新污染；同时观察血量、水量与意识。'),
      'respiratory':('呼吸道感染','环境中的已识别同名病原；还可由同维度、8 格内症状期或恢复期携带者传播。','发热组；附近传播按距离、通风、双方呼吸防护和携带者负担缩放。','与感染者拉开距离、改善通风，使用服务器 RespiratoryProtectionByCode 中登记的装备。单纯远离烟雾不保证消除病原。'),
      'common-cold':('普通感冒','已识别病原暴露或 8 格内症状/恢复期玩家传播；源码不能仅因气温低就推出感染。','CommonCold 组；与发热组分开，不能默认具有同样的体温设定点。','休息、保持水和能量供应；多人共同居住时改善通风并拉开距离，恢复期也应注意传播。'),
      'qfever':('Q 热','环境快照 DiseaseSources 必须实际提供 qfever；空气途径。','发热组，设定点随该组最强有效负担上升。','离开提供病原的区域并改善通风，监测核心温度、出汗和水量。不能只凭附近有动物就认定已经感染。'),
      'tularemia':('土拉菌感染','环境快照实际提供 tularemia；空气途径。','发热组；本版本通用病程比 Q 热初始负担高（0.7 对 0.65）。','减少该区域空气接触，保障饮水和休息；以疾病列表的 ID 确认，不从现实疾病的其他传播方式推断游戏规则。'),
      'histoplasmosis':('组织胞浆菌感染','环境快照实际提供 histoplasmosis；空气途径。','发热组；基准潜伏 12 游戏小时，比 Q 热与土拉菌的 6 小时长。','暴露后短期没有可见症状不能排除潜伏；离开来源并定期检查疾病阶段。'),
      'pasteurella':('巴氏杆菌感染','AnimalBitePathogen 将 wolf、hyena、bear、fox、boar 代码词元映射到本病原；也属于可进入伤口的病原。','发热组与败血症候选；基准潜伏 3 游戏小时。','动物咬伤后先止血、清洁、检查伤口，后续持续看体温和疾病列表；不要只等伤口疼痛消失。'),
      'sporotrichosis':('孢子丝菌感染','动物代码词元 hare、rabbit、raccoon、squirrel、rat、mouse 映射到本病原；也属于伤口病原。','发热组；不在 SepsisAgent 四种病原清单内。','小型动物造成的伤害也应护理；本病基准症状期 36 小时，不应在短暂缓解后立刻大量劳动。'),
      'murinetyphus':('鼠型斑疹伤寒','媒介附着时，局部 DiseaseSources 中必须有 murinetyphus 才可选中。','发热组；VectorAttached 与已感染是不同状态。','看到虫媒携带先洗浴清除附着，不要等待叮咬成熟。已经进入病程后，洗浴不会直接删除疾病记录。'),
      'malaria':('疟疾','媒介附着时，局部 DiseaseSources 中必须有 malaria 才可选中；不能在没有病原来源的环境里凭空生成。','发热组；基准潜伏 12、症状 36、恢复 24 游戏小时。','洗浴清除附着媒介，离开适宜媒介环境；感染后监测长病程带来的水和能量消耗。'),
      'trichinosis':('旋毛虫感染','已识别的生 bushmeat 在沙门氏菌之外增加 quantity × 0.08 的旋毛虫负荷。','食物中毒组；恶心系数 0.7、腹痛系数 0.5；Enteric=true，但 Fecal=false。','把野味实际做熟；本病不进入粪源分类，不要把防治重点只放在饮水处理。'),
      'anthrax':('炭疽感染','同名皮肤接触来源；Skin 屏障溢出允许本病进入，即使没有开放伤口；也属于伤口病原。','发热组、败血症候选。','离开明确污染来源，洗净皮肤并护理伤口；如果出现严重失水、失血或意识异常，需要同时处理这些危险因素。'),
      'tetanus':('破伤风感染','皮肤途径的伤口病原；从皮肤屏障进入需有未愈合开放伤口。MicroclimateAdapter 按鞋类保护削减来源。','发热组；初始负担 0.75，基准症状期 36 小时；不属于 SepsisAgent 四种。','穿戴有效鞋类、清洁并保护开放伤口。当前通用症状实现不能扩写成现实破伤风的锁颌或肌痉挛机制。'),
      'skin-fungal':('皮肤真菌感染','已识别皮肤环境来源，Skin 屏障溢出可进入，不要求伤口。','不映射到四个 SymptomKit；基准潜伏仅 30 生物秒，症状 45 游戏小时。','清洁皮肤、降低持续污染暴露，观察疾病条目；不要凭本病名称宣称有源码未实现的瘙痒、皮疹或特效药。'),
      'water-enteric':('水源肠道感染','WithGenericEnteric 将通用肠道负荷转成该病原；走实际摄入链。','食物中毒组；不具有诺如、沙门等各自额外的恶心/腹痛系数。','检查取水、处理、储存及容器再污染整个流程；看处理设备的病原结果，水看起来清澈不等于病原清零。'),
      'wound-local':('局部伤口感染','通用伤口病原定义，按实际伤口污染负荷推进。','发热组与败血症候选。','检查开放伤口污染与清洁保护时间；止血、清洁、营养支持应同时关注，不能把包扎等同于立即清除所有感染。')}
    lines=build_diseases(records,specific)
    write('guide/diseases.md',lines)
    return len(records)

def metrics():
    allcalls={}
    for path in sorted((SRC/'Seraph/Server').glob('*.cs')):
        text=path.read_text(encoding='utf-8-sig')
        for m in re.finditer(r'\b(Metric|Function)\("([a-z][a-z0-9-]*)"\s*[,)]',text):
            call=args(text,text.index('(',m.start())+1)
            if len(call)<2: continue
            key=m.group(2); expr=call[1]
            if m.group(1)=='Function': expr='('+expr+') * 100'
            unit='%' if m.group(1)=='Function' else (call[2].strip('"') if len(call)>2 and re.fullmatch(r'"[^"\n]*"',call[2]) else '')
            if not unit and any('maximum: 100' in a for a in call): unit='%（0–100 标尺）'
            allcalls.setdefault(key,[]).append((path.name,text[:m.start()].count('\n')+1,expr,unit,call))
    arrays=[]
    for filename in ['CharacterMetricsPanel.cs','CharacterPanelIntegration.cs']:
        text=read('Seraph/Client/'+filename)
        for group,body in re.findall(r'(?:private|internal) static readonly string\[\] (\w+Keys) = \[(.*?)\];',text,re.S):
            if group not in ('OwnedKeys','PinnableKeys'): arrays.append((group,re.findall('"([^"\\n]+)"',body)))
    groups={'StatusKeys':'身体状态','BloodCirculationKeys':'血液循环','DiseaseRecoveryKeys':'疾病恢复','EnergyStatusKeys':'能量状态','EnergyDemandKeys':'能量需求','FunctionKeys':'功能倍率','ThermoregulationKeys':'体温调节','EnvironmentKeys':'环境'}
    lines=['# C 键数值：单位、来源与读法','','这份表把窗口实际使用的键与服务端生成 `PanelMetric` 的代码对照。百分比标尺不一定代表概率；移动倍率可以含原版、负重及其他模组的修正。','',
      '## 操作与窗口固定','','按 C 打开角色窗口。将指针停在数值上查看原因和收支趋势；有滚动条的窗口可向下查看。可固定的六个窗口在标题栏有固定按钮：身体、血液循环、疾病恢复、功能、能量平衡、体温调节。固定后关闭 C 仍可显示；环境窗口没有固定按钮，退出世界会清除本次固定记录。来源：`PinnedCharacterPanels.cs`。','',
      '## 按问题找指标','','| 想判断的问题 | 连着看哪些值 | 如何读 |','| --- | --- | --- |',
      '| 喝水为什么没恢复 | 水量、胃水、消化、出汗、出血 | 胃内水尚未等于可用水；吸收和损失可同时发生，悬停看两路流量。 |',
      '| 吃饱为什么还没力气 | 胃内容物、糖原、血糖、耐力、疲劳 | 食物需要消化；耐力、疲劳、能量库存互不等同。 |',
      '| 血液废物越来越多 | 血液废物、过滤、排废速率、肠道、水量 | 排废需要肠道空间与循环/水分；看速率，不能把过滤能力百分比当作 mL/h。 |',
      '| 移动变慢 | 移动悬停来源、腿伤、耐力、石板负重 | 移动显示合并后的 walkspeed，不能全部归因于生存模组。 |',
      '| 发热还是环境过热 | 核心温度、发热设定点、体感、产热/散热 | 发热提高设定点；热平衡反映环境和代谢，两个来源可同时存在。 |',
      '| 免疫储备为何不等于免疫效率 | 免疫储备、实际免疫、毒性、营养、躯干伤势 | 实际效率经过修正，可超出 100%，不是基础储备的重复显示。 |','']
    count=0
    for group,keys in arrays:
        if group not in groups: continue
        lines += [f'## {groups[group]}','','| 指标 | 单位/尺度 | 玩家读法 | 服务端取值与代码行 |','| --- | --- | --- | --- |']
        for key in keys:
            count+=1
            calls=allcalls.get(key,[])
            if key=='mobility': calls=[x for x in calls if 'combined' in x[2]] or calls
            if key=='healingrate': calls=[x for x in calls if 'text: healing' in x[2]] or calls
            helptext=LANG.get('metric-help-'+key,'按服务端快照显示。')
            if key=='jump': helptext='实际起跳速度倍率；受腿部功能、冷却与是否允许跳跃影响。不要把语言资源中旧的“跳跃增加乳酸”描述代替当前 Exertion 实现。'
            if calls:
                fn,line,expr,unit,call=calls[0]
                unit=unit or ('愈合百分点/游戏小时' if key=='healingrate' else '格式化文本' if expr.startswith('text:') else '代码原尺度')
                source=f'<code>{esc(re.sub(chr(92)+"s+"," ",expr))}</code><br>{fn}:{line}'
            else: unit='由对应专用控件提供'; source='不在 Server/Metric 静态调用中；需看专用控件，不能填零。'
            lines.append(f'| {esc(label("metric-"+key))}<br><code>{key}</code> | {esc(unit)} | {esc(helptext)} | {source} |')
        lines.append('')
    lines += ['## 面板之外与动态行','','血糖、酮症、肾过滤、氧气、肠道等键可能由服务器生成但未进入上述所有固定数组；窗口实际展示由客户端键清单决定。疾病、伤口和综合症是动态行，不是固定 58 个字段的全部。','',
      '疾病行用 `Treatments.Burden` 显示当前负担，悬停剩余小时由当前免疫病程与治疗速度计算。伤口行显示部位、种类、剩余结构损伤，悬停看愈合百分比及该伤口出血。无伤口时的愈合速率为“当前姿态下新伤口的预计速率”，不是角色正在回血。','',
      '## 显示转换','','热流从 W 乘 `3600 / 4184` 变为 kcal/h；能量从 kJ 除 `4.184` 变为 kcal；肌肉克数除 1000 成 kg。产热/散热无有效采样间隔时留空；快照过期不能解释成所有值都为零。热适应显示内部 0–1 ×15%，冷适应 ×10%，它们不是 0–100% 的适应进度。','',
      '[面板布局](/guide/character-panel) · [全部窗口](/guide/windows) · [营养](/guide/nutrition) · [公式](/develop/formulas)']
    write('guide/metric-sources.md',lines)
    return count

def conditions():
    text=read('Seraph.Core/Framework/ClinicalEffects.cs'); rows=[]
    for m in re.finditer(r'\bAdd\("([^"]+)"\s*,',text):
        a=args(text,text.index('(',m.start())+1)
        rows.append((m.group(1),re.sub(r'\s+',' ',a[1])))
    lines=['# 身体异常、症状与恢复','','疾病窗口中不全是传染病。以下项目来自 `ClinicalEffects.Evaluate`，负担大于零时才加入，严重度会夹到 0–1。命名病原见[疾病百科](/guide/diseases)。','',
      '## 玩家处理顺序','','先控制仍在持续的来源：出血、烟气、污染、缺水、寒冷或高温；然后补充可吸收的水、能量和营养并休息。耐力低、疲劳高、睡压高需要分别观察，单靠不停吃饭不能替代休息。','',
      '| 状态 | 游戏说明 | 触发/严重度表达式 |','| --- | --- | --- |']
    for id,expr in rows:
        lines.append(f'| {esc(label("effect-"+id))}<br><code>{id}</code> | {esc(LANG.get("effect-help-"+id,"以该状态的取值和阈值为准；没有独立悬停说明。"))} | <code>{esc(expr)}</code> |')
    lines += ['','## 动态生成的项目','','口渴/脱水按 `Hydration.Stage` 切换；缺铁性贫血、B 族不足、夜视受损、骨骼脆弱、维 C 不足及修复不足取对应微量营养的缺乏负担。治疗登记的投诉也会加入；恶心和腹痛另外合并感染、投诉与植物毒性后取最大值。','',
      '## 热病和失温','','低体温标签在核心温度 ≤35°C 出现。热应激在核心 ≥39.5°C，或可用水低于 800 mL 且核心温度达到 `37.5 + 发热设定点 − 37` 时成立。衣物、环境热量、风、湿身和发热需一起判断。局部冻伤另外按暴露部位计时，不能用平均皮肤温度正常来排除脚部或手臂风险。','',
      '## 烟气、中毒与废物','','烟雾剂量、一氧化碳、化学负担、药物毒性与血液废物分别记录。离开来源后还需要清除已积累负担；空气污染百分比下降不意味着所有体内指标已经恢复。血液废物通过肠道排出，肠道满会阻碍清除。','',
      '## 持续损伤如何叠加','','`DamagePerSecond` 在严重脱水、休克、极端体温、毒性和血液毒性之间取最强项，避免相关原因重复收费；败血症等其他结算仍要看各自调用点。普通症状标签出现不等于该项已经达到持续伤害阈值。','',
      '[伤口护理](/guide/care-tutorial) · [指标来源](/guide/metric-sources) · [疾病清单](/guide/diseases)']
    write('guide/conditions.md',lines)

if __name__=='__main__':
    count=diseases(); metric_count=metrics(); conditions()
    print(f'updated diseases={count}, UI keys={metric_count}, clinical effects')
