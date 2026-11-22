<!-- generated:start -->
# C 键数值：单位与读法

按 C 打开角色窗口，在下表查找属性名称。展开“标识与计算”可查看属性标识和计算式。百分比标尺不一定代表概率；移动倍率可以含原版、负重及其他模组的修正。

## 操作与窗口固定

按 C 打开角色窗口。将指针停在数值上查看原因和收支趋势；有滚动条的窗口可向下查看。可固定的六个窗口在标题栏有固定按钮：身体、血液循环、疾病恢复、功能、能量平衡、体温调节。固定后关闭 C 仍可显示；环境窗口没有固定按钮，退出世界会清除本次固定记录。

## 按问题找指标

| 想判断的问题 | 连着看哪些值 | 如何读 |
| --- | --- | --- |
| 喝水为什么没恢复 | 水量、胃水、消化、出汗、出血 | 胃内水尚未等于可用水；吸收和损失可同时发生，悬停看两路流量。 |
| 吃饱为什么还没力气 | 胃内容物、糖原、血糖、耐力、疲劳 | 食物需要消化；耐力、疲劳、能量库存互不等同。 |
| 血液废物越来越多 | 血液废物、过滤、排废速率、肠道、水量 | 排废需要肠道空间与循环/水分；看速率，不能把过滤能力百分比当作 mL/h。 |
| 移动变慢 | 移动悬停来源、腿伤、耐力、石板负重 | 移动显示合并后的 行走速度属性，不能全部归因于生存模组。 |
| 发热还是环境过热 | 核心温度、发热设定点、体感、产热/散热 | 发热提高设定点；热平衡反映环境和代谢，两个来源可同时存在。 |
| 免疫储备为何不等于免疫效率 | 免疫储备、实际免疫、毒性、营养、躯干伤势 | 实际效率经过修正，可超出 100%，不是基础储备的重复显示。 |

## 身体状态

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 水量 | g | 可用水量（克）。基础失水 75 mL/h，出汗、疾病和出血另计。胃水半衰期为 1/3 游戏小时，吸收上限为 2000 mL/h；体水已满时，未吸收的水留在胃内；电解质和可用碳水支持水分留存，严重蛋白质或脂肪缺乏会小幅降低吸收。 | <details><summary>标识与计算</summary>标识：<code>bodywater</code><br><code>ReserveDisplay.HydrationG(s.State, s.Profile)</code></details> |
| 肌肉量 | kg | 肌肉质量，单位 kg。劳动积累训练储备，休息或睡眠消耗储备、已吸收蛋白质和能量来增肌。 | <details><summary>标识与计算</summary>标识：<code>musclemass</code><br><code>s.State.MuscleMassG / 1000</code></details> |

