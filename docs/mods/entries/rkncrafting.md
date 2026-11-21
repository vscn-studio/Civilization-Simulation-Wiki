# 制作系统

RKN Generic Crafting · 模组代码：rkncrafting

> 来源：整合包安装包 `RKN Generic Crafting-1.4.5.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `rkncrafting` |
| 版本 | 1.4.5 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0, jsonpatcheslib 1.5.0 |
| 作者 | Runekn |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Generic crafting system that completely replaces the UI grid with a more immersive mechanic.

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
| 程序集 | 1 | `RknCrafting.dll` |
| 方块定义 | 1 | `assets/rkncrafting/blocktypes/crafting.json` |
| 物品定义 | 1 | `assets/rkncrafting/itemtypes/unfinishedcraft.json` |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 16 | `assets/rkncrafting/patches/animations/axe.json`<br>`assets/rkncrafting/patches/animations/axehammer.json`<br>`assets/rkncrafting/patches/animations/chisel.json`<br>`assets/rkncrafting/patches/animations/chiselhammer.json`<br>`assets/rkncrafting/patches/animations/hammer.json`<br>`assets/rkncrafting/patches/animations/handsmixing.json`<br>`assets/rkncrafting/patches/animations/knife.json`<br>`assets/rkncrafting/patches/animations/saw.json`<br>`assets/rkncrafting/patches/animations/shears.json`<br>`assets/rkncrafting/patches/craftablesurface.json`<br>`assets/rkncrafting/patches/modcompatibility/butchering.json`<br>`assets/rkncrafting/patches/transformations/antlertransformations.json`<br>另有 4 个文件 |
| 语言资源 | 1 | `assets/rkncrafting/lang/en.json` |
| 手册资源 | 1 | `assets/rkncrafting/config/handbook/craftingguide.json` |
| 包内配置数据 | 1 | `assets/rkncrafting/config/rkncrafting_animations.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**RknCrafting.dll**（`d843de9058b84281`）：62 个类型。

```text
Class <Module>
Class <>z__ReadOnlySingleElementList
Class RknCrafting.GridIngredientAttribute
Class RknCrafting.HudMouseWorldSlotInteract
Class RknCrafting.RecipeSelectionDialog
Class RknCrafting.RknCraftingConfig
Class RknCrafting.UncommentContractResolver
Class RknCrafting.Patches.CraftingRecipeIngredientPatch
Class RknCrafting.Patches.GuiHandbookItemStackPagePatch
Class RknCrafting.Patches.SystemRenderDecalsPatch
Class RknCrafting.Entities.BlockBehaviorChiselSpawnCraftingSurface
Class RknCrafting.Entities.BlockEntityBehaviorCraftingSurfaceInWorldInventory
Class RknCrafting.Entities.CraftingItemRenderer
Class RknCrafting.Entities.SurfacePosTransform
Class RknCrafting.Entities.GridCountRenderer
Class RknCrafting.Entities.ItemUnfinishedCraft
Class RKN.Crafting.CoreApiExtensions
Class RKN.Crafting.RecipeService
Class RKN.Crafting.GridRecipeWrapper
Class RKN.Crafting.RecipeInputSlots
Class RKN.Crafting.DummySlot
Class RKN.Crafting.DummyInventory
Class RKN.Crafting.RknCraftingModSystem
Class RKN.Crafting.Patches.GridRecipePatch
Class RKN.Crafting.Patches.GuiDialogInventoryPatch
Class RKN.Crafting.Patches.GuiDialogTransformEditorPatch
Class RKN.Crafting.Network.CreateCraftingBlockMessage
Class RKN.Crafting.Network.CraftingStoppedMessage
Class RKN.Crafting.Network.SelectNextRecipeMessage
Class RKN.Crafting.Network.InventoryChangedMessage
Class RKN.Crafting.Network.ConfigMessage
Class RKN.Crafting.Network.ClientStartedCraftingMessage
Class RKN.Crafting.Network.PutToolIngredientMessage
Class RKN.Crafting.Network.BlockMouseInteractionMessage
Class RKN.Crafting.Network.RknCraftingNetwork
Class RKN.Crafting.Entities.BlockBehaviorSpawnCraftingSurface
Class RKN.Crafting.Entities.BlockCraftingSurface
Class RKN.Crafting.Entities.BlockEntityCraftingSurface
Class RKN.Crafting.Entities.CraftingParams
Class RKN.Crafting.Animation.AnimationConfig
```

其余 22 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 0 个配方文件与 1 个手册章节](/reference/recipes/rkncrafting)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
