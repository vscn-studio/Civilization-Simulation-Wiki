# 手册改进

Better Handbook · 模组代码：betterhandbook

> 来源：整合包安装包 `Better Handbook-1.0.9.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `betterhandbook` |
| 版本 | 1.0.9 |
| 类型 | 含程序代码 |
| 运行端 | client |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | garward |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“界面、汉化与客户端工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Improves the survival handbook with fast cached opening/scrolling, adds item usage lookup, and adds handbook auto fill helpers.

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
| 程序集 | 1 | `BetterHandbook.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 1 | `assets/betterhandbook/lang/en.json` |
| 手册资源 | 2 | `BetterHandbook.deps.json`<br>`assets/betterhandbook/config/configlib-patches.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**BetterHandbook.dll**（`0929a66242d5431c`）：84 个类型。

```text
Class <Module>
Class HandbookCache.CraftingOutputConflictScrollSystem
Class HandbookCache.CraftingOutputConflictSelector
Class HandbookCache.CraftingOutputActivateSlotPatch
Class HandbookCache.CraftingOutputFindMatchingRecipePatch
Class HandbookCache.CraftingOutputMouseWheelPatch
Class HandbookCache.HandbookBarrelRecipeStackIsolationPatch
Class HandbookCache.HandbookBookmarks
Class HandbookCache.HandbookBookmarkButtonPatch
Class HandbookCache.HandbookCacheModSystem
Class HandbookCache.HandbookCreatedByRecipeFilter
Class HandbookCache.HandbookGetInfoCreatedByFilterPatch
Class HandbookCache.HandbookCreatedByGridRecipesPatch
Class HandbookCache.HandbookCreatedByRecipeFilterInvalidationPatch
Class HandbookCache.HandbookCacheDiagnostics
Class HandbookCache.HandbookFilterCachePatch
Class HandbookCache.HandbookSearchTextPatch
Class HandbookCache.HandbookOverviewScrollPatch
Class HandbookCache.HandbookOpenCachePatch
Class HandbookCache.HandbookDetailCacheTrackingPatch
Class HandbookCache.HandbookLoadEntriesCacheInvalidationPatch
Class HandbookCache.HandbookLoadPagesCacheInvalidationPatch
Class HandbookCache.HandbookCloseCachePatch
Class HandbookCache.HandbookGenericTypedContainerDropPatch
Class HandbookCache.HandbookModCategories
Class HandbookCache.ModCategoryListItem
Class HandbookCache.HandbookModTabsPatch
Class HandbookCache.HandbookModListClickPatch
Class HandbookCache.HandbookModsTabClickPatch
Class HandbookCache.HandbookModOverviewCategoryPatch
Class HandbookCache.HandbookSlideshowScrollPatch
Class HandbookCache.HandbookVariantGrouping
Class HandbookCache.VariantGroupHandbookPage
Class RecipeExplorer.AutoCraftSystem
Class RecipeExplorer.BetterHandbookConfigLibIntegration
Class RecipeExplorer.GuiDialogRecipeUses
Class RecipeExplorer.HandbookRecipeAssets
Class RecipeExplorer.HandbookRecipeOverlays
Class RecipeExplorer.ModConfig
Class RecipeExplorer.BetterHandbookLog
```

其余 44 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
