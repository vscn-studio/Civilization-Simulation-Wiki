# 生存模拟

Seraph A Living Survival Simulation · 模组代码：vsslssmod

> 来源：整合包安装包 `vsslssmod-1.0.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vsslssmod` |
| 版本 | 1.0.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | HansJack, ch4Ver, buzidao9, Zhiketangjiang2, KitamuraEri |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

生存模拟把饮食消化、饮水、水处理、体力、睡眠、体温、伤病和卫生连接起来，并提供井、浴缸及烟雾暴露等玩法。

### 玩家完整入口

| 系统 | 玩家应先看 | 关键实现 |
| --- | --- | --- |
| 水与卫生 | [水与卫生](/pack/water-and-sanitation)、[护理操作](/guide/care-tutorial) | 水批次同时保存温度、浑浊度、病原和化学危害；过滤、煮沸、洗浴、洗手分别结算。 |
| 食物与营养 | [营养规则](/guide/nutrition)、[食物检索](/guide/food-catalogue) | 校准、运行时注册、原版营养属性、分类基线和回退按 `FoodCatalog` 优先级合并；混合餐按实际配料处理。 |
| 疾病与状态 | [疾病百科](/guide/diseases)、[非传染性状态](/guide/conditions) | 暴露路径、潜伏/症状/恢复、免疫修正和败血症条件分开记录；症状不等于病原已清除。 |
| C 键与休息 | [窗口清单](/guide/windows)、[指标来源](/guide/metric-sources) | 65 个 UI 指标来自服务端快照；固定窗口、快照过期和空值边界均按源码实现。 |

### 管理员与开发者入口

服务器命令见[完整指令参考](/admin/commands-full)，125 个配置文件和 6001 个叶字段见[完整配置表](/admin/config-tables)，公开治疗和适配器契约见[API](/develop/api)。源码中 `Seraph.Core` 负责纯模拟，`Seraph.Application` 负责服务端契约，`Seraph` 负责 Vintage Story 桥接；客户端不能提交营养、病原、伤口或完成时间。

[返回整合包图鉴](/mods/)

## 源码实现矩阵（当前源码树）