## 血液循环

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 血量 | L | 血量，单位 L。 | <details><summary>标识与计算</summary>标识：<code>blood</code><br><code>s.State.BloodVolumeL(s.Profile)</code></details> |
| 心率 | bpm | 当前心跳频率。 | <details><summary>标识与计算</summary>标识：<code>heartrate</code><br><code>AdrenalineEffects.HeartRate(s.Framework)</code></details> |
| 呼吸频率 | min⁻¹ | 当前呼吸频率。 | <details><summary>标识与计算</summary>标识：<code>breathrate</code><br><code>s.Framework.BreathDemandPerMinute</code></details> |
| 出血速率 | mL/min | 实际出血量（mL/min）。新伤每点实际损伤初始出血 1.122 mL/游戏分钟，总出血速率最高 12 mL/游戏分钟；自然凝血缓慢，新重伤未经处理保留出血底限。按压减流 90%；肾上腺素和充足营养也可减少出血，绷带可止血。 | <details><summary>标识与计算</summary>标识：<code>bleeding</code><br><code>ClinicalBleeding(s) * 60000</code></details> |
| 血液废物 | mL | 实际废物来自能量消耗、蛋白质修复、吸收的浑浊物、酒精、盐、免疫清除和营养过滤。基础过滤能力为 72 mL/h；肠道满时无法过滤。废物负荷达到 40% 后会逐步影响意识和劳动。 | <details><summary>标识与计算</summary>标识：<code>bloodwaste</code><br><code>s.Framework.Blood.WasteMl</code></details> |
| 血液毒性强度 | %（0–100 标尺） | 这里显示功能毒性强度，不是原始废物负荷。废物负荷在 40/55/70/85% 分阶段警告；毒性强度从负荷 40% 时的 0% 线性增加至负荷 85% 时的 100%。 | <details><summary>标识与计算</summary>标识：<code>bloodtoxicity</code><br><code>s.Framework.Blood.Toxicity * 100</code></details> |
| 血液再生 | mL/h | 当前实际造血速度，需要已吸收蛋白、能量和充足水分。 | <details><summary>标识与计算</summary>标识：<code>bloodregen</code><br><code>s.Framework.Blood.RegenerationMlPerGameHour</code></details> |
| 血液过滤 | %（0–100 标尺） | 循环、躯干伤势和脱水决定过滤能力；肠道满载时无法排废。 | <details><summary>标识与计算</summary>标识：<code>bloodfiltration</code><br><code>BloodCirculation.Filtration(s.Framework, s.State, s.Profile) * 100</code></details> |
| 排废速率 | mL/h | 当前实际从血液转入肠道的废物量。 | <details><summary>标识与计算</summary>标识：<code>bloodclearance</code><br><code>s.Framework.Blood.FiltrationMlPerGameHour</code></details> |
| 血糖 | mmol/L | 血液中可供组织使用的葡萄糖。血糖不足会影响意识和身体机能。 | <details><summary>标识与计算</summary>标识：<code>bloodglucose</code><br><code>s.Framework.Clinical.BloodGlucoseMmol</code></details> |
| 乳酸 | g | 只有疾跑爆发会缓慢增加乳酸，每秒 0.1 g；连续 10 秒约增加 1 g。劳动、攻击、跳跃和点火不会增加乳酸，其体力消耗另行计算。乳酸不会逐渐削弱普通劳动；满载时会阻止疾跑爆发并强制慢跑。站立、步行、坐姿半衰期分别为 180、300、150 现实秒；循环不足会减慢恢复。肌肉酸痛单独恢复。 | <details><summary>标识与计算</summary>标识：<code>lactate</code><br><code>s.Framework.Blood.LactateG</code></details> |

## 能量状态

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 耐力 | %（0–100 标尺） | 疾跑键先冲刺 3 s，再用 1 s 过渡为快跑。营养增益前健康冲刺消耗 1%/s，快跑消耗 0.6%/s；碳水、蛋白、脂肪和电解质各可增加最多 5% 耐力续航；低于 20% 逐渐降速，耗尽后只能慢跑。快跑和慢跑均不恢复耐力。松开强动作 2 s 后坐姿恢复 4.8%/s、站立 2.4%/s、步行 1.2%/s；伤病影响实际速率。 | <details><summary>标识与计算</summary>标识：<code>stamina</code><br><code>s.Framework.Stamina * 100</code></details> |
| 疲劳 | %（0–100 标尺） | 越低越好。活动按实际消耗的能量积累疲劳；按原版 G 坐下或真正入睡可缓解。 | <details><summary>标识与计算</summary>标识：<code>fatigue</code><br><code>s.Framework.Fatigue * 100</code></details> |
| 睡压 | %（0–100 标尺） | 清醒时累积；床上睡眠恢复最快，K键合眼较慢。 | <details><summary>标识与计算</summary>标识：<code>sleeppressure</code><br><code>s.State.SleepPressure * 100</code></details> |

## 能量需求

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 基础代谢 | kcal/h | 维持身体基础机能实际支付的能量，单位为 kcal/h。按最近一个约 1 s的同步区间平均。 | <details><summary>标识与计算</summary>标识：<code>energybasal</code><br><code>s.HasEnergySnapshot ? s.EnergyBasalKcalPerGameHour : null</code></details> |
| 寒冷产热 | kcal/h | 御寒与颤抖实际支付的额外能量，单位为 kcal/h。按最近一个约 1 s的同步区间平均。 | <details><summary>标识与计算</summary>标识：<code>energycold</code><br><code>s.HasEnergySnapshot ? s.EnergyColdKcalPerGameHour : null</code></details> |
| 活动消耗 | kcal/h | 移动和有效手部劳动实际支付的能量，按最近一个约 1 s的同步区间平均。重叠劳动取最高活动档：轻劳动 160、强劳动 450 kcal/h；间歇劳动按实际工作时间计费。 | <details><summary>标识与计算</summary>标识：<code>energyactivity</code><br><code>s.HasEnergySnapshot ? s.EnergyActivityKcalPerGameHour : null</code></details> |
| 修复 | kcal/h | 愈合与造血实际支付的能量，单位为 kcal/h。按最近一个约 1 s的同步区间平均。 | <details><summary>标识与计算</summary>标识：<code>energyrecovery</code><br><code>s.HasEnergySnapshot ? s.EnergyRecoveryKcalPerGameHour : null</code></details> |
| 总能量需求 | kcal/h | 基础机能、御寒、活动与恢复实际支付的能量总和，单位为 kcal/h，按最近一个约 1 s的同步区间平均。供能不足时，实际支付量会低于需求。 | <details><summary>标识与计算</summary>标识：<code>energytotal</code><br><code>s.HasEnergySnapshot ? s.EnergyTotalKcalPerGameHour : null</code></details> |

