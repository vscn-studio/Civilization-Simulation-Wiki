# 采集收获

Foragers Gamble · 模组代码：foragersgamble

> 来源：整合包安装包 `Foragers Gamble-1.3.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `foragersgamble` |
| 版本 | 1.3.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | Chronolegionnaire |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Masks food safety and names until after eaten.

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
| 程序集 | 1 | `ForagersGamble.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 1 | `assets/foragersgamble/itemtypes/knowledgebook.json` |
| 实体定义 | 0 | — |
| 配方定义 | 2 | `assets/foragersgamble/recipes/grid/booktoknowledge.json`<br>`assets/foragersgamble/recipes/grid/knowledgetobook.json` |
| 资产补丁 | 0 | — |
| 语言资源 | 3 | `assets/foragersgamble/lang/en.json`<br>`assets/foragersgamble/lang/pt-br.json`<br>`assets/foragersgamble/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ForagersGamble.dll**（`e0ca2536d4c3a63b`）：90 个类型。

```text
Class <Module>
Class HandbookVisibility
Class Patch_CookingRecipe_GetOutputName
Class Patch_Handbook_FilterItems
Class Patch_BlockMeal_GetContentNutritionFacts_Postfix
Class Patch_Handbook_OpenDetail
Class ForagersGamble.FoodKnowledgeIndex
Class ForagersGamble.ForagersGambleModSystem
Class ForagersGamble.Knowledge
Class ForagersGamble.PlantKnowledgeIndex
Class ForagersGamble.PlantKnowledgeUtil
Class ForagersGamble.Util
Class ForagersGamble.Randomize.Randomizer
Class ForagersGamble.Patches.NameMaskingScope
Class ForagersGamble.Patches.FruitTreeGatingHelpers
Class ForagersGamble.Patches.Patch_BlockFruitTreeBranch_GetPlacedBlockName
Class ForagersGamble.Patches.Patch_BlockFruitTreeFoliage_GetPlacedBlockName
Class ForagersGamble.Patches.Patch_BlockFruitTreeBranch_GetHeldItemName
Class ForagersGamble.Patches.ComposeCreativeInvDialog
Class ForagersGamble.Patches.Patch_CreativeTabs_CreateSearchCache
Class ForagersGamble.Patches.EatPoisonInterceptor
Class ForagersGamble.Patches.Patch_Entity_ReceiveDamage
Class ForagersGamble.Patches.Patch_EntityAgent_ReceiveDamage
Class ForagersGamble.Patches.Patch_TopOpened_GetContainedInfo_UnknownLiquid
Class ForagersGamble.Patches.Patch_Base_GetContentInfo_UnknownLiquid
Class ForagersGamble.Patches.DisplayGating
Class ForagersGamble.Patches.Patch_CollectibleObject_GetHeldItemInfo
Class ForagersGamble.Patches.Patch_CollectibleObject_GetHeldItemName
Class ForagersGamble.Patches.Patch_Block_GetPlacedBlockInfo
Class ForagersGamble.Patches.Patch_Base_GetPlacedBlockInfo_UnknownLiquid
Class ForagersGamble.Patches.Patch_ItemPlantableSeed_GetHeldItemInfo
Class ForagersGamble.Patches.NibbleLiquidKeys
Class ForagersGamble.Patches.Patch_LiquidContainer_TryEatStop_ScaleOnSneak
Class ForagersGamble.Patches.Patch_LiquidContainer_TryEatStop_Capture
Class ForagersGamble.Patches.Patch_LiquidContainer_TryEatStop_Knowledge
Class ForagersGamble.Patches.NibblePortionUtil
Class ForagersGamble.Patches.Patch_LiquidContainer_TryEatStop_HydrationPortion
Class ForagersGamble.Patches.Patch_GuiDialogHandbook_LoadPages_Async
Class ForagersGamble.Patches.IngredientMasking
Class ForagersGamble.Patches.Patch_ItemPressedMash_GetHeldItemName
```

其余 50 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 2 个配方文件与 0 个手册章节](/reference/recipes/foragersgamble)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