逐文件类型、方法及哈希已集中到[开发者源码索引](/develop/sources/vsslssmod)。

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 3 | `vsslssmod.Application.dll`<br>`vsslssmod.Core.dll`<br>`vsslssmod.dll` |
| 方块定义 | 23 | `assets/vsslssmod/blocktypes/bathtub-part.json`<br>`assets/vsslssmod/blocktypes/bathtub.json`<br>`assets/vsslssmod/blocktypes/chimney-middle.json`<br>`assets/vsslssmod/blocktypes/chimney-top.json`<br>`assets/vsslssmod/blocktypes/chimney.json`<br>`assets/vsslssmod/blocktypes/compostdung-1.json`<br>`assets/vsslssmod/blocktypes/compostdung-2.json`<br>`assets/vsslssmod/blocktypes/compostdung-3.json`<br>`assets/vsslssmod/blocktypes/compostdung-4.json`<br>`assets/vsslssmod/blocktypes/copperbathtub-end.json`<br>`assets/vsslssmod/blocktypes/copperbathtub-part.json`<br>`assets/vsslssmod/blocktypes/copperbathtub.json`<br>另有 11 个文件 |
| 物品定义 | 6 | `assets/vsslssmod/itemtypes/ash.json`<br>`assets/vsslssmod/itemtypes/lye.json`<br>`assets/vsslssmod/itemtypes/manure.json`<br>`assets/vsslssmod/itemtypes/seasalt.json`<br>`assets/vsslssmod/itemtypes/soap-powder.json`<br>`assets/vsslssmod/itemtypes/soap.json` |
| 实体定义 | 0 | — |
| 配方定义 | 12 | `assets/vsslssmod/recipes/barrel/lye.json`<br>`assets/vsslssmod/recipes/barrel/seasalt-curedmeat.json`<br>`assets/vsslssmod/recipes/barrel/soap.json`<br>`assets/vsslssmod/recipes/grid/bathtub.json`<br>`assets/vsslssmod/recipes/grid/chimney.json`<br>`assets/vsslssmod/recipes/grid/copperbathtub.json`<br>`assets/vsslssmod/recipes/grid/drainpot.json`<br>`assets/vsslssmod/recipes/grid/filterpot.json`<br>`assets/vsslssmod/recipes/grid/latrine.json`<br>`assets/vsslssmod/recipes/grid/soap.json`<br>`assets/vsslssmod/recipes/grid/wellhead.json`<br>`assets/vsslssmod/recipes/grid/wellwall.json` |
| 资产补丁 | 7 | `assets/vsslssmod/patches/expanded-matter-soap.json`<br>`assets/vsslssmod/patches/food-calibration.json`<br>`assets/vsslssmod/patches/player-closed-eye-rest.json`<br>`assets/vsslssmod/patches/player-squat.json`<br>`assets/vsslssmod/patches/player-vomit.json`<br>`assets/vsslssmod/patches/realsmoke-chimney.json`<br>`assets/vsslssmod/patches/water-distillation.json` |
| 语言资源 | 4 | `assets/game/lang/en.json`<br>`assets/game/lang/zh-cn.json`<br>`assets/vsslssmod/lang/en.json`<br>`assets/vsslssmod/lang/zh-cn.json` |
| 手册资源 | 18 | `assets/vsslssmod/config/handbook/01-start.json`<br>`assets/vsslssmod/config/handbook/02-interface.json`<br>`assets/vsslssmod/config/handbook/03-water.json`<br>`assets/vsslssmod/config/handbook/04-filter.json`<br>`assets/vsslssmod/config/handbook/05-wells.json`<br>`assets/vsslssmod/config/handbook/06-distillation.json`<br>`assets/vsslssmod/config/handbook/07-food.json`<br>`assets/vsslssmod/config/handbook/08-stamina.json`<br>`assets/vsslssmod/config/handbook/09-sleep.json`<br>`assets/vsslssmod/config/handbook/10-firstaid.json`<br>`assets/vsslssmod/config/handbook/11-blood.json`<br>`assets/vsslssmod/config/handbook/12-disease.json`<br>另有 6 个文件 |
| 包内配置数据 | 2 | `assets/vsslssmod/config/compatibility.json`<br>`assets/vsslssmod/config/foods.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**vsslssmod.dll**（`be4600998b3653ce`）：526 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>f__AnonymousType1
Class <>f__AnonymousType2
Class <>f__AnonymousType3
Class <>f__AnonymousType4
Class <>f__AnonymousType5
Class <>f__AnonymousType6
Class <>f__AnonymousType7
Class <>f__AnonymousType8
Class <>f__AnonymousType9
Class <>f__AnonymousType10
Class <>f__AnonymousType11
Class <>z__ReadOnlyArray
Class <>z__ReadOnlySingleElementList
Class Seraph.LocalizedText
Class Seraph.SeraphModSystem
Class Seraph.SlowCallbackProbe
Class Seraph.TreatmentUseResult
Class Seraph.World.BedRestProperties
Class Seraph.World.BlockBathtub
Class Seraph.World.BlockEntityBathtub
Class Seraph.World.BlockChimney
Class Seraph.World.BlockChimneyPart
Class Seraph.World.BlockEntityChimney
Class Seraph.World.BlockEntityWaterTreatment
Class Seraph.World.BlockEntityWellWall
Class Seraph.World.BlockLatrine
Class Seraph.World.BlockEntityLatrine
Class Seraph.World.BlockWaterTreatment
Class Seraph.World.BlockWellHead
Class Seraph.World.BlockEntityWellHead
Class Seraph.World.ChimneyHost
Class Seraph.World.ChimneyInstallationPlan
Class Seraph.World.ChimneyGeometry
Class Seraph.World.PollutionSnapshot
Class Seraph.World.ChunkPollutionStore
Class Seraph.World.ClosedEyePose
Class Seraph.World.CottageWaterCompatibility
Class Seraph.World.DefecationPose
```

其余 486 个类型未在此列出；可按维护说明重新分析程序集。

**vsslssmod.Application.dll**（`6a320450d68ac1f4`）：33 个类型。

