# 蜂箱与养蜂

From Golden Combs · 模组代码：fromgoldencombs

> 来源：整合包安装包 `From Golden Combs-2.1.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `fromgoldencombs` |
| 版本 | 2.1.0 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | Vinter Nacht |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adding depth, variety, and complexity to Vintage Apiculture

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
| 程序集 | 1 | `FromGoldenCombs.dll` |
| 方块定义 | 9 | `assets/fromgoldencombs/blocktypes/ceramicpot/ceramicbroodpot-fancy.json`<br>`assets/fromgoldencombs/blocktypes/ceramicpot/ceramicbroodpot-new.json`<br>`assets/fromgoldencombs/blocktypes/ceramicpot/hivetop-fancy.json`<br>`assets/fromgoldencombs/blocktypes/ceramicpot/hivetop-new.json`<br>`assets/fromgoldencombs/blocktypes/langstroth/framerack.json`<br>`assets/fromgoldencombs/blocktypes/langstroth/langstrothbase.json`<br>`assets/fromgoldencombs/blocktypes/langstroth/langstrothbrood.json`<br>`assets/fromgoldencombs/blocktypes/langstroth/langstrothstack.json`<br>`assets/fromgoldencombs/blocktypes/langstroth/langstrothsuper.json` |
| 物品定义 | 5 | `assets/fromgoldencombs/itemtypes/beeframe.json`<br>`assets/fromgoldencombs/itemtypes/frameliner.json`<br>`assets/fromgoldencombs/itemtypes/langstrothparts/langstrothbroodtop.json`<br>`assets/fromgoldencombs/itemtypes/langstrothparts/langstrothside.json`<br>`assets/fromgoldencombs/itemtypes/waxedtwine.json` |
| 实体定义 | 1 | `assets/fromgoldencombs/shapes/entities/skunk.json` |
| 配方定义 | 11 | `assets/fromgoldencombs/recipes/barrel/langstrothparts.json`<br>`assets/fromgoldencombs/recipes/barrel/waxedlinen.json`<br>`assets/fromgoldencombs/recipes/barrel/waxedtwine.json`<br>`assets/fromgoldencombs/recipes/clayforming/hivetop.json`<br>`assets/fromgoldencombs/recipes/clayforming/rawclaypothive.json`<br>`assets/fromgoldencombs/recipes/grid/framerack.json`<br>`assets/fromgoldencombs/recipes/grid/langstrothbase.json`<br>`assets/fromgoldencombs/recipes/grid/langstrothsuper.json`<br>`assets/fromgoldencombs/recipes/grid/parts/beeframe.json`<br>`assets/fromgoldencombs/recipes/grid/parts/frameliner.json`<br>`assets/fromgoldencombs/recipes/grid/parts/langstrothpart-brood.json` |
| 资产补丁 | 8 | `assets/fromgoldencombs/compatibility/flora/patches/block-item/smallberrybush.json`<br>`assets/game/patches/artisantraderpatch.json`<br>`assets/game/patches/beehive.json`<br>`assets/game/patches/beeswax.json`<br>`assets/game/patches/berrybushpatch.json`<br>`assets/game/patches/croppatch.json`<br>`assets/game/patches/waxedlinen.json`<br>`assets/newworldcrops/patches/croppatch.json` |
| 语言资源 | 17 | `assets/fromgoldencombs/lang/cs-cz.json`<br>`assets/fromgoldencombs/lang/cs.json`<br>`assets/fromgoldencombs/lang/de.json`<br>`assets/fromgoldencombs/lang/en.json`<br>`assets/fromgoldencombs/lang/es-419.json`<br>`assets/fromgoldencombs/lang/es-es.json`<br>`assets/fromgoldencombs/lang/fr.json`<br>`assets/fromgoldencombs/lang/is.json`<br>`assets/fromgoldencombs/lang/it.json`<br>`assets/fromgoldencombs/lang/ja.json`<br>`assets/fromgoldencombs/lang/ko.json`<br>`assets/fromgoldencombs/lang/pl.json`<br>另有 5 个文件 |
| 手册资源 | 3 | `assets/fromgoldencombs/config/handbook/FGC01-fromgoldencombsguide.json`<br>`assets/fromgoldencombs/config/handbook/FGC02-fromgoldencombs-pollination.json`<br>`assets/fromgoldencombs/config/handbook/FGC03-fromgoldencombs-langstrothguide.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**FromGoldenCombs.dll**（`eebf1b6a07f06c7c`）：59 个类型。

```text
Class <Module>
Class VFromGoldenCombs.Blocks.Langstroth.LangstrothBase
Class FromGoldenCombs.FromGoldenCombs
Class FromGoldenCombs.Util.HarmonyPatches.FGCHarmonySystem
Class FromGoldenCombs.Util.Config.FGCClientConfig
Class FromGoldenCombs.Util.Config.FGCServerConfig
Class FromGoldenCombs.Util.Config.NetworkHandler
Class FromGoldenCombs.RoamingBees.AngrySwarmClient
Class FromGoldenCombs.RoamingBees.BeeFlightPath
Class FromGoldenCombs.RoamingBees.BeeRandom
Class FromGoldenCombs.RoamingBees.BeeFlightTimeline
Class FromGoldenCombs.RoamingBees.BeeFlightPlanner
Class FromGoldenCombs.RoamingBees.BeeParticleRenderer
Class FromGoldenCombs.RoamingBees.ForageRegistry
Class FromGoldenCombs.RoamingBees.HiveEntrance
Class FromGoldenCombs.RoamingBees.RoamingBeeClient
Class FromGoldenCombs.RoamingBees.BeeSpawnPacket
Class FromGoldenCombs.RoamingBees.BeeCatchupRequestPacket
Class FromGoldenCombs.RoamingBees.BeeCatchupPacket
Class FromGoldenCombs.RoamingBees.RoamingBeeServer
Class FromGoldenCombs.RoamingBees.RoamingBeesModSystem
Class FromGoldenCombs.RoamingBees.WildHiveAdapter
Class FromGoldenCombs.Properties.Resources
Class FromGoldenCombs.Items.LangstrothPartCore
Class FromGoldenCombs.Blocks.ClayHiveTop
Class FromGoldenCombs.Blocks.RawBroodPot
Class FromGoldenCombs.Blocks.FrameRack
Class FromGoldenCombs.Blocks.LangstrothSuper
Class FromGoldenCombs.Blocks.Langstroth.LangstrothBrood
Class FromGoldenCombs.Blocks.Langstroth.LangstrothCore
Class FromGoldenCombs.Blocks.Langstroth.LangstrothStack
Class FromGoldenCombs.Blocks.ClaypotHive.CeramicBroodPot
Class FromGoldenCombs.BlockEntities.BECeramicBroodPot
Class FromGoldenCombs.BlockEntities.BEFGCBeehive
Class FromGoldenCombs.BlockEntities.BEFrameRack
Class FromGoldenCombs.BlockEntities.BELangstrothStack
Class FromGoldenCombs.BlockEntities.BELangstrothSuper
Class FromGoldenCombs.BlockBehaviors.PushEventOnBlockHarvested
Class FromGoldenCombs.BlockBehaviors.PushEventOnCropBreakBehavior
Class FromGoldenCombs.Util.Config.NetworkHandler.FGCConfigFromServerMessage
```

其余 19 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 11 个配方文件与 3 个手册章节](/reference/recipes/fromgoldencombs)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
