# -*- coding: utf-8 -*-
import json, re, zipfile, os, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SURV = Path(os.environ.get('SERAPH_SURVIVAL_SOURCE', r'E:\vintagestory\Seraph Living Survival Simulation'))
PACK = Path(os.environ.get('SERAPH_MODS_DIR', r'C:\Users\29596\AppData\Roaming\MVL\Modpack\测试服务器\Mods'))
SRC = SURV / 'src'
LANG = json.loads((SURV/'assets/vsslssmod/lang/zh-cn.json').read_text(encoding='utf-8-sig'))

def esc(x):
    return str(x).replace('|', r'\|').replace('\n','<br>').replace('<','&lt;').replace('>','&gt;')
def write(rel, lines):
    # Legacy extraction is draft-only: it must never overwrite reviewed player pages.
    p=ROOT/'scripts/generated/legacy'/rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text('\n'.join(lines)+'\n', encoding='utf-8')
def lang(key, default=None):
    return LANG.get(key, default or key)

# Nutrition definitions and all release food calibration records.
nutrition_src=(SRC/'Seraph.Core/Framework/NutritionState.cs').read_text(encoding='utf-8')
nutrients=[]
for m in re.finditer(r'new\("([^"]+)",\s*"([^"]*)",\s*([0-9.]+)', nutrition_src):
    nutrients.append((m.group(1), m.group(2), m.group(3)))
foods=json.loads((SURV/'assets/vsslssmod/config/foods.json').read_text(encoding='utf-8-sig')).get('Foods',[])
lines=['# 营养系统与完整食物清单','', '> 证据：`Seraph.Core/Framework/NutritionState.cs`、`MicroNutrition.cs` 与 `assets/vsslssmod/config/foods.json`。以下数值是当前源码/发布资源的游戏数据，不代表现实医疗建议。','', '## 运行时营养槽位','', '| ID | 单位 | 日预算 | 代码中的上限/消耗规则 |','| --- | --- | ---: | --- |']
known={
 'carbohydrate':('g','275','日预算 × 3，按连续生理时间'), 'protein':('g','75','日预算 × 3，按连续生理时间'),
 'fat':('g','70','日预算 × 3，按连续生理时间'), 'fiber':('g','30','日预算 × 3；进入肠道残渣，不成为身体储备'),
 'electrolytes':('g','3.5','日预算 × 3；钠/钾进入电解质账本'), 'calcium':('%','22','微量素储备上限 100'),
 'a':('%','22','维生素 A；上限 100，半衰期 4 h，100/30 点/日'), 'd':('µg','15','保留 D 槽位；微量素上限 100'),
 'k':('µg','120','保留 K 槽位；微量素上限 100'), 'bcomplex':('%','22','B 复合；半衰期 2 h，100/7 点/日'),
 'iron':('%','22','铁负担参与恢复/出血修正'), 'zinc':('%','22','锌储备；独立 zinc 校准开启'), 'c':('%','22','维生素 C；半衰期 1 h，100/7 点/日')}
for n in nutrients:
    k=n[0]; u,b,r=known.get(k,('',n[2],'')); lines.append(f'| `{esc(k)}` | {u} | {b} | {r} |')