```text
Class <Module>
Class Seraph.Application.CapabilityAssignment
Class Seraph.Application.CapabilityRegistry
Class Seraph.Application.SideEffectBarrier
Class Seraph.Application.IntegrationStatus
Class Seraph.Application.ClinicalWarning
Class Seraph.Application.ClinicalWarningPolicy
Class Seraph.Application.ClinicalWarningTracker
Class Seraph.Application.InboundGate
Class Seraph.Application.AdapterEvidence
Class Seraph.Application.RoomSample
Class Seraph.Application.ExposureSample
Class Seraph.Application.InjurySample
Class Seraph.Application.FoodPortion
Class Seraph.Application.MedicalAction
Class Seraph.Application.MedicalActionCoordinator
Class Seraph.Application.MetricTrends
Class Seraph.Application.SeraphServerConfig
Class Seraph.Application.TargetVersion
Class Seraph.Application.SettingsAuthority
Class Seraph.Application.ShadowSave
Class Seraph.Application.SaveDecodeResult
Class Seraph.Application.ShadowSaveCodec
Class <PrivateImplementationDetails>
Class Seraph.Application.CapabilityRegistry.<>c__DisplayClass7_1
Class Seraph.Application.ClinicalWarningPolicy.<>c
Class Seraph.Application.ClinicalWarningPolicy.<>c__DisplayClass0_0
Class Seraph.Application.ClinicalWarningTracker.Episode
Class Seraph.Application.ClinicalWarningTracker.<>c
Class Seraph.Application.InboundGate.Bucket
Class Seraph.Application.MetricTrends.Series
Class Seraph.Application.SeraphServerConfig.<>c
Class Seraph.Application.ShadowSaveCodec.Envelope
```

**vsslssmod.Core.dll**（`6744329b70073fcc`）：232 个类型。

```text
Class <Module>
Class <>z__ReadOnlyArray
Class Seraph.Core.BuildInfo
Class Seraph.Core.State.BodyProfile
Class Seraph.Core.State.BodyState
Class Seraph.Core.State.EnvironmentSample
Class Seraph.Core.Simulation.ActionEnergyBudget
Class Seraph.Core.Simulation.SchedulerOptions
Class Seraph.Core.Simulation.TimeBudgetPlan
Class Seraph.Core.Simulation.BoundedTimeScheduler
Class Seraph.Core.Simulation.CalendarSleepTimeline
Class Seraph.Core.Simulation.CalendarTimeScheduler
Class Seraph.Core.Simulation.StepInputs
Class Seraph.Core.Simulation.IntakeEvent
Class Seraph.Core.Simulation.StateChangeResult
Class Seraph.Core.Simulation.StepResult
Class Seraph.Core.Simulation.SimulationDiagnostics
Class Seraph.Core.Simulation.ModelOptions
Class Seraph.Core.Simulation.PhysiologyFlowLedger
Class Seraph.Core.Simulation.SimulationKernel
Class Seraph.Core.Simulation.ThermalLedger
Class Seraph.Core.Framework.AdrenalineEffects
Class Seraph.Core.Framework.AshAndFertilizer
Class Seraph.Core.Framework.BathWaterTreatment
Class Seraph.Core.Framework.BloodState
Class Seraph.Core.Framework.CirculationOptions
Class Seraph.Core.Framework.BloodCirculation
Class Seraph.Core.Framework.InjuryEvent
Class Seraph.Core.Framework.Anatomy
Class Seraph.Core.Framework.BodyFunctions
Class Seraph.Core.Framework.BodyFunctionResolver
Class Seraph.Core.Framework.CombatFunctions
Class Seraph.Core.Framework.BowelSettlement
Class Seraph.Core.Framework.ClinicalEffect
Class Seraph.Core.Framework.ClinicalEffects
Class Seraph.Core.Framework.WoundCare
Class Seraph.Core.Framework.SoapCare
Class Seraph.Core.Framework.ColdExposure
Class Seraph.Core.Framework.CropSurfaceContamination
Class Seraph.Core.Framework.DietaryMetabolism
```

其余 192 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 12 个配方文件与 18 个手册章节](/reference/recipes/vsslssmod)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
