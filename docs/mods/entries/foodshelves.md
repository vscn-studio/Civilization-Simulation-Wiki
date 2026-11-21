# 食物架

FoodShelves · 模组代码：foodshelves

> 来源：整合包安装包 `FoodShelves-3.1.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `foodshelves` |
| 版本 | 3.1.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | SONZ-INA |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Contains various food shelves and food storage, mainly made to be used alongside Expanded Foods.

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
| 程序集 | 1 | `FoodShelves.dll` |
| 方块定义 | 33 | `assets/foodshelves/blocktypes/barrels/barrelrack.json`<br>`assets/foodshelves/blocktypes/barrels/tun.json`<br>`assets/foodshelves/blocktypes/barrels/tunrack.json`<br>`assets/foodshelves/blocktypes/baskets/eggbasket.json`<br>`assets/foodshelves/blocktypes/baskets/fruitbasket.json`<br>`assets/foodshelves/blocktypes/baskets/mushroombasket.json`<br>`assets/foodshelves/blocktypes/baskets/vegetablebasket.json`<br>`assets/foodshelves/blocktypes/coolers/coolingcabinet.json`<br>`assets/foodshelves/blocktypes/coolers/fruitcooler.json`<br>`assets/foodshelves/blocktypes/coolers/icekeeper.json`<br>`assets/foodshelves/blocktypes/coolers/meatfreezer.json`<br>`assets/foodshelves/blocktypes/glassware/fooddisplayblock.json`<br>另有 21 个文件 |
| 物品定义 | 1 | `assets/foodshelves/itemtypes/cutice.json` |
| 实体定义 | 0 | — |
| 配方定义 | 32 | `assets/foodshelves/recipes/grid/barrels/barrelrack.json`<br>`assets/foodshelves/recipes/grid/barrels/tun.json`<br>`assets/foodshelves/recipes/grid/barrels/tunrack.json`<br>`assets/foodshelves/recipes/grid/baskets/eggbasket.json`<br>`assets/foodshelves/recipes/grid/baskets/fruitbasket.json`<br>`assets/foodshelves/recipes/grid/baskets/mushroombasket.json`<br>`assets/foodshelves/recipes/grid/baskets/vegetablebasket.json`<br>`assets/foodshelves/recipes/grid/coolers/coolingcabinet.json`<br>`assets/foodshelves/recipes/grid/coolers/fruitcooler.json`<br>`assets/foodshelves/recipes/grid/coolers/icekeeper.json`<br>`assets/foodshelves/recipes/grid/coolers/meatfreezer.json`<br>`assets/foodshelves/recipes/grid/cutice.json`<br>另有 20 个文件 |
| 资产补丁 | 21 | `assets/foodshelves/patches/artofcooking.json`<br>`assets/foodshelves/patches/artofgrowing.json`<br>`assets/foodshelves/patches/butchering.json`<br>`assets/foodshelves/patches/carryon.json`<br>`assets/foodshelves/patches/chiseltools.json`<br>`assets/foodshelves/patches/clayworks.json`<br>`assets/foodshelves/patches/detailedanimals.json`<br>`assets/foodshelves/patches/expandedfoods.json`<br>`assets/foodshelves/patches/floralzones.json`<br>`assets/foodshelves/patches/gourmand.json`<br>`assets/foodshelves/patches/lakeicerecipe.json`<br>`assets/foodshelves/patches/longtermfood.json`<br>另有 9 个文件 |
| 语言资源 | 9 | `assets/foodshelves/lang/cs.json`<br>`assets/foodshelves/lang/en.json`<br>`assets/foodshelves/lang/fr.json`<br>`assets/foodshelves/lang/pl.json`<br>`assets/foodshelves/lang/pt-br.json`<br>`assets/foodshelves/lang/ru.json`<br>`assets/foodshelves/lang/sr.json`<br>`assets/foodshelves/lang/uk.json`<br>`assets/foodshelves/lang/zn-cn.json` |
| 手册资源 | 1 | `assets/foodshelves/config/handbook/31-foodshelvesguide.json` |
| 包内配置数据 | 33 | `assets/foodshelves/config/restrictions/barrels/barrelrack.json`<br>`assets/foodshelves/config/restrictions/barrels/firkinrack.json`<br>`assets/foodshelves/config/restrictions/barrels/tunrack.json`<br>`assets/foodshelves/config/restrictions/baskets/eggbasket.json`<br>`assets/foodshelves/config/restrictions/baskets/fruitbasket.json`<br>`assets/foodshelves/config/restrictions/baskets/mushroombasket.json`<br>`assets/foodshelves/config/restrictions/baskets/vegetablebasket.json`<br>`assets/foodshelves/config/restrictions/coolers/fruitcooler.json`<br>`assets/foodshelves/config/restrictions/coolers/meatfreezer.json`<br>`assets/foodshelves/config/restrictions/general/coolingonly.json`<br>`assets/foodshelves/config/restrictions/general/fooduniversal.json`<br>`assets/foodshelves/config/restrictions/general/holderuniversal.json`<br>另有 21 个文件 |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**FoodShelves.dll**（`690d47229d8cdda2`）：134 个类型。

```text
Class <Module>
Class FoodShelves.BaseFSBasket
Class FoodShelves.BaseFSContainer
Class FoodShelves.BEBaseFSAnimatable
Class FoodShelves.BEBaseFSBasket
Class FoodShelves.BEBaseFSContainer
Class FoodShelves.BEBaseFSCooler
Class FoodShelves.BlockBehaviorShiftRightClickPickup
Class FoodShelves.BEBarrelRack
Class FoodShelves.BETunRack
Class FoodShelves.BEEggBasket
Class FoodShelves.BEFruitBasket
Class FoodShelves.BEMushroomBasket
Class FoodShelves.BEVegetableBasket
Class FoodShelves.BECoolingCabinet
Class FoodShelves.BEFruitCooler
Class FoodShelves.BEIceKeeper
Class FoodShelves.BEMeatFreezer
Class FoodShelves.BEFoodDisplayBlock
Class FoodShelves.BEFoodDisplayCase
Class FoodShelves.BEJar
Class FoodShelves.BEJarLarge
Class FoodShelves.BESeedBins
Class FoodShelves.BEWallCabinet
Class FoodShelves.BEBucketHook
Class FoodShelves.BECeilingRack
Class FoodShelves.BEFlourSack
Class FoodShelves.BEJarStand
Class FoodShelves.BEPumpkinCase
Class FoodShelves.BETableWShelf
Class FoodShelves.BEBarShelf
Class FoodShelves.BEBreadShelf
Class FoodShelves.BEDoubleShelf
Class FoodShelves.BEEggShelf
Class FoodShelves.BEPieShelf
Class FoodShelves.BESeedShelf
Class FoodShelves.BEShortShelf
Class FoodShelves.BESushiShelf
Class FoodShelves.BlockBarrelRack
Class FoodShelves.BlockTunRack
```

其余 94 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 32 个配方文件与 1 个手册章节](/reference/recipes/foodshelves)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