lines += ['', '`Starting()` 将碳水、蛋白、脂肪、纤维储备置 0；其他营养置最大值的 50%，所有槽位 `Known=true`。除四个宏量槽位外，微量营养按游戏日推进；`NutritionBands.Stage` 当前实现为 `<=0.01 Empty`、`<=80 Normal`、`>80 Abundant`，`VeryLow/Low` 枚举存在但当前 Stage 不返回。','', '## 食品校准字段','', '`foods.json` 顶层格式为 `seraph.release.foods`/版本 1。每条记录由 `Codes`、来源、置信度、准备方式、份量基准、含水量、能量、钠钾、四种宏量营养及微量营养组成。服务器只接受模组注册或校准记录，未映射食品会增加 `UnmappedPortions`，不会猜测营养。','', '## 当前发布资源的完整食物表','', f'共 **{len(foods)}** 条校准记录；同一行的多个代码共享同一份量数据。','', '| 代码 | 来源/置信度 | 每份克数 | 水 g | 能量 kJ | 碳水/蛋白/脂肪/纤维 g/100g | 微量字段（每100g） |','| --- | --- | ---: | ---: | ---: | --- | --- |']
for f in foods:
    codes=', '.join(f.get('Codes',[])); p=f.get('Per100G',{}); mi=f.get('MicroPer100G',{})
    macro='/'.join(f'{p.get(x,0):g}' for x in ['carbohydrate','protein','fat','fiber'])
    micros='; '.join(f'{k}={v:g}' for k,v in mi.items())
    src=f"{f.get('Source','未声明')} / {f.get('Confidence','未声明')}"
    lines.append(f"| `{esc(codes)}` | {esc(src)} | {f.get('PortionG','—')} | {f.get('WaterGPer100G','—')} | {f.get('EnergyKJPer100G','—')} | {macro} | {esc(micros)} |")
lines += ['', '## 原版与整合包覆盖边界', '', '本机当前可核验到的是 Seraph 发布的 414 条食品校准记录。原版游戏营养值可能由运行时 `CollectibleObject`、配方或其他模组动态提供；工作区未发现可读取的 `Vintagestory.exe` 原版资产，因此不能把未映射代码补成“原版完整清单”。整合包静态资源中的 `NutritionProps` 也可能被 patch 或运行时桥接覆盖；请以本页校准表和服务器诊断为准。']
write('guide/nutrition.md', lines)

# Diseases and immune formulas.
path_src=(SRC/'Seraph.Core/Framework/Pathogens.cs').read_text(encoding='utf-8')
pat=[]
for m in re.finditer(r'new\("([^"]+)",\s*"([^"]+)",\s*ExposureRoute\.([A-Za-z]+),\s*new\("[^"].*?,\s*([0-9.]+),\s*([0-9.]+),\s*([0-9.]+),\s*([0-9.]+)\)\)', path_src):
    id,agent,route,inc,sym,rec,severity=m.groups(); pat.append((id,agent,route,float(inc)*30,float(sym)*30,float(rec)*30,float(severity)))
