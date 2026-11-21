# 野生种植

Wild Farming Fork · 模组代码：wildfarmingfork

> 来源：整合包安装包 `Wild Farming Fork-2.1.9.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `wildfarmingfork` |
| 版本 | 2.1.9 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | jakecool19, SpearAndFang, Aimli_ |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Cultivate flowers, herbs, mushrooms, trees, and shrubs. And much more. A port to Vintage Story 1.22, with configurable crafting and grafting recipes for berry cuttings.

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
| 程序集 | 1 | `WildFarmingFork.dll` |
| 方块定义 | 13 | `assets/game/blocktypes/soil/muddygravel-layered.json`<br>`assets/wildfarmingfork/blocktypes/mushroomsubstrate.json`<br>`assets/wildfarmingfork/blocktypes/mushroomsubstrateincubated.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant-bigberrybush.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant-cacti.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant-croton.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant-fern.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant-lupine.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant-rafflesia.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant-smallberrybush.json`<br>`assets/wildfarmingfork/blocktypes/plant/wildplant.json`<br>`assets/wildfarmingfork/blocktypes/wood/trunk.json`<br>另有 1 个文件 |
| 物品定义 | 8 | `assets/wildfarmingfork/itemtypes/cactiseeds.json`<br>`assets/wildfarmingfork/itemtypes/wildseeds-bigberrybush.json`<br>`assets/wildfarmingfork/itemtypes/wildseeds-croton.json`<br>`assets/wildfarmingfork/itemtypes/wildseeds-fern.json`<br>`assets/wildfarmingfork/itemtypes/wildseeds-lupine.json`<br>`assets/wildfarmingfork/itemtypes/wildseeds-rafflesia.json`<br>`assets/wildfarmingfork/itemtypes/wildseeds-smallberrybush.json`<br>`assets/wildfarmingfork/itemtypes/wildseeds.json` |
| 实体定义 | 0 | — |
| 配方定义 | 12 | `assets/wildfarmingfork/recipes/barrel/cattailroot.json`<br>`assets/wildfarmingfork/recipes/barrel/papyrusroot.json`<br>`assets/wildfarmingfork/recipes/barrel/tuleroot.json`<br>`assets/wildfarmingfork/recipes/grid/cactiseeds.json`<br>`assets/wildfarmingfork/recipes/grid/cropseeds.json`<br>`assets/wildfarmingfork/recipes/grid/flowerseeds.json`<br>`assets/wildfarmingfork/recipes/grid/fruitingbushcutting.json`<br>`assets/wildfarmingfork/recipes/grid/fruitingbushgrafting-handbook.json`<br>`assets/wildfarmingfork/recipes/grid/fruitingbushgrafting.json`<br>`assets/wildfarmingfork/recipes/grid/fruitseeds.json`<br>`assets/wildfarmingfork/recipes/grid/mushroomsubstrate.json`<br>`assets/wildfarmingfork/recipes/grid/vinetrimming.json` |
| 资产补丁 | 16 | `assets/wildfarmingfork/compatibility/expandedfoods/patches/survival-blocktypes-plant-seaweed.json`<br>`assets/wildfarmingfork/patches/berryseedpanning.json`<br>`assets/wildfarmingfork/patches/enabledpatches.json`<br>`assets/wildfarmingfork/patches/ferntree.json`<br>`assets/wildfarmingfork/patches/fruitingbushcutting.json`<br>`assets/wildfarmingfork/patches/ghostpipe-seed-drops.json`<br>`assets/wildfarmingfork/patches/log.json`<br>`assets/wildfarmingfork/patches/logsection.json`<br>`assets/wildfarmingfork/patches/old-id-remaps.json`<br>`assets/wildfarmingfork/patches/saguarocactus.json`<br>`assets/wildfarmingfork/patches/saplings.json`<br>`assets/wildfarmingfork/patches/seaweed.json`<br>另有 4 个文件 |
| 语言资源 | 16 | `assets/game/lang/de.json`<br>`assets/game/lang/en.json`<br>`assets/game/lang/fr.json`<br>`assets/game/lang/ja.json`<br>`assets/game/lang/ru.json`<br>`assets/game/lang/uk.json`<br>`assets/game/lang/zh-cn.json`<br>`assets/wildfarmingfork/lang/cs.json`<br>`assets/wildfarmingfork/lang/de.json`<br>`assets/wildfarmingfork/lang/en.json`<br>`assets/wildfarmingfork/lang/fr.json`<br>`assets/wildfarmingfork/lang/ja.json`<br>另有 4 个文件 |
| 手册资源 | 1 | `assets/wildfarmingfork/config/handbook/botanyguide.json` |
| 包内配置数据 | 1 | `assets/wildfarmingfork/config/configlib-patches.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**WildFarmingFork.dll**（`a2456faac28b5c11`）：31 个类型。

```text
Class <Module>
Class WildFarmingFork.ModSystem.BESeaweed
Class WildFarmingFork.ModSystem.BEVines
Class WildFarmingFork.ModSystem.BlockBehaviorScore
Class WildFarmingFork.ModSystem.BlockBehaviorXSkillsSaplingCompat
Class WildFarmingFork.ModSystem.BlockEnhancedMushroom
Class WildFarmingFork.ModSystem.BlockEnhancedVines
Class WildFarmingFork.ModSystem.BlockEntityMushroomSubstrate
Class WildFarmingFork.ModSystem.BlockEntityRegenSapling
Class WildFarmingFork.ModSystem.BlockEntityTermiteMound
Class WildFarmingFork.ModSystem.BlockEntityTrunk
Class WildFarmingFork.ModSystem.BlockLivingLogSection
Class WildFarmingFork.ModSystem.BlockMushroomSubstrate
Class WildFarmingFork.ModSystem.BlockTrunk
Class WildFarmingFork.ModSystem.BotanyConfig
Class WildFarmingFork.ModSystem.ItemMushroomSpawn
Class WildFarmingFork.ModSystem.SyncClientPacket
Class WildFarmingFork.ModSystem.TreeFriend
Class WildFarmingFork.ModSystem.TreeGenModifications
Class WildFarmingFork.ModSystem.WFR_BlockGetPlacedBlockInfo_Patch
Class WildFarmingFork.ModSystem.WildFarmingForkSystem
Class WildFarmingFork.ModSystem.WildPlantBlockEntity
Class WildFarmingFork.ModSystem.WildSeed
Class WildFarmingFork.ModConfig.ModConfig
Class WildFarmingFork.ModSystem.BlockBehaviorScore.<>c__DisplayClass8_0
Class WildFarmingFork.ModSystem.BlockBehaviorXSkillsSaplingCompat.<>c
Class WildFarmingFork.ModSystem.BlockBehaviorXSkillsSaplingCompat.<>c__DisplayClass5_0
Class WildFarmingFork.ModSystem.BlockEntityRegenSapling.<>c__DisplayClass1_0
Class WildFarmingFork.ModSystem.BlockEntityTermiteMound.<>c__DisplayClass1_0
Class WildFarmingFork.ModSystem.BlockEntityTrunk.<>c__DisplayClass29_0
Class WildFarmingFork.ModSystem.WildFarmingForkSystem.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 12 个配方文件与 1 个手册章节](/reference/recipes/wildfarmingfork)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
