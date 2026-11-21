# 天然肥料

Natural Fertilizer · 模组代码：naturalfertilizer

> 来源：整合包安装包 `Natural Fertilizer-1.5.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `naturalfertilizer` |
| 版本 | 1.5.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | xXx_Ape_xXx |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds natural fertilizer created from animal droppings

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
| 程序集 | 1 | `naturalfertilizer.dll` |
| 方块定义 | 6 | `assets/naturalfertilizer/blocktypes/dung.json`<br>`assets/naturalfertilizer/blocktypes/fertilizer/weakfertilizerblock.json`<br>`assets/naturalfertilizer/blocktypes/manure/manurepile.json`<br>`assets/naturalfertilizer/blocktypes/manure/manurestack.json`<br>`assets/naturalfertilizer/blocktypes/poop/chickenpoop.json`<br>`assets/naturalfertilizer/blocktypes/poop/smallpoop.json` |
| 物品定义 | 5 | `assets/naturalfertilizer/itemtypes/liquid/manuremixportion.json`<br>`assets/naturalfertilizer/itemtypes/liquid/manureslurryportion.json`<br>`assets/naturalfertilizer/itemtypes/manure.json`<br>`assets/naturalfertilizer/itemtypes/maturefertilizer.json`<br>`assets/naturalfertilizer/itemtypes/weakfertilizer.json` |
| 实体定义 | 0 | — |
| 配方定义 | 4 | `assets/naturalfertilizer/recipes/barrel/manurecompost.json`<br>`assets/naturalfertilizer/recipes/barrel/manuremixgrass.json`<br>`assets/naturalfertilizer/recipes/barrel/manuremixthatch.json`<br>`assets/naturalfertilizer/recipes/barrel/manureslurry.json` |
| 资产补丁 | 9 | `assets/naturalfertilizer/compatibility/bovinae/patches/entity-patches.json`<br>`assets/naturalfertilizer/compatibility/equus/patches/entity-patches.json`<br>`assets/naturalfertilizer/compatibility/feverstonehorses/patches/entity-patches.json`<br>`assets/naturalfertilizer/compatibility/fowlmod/patches/entity-patches.json`<br>`assets/naturalfertilizer/compatibility/lichenredux/patches/entity-patches.json`<br>`assets/naturalfertilizer/compatibility/medievalexpansionpatch/patches/entity-patches.json`<br>`assets/naturalfertilizer/compatibility/moreanimals/patches/entity-patches.json`<br>`assets/naturalfertilizer/compatibility/thecritterpack/patches/entity-patches.json`<br>`assets/naturalfertilizer/patches/entity-patches.json` |
| 语言资源 | 3 | `assets/naturalfertilizer/lang/en.json`<br>`assets/naturalfertilizer/lang/ru.json`<br>`assets/naturalfertilizer/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**naturalfertilizer.dll**（`7dea03978371eb21`）：38 个类型。

```text
Class <Module>
Class naturalfertilizer.BEManurePile
Class naturalfertilizer.BlockEntityManureStack
Class naturalfertilizer.ManureFermentationProps
Class naturalfertilizer.ManurePileTypeProperties
Class naturalfertilizer.ManurePileProperties
Class naturalfertilizer.ItemStackRenderCacheItem
Class naturalfertilizer.CollectibleBehaviorManurePile
Class naturalfertilizer.BlockManurePile
Class naturalfertilizer.BlockManureStack
Class naturalfertilizer.ManureStackProperties
Class naturalfertilizer.CollectibleBehaviorManureStack
Class naturalfertilizer.Core
Class naturalfertilizer.EntityBehaviorDefecate
Class naturalfertilizer.EntityBehaviorTrackEating
Class naturalfertilizer.BuzzingFlies
Class naturalfertilizer.Patch_AiTaskSeekFoodAndEat
Class naturalfertilizer.EatTaskAccess
Class naturalfertilizer.Configs
Class naturalfertilizer.AnimalNutritionTracker
Class naturalfertilizer.AiTask.AiTaskDefecate
Class naturalfertilizer.BEManurePile.<>c
Class naturalfertilizer.BlockEntityManureStack.<>c
Class naturalfertilizer.BlockEntityManureStack.<>c__DisplayClass63_0
Class naturalfertilizer.BlockEntityManureStack.<>c__DisplayClass68_0
Class naturalfertilizer.BlockEntityManureStack.<>c__DisplayClass68_1
Class naturalfertilizer.BlockEntityManureStack.<>c__DisplayClass68_2
Class naturalfertilizer.BlockManurePile.<>c
Class naturalfertilizer.BlockManureStack.<>c
Class naturalfertilizer.Core.DebugUtil
Class naturalfertilizer.EntityBehaviorDefecate.<>O
Class naturalfertilizer.EntityBehaviorDefecate.<>c__DisplayClass21_0
Class naturalfertilizer.BuzzingFlies.<>c
Class naturalfertilizer.BuzzingFlies.<>c__DisplayClass10_0
Class naturalfertilizer.BuzzingFlies.<>c__DisplayClass18_0
Class naturalfertilizer.BuzzingFlies.<>c__DisplayClass20_0
Class naturalfertilizer.Configs.ServerConfig
Class naturalfertilizer.Configs.ClientConfig
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 4 个配方文件与 0 个手册章节](/reference/recipes/naturalfertilizer)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