pat += [('water-enteric','水源肠道病原体','Ingestion',9000,54000,45000,.6),('wound-local','局部伤口病原体','OpenWound',18000,108000,81000,.5)]
lines=['# 疾病清单、病程与应对','', '> 来源：`Pathogens.cs` 的病原定义、`FrameworkKernel.cs` 的病程推进、`ImmuneSystem.cs` 的免疫修正、`Treatments.cs` 的治疗效果。源码将 PathogenProfile 中的秒数统一乘以 30；表中为运行时生物秒。','', '## 阶段与免疫公式','', '`DiseasePhase` 顺序为 Exposed → Incubating → Symptomatic → Recovering。暴露由服务器确认事件调用 `Expose`，不是客户端随机诊断。有效免疫 `Effective = clamp(ImmuneReserve × (1 + 微营养加成) × (1−0.4×躯干结构损伤) × (1−0.3×最大毒性), 0.1, 1.5)`；易感度 `1 + (1−Effective)×1.5`。潜伏期乘 `(1−缺口×0.25)`，症状期乘 `(1+缺口×0.75)`，恢复期乘 `(1+缺口×0.5)`。','', '| ID | 病原 | 路径 | 潜伏生物秒 | 症状生物秒 | 恢复生物秒 | 初始严重度 |','| --- | --- | --- | ---: | ---: | ---: | ---: |']
for x in pat: lines.append(f'| `{x[0]}` | {x[1]} | {x[2]} | {x[3]:g} | {x[4]:g} | {x[5]:g} | {x[6]:g} |')
lines += ['', '## 逐病原说明','', '> 每一项均直接对应 `Pathogens.All` 或 `Pathogens.Definitions`。源码只定义病原、路线、病程和严重度；具体投诉由 `Complaint` 注册表在症状阶段产生，因此没有在源码中出现的症状文字不会被本页臆造。', '']
route_help={'Ingestion':'从食物、水或胃肠内容物进入；优先过滤后煮沸/蒸馏，并清洁手部。','OpenWound':'从开放伤口进入；止血、清洁伤口并避免再次污染。','Airborne':'空气传播；通风、降低烟雾/空气污染并使用已注册的呼吸防护。','Skin':'皮肤接触；清洁皮肤和污染物，避免接触可疑材料。','Internal':'内部适配器确认的感染；依据 `/vsslssmod check` 的病原 ID 使用匹配治疗。','Vector':'媒介适配器确认的感染；减少媒介暴露并在出现病程后使用匹配治疗。'}
for x in pat:
    lines += [f'### `{x[0]}` · {x[1]}', '', f'- **路线**：`{x[2]}`；{route_help.get(x[2],"按诊断来源处理")}', f'- **源码病程**：潜伏 {x[3]:g} 生物秒，症状 {x[4]:g}，恢复 {x[5]:g}；初始严重度 `{x[6]:g}`。免疫缺口会按上方公式修正阶段时长。', '- **玩家处理**：先在 C 键免疫面板或 `/vsslssmod check` 确认 ID、阶段和投诉，再选择 `TreatmentDefinition.Pathogens` 或 `Symptoms` 匹配的治疗；重复剂量会受同组、5 小时窗口、恶心和毒性规则限制。', '- **可见表现边界**：源码没有为该 ID 单独写医学症状段落；显示的发热、食物中毒、痢疾、普通感冒或败血症标签来自 `DiseaseSyndromes` 的分组映射。', '']
lines += ['## 按传播路径的玩家应对','', '| 路径 | 代码判定与实际操作 |','| --- | --- |', '| Ingestion（水/食物） | `Pathogens.Enteric/Fecal` 将水源肠道病原体及除旋毛虫外的摄入病原归类；饮用前过滤/煮沸/蒸馏，处理排泄物后清洁双手，避免生食和污染水。 |', '| OpenWound | 伤口感染风险由伤口状态与 `WoundInfectionHazardPerSecond` 驱动；保持清洁、使用需要伤口的 Topical treatment，并避免再次污染。 |', '| Airborne | 呼吸暴露按空气病原负荷和防护适配器采样；通风、远离烟气/污染源、使用已登记呼吸防护。 |', '| Skin/Internal/Vector | 由服务器的接触、内部或媒介适配器产生；源码没有把这些路径自动等同为饮水，需按诊断的 `Pathogen` 和暴露来源处理。 |', '', '## 症状与诊断边界','', '疾病面板显示已进入病程的 ID 与阶段；`Effective`、白细胞、污染、疼痛和治疗投诉是可观察代理。源码没有为每个病原硬编码一套医学症状文本，症状通过 `Complaint`/治疗注册表按来源添加，因此“没有投诉”不能证明未暴露。管理员可用 `/vsslssmod check` 查看自身状态、`probe` 查看环境与时钟。', '', '## 病原到综合症的源码映射', '', '| 综合症 | 病原 ID | 游戏表现 |', '| --- | --- | --- |', '| `FoodPoisoning` | `salmonella`, `trichinosis`, `norovirus`, `ecoli`, `water-enteric` | 有症状阶段会在结算时把胃内容物转入肠道并损失部分水、能量与营养队列。 |', '| `Dysentery` | `shigella` | 与食物中毒分组独立显示；具体投诉仍由 Complaint 注册产生。 |', '| `Fever` | `qfever`, `tularemia`, `histoplasmosis`, `pasteurella`, `sporotrichosis`, `murinetyphus`, `malaria`, `anthrax`, `tetanus`, `wound-staph`, `wound-local`, `respiratory` | 发热设定点为 `37 + 2 × Fever 严重度`。 |', '| `CommonCold` | `common-cold` | 客户端按综合症标签显示普通感冒。 |', '| `Sepsis` | 伤口葡萄球菌、局部伤口、巴氏杆菌、炭疽 | 严重症状且脱水/低血容量/意识危险持续达到配置时进入败血症；恢复需要危险条件解除并持续恢复时间。 |']
write('guide/diseases.md', lines)

