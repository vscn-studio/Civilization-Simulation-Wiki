<!-- generated:start -->
# 身体异常、症状与恢复

疾病窗口中不全是传染病。这里也会显示失温、疲惫、出血和营养不足等身体异常。命名病原见[疾病百科](/guide/diseases)。

## 玩家处理顺序

先控制仍在持续的来源：出血、烟气、污染、缺水、寒冷或高温；然后补充可吸收的水、能量和营养并休息。耐力低、疲劳高、睡压高需要分别观察，单靠不停吃饭不能替代休息。

| 状态 | 表现与应对 | 技术说明 |
| --- | --- | --- |
| 失温 | 核心体温偏低会限制行动；低于35°C时出现原版结霜视野和寒冷发抖，严重失温损伤生命。避风、换干衣并靠近适度热源。 | <details><summary>标识与计算</summary>标识：<code>hypothermia</code><br><code>body.CoreTemperatureC &lt;= 35 ? (36 - body.CoreTemperatureC) / 5 : 0</code></details> |
| 热应激 | 核心温度达到37.5°C＋发热设定点偏移，且已吸收的可用水储备低于800 mL时提示热应激；达到39.5°C时无论储水多少均警告。降低劳动、改善散热并补水，胃里的水需吸收后才可用。连续出汗、热收支及高温伤害仍按实际体温结算。 | <details><summary>标识与计算</summary>标识：<code>heat-illness</code><br><code>HeatStress(state, body, profile) ? (body.CoreTemperatureC - 37) / 4 : 0</code></details> |
| 困倦 | 睡压超过 70% 后，画面逐渐失焦、四周变暗；75% 后上眼皮逐渐下垂，持续注视时可出现轻微重影和焦距波动。90% 起先提示再不自主合眼；90/95/100% 时，睁眼间隔为 60/45/25 s，完全闭合保持 0.25/0.4/0.7 s。完全合眼时闪避为 0%，睁眼后恢复。每次完全闭合最多转向一次 60°～180°，主动 K 键休息不转向。恢复和提神后效果消退。 | <details><summary>标识与计算</summary>标识：<code>drowsy</code><br><code>body.SleepPressure &gt;= .7 ? (body.SleepPressure - .5) * 2 : 0</code></details> |
| 疲惫 | 疲劳超过 60% 后渐进降低步行、冲刺增益及劳动效率。80/90/100% 时，步行保留 95/90/85%，劳动保留 90/80/75%；边缘昏暗仅为 4/7/10%，没有模糊脉冲。按 G 坐下、K 合眼休息，或在床上睡觉。 | <details><summary>标识与计算</summary>标识：<code>exhaustion</code><br><code>state.Fatigue &gt;= .6 ? state.Fatigue : 0</code></details> |
| 酮症 | 持续低糖原且实际供能以脂肪为主时逐渐累积；短暂消耗脂肪不会立即受罚。达到25%出现症状、60%升级提醒。劳动效率和耐力恢复最低为85%，与其他负荷取最强限制。补充并吸收碳水、降低脂肪供能占比后逐渐缓解；这不是酮症酸中毒诊断。 | <details><summary>标识与计算</summary>标识：<code>ketosis</code><br><code>Ketosis.Symptomatic(state.Clinical.Ketosis) ? state.Clinical.Ketosis : 0</code></details> |
| 疼痛 | 伤口疼痛影响动作；清洁、包扎、营养和休息支持自然恢复。 | <details><summary>标识与计算</summary>标识：<code>pain</code><br><code>Treatments.Pain(state, BloodCirculation.LactateCapacityG(body, profile))</code></details> |
| 烟雾吸入 | 吸入烟雾会降低呼吸能力，剧烈劳动会增加吸入剂量。请离开烟雾、呼吸清洁空气；严重暴露会损伤生命。这是游戏相对剂量，不是医学浓度。 | <details><summary>标识与计算</summary>标识：<code>smoke-inhalation</code><br><code>SmokeInhalation.Severity(state.SmokeDose)</code></details> |
| 一氧化碳暴露 | 燃烧废气会削弱呼吸能力和意识状态。请离开烟气并保持房间通风，严重暴露会损害生命。 | <details><summary>标识与计算</summary>标识：<code>carbon-monoxide</code><br><code>state.CarbonMonoxideBurden &gt;= .15 ? state.CarbonMonoxideBurden : 0</code></details> |
| 刺激性气体暴露 | 烟气和腐败废物产生的气体会削弱呼吸及耐力。请移至空气清洁处并处理污染源。 | <details><summary>标识与计算</summary>标识：<code>toxic-exposure</code><br><code>Math.Max(state.ToxicBurden, state.DrugToxicBurden) &gt;= .2 ? Math.Max(state.ToxicBurden, state.DrugToxicBurden) : 0</code></details> |
| 环境气体暴露 | 吸入的一氧化碳或刺激性气体会增加身体负担。离开烟团和有机污染源，恢复需要时间。 | <details><summary>标识与计算</summary>标识：<code>chemical-exposure</code><br><code>state.ChemicalBurden &gt;= .2 ? state.ChemicalBurden : 0</code></details> |
| 发热 | 体温调节目标升高，可能寒战并增加耗能；补水休息，监测核心体温。 | <details><summary>标识与计算</summary>标识：<code>fever</code><br><code>DiseaseSyndromes.Severity(state, SymptomKit.Fever)</code></details> |
| 普通感冒 | 可传播的呼吸道感染。休息、保暖，出现症状时避免近距离接触他人。 | <details><summary>标识与计算</summary>标识：<code>common-cold</code><br><code>DiseaseSyndromes.Severity(state, SymptomKit.CommonCold)</code></details> |
| 食物中毒症状 | 首次发作将胃内容物转入肠道；症状期新吃食物的85%无法吸收。分次补水休息。 | <details><summary>标识与计算</summary>标识：<code>food-poisoning</code><br><code>DiseaseSyndromes.Severity(state, SymptomKit.FoodPoisoning)</code></details> |
| 痢疾症状 | 增加腹泻失水和排便需求；补充洁净水并休息，普通绷带不治疗肠道感染。 | <details><summary>标识与计算</summary>标识：<code>dysentery</code><br><code>DiseaseSyndromes.Severity(state, SymptomKit.Dysentery)</code></details> |
| 败血症 | 候选感染处于严重症状期，并叠加严重脱水、失血或意识危险，持续达到配置时间后出现。具体条件和恢复要求见疾病百科的败血症条目。 | <details><summary>标识与计算</summary>标识：<code>sepsis</code><br><code>state.Syndromes.Sepsis ? 1 : 0</code></details> |
| 虫附着 | 清洗、雨淋或游泳可去虫；附着两h后有叮咬传播疾病的风险。 | <details><summary>标识与计算</summary>标识：<code>insect-carrier</code><br><code>state.Syndromes.VectorAttached ? .5 : 0</code></details> |
| 血液废物蓄积 | 血液废物会限制身体功能。高负荷会触发额外过滤，电解质储备越高，额外过滤越强；过滤需要肠道空间且不会直接消耗电解质。 | <details><summary>标识与计算</summary>标识：<code>blood-toxicity</code><br><code>state.Blood.Toxicity</code></details> |
| 肾脏亢进 | 高血液废物负荷会触发额外过滤，电解质储备越高，强化效果越强；过滤需要肠道空间且不会直接消耗电解质。 | <details><summary>标识与计算</summary>标识：<code>renal-hyperactivity</code><br><code>state.Blood.RenalHyperactivity ? 1 : 0</code></details> |
| 乳酸积累 | 乳酸满载时会阻止疾跑爆发并限制为慢跑；普通劳动仍可进行。站立、步行或坐姿可按现实时间恢复乳酸。 | <details><summary>标识与计算</summary>标识：<code>lactate-overload</code><br><code>Math.Clamp((state.Blood.LactateG / BloodCirculation.LactateCapacityG(body, profile) - .5) / .5, 0, 1)</code></details> |
| 失血 | 循环血量下降，灌注和耐力受影响；严重时损伤生命。持续按压一处出血伤口，再用绷带处理。 | <details><summary>标识与计算</summary>标识：<code>blood-loss</code><br><code>body.BloodVolumeL(profile) &lt; profile.ReferenceBloodVolumeL * .85 ? 1 - body.BloodVolumeL(profile) / profile.ReferenceBloodVolumeL : 0</code></details> |
| 营养相关贫血趋势 | 已知铁储备耗尽会降低耐力。这是营养相关趋势，不是血液化验；出血另行核算。 | <details><summary>标识与计算</summary>标识：<code>anemia</code><br><code>Burden("iron")</code></details> |
| B 族缺乏症状 | 持续缺乏 B 族增加疲劳负担并降低耐力。通过多样化饮食逐步恢复。 | <details><summary>标识与计算</summary>标识：<code>bcomplex-deficiency</code><br><code>Burden("bcomplex")</code></details> |
| 暗适应下降 | 持续维生素 A 缺乏会降低暗处辨认轮廓的能力。 | <details><summary>标识与计算</summary>标识：<code>night-vision</code><br><code>Burden("a")</code></details> |
| 骨骼支持不足 | 已知钙储备耗尽会降低骨骼支持与生命上限。普通饮食缺乏不降低跳跃高度。 | <details><summary>标识与计算</summary>标识：<code>bone-weakness</code><br><code>Burden("calcium")</code></details> |
| 维生素C缺乏 | 食用水果补充维生素C，支持恢复。 | <details><summary>标识与计算</summary>标识：<code>vitaminc-deficiency</code><br><code>Burden("c")</code></details> |
| 组织修复支持不足 | 持续蛋白质或锌缺乏降低恢复效率。多样饮食与休息有助恢复。 | <details><summary>标识与计算</summary>标识：<code>repair-deficiency</code><br><code>Burden("iron")</code></details> |