## 功能倍率

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 意识 | % | 头部、严重失血、实际窒息及酒精等影响意识。 | <details><summary>标识与计算</summary>标识：<code>consciousness</code><br><code>(f.Consciousness) * 100</code></details> |
| 移动 | % | 实际行走能力；严重伤势和明显异常会降低。 | <details><summary>标识与计算</summary>标识：<code>mobility</code><br><code>combined * 100</code></details> |
| 呼吸 | % | 胸部伤势、呼吸疾病和烟气影响呼吸能力。 | <details><summary>标识与计算</summary>标识：<code>respiratory</code><br><code>(f.RespiratoryCapacity) * 100</code></details> |
| 泵血 | % | 血量与躯干损伤决定循环；严重不足影响意识及耐力恢复。 | <details><summary>标识与计算</summary>标识：<code>circulation</code><br><code>(f.Circulation) * 100</code></details> |
| 食物消化 | % | 消化能力统一影响水、碳水、蛋白、脂肪和残渣的处理速率；腹部损伤、肠道疾病及严重寒热可使其变慢。 | <details><summary>标识与计算</summary>标识：<code>digestion</code><br><code>(f.Digestion) * 100</code></details> |
| 免疫 | % | 实际抗感染效率，与免疫系统窗口相同；影响感染、病程和康复。 | <details><summary>标识与计算</summary>标识：<code>immunity</code><br><code>(f.Immunity) * 100</code></details> |
| 操作 | % | 双臂的操作能力；严重伤势限制持物动作。 | <details><summary>标识与计算</summary>标识：<code>manipulation</code><br><code>(f.Manipulation) * 100</code></details> |
| 跳跃能力 | % | 实际起跳速度倍率；受腿部功能、冷却与是否允许跳跃影响。不要把语言资源中旧的“跳跃增加乳酸”描述代替当前体力系统实现。 | <details><summary>标识与计算</summary>标识：<code>jump</code><br><code>jumpValue * 100</code></details> |
| 滤血 | % | 血液过滤能力；受循环和缺水影响。 | <details><summary>标识与计算</summary>标识：<code>filtration</code><br><code>(f.Filtration) * 100</code></details> |
| 闪避 | % | 受到战斗攻击时的基础闪避概率。完全合眼、K 键合眼休息及睡眠期间为 0%；睁眼后恢复，睡压本身不扣除闪避。 | <details><summary>标识与计算</summary>标识：<code>dodge</code><br><code>(eyesClosed ? 0 : f.Dodge) * 100</code></details> |
| 正面闪避 | % | 面对攻击者时的闪避概率。合眼或睡眠期间为 0%。 | <details><summary>标识与计算</summary>标识：<code>dodgefront</code><br><code>(eyesClosed ? 0 : CombatFunctions.FacingDodge(f.Dodge, 1)) * 100</code></details> |
| 背后闪避 | % | 背对攻击者时的闪避概率。合眼或睡眠期间为 0%。 | <details><summary>标识与计算</summary>标识：<code>dodgeback</code><br><code>(eyesClosed ? 0 : CombatFunctions.FacingDodge(f.Dodge, -1)) * 100</code></details> |
| 脂肪减伤 | % | 脂肪提供的战斗减伤；不代替护甲。 | <details><summary>标识与计算</summary>标识：<code>fatprotection</code><br><code>(f.FatDamageReduction) * 100</code></details> |
| 肌肉近战增益 | % | 肌肉提供的近战伤害加成。 | <details><summary>标识与计算</summary>标识：<code>musclemelee</code><br><code>(f.MuscleMeleeBonus) * 100</code></details> |
| 愈合速率 | 愈合百分点/游戏小时 | 伤口每h增加的愈合百分点；不是生命值恢复量。 | <details><summary>标识与计算</summary>标识：<code>healingrate</code><br><code>text: healing</code></details> |
| 暗适应 | 由对应专用控件提供 | 随眼部光照改变；暗处逐渐辨认近处轮廓，强光会快速降低适应。 | <details><summary>标识与计算</summary>标识：<code>darkadaptation</code><br>不在 Server/Metric 静态调用中；需看专用控件，不能填零。</details> |

