# 背负搬运

Carry On · 模组代码：carryon

> 来源：整合包安装包 `Carry On-2.0.0-rc.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `carryon` |
| 版本 | 2.0.0-rc.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0, carryonlib 1.0.0-rc.1 |
| 作者 | copygirl, NerdScurvy |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds the capability to carry various things

</details>

作者提供的链接：https://github.com/NerdScurvy/CarryOn

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `CarryOn.dll` |
| 方块定义 | 1 | `assets/carryon/blocktypes/carriedplaceholder.json` |
| 物品定义 | 16 | `assets/carryon/itemtypes/cactus.json`<br>`assets/carryon/itemtypes/cattail.json`<br>`assets/carryon/itemtypes/croton.json`<br>`assets/carryon/itemtypes/eternalstew-lid.json`<br>`assets/carryon/itemtypes/fern.json`<br>`assets/carryon/itemtypes/flower-lupine.json`<br>`assets/carryon/itemtypes/flower.json`<br>`assets/carryon/itemtypes/icon.json`<br>`assets/carryon/itemtypes/mushroom.json`<br>`assets/carryon/itemtypes/papyrus.json`<br>`assets/carryon/itemtypes/sapling.json`<br>`assets/carryon/itemtypes/soil.json`<br>另有 4 个文件 |
| 实体定义 | 1 | `assets/carryon/entities/carriedblock.json` |
| 配方定义 | 0 | — |
| 资产补丁 | 58 | `assets/carryon/patches/animations.json`<br>`assets/carryon/patches/boat.json`<br>`assets/carryon/patches/carryable/anvil.json`<br>`assets/carryon/patches/carryable/banner.json`<br>`assets/carryon/patches/carryable/barrel.json`<br>`assets/carryon/patches/carryable/bookshelf-clutter.json`<br>`assets/carryon/patches/carryable/bookshelf-legacy.json`<br>`assets/carryon/patches/carryable/bookshelf.json`<br>`assets/carryon/patches/carryable/bunchocandles.json`<br>`assets/carryon/patches/carryable/cabinet.json`<br>`assets/carryon/patches/carryable/chandelier.json`<br>`assets/carryon/patches/carryable/chest-labeled.json`<br>另有 46 个文件 |
| 语言资源 | 13 | `assets/carryon/lang/be.json`<br>`assets/carryon/lang/cs.json`<br>`assets/carryon/lang/de.json`<br>`assets/carryon/lang/en.json`<br>`assets/carryon/lang/es-es.json`<br>`assets/carryon/lang/fr.json`<br>`assets/carryon/lang/it.json`<br>`assets/carryon/lang/ja.json`<br>`assets/carryon/lang/ko.json`<br>`assets/carryon/lang/pl.json`<br>`assets/carryon/lang/pt-br.json`<br>`assets/carryon/lang/ru.json`<br>另有 1 个文件 |
| 手册资源 | 0 | — |
| 包内配置数据 | 16 | `assets/carryon/config/transformtemplates/carry-bag.json`<br>`assets/carryon/config/transformtemplates/carry-barrel.json`<br>`assets/carryon/config/transformtemplates/carry-chest-compact.json`<br>`assets/carryon/config/transformtemplates/carry-chest.json`<br>`assets/carryon/config/transformtemplates/carry-crate.json`<br>`assets/carryon/config/transformtemplates/carry-displaycase.json`<br>`assets/carryon/config/transformtemplates/carry-flowerpot.json`<br>`assets/carryon/config/transformtemplates/carry-planter.json`<br>`assets/carryon/config/transformtemplates/carry-reedchest.json`<br>`assets/carryon/config/transformtemplates/carry-resonator.json`<br>`assets/carryon/config/transformtemplates/carry-storagevessel-planter.json`<br>`assets/carryon/config/transformtemplates/carry-storagevessel.json`<br>另有 4 个文件 |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**CarryOn.dll**（`2c52317df0cacb45`）：309 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class CarryOn.CarrySystem
Class CarryOn.Utility.AttachableCarryConversion
Class CarryOn.Utility.AttachableEntitySync
Class CarryOn.Utility.AttachableGateValidator
Class CarryOn.Utility.CarryEntityPlacementPolicy
Class CarryOn.Utility.CarryExtensions
Class CarryOn.Utility.CarryPatcher
Class CarryOn.Utility.CarryRotationHelper
Class CarryOn.Utility.CarrySlotGuard
Class CarryOn.Utility.CollectionHelper
Class CarryOn.Utility.ColorHelper
Class CarryOn.Utility.EntityHandlerSpawner
Class CarryOn.Utility.HelpIconStacks
Class CarryOn.Utility.MultiblockUtils
Class CarryOn.Utility.PlayerBackpackExtensions
Class CarryOn.Utility.SoundHelper
Class CarryOn.Server.Models.DroppedBlockInfo
Class CarryOn.Server.Logic.AttachableRecoveryService
Class CarryOn.Server.Logic.BehavioralConditioning
Class CarryOn.Server.Logic.BlockPlacer
Class CarryOn.Server.Logic.CarriedBlockEntityService
Class CarryOn.Server.Logic.ModConfig
Class CarryOn.Server.Logic.ServerCommands
Class CarryOn.Server.Logic.BehavioralConditions.BehaviorAutoMapper
Class CarryOn.Server.Logic.BehavioralConditions.BlockFilter
Class CarryOn.Server.Logic.BehavioralConditions.ConditioningBaseline
Class CarryOn.Server.Logic.BehavioralConditions.MultipleBehaviorResolver
Class CarryOn.Server.Behaviors.EntityBehaviorDropCarriedOnDamage
Class CarryOn.Patches.ClientMain_sendRuntimeSettings_Patch
Class CarryOn.Patches.EntityBehaviorAttachable_TryRemoveAttachment_Patch
Class CarryOn.Patches.EntitySeat_onControls_Patch
Class CarryOn.Events.DroppedBlockTracker
Class CarryOn.Events.MeshAngleFix
Class CarryOn.Events.MessageOnBlockDropped
Class CarryOn.Events.TooHotToPickup
Class CarryOn.Common.Services.CarryableReportService
Class CarryOn.Common.Services.CarryDropService
Class CarryOn.Common.Services.CarryEventBootstrapper
```

其余 269 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
