# 生存模拟默认配置

以下为生存模拟的常用默认值，实际生成文件是该安装版本的完整参考。服务端编辑 `ModConfig/vsslssmod.Server.json` 后需重启。无效配置不会覆盖原文件；配置格式和版本字段须保留。

| 字段 | 默认值 | 说明 |
| --- | --- | --- |
| `Format` / `ConfigVersion` | `seraph.release.config` / `1` | 发布版配置格式及版本 |
| `Mode` | `survival` | `survival` 应用效果；`shadow` 仅模拟；`observe` 不推进模拟 |
| `PhysiologySpeed` | `1` | 生理速度倍率；范围 0.1–20 |
| `EnableClinicalEffects` / `EnableMovementEffects` | `true` | 生理状态和移动效果 |
| `EnableSymptomVisuals` | `true` | 症状视觉效果 |
| `EnableGroundWaterDrinking` / `EnableMedicalActions` / `EnableDefecation` | `true` | 饮水、护理、排泄 |
| `DrinkServingL` / `DrinkCooldownRealSeconds` | `0.25` / `3` | 单次饮水升数、现实秒冷却 |
| `DigestionGPerGameHour` | `1667` | 每游戏小时食物消化量，克 |
| `Digestion.WaterMlPerHour` / `WaterHalfLifeHours` | `2000` / `0.3333333333333333` | 每游戏小时吸水上限和胃水半衰期 |
| `SolarPowerWAtFullExposure` | `500` | 完全暴露时的日光热量，瓦 |
| `ClothingCloByCode` / `HeadgearShadeByCode` | `{}` | 按物品代码覆盖保暖和遮阳比例 |
| `TelemetryEnabled` / `CheckpointSeconds` | `false` / `30` | 遥测开关与存档检查点间隔，现实秒 |
| `SurfaceWater` / `DiseaseExposure` / `Sanitation` | 配置对象 | 水、疾病暴露与卫生污染 |
| `Exertion` / `ThermalAdaptation` / `Pain` / `Circulation` | 配置对象 | 劳动、热适应、疼痛与循环 |

部分睡压和疲劳参数可用显式游戏小时覆盖相应游戏秒设置。具体字段的有效范围以当前版本的配置校验和生成文件为准。更多功能和命令见[生存模拟](/guide/survival)。
