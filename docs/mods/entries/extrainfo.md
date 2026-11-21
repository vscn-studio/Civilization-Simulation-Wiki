# 额外信息

Extra Info · 模组代码：extrainfo

> 来源：整合包安装包 `Extra Info-2.2.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `extrainfo` |
| 版本 | 2.2.1 |
| 类型 | 含程序代码 |
| 运行端 | client |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Craluminum2413 (Dana) |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“界面、汉化与客户端工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Useful information for handbook, blocks, items and entities

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
| 程序集 | 1 | `ExtraInfo.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 22 | `assets/extrainfo/lang/ar.json`<br>`assets/extrainfo/lang/cs.json`<br>`assets/extrainfo/lang/de.json`<br>`assets/extrainfo/lang/en.json`<br>`assets/extrainfo/lang/eo.json`<br>`assets/extrainfo/lang/es-419.json`<br>`assets/extrainfo/lang/es-es.json`<br>`assets/extrainfo/lang/fr.json`<br>`assets/extrainfo/lang/it.json`<br>`assets/extrainfo/lang/ja.json`<br>`assets/extrainfo/lang/ko.json`<br>`assets/extrainfo/lang/nl.json`<br>另有 10 个文件 |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ExtraInfo.dll**（`3568d91a6053ca70`）：79 个类型。

```text
Class <Module>
Class ExtraInfo.HarmonyReflectionExtensions
Class ExtraInfo.InfoExtensions
Class ExtraInfo.ItemstackExtensions
Class ExtraInfo.LoggerUtil
Class ExtraInfo.ProgressBarBuilder
Class ExtraInfo.RichTextExtensions
Class ExtraInfo.TextExtensions
Class ExtraInfo.TimeBasedProgressBarProperties
Class ExtraInfo.TimeFormatter
Class ExtraInfo.Systems.ConfigLibCompatibility
Class ExtraInfo.Systems.Core
Class ExtraInfo.Systems.TreeStats.CollectibleBehaviorTreeGrowthDescription
Class ExtraInfo.Systems.TreeStats.Core
Class ExtraInfo.Systems.TreeProgress.TreeProgressPatch
Class ExtraInfo.Systems.TranslocatorDestination.TranslocatorDestinationPatch
Class ExtraInfo.Systems.StackMetalUnits.NuggetMetalUnitsPatch
Class ExtraInfo.Systems.StackMetalUnits.OreMetalUnitsPatch
Class ExtraInfo.Systems.SkepProgress.SkepProgressPatch
Class ExtraInfo.Systems.QuernGrindingProgress.QuernGrindingProgressPatch
Class ExtraInfo.Systems.PumpkinVineProgress.PumpkinVineProgressPatch
Class ExtraInfo.Systems.PitKilnProgress.PitKilnProgressPatch
Class ExtraInfo.Systems.PileTotalItems.PileTotalItemsPatch
Class ExtraInfo.Systems.OpenHandbookPageForEntity.OpenHandbookPageForEntityPatch
Class ExtraInfo.Systems.MechanicalBlockInfo.MechanicalBlockInfoPatch
Class ExtraInfo.Systems.Handbook.HandbookWorkableTemp.HandbookWorkableTempPatch
Class ExtraInfo.Systems.Handbook.HandbookTroughFeedOptions.HandbookTroughFeedOptionsPatch
Class ExtraInfo.Systems.Handbook.HandbookTraderGoods.Core
Class ExtraInfo.Systems.Handbook.HandbookTraderGoods.HandbookTraderGoodsPatch
Class ExtraInfo.Systems.Handbook.HandbookTraderGoods.RemoveVanillaTradeHandbookInfoPatch
Class ExtraInfo.Systems.Handbook.HandbookTraderGoods.TradeHandbookInfoSystem
Class ExtraInfo.Systems.Handbook.HandbookPitKiln.HandbookPitKilnPatch
Class ExtraInfo.Systems.Handbook.HandbookPanningDrops.HandbookPanningDropsPatch
Class ExtraInfo.Systems.Handbook.HandbookPanningDrops.PanningDropExt
Class ExtraInfo.Systems.Handbook.HandbookPanningDrops.PanningGroup
Class ExtraInfo.Systems.Handbook.HandbookEntityDrops.HandbookEntityDropsPatch
Class ExtraInfo.Systems.Handbook.HandbookEatableByCreatures.HandbookEatableByCreaturesPatch
Class ExtraInfo.Systems.Handbook.HandbookCreatureDiet.HandbookCreatureDietPatch
Class ExtraInfo.Systems.FuelProgress.BurnablePileProgressPatch
Class ExtraInfo.Systems.FuelProgress.CoalPileProgressPatch
```

其余 39 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