# C-key metric tables from actual panel arrays and localization.
cm=(SRC/'Seraph/Client/CharacterMetricsPanel.cs').read_text(encoding='utf-8')
groups=[]
for name,body in re.findall(r'private static readonly string\[\] (\w+) = \[(.*?)\];', cm, re.S):
    keys=re.findall(r'"([^"]+)"', body); groups.append((name,keys))
lines=['# C 键角色面板逐项属性','', '> 证据：`CharacterPanelIntegration.cs`、`CharacterMetricsPanel.cs`、`CharacterImmunePanel.cs`、`NutritionPanel.cs`、`NutritionHandbookDialog.cs` 与中文语言资源。打开原版角色窗口后，Seraph 将身体、血液循环、疾病恢复、能量、功能、体温调节、营养和环境面板挂入同一 C 键界面。数值来自服务器快照；没有新鲜快照时界面留空。','', '## 窗口布局','', '| 面板 | 源码数组/组件 | 功能 |','| --- | --- | --- |', '| 身体/营养 | `StatusKeys` + `NutritionPanel` | 水量、肌肉量、胃/肠道图、糖原/脂肪能量与营养储备 |','| 血液循环 | `BloodCirculationKeys` | 血量、心肺、毒性、代谢 |','| 疾病恢复 | `DiseaseRecoveryKeys` + `CharacterImmunePanel` | 卫生、免疫、白细胞、疼痛和可滚动疾病列表 |','| 能量平衡 | `EnergyStatusKeys` + `EnergyDemandKeys` | 耐力/疲劳/睡压及能量需求 |','| 功能 | `FunctionKeys` | 意识、移动、操作、跳跃、治疗等倍率 |','| 体温调节 | `ThermoregulationKeys` | 核心/皮肤温度、湿润、产热散热 |','| 环境 | `EnvironmentKeys` | 气温、湿度、风、通风、污染 |','', '### 营养窗口的特殊元素', '', '- 胃部圆形图按水、碳水、蛋白、脂肪、纤维和残渣分层；旁边的肠道图按 `BowelUnits/5000g` 填充。', '- 能量行显示糖原、脂肪能量和胃内能量；宏量营养显示当前值/最大值，微量营养显示 0–100 分数。', '- 面板把铁和锌合并为 `ironzinc` 行，取两者相对储备较低者；D、K 和独立锌不单独展示。', '- `NutritionHandbookDialog` 使用服务器同源的食品份量、能量、水和营养数据；未连接服务器时不会用客户端猜测值。', '', '### 免疫窗口的特殊元素', '', '- 疾病恢复面板在摘要指标下方显示疾病、伤口和综合症行，最多 80 行，内容区域可滚动。', '- 没有疾病时显示 `effect-none`；快照过期时显示未知，而不是把 0 当成健康。', '- 每行悬停文本来自服务器 `PanelMetric.Detail`，疾病行显示病原、阶段或 Complaint 详情。', '', '## 逐项属性','']
for name,keys in groups:
    title={'StatusKeys':'身体状态','BloodCirculationKeys':'血液循环','EnergyStatusKeys':'能量状态','EnergyDemandKeys':'能量需求','FunctionKeys':'功能倍率','DiseaseRecoveryKeys':'疾病恢复','ThermoregulationKeys':'体温调节'}.get(name,name)
    lines += [f'### {title}','', '| 键 | 中文标题 | 单位/显示 | 源码 tooltip |','| --- | --- | --- | --- |']
    for k in keys:
        label=lang('metric-'+k,k); helptext=lang('metric-help-'+k,'源码未提供独立 tooltip；数值来自服务器 `PanelMetric`.')
        unit={'bodywater':'g','musclemass':'kg','blood':'L','bleeding':'mL/min','bloodwaste':'mL','bloodregen':'mL/h','bloodclearance':'mL/h','heatproduction':'kcal/h','heatloss':'kcal/h','heatbalance':'kcal/h','shivering':'kcal/h','sweat':'L/h','coretemp':'°C','skintemp':'°C','feelslike':'°C','radianttemp':'°C'}.get(k,'由服务器 metric.Unit')
        lines.append(f'| `{k}` | {esc(label)} | {unit} | {esc(helptext)} |')