## 疾病恢复

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 脏污度 | % | 污染接触使身体变脏；用水清洗。 | <details><summary>标识与计算</summary>标识：<code>dirtiness</code><br><code>frame.Dirtiness * 100</code></details> |
| 免疫储备 | % | 缓慢随营养、能量、休息和体温变化的免疫储备。 | <details><summary>标识与计算</summary>标识：<code>immune</code><br><code>frame.ImmuneReserve * 100</code></details> |
| 免疫系统 | % | 用于感染和疾病康复的有效免疫效率；同种病原记忆另算。 | <details><summary>标识与计算</summary>标识：<code>immunesystem</code><br><code>ImmuneSystem.Effective(frame) * 100</code></details> |
| 愈合速率 | 愈合百分点/游戏小时 | 伤口每h增加的愈合百分点；不是生命值恢复量。 | <details><summary>标识与计算</summary>标识：<code>healingrate</code><br><code>text: healing</code></details> |
| 白细胞储备 | % | 白细胞参与免疫清除。感染和身体状况会影响可用的免疫能力。 | <details><summary>标识与计算</summary>标识：<code>whitecells</code><br><code>s.Framework.Clinical.WhiteCellReserve * 100</code></details> |
| 疼痛 | %（0–100 标尺） | 疼痛取伤口和肌肉酸痛中较强的一项。乳酸满载只限制疾跑爆发；肌肉酸痛按 h 缓慢恢复，休息和睡眠更快。 | <details><summary>标识与计算</summary>标识：<code>pain</code><br><code>s.Framework.Pain * 100</code></details> |

## 体温调节

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 核心温度 | °C | 核心温度。 | <details><summary>标识与计算</summary>标识：<code>coretemp</code><br><code>s.State.CoreTemperatureC</code></details> |
| 皮肤温度 | °C | 皮肤温度。 | <details><summary>标识与计算</summary>标识：<code>skintemp</code><br><code>s.State.SkinTemperatureC</code></details> |
| 体感温度 | °C | 综合空气、辐射、风、衣物和水接触换热的等效温度。 | <details><summary>标识与计算</summary>标识：<code>feelslike</code><br><code>s.Environment is { } boundary ? s.Kernel.EquivalentTemperatureC(boundary) : null</code></details> |
| 辐射温度 | °C | 身体表面接收到的辐射边界温度，包含附近热源。 | <details><summary>标识与计算</summary>标识：<code>radianttemp</code><br><code>s.Environment?.RadiantTemperatureC</code></details> |
| 调节目标 | °C | 正常37°C；发热时升高，寒战和散热以此为目标。 | <details><summary>标识与计算</summary>标识：<code>feversetpoint</code><br><code>DiseaseSyndromes.FeverSetpointC(s.Framework)</code></details> |
| 衣物保暖 | 格式化文本 | 衣物减少干散热的比例；寒冷时有助保温，炎热时也会妨碍散热。 | <details><summary>标识与计算</summary>标识：<code>clothing</code><br><code>text: losingHeat ? L(s.Player, "clothing-insulation-value", Math.Clamp(100 * (1 - clothed!.Value / bare!.Value), 0, 100)) : L(s.Player, "clothing-no-outward-loss")</code></details> |
| 湿润度 | % | 原版湿润程度，影响衣物与蒸发散热。 | <details><summary>标识与计算</summary>标识：<code>wetness</code><br><code>s.Player.Entity.WatchedAttributes.TryGetFloat("wetness") is { } wet ? wet * 100 : null</code></details> |
| 产热 | kcal/h | 实际代谢产生的热量，包含活动和发抖。 | <details><summary>标识与计算</summary>标识：<code>heatproduction</code><br><code>Rate(t.HeatInW * 3600 / 4184)</code></details> |
| 散热 | kcal/h | 正数为向外散热，负数为环境加热。 | <details><summary>标识与计算</summary>标识：<code>heatloss</code><br><code>Rate(t.HeatOutW * 3600 / 4184)</code></details> |
| 净热变化 | kcal/h | 正数为蓄热，负数为失热；结合核心体温判断冷暖。 | <details><summary>标识与计算</summary>标识：<code>heatbalance</code><br><code>Rate(t.NetW * 3600 / 4184)</code></details> |
| 出汗 | L/h | 实际出汗耗水；汗液蒸发后才能散热。 | <details><summary>标识与计算</summary>标识：<code>sweat</code><br><code>Rate(t.SweatLPerGameHour)</code></details> |
| 寒战 | kcal/h | 发抖消耗能量产热；已包含在体内产热中。 | <details><summary>标识与计算</summary>标识：<code>shivering</code><br><code>Rate(t.ShiveringW * 3600 / 4184)</code></details> |
| 出汗负担 | L | 尚未散去的出汗负担；不直接降低动作能力。 | <details><summary>标识与计算</summary>标识：<code>sweatdebt</code><br><code>s.State.SweatDebtL</code></details> |
| 热适应 | % | 显示适应带来的出汗增幅（0～15%），不是适应进度或体温。热需求下提高出汗反应，仍受汗量上限、水和电解质限制。 | <details><summary>标识与计算</summary>标识：<code>heatadaptation</code><br><code>s.Framework.HeatAdaptation * 15</code></details> |
| 冷适应 | % | 显示冷需求下核心向皮肤传热的减少比例（0～10%），不是降温度数或完全保温。发抖仍消耗能量。 | <details><summary>标识与计算</summary>标识：<code>coldadaptation</code><br><code>s.Framework.ColdAdaptation * 10</code></details> |

