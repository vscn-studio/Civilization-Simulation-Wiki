# 开发者 API 与适配器契约

> 本页只记录源码中明确公开的 `Seraph`/`Seraph.Application` API；内部类和 Vintage Story 原生 API 不在此冒充稳定接口。

## 治疗注册 API

| 方法 | 签名/行为 | 错误条件 |
| --- | --- | --- |
| `RegisterTreatmentV1` | `RegisterTreatmentV1(string itemCode, TreatmentDefinition definition)`；启动时注册一次，复制数组快照 | AssetLocation 字符串不规范、定义校验失败、重复 item code 抛 `ArgumentException` |
| `QueryTreatment` | 检查手持物品与路由，不启动、不消费、不改生理 | 未注册物品 `treatment-unknown`；服务端不可用 `treatment-unavailable` |
| `BeginTreatment` | 服务端开始动作，返回 `TreatmentUseResult` | 同上及服务端动作条件 |
| `ContinueTreatment` | `bool`；继续已开始动作 | 无活动返回 false |
| `CompleteTreatment` | 完成并由服务器验证消费/效果 | 不可用返回 `treatment-unavailable` |
| `CancelTreatment` | 取消当前玩家治疗 | 无返回值 |
| `ReadHerbalWater` | 读取已验证的 `WaterBatch`，优先使用核心世界 API | 未接入核心时读取本地 metadata |

## IntegrationContracts

| 类型 | 成员 | 用途 |
| --- | --- | --- |
| `AdapterEvidence` | `AdapterId`, `ProviderVersion`, `UnitsVerified`, `Evidence` | 适配器必须证明单位和来源 |
| `RoomSample` | `Enclosed`, `WindAttenuation`, `RadiantDeltaC`, `Evidence` | 房间/热环境采样 |
| `ExposureSample` | `EventId`, `Pathogen`, `Route`, `HazardPerBioSecond`, `Evidence` | 服务器确认暴露 |
| `InjurySample` | `EventId`, `WoundKind`, `Region`, `Severity`, `BleedLps`, `Evidence` | 服务器命中部位与伤口 |
| `FoodPortion` | 代码、水 L/份、能量 kJ/份、质量 g/份、证据 | `Receipt` 只接受 UnitsVerified 且份数 0–1 |
| `IRoomEnvironmentAdapter` | `TrySample(playerUid, out RoomSample)` | 可选环境提供者 |
| `IExposureAdapter` | `Sample(playerUid, bioSeconds)` | 提供暴露事件 |
| `IInjuryAdapter` | `TryResolve(serverDamageEvent, out InjurySample)` | 解析伤害部位 |
| `IDownedDelegate` | `ProviderId`, `OwnsRevival`, `IsDowned`, `TryEnter`, `TryRescue` | 倒地/复苏所有权协商 |

## 兼容实现原则

所有生理写入都由服务端控制；客户端只显示快照。`AdapterEvidence.UnitsVerified=false` 的数据不得进入物理账本；不能把饱食度自动推断成食品能量。