lines += ['', '### 环境键（`CharacterPanelIntegration.EnvironmentKeys`）','', '| 键 | 中文标题 | tooltip |','| --- | --- | --- |']
for k in ['airtemp','humidity','wind','roomheat','ventilation','airpollution','environmentalcontamination']:
    lines.append(f'| `{k}` | {esc(lang("metric-"+k,k))} | {esc(lang("metric-help-"+k,"未提供"))} |')
lines += ['', '## 数值如何阅读','', '带条形图的键会按服务器提供的 `Minimum/Maximum` 投影到 0–1；标签仍显示物理值。功能面板显示百分比倍率。血液循环、疾病恢复、体温调节和环境使用内联文本；悬停可以看到 `PanelMetric.Detail`。趋势箭头来自客户端 `MetricTrendDisplay`，不是新的生理变量。']
write('guide/character-panel.md', lines)

# Treatments and developer API.
t=(SRC/'Seraph.Core/Framework/Treatments.cs').read_text(encoding='utf-8')
lines=['# 治疗、护理与剂量规则','', '> 证据：`Treatments.cs`、`TreatmentApi.cs`。模组治疗是游戏机制；源码明确写明不代表现实医疗剂量。','', '## TreatmentDefinition 字段','', '| 字段 | 默认值/范围 | 作用 |','| --- | --- | --- |', '| `Id` / `Group` | 非空，最多 96 字符 | ID 用于效果；Group 决定同类效果互斥 |','| `Route` | `Oral` / `Topical` | 必须与调用路由一致 |','| `Pathogens` / `Symptoms` | 每项最多 16 | 匹配病原恢复速度或投诉缓解 |','| `DelaySeconds` | 0–108000，默认 60 | 开始后延迟 |','| `DurationSeconds` | 1–2592000，默认 900 | 活性持续时间 |','| `Relief` | 0–0.6，默认 0.4 | 症状缓解 |','| `RecoveryBonus` | 0–1.5，默认 1 | 病原恢复速度加成 |','| `SleepSupport` | 0–0.3 | 睡眠质量加成 |','| `WoundRepair` / `CleanFraction` / `Hemostasis` | 0–1 | 伤口修复、清洁、止血；必须 `RequiresWound=true` |','| `WaterL` / `AlcoholL` / `Toxicity` | 0–0.25 / 0.05 / 1 | 饮水、酒精负担、药物毒性 |','', '## 实际应用规则','', '`Apply` 会验证状态、路由、伤口、唯一 receipt、同组活动效果和最多 32 个活动治疗；同组已有效果时保留更强定义但不叠加延长时长。5 小时生物时间内同组重复剂量会记录，第二次及以后可能添加 `nausea`；有 SleepSupport 会添加 `sedated`。毒性按 `Toxicity + (repeats >= 2 ? 0.2 : 0)` 累加，酒精按 `AlcoholL×20` 累加。','', '## 玩家操作建议','', '先用 C 键和 `/vsslssmod check` 判断投诉/病程，再选择匹配病原或症状的物品；Topical 只能对有效伤口使用，口服治疗不能带伤口参数。连续重复使用会增加恶心和毒性，等待活动窗口结束。']
write('guide/treatments.md', lines)

