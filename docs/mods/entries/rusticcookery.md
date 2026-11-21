# 乡野烹饪

Rustic Cookery · 模组代码：rusticcookery

> 来源：整合包安装包 `Rustic Cookery-1.2.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `rusticcookery` |
| 版本 | 1.2.0 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Fleece |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Enjoy hearty pot roasts and braised dishes alongside a new meat slab texture compatible with most creature mods.

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
| 程序集 | 1 | `RusticCookery.dll` |
| 方块定义 | 9 | `assets/rusticcookery/blocktypes/braise.json`<br>`assets/rusticcookery/blocktypes/placedslab.json`<br>`assets/rusticcookery/blocktypes/roast.json`<br>`assets/rusticcookery/blocktypes/roastingdish-fired.json`<br>`assets/rusticcookery/blocktypes/roastingdish-raw.json`<br>`assets/rusticcookery/blocktypes/roastingdishlid-fired.json`<br>`assets/rusticcookery/blocktypes/roastingdishlid-raw.json`<br>`assets/rusticcookery/blocktypes/smokehook.json`<br>`assets/rusticcookery/blocktypes/smokerack.json` |
| 物品定义 | 2 | `assets/rusticcookery/itemtypes/meatslab.json`<br>`assets/rusticcookery/itemtypes/smokedfish.json` |
| 实体定义 | 0 | — |
| 配方定义 | 4 | `assets/rusticcookery/recipes/clayforming/roastingdish.json`<br>`assets/rusticcookery/recipes/clayforming/roastingdishlid.json`<br>`assets/rusticcookery/recipes/grid/smokehook.json`<br>`assets/rusticcookery/recipes/grid/smokerack.json` |
| 资产补丁 | 2 | `assets/rusticcookery/patches/firepit-braising.json`<br>`assets/rusticcookery/patches/vanilla-smoked-meat.json` |
| 语言资源 | 1 | `assets/rusticcookery/lang/en.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 5 | `assets/rusticcookery/config/braisingfats.json`<br>`assets/rusticcookery/config/braisingliquids.json`<br>`assets/rusticcookery/config/braisingmeats.json`<br>`assets/rusticcookery/config/eggsides.json`<br>`assets/rusticcookery/config/toppings.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**RusticCookery.dll**（`439fb78eea33a850`）：108 个类型。

```text
Class <Module>
Class RusticCookery.BlockEntitySmokeHook
Class RusticCookery.BlockEntitySmokeRack
Class RusticCookery.BlockSmokeHook
Class RusticCookery.BlockSmokeRack
Class RusticCookery.BEBehaviorBraisingSound
Class RusticCookery.BlockBehaviorBraising
Class RusticCookery.BlockBraise
Class RusticCookery.BlockEntityBraise
Class RusticCookery.BraiseActions
Class RusticCookery.BraiseMeshes
Class RusticCookery.BraiseRecipe
Class RusticCookery.BraiseNaming
Class RusticCookery.BraisingFats
Class RusticCookery.BraisingMeats
Class RusticCookery.EggMeshes
Class RusticCookery.EggRecipes
Class RusticCookery.EggNaming
Class RusticCookery.EggSides
Class RusticCookery.ButcheringCompat
Class RusticCookery.ConfigSync
Class RusticCookery.ItemMeatSlab
Class RusticCookery.ItemSmokedFish
Class RusticCookery.BlockEntityRoast
Class RusticCookery.BlockRoast
Class RusticCookery.BlockRoastingDish
Class RusticCookery.BraisingLiquids
Class RusticCookery.DishLid
Class RusticCookery.PotRoastRecipe
Class RusticCookery.PotRoastNaming
Class RusticCookery.RoastHandbookPatch
Class RusticCookery.RoastMeshes
Class RusticCookery.RoastNutrition
Class RusticCookery.RoastSides
Class RusticCookery.RoastSideStyles
Class RusticCookery.StewLooks
Class RusticCookery.Toppings
Class RusticCookery.RusticCookeryConfig
Class RusticCookery.SlabRule
Class RusticCookery.RusticCookeryModSystem
```

其余 68 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 4 个配方文件与 0 个手册章节](/reference/recipes/rusticcookery)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
