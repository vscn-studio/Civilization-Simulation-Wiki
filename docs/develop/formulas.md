# 生理公式与数值来源

> 本页只写入可以在当前源码中定位到的公式、常量和单位。源码路径均相对于 `Seraph Living Survival Simulation/src/Seraph.Core/Framework`；配置覆盖源码默认值时，以服务端配置快照为准。

## 时间和单位

| 名称 | 代码约定 | 说明 |
| --- | --- | --- |
| 生物秒 | `FrameworkKernel` 的推进时间 | 病程、治疗和恢复使用生物秒；病原定义中的秒数在 `Pathogens.Definitions` 创建时统一乘 30。 |
| 游戏小时 | 配置字段名含 `GameHour` | 卫生、循环、体温适应等按游戏时间推进；不要和现实秒直接相乘。 |
| 份量 | `FoodPortion` / `foods.json` | 质量用 g，水用 L 或 mL，能量用 kJ；未经 `UnitsVerified` 的适配器不能写入营养账本。 |

## 消化与营养吸收

`DigestionOptions.Empty(amount, hours, halfLife, capacity)` 使用指数清空：

```text
processed = amount × (1 − exp(−ln(2) × hours × capacity / halfLife))
```

`DietaryMetabolism.DigestStep` 对水、碳水、蛋白、脂肪、纤维和胃残渣分别使用半衰期。水还受 `WaterMlPerHour × waterAbsorptionEfficiency × hours`、身体参考水量缺口和胃肠空间限制；蛋白的请求量额外乘 `ProteinDigestSlowMul`（默认 2.25）。总吞吐量为：

```text
throughput = min(1, DigestionGPerGameHour × efficiency × hours / requested)
```

宏量能量常量在 `DietaryMetabolism` 中定义：碳水、蛋白和脂肪分别按代码中的 `CarbKJPerG`、`ProteinKJPerG`、`FatKJPerG` 计算，不能用原版饱食度反推。吸收后的碳水先填充 `GlycogenCapacityKJ`，脂肪先填充 `FatCapacityKJ`；溢出的碳水按源码转换规则进入脂肪，剩余才记录为热量溢出。

微量营养由 `MicroNutrition.Settle` 结算。储备范围为 0–100，低于 20 开始累计缺口（`Deficiency`），高于 20 会恢复缺口。每日参考点数：A 为 `100/30`，C 与 B 复合为 `100/7`，其余铁、锌、钙为 22；半衰期 A=4 小时、C=1 小时、B 复合=2 小时、其余=2 小时。免疫营养加成为六组储备相对值平均数的 0.2 倍。

## 免疫、病程和败血症

有效免疫在 `ImmuneSystem.Effective` 中按免疫储备、营养支持、躯干结构损伤和毒性求值，并限制在源码规定范围。缺口会缩短潜伏期、延长症状期和恢复期；具体乘数见[疾病页](/guide/diseases)。败血症在 `DiseaseExposure`/`DiseaseSyndromes` 中还要求伤口或系统性感染达到严重度，并持续满足脱水、低血容量或意识危险条件；`SepsisOnsetHours` 与 `SepsisRecoveryHours` 来自配置，不能从病原潜伏期推断。

## 身体、伤口和行动倍率

`VitalState` 将六个区域（头颈、躯干、左右臂、左右腿）分别存储损伤缺口。基础最大值为头颈/躯干 20、四肢 15，总计 100；外部最大生命、肌肉加成和钙缺口会改变有效最大值。头颈或躯干有效值达到 0 即为致命。区域伤口和区域生命缺口使用 `max` 合并，避免同一伤害重复扣除。

`BodyFunctions` 的主要限制取所有候选因素的最小值：

- 消化：脱水器官系数、躯干伤害、肠道疾病负担、核心温度偏离 34–39.5°C、能量储备不足；再乘肾上腺素消化修正，最终夹在 0.15–1。
- 呼吸：胸部结构损伤、呼吸道疾病、烟雾吸入和气体负担。
- 意识：头部损伤、循环、缺氧/一氧化碳、酒精/致幻物和镇静投诉。
- 移动：左右腿、肌肉酸痛、疲劳、热应激、脱水、体成分和肠道负荷；肌肉量低于 5 kg 时有 0.9 系数。
- 劳动耐力：呼吸、循环、肌肉比例、电解质和血液废物；冲刺另受乳酸、耐力、疲劳和睡压限制。

行动阶段 `ActionStage` 为剩余能力 ≥0.8 时 1，≥0.6 时 0.9，≥0.4 时 0.75，≥0.2 时 0.5，否则 0.25。肌肉量达到 25 kg 和 45 kg 时分别提供 0.05 与 0.10 的近战加成。

## 水处理

`WaterFiltration` 的常量为：滤材寿命 80 L、储液 10 L、普通流量 0.025 L/s、布过滤 0.05 L/s、排水 0.1 L/s。分层过滤把浑浊度乘 0.08、病原和肠道危险乘 0.15，并清除化学危险；布过滤分别乘 0.45 和 0.8。过滤结果仍标记 `Unverified`，不能当作无菌水。

`WaterHeating` 的热预算上限 20 kJ/s，水比热 4.184 kJ/L/K，汽化潜热 2257 kJ/L。达到 100°C 时清空病原、肠道危险并标记为 `Disinfected`；超过 100°C 的炉温才会在剩余热量足够时蒸发体积，蒸馏会浓缩水中盐分和残余悬浮物。

## 环境与卫生

`RegionalEnvironment` 将空气化学物质夹在 0–1；温度衰减因子为 `clamp(2^((temperatureC−15)/20), 0.25, 4)`。土壤损害为 `clamp(Erosion×0.3,0,1)`，地下水补给倍率为 `clamp((0.5+OrganicMatter×0.5)×(1−Erosion×0.4)×(1−GroundwaterStress×0.3),0.2,1)`。

卫生、污染、洗浴、雨水冲刷、手部转移和伤口感染使用 `SeraphServerConfig` 与其嵌套选项；[完整配置](/admin/survival-config-full)同时列出源码默认值和[当前实例实值](/admin/installed-configs)。

## 证据边界

这些公式描述当前源码路径中的纯函数和配置默认值。原版食物、其他模组运行时 patch、服务器热重载后的状态以及未接入 `AdapterEvidence` 的数据可能改变结果；遇到冲突时记录版本、配置、`/vsslssmod probe` 输出和日志，再按源码版本复核。