api_src=(SRC/'Seraph/TreatmentApi.cs').read_text(encoding='utf-8'); contracts=(SRC/'Seraph.Application/IntegrationContracts.cs').read_text(encoding='utf-8')
lines=['# 开发者 API 与适配器契约','', '> 本页只记录源码中明确公开的 `Seraph`/`Seraph.Application` API；内部类和 Vintage Story 原生 API 不在此冒充稳定接口。','', '## 治疗注册 API','', '| 方法 | 签名/行为 | 错误条件 |','| --- | --- | --- |', '| `RegisterTreatmentV1` | `RegisterTreatmentV1(string itemCode, TreatmentDefinition definition)`；启动时注册一次，复制数组快照 | AssetLocation 字符串不规范、定义校验失败、重复 item code 抛 `ArgumentException` |','| `QueryTreatment` | 检查手持物品与路由，不启动、不消费、不改生理 | 未注册物品 `treatment-unknown`；服务端不可用 `treatment-unavailable` |','| `BeginTreatment` | 服务端开始动作，返回 `TreatmentUseResult` | 同上及服务端动作条件 |','| `ContinueTreatment` | `bool`；继续已开始动作 | 无活动返回 false |','| `CompleteTreatment` | 完成并由服务器验证消费/效果 | 不可用返回 `treatment-unavailable` |','| `CancelTreatment` | 取消当前玩家治疗 | 无返回值 |','| `ReadHerbalWater` | 读取已验证的 `WaterBatch`，优先使用核心世界 API | 未接入核心时读取本地 metadata |']
lines += ['', '## IntegrationContracts','', '| 类型 | 成员 | 用途 |','| --- | --- | --- |', '| `AdapterEvidence` | `AdapterId`, `ProviderVersion`, `UnitsVerified`, `Evidence` | 适配器必须证明单位和来源 |','| `RoomSample` | `Enclosed`, `WindAttenuation`, `RadiantDeltaC`, `Evidence` | 房间/热环境采样 |','| `ExposureSample` | `EventId`, `Pathogen`, `Route`, `HazardPerBioSecond`, `Evidence` | 服务器确认暴露 |','| `InjurySample` | `EventId`, `WoundKind`, `Region`, `Severity`, `BleedLps`, `Evidence` | 服务器命中部位与伤口 |','| `FoodPortion` | 代码、水 L/份、能量 kJ/份、质量 g/份、证据 | `Receipt` 只接受 UnitsVerified 且份数 0–1 |','| `IRoomEnvironmentAdapter` | `TrySample(playerUid, out RoomSample)` | 可选环境提供者 |','| `IExposureAdapter` | `Sample(playerUid, bioSeconds)` | 提供暴露事件 |','| `IInjuryAdapter` | `TryResolve(serverDamageEvent, out InjurySample)` | 解析伤害部位 |','| `IDownedDelegate` | `ProviderId`, `OwnsRevival`, `IsDowned`, `TryEnter`, `TryRescue` | 倒地/复苏所有权协商 |','', '## 兼容实现原则','', '所有生理写入都由服务端控制；客户端只显示快照。`AdapterEvidence.UnitsVerified=false` 的数据不得进入物理账本；不能把饱食度自动推断成食品能量。']
write('develop/api.md', lines)