## 动态生成的项目

口渴/脱水按 `Hydration.Stage` 切换；缺铁性贫血、B 族不足、夜视受损、骨骼脆弱、维 C 不足及修复不足取对应微量营养的缺乏负担。治疗登记的不适症状也会加入；恶心和腹痛另外合并感染、不适症状与植物毒性后取最大值。

## 热病和失温

低体温标签在核心温度 ≤35°C 出现。热应激在核心 ≥39.5°C，或可用水低于 800 mL 且核心温度达到 `37.5 + 发热设定点 − 37` 时成立。衣物、环境热量、风、湿身和发热需一起判断。局部冻伤另外按暴露部位计时，不能用平均皮肤温度正常来排除脚部或手臂风险。

## 烟气、中毒与废物

烟雾剂量、一氧化碳、化学负担、药物毒性与血液废物分别记录。离开来源后还需要清除已积累负担；空气污染百分比下降不意味着所有体内指标已经恢复。血液废物通过肠道排出，肠道满会阻碍清除。

## 持续损伤如何叠加

`DamagePerSecond` 在严重脱水、休克、极端体温、毒性和血液毒性之间取最强项，避免相关原因重复收费；败血症等其他结算仍要看各自调用点。普通症状标签出现不等于该项已经达到持续伤害阈值。

[伤口护理](/guide/care-tutorial) · [指标来源](/guide/metric-sources) · [疾病清单](/guide/diseases)
<!-- generated:end -->
