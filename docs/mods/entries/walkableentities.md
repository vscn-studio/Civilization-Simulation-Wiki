# 实体表面行走

Walkable Entities · 模组代码：walkableentities

> 来源：整合包安装包 `Walkable Entities-1.0.52.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `walkableentities` |
| 版本 | 1.0.52 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | 未声明 |
| 作者 | Omikronlex |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Walk aboard moving boats and supported trains. Extensible player platforms for Vanilla and modded entities.

</details>

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `WalkableEntities.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/walkableentities/lang/de.json`<br>`assets/walkableentities/lang/en.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 32 | `assets/walkableentities/config/platforms/airships-tier1.json`<br>`assets/walkableentities/config/platforms/airships-tier2.json`<br>`assets/walkableentities/config/platforms/barkcanoe.json`<br>`assets/walkableentities/config/platforms/catboat.json`<br>`assets/walkableentities/config/platforms/coracle.json`<br>`assets/walkableentities/config/platforms/drakkar.json`<br>`assets/walkableentities/config/platforms/faering.json`<br>`assets/walkableentities/config/platforms/joyofsailing.json`<br>`assets/walkableentities/config/platforms/kayak.json`<br>`assets/walkableentities/config/platforms/largejunker.json`<br>`assets/walkableentities/config/platforms/punter.json`<br>`assets/walkableentities/config/platforms/reedlongboat.json`<br>另有 20 个文件 |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**WalkableEntities.dll**（`0f77c746862ad358`）：100 个类型。

```text
Class <Module>
Class WalkableEntities.AirshipPlatforms
Class WalkableEntities.AnimalDecks
Class WalkableEntities.AnimalDeckHello
Class WalkableEntities.AnimalDeckBatch
Class WalkableEntities.AnimalDeckSample
Class WalkableEntities.AnimalDeckVisuals
Class WalkableEntities.PlatformRegistry
Class WalkableEntities.BoatAudio
Class WalkableEntities.BoatSailing
Class WalkableEntities.CameraAlignment
Class WalkableEntities.CollisionDebug
Class WalkableEntities.CollisionSolver
Class WalkableEntities.DeckFootsteps
Class WalkableEntities.DryInteriors
Class WalkableEntities.EquipmentChanges
Class WalkableEntities.PlatformGeometry
Class WalkableEntities.GeometryContributor
Class WalkableEntities.GeometryContributorRegistration
Class WalkableEntities.GeometryContributions
Class WalkableEntities.HoldDiagnostics
Class WalkableEntities.HullTerrainSweep
Class WalkableEntities.JoySailing
Class WalkableEntities.MovingFrame
Class WalkableEntities.DeckVisualMessage
Class WalkableEntities.PlatformVisuals
Class WalkableEntities.Profile
Class WalkableEntities.BoatAdapter
Class WalkableEntities.PlatformBody
Class WalkableEntities.RailPoseHistory
Class WalkableEntities.SafeDismount
Class WalkableEntities.SeaworthySailing
Class WalkableEntities.ShapeCompiler
Class WalkableEntities.VehicleExterior
Class WalkableEntities.WalkableEntitiesConfig
Class WalkableEntities.ConfigMessage
Class WalkableEntities.ExitRequest
Class WalkableEntities.ExitReply
Class WalkableEntities.WalkableEntitiesSystem
Class WalkableEntities.WallKicksCompatibility
```

其余 60 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