# Commands page, based on registrations and handlers.
lines=['# 管理员指令完整参考','', '> 以下命令从三个模组的命令注册代码提取。权限以源码 `.RequiresPrivilege` 和 handler 二次检查为准。','', '## Living Survival Simulation（`/vsslssmod`）','', '| 命令 | 权限/执行者 | 实际行为 |','| --- | --- | --- |', '| `/vsslssmod` | `chat` | 输出模式、在线会话数、边界状态和版本 |','| `/vsslssmod check` | `chat`、玩家 | 读取自身状态诊断 |','| `/vsslssmod drink` | `chat`、玩家 | 触发一次服务器验证饮水 |','| `/vsslssmod pressure` | `chat`、玩家 | 开始医疗压力动作 |','| `/vsslssmod clean` | `chat`、玩家 | 开始清洁护理动作 |','| `/vsslssmod cancel` | `chat`、玩家 | 取消护理动作 |','| `/vsslssmod mode <mode>` | `controlserver` | 运行时设置 `survival`/`shadow`/`observe`，经配置校验和版本递增 |','| `/vsslssmod compat` | `controlserver` | 列出 capability owner 与 provider |','| `/vsslssmod probe` | `controlserver`、玩家 | 强制快照并输出时钟、环境、质量行 |','| `/vsslssmod speed <倍率>` | `controlserver` | 当前 handler 返回 speed 配置提示；实际设置走设置协议，不把聊天参数直接写入 |','', '客户端调试命令：`.vsslssmodhud` 切换 HUD，`.slssdebug` 打开调试窗口，`.slsspollution` 切换污染高亮，`.slssperf start|stop|status` 管理性能采样。','', '## Civilization Simulation（`/vsscsmod` / `/vscncs`）','', '| 命令族 | 权限 | 子命令/用途 |','| --- | --- | --- |', '| `statuscopy` | 玩家可用 | 只导出自己的状态 |','| `name` | `controlserver` | 名称校验/重置 |','| `territory debug` | `controlserver`、游戏内管理员 | 领地调试 |','| `tribe` | `controlserver` | `list`、`delete <部落名>`、`solo on\|off\|toggle\|status` |','| `sleep` | `controlserver` | `on\|off\|toggle\|status` |','| `cluster` | `chat` 的 `info`；管理操作需 `controlserver` | `infoall`、`list`、`who`、`tp`、`assign`、`reset`、`resetall`、`reroll` |','| `content` | `controlserver` | 公告/教程 `list\|add\|edit\|delete\|clear` |','| `reset` | `controlserver` | `<玩家>`、`start <正整数>`、`stop` |','| `resetall` | `controlserver` | 重置所有玩家死亡计数 |','| `reload` | `controlserver` | `config` 或 `content [all\|announcements\|tutorials]` 热重载 |','', '## Civilization Patches（`/vsscpmod`）','', '| 命令 | 权限 | 行为 |','| --- | --- | --- |','| `/vsscpmod` | `chat` | `info status\|on\|off\|reload`、`fixstack`、`trunkrelease` |','| `.vsscpmod inventory start\|stop` | 客户端 | 切换 CarryOn 兼容库存诊断 |','', '命令行为可能被兼容模组是否加载、服务端/客户端侧和当前版本 API 改变；排障时保留服务器日志中的 capability/compatibility 输出。']
write('admin/commands-full.md', lines)

# Pack progression and configuration evidence.
lines=['# 整合包真实资源与玩法路线','', '> 本页基于本机 `Mods` 目录的 129 个安装包/目录、资源索引、语言/手册 JSON、DLL 类型索引和 Seraph 源码。没有资源或程序集证据的玩法不会在此臆测。','', '## 从零到稳定生存','', '1. 先阅读[生存手册章节](/guide/handbook)，再用原版 H 搜索 `vsslssmod` 条目；手册由 `assets/vsslssmod/config/handbook` 逐条解析。\n2. 建立饮水闭环：记录水源 → 使用过滤/排水/浴缸相关方块 → 观察 C 键水量与污染 → 只饮用经过服务器验证的液体。\n3. 建立卫生闭环：处理排泄物、清洁双手、避免把污染水带入食物；疾病暴露按真实交互路径进入。\n4. 建立营养闭环：用本页[营养表](/guide/nutrition)选择有校准记录的食品；没有映射的食品不会被自动猜测。\n5. 建立休息/劳动节奏：监控耐力、疲劳、睡压、核心温度和出汗负担；坐下或睡眠会触发源码中的恢复路径。\n6. 受伤后先看血量、出血、疼痛、白细胞和疾病恢复面板，再进行匹配护理；治疗不要连续盲目重复。','', '## 手册没有覆盖的补齐规则','', '- C 键所有字段的实际源码数组和 tooltip 见[角色面板](/guide/character-panel)。\n- 疾病阶段、传播路径、免疫修正见[疾病清单](/guide/diseases)。\n- 治疗定义的剂量容量、重复剂量和毒性规则见[治疗规则](/guide/treatments)。\n- 管理员应先用 `/vsslssmod compat` 确认 capability owner，再改配置；配置失败时服务器保留上一次有效值。','', '## 资源覆盖与限制','', '每个整合包条目的“安装包实现证据”列出实际方块、物品、配方、patch、手册、配置和可反编译 DLL 类型。DLL 类型索引证明类型存在，不能单独证明某个世界条件下必然启用；无源码的第三方行为必须按反编译证据和运行日志复核。']
write('pack/overview.md', lines)