## 环境

| 属性 | 单位 | 含义与读法 | 技术说明 |
| --- | --- | --- | --- |
| 环境温度 | °C | 来自原版世界和天气的环境温度采样。 | <details><summary>标识与计算</summary>标识：<code>airtemp</code><br><code>s.Environment?.AirTemperatureC</code></details> |
| 湿度 | % | 当前环境的相对湿度。 | <details><summary>标识与计算</summary>标识：<code>humidity</code><br><code>s.Environment?.RelativeHumidity * 100</code></details> |
| 风速 | m/s | 当前环境的风速。 | <details><summary>标识与计算</summary>标识：<code>wind</code><br><code>s.Environment?.WindSpeedMps</code></details> |
| 室内外温差 | °C | 房间相对室外的温差，已计入环境温度。 | <details><summary>标识与计算</summary>标识：<code>roomheat</code><br><code>s.Environment?.RoomHeatDeltaC</code></details> |
| 通风 | % | 房间空气交换程度；低通风会积累污染和环境噪声。 | <details><summary>标识与计算</summary>标识：<code>ventilation</code><br><code>s.Environment?.RoomVentilation * 100</code></details> |
| 空气污染 | % | 当前环境采样的空气负荷。烟尘剂量、一氧化碳、毒性负荷和命名空气病原分别进入各自的人体路径。 | <details><summary>标识与计算</summary>标识：<code>airpollution</code><br><code>s.Environment?.AirPollution * 100</code></details> |
| 环境污染 | % | 附近地表/房间污染代理。水、食物、皮肤和伤口只通过适用的交互路径暴露。 | <details><summary>标识与计算</summary>标识：<code>environmentalcontamination</code><br><code>s.Environment?.EnvironmentalContamination * 100</code></details> |

## 面板之外与动态行

血糖、酮症、肾过滤、氧气、肠道等键可能由服务器生成但未进入上述所有固定数组；窗口实际展示由客户端键清单决定。疾病、伤口和综合征是动态行，不是固定 58 个字段的全部。

疾病行用 `Treatments.Burden` 显示当前负担，悬停剩余小时由当前免疫病程与治疗速度计算。伤口行显示部位、种类、剩余结构损伤，悬停看愈合百分比及该伤口出血。无伤口时的愈合速率为“当前姿态下新伤口的预计速率”，不是角色正在回血。

## 显示转换

热流从 W 乘 `3600 / 4184` 变为 kcal/h；能量从 kJ 除 `4.184` 变为 kcal；肌肉克数除 1000 成 kg。产热/散热无有效采样间隔时留空；快照过期不能解释成所有值都为零。热适应显示内部 0–1 ×15%，冷适应 ×10%，它们不是 0–100% 的适应进度。

[面板布局](/guide/character-panel) · [全部窗口](/guide/windows) · [营养](/guide/nutrition) · [公式](/develop/formulas)
<!-- generated:end -->