# Config full top-level table from source property declarations.
cfg=(SRC/'Seraph.Application/SeraphServerConfig.cs').read_text(encoding='utf-8')
rows=[]
for m in re.finditer(r'^\s*public\s+([\w<>?,]+)\s+(\w+)\s*\{\s*get;\s*init;\s*\}\s*=\s*([^;]+);', cfg, re.M): rows.append(m.groups())
lines=['# 生存配置字段（源码默认值）','', '> 从 `SeraphServerConfig.cs` 顶层属性声明提取；嵌套 `SurfaceWater`、`DiseaseExposure`、`Sanitation`、`Exertion`、`ThermalAdaptation`、`Pain`、`Circulation`、`Digestion` 仍需展开对应类型的 `Validate` 与默认值。','', '| 类型 | 字段 | 默认表达式 |','| --- | --- | --- |']
for typ,name,val in rows: lines.append(f'| `{typ}` | `{name}` | `{esc(val)}` |')
lines += ['', '## 校验边界','', '`Format` 必须为 `seraph.release.config`，`ConfigVersion=1`；`Mode` 只能 `survival`、`shadow`、`observe`；`PhysiologySpeed` 只能 0.1–20；检查点 10–300 秒；饮水份量 0.01–1 L；所有对象和映射都有数量/数值上限。修改后使用 `/vsscsmod reload config` 仅适用于文明配置；生存配置由 `vsslssmod.Server.json` 启动时读取，重启后验证。']
lines += ['', '## 嵌套选项默认值与校验', '', '以下表格直接来自配置属性所引用的 record 类型；范围来自各类型的 `Validate()`。', '']
option_files = {
    'DiseaseExposure':'DiseaseSyndromes.cs', 'SurfaceWater':'SurfaceWater.cs', 'Sanitation':'Sanitation.cs',
    'ThermalAdaptation':'ThermalAdaptation.cs', 'Pain':'WoundPain.cs', 'Circulation':'BloodCirculation.cs',
    'Exertion':'Exertion.cs', 'Digestion':'DigestionOptions.cs'}
for opt, fn in option_files.items():
    src = (SRC/'Seraph.Core/Framework'/fn).read_text(encoding='utf-8')
    mm = re.search(r'(?:record|class)\s+'+re.escape(opt)+r'Options\s*\{(.*?)\n\}', src, re.S)
    if not mm: continue
    lines += [f'### `{opt}`', '', '| 类型 | 字段 | 默认值 |', '| --- | --- | --- |']
    for typ, name, val in re.findall(r'public\s+([\w<>?]+)\s+(\w+)\s*\{\s*get;\s*init;\s*\}\s*=\s*([^;]+);', mm.group(1)):
        lines.append(f'| `{typ}` | `{name}` | `{esc(val)}` |')
write('admin/survival-config-full.md', lines)

print(f'generated foods={len(foods)} pathogens={len(pat)} metrics={sum(len(k) for _,k in groups)} config={len(rows)}')
