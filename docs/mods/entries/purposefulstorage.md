# 专用储存

PurposefulStorage · 模组代码：purposefulstorage

> 来源：整合包安装包 `PurposefulStorage-2.3.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `purposefulstorage` |
| 版本 | 2.3.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | SONZ-INA |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds a variety of storage blocks designed for both aesthetic appeal and functional item organization.

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
| 程序集 | 1 | `PurposefulStorage.dll` |
| 方块定义 | 26 | `assets/purposefulstorage/blocktypes/clothes/belthooks.json`<br>`assets/purposefulstorage/blocktypes/clothes/blanketrack.json`<br>`assets/purposefulstorage/blocktypes/clothes/gloverack.json`<br>`assets/purposefulstorage/blocktypes/clothes/hatrack.json`<br>`assets/purposefulstorage/blocktypes/clothes/necklacestand.json`<br>`assets/purposefulstorage/blocktypes/clothes/pantsrack.json`<br>`assets/purposefulstorage/blocktypes/clothes/shoerack.json`<br>`assets/purposefulstorage/blocktypes/clothes/wardrobe.json`<br>`assets/purposefulstorage/blocktypes/general/apothecarycabinet.json`<br>`assets/purposefulstorage/blocktypes/general/butterflydisplaypanel.json`<br>`assets/purposefulstorage/blocktypes/general/gearrack.json`<br>`assets/purposefulstorage/blocktypes/general/glidermount.json`<br>另有 14 个文件 |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 26 | `assets/purposefulstorage/recipes/grid/clothes/belthooks.json`<br>`assets/purposefulstorage/recipes/grid/clothes/blanketrack.json`<br>`assets/purposefulstorage/recipes/grid/clothes/gloverack.json`<br>`assets/purposefulstorage/recipes/grid/clothes/hatrack.json`<br>`assets/purposefulstorage/recipes/grid/clothes/necklacestand.json`<br>`assets/purposefulstorage/recipes/grid/clothes/pantsrack.json`<br>`assets/purposefulstorage/recipes/grid/clothes/shoerack.json`<br>`assets/purposefulstorage/recipes/grid/clothes/wardrobe.json`<br>`assets/purposefulstorage/recipes/grid/general/apothecarycabinet.json`<br>`assets/purposefulstorage/recipes/grid/general/butterflydisplaypanel.json`<br>`assets/purposefulstorage/recipes/grid/general/gearrack.json`<br>`assets/purposefulstorage/recipes/grid/general/glidermount.json`<br>另有 14 个文件 |
| 资产补丁 | 10 | `assets/purposefulstorage/patches/allclasses.json`<br>`assets/purposefulstorage/patches/armory.json`<br>`assets/purposefulstorage/patches/basegame.json`<br>`assets/purposefulstorage/patches/betterruins.json`<br>`assets/purposefulstorage/patches/butchering.json`<br>`assets/purposefulstorage/patches/carryon.json`<br>`assets/purposefulstorage/patches/draconis.json`<br>`assets/purposefulstorage/patches/longtermfood.json`<br>`assets/purposefulstorage/patches/primitivesurvival.json`<br>`assets/purposefulstorage/patches/wool&amp;more.json` |
| 语言资源 | 5 | `assets/purposefulstorage/lang/en.json`<br>`assets/purposefulstorage/lang/ko.json`<br>`assets/purposefulstorage/lang/pl.json`<br>`assets/purposefulstorage/lang/ru.json`<br>`assets/purposefulstorage/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 56 | `assets/purposefulstorage/config/restrictions/clothes/blankets.json`<br>`assets/purposefulstorage/config/restrictions/clothes/footware.json`<br>`assets/purposefulstorage/config/restrictions/clothes/handware.json`<br>`assets/purposefulstorage/config/restrictions/clothes/headware.json`<br>`assets/purposefulstorage/config/restrictions/clothes/lowerbodyware.json`<br>`assets/purposefulstorage/config/restrictions/clothes/neckware.json`<br>`assets/purposefulstorage/config/restrictions/clothes/shoulderware.json`<br>`assets/purposefulstorage/config/restrictions/clothes/upperbodyware.json`<br>`assets/purposefulstorage/config/restrictions/clothes/waistware.json`<br>`assets/purposefulstorage/config/restrictions/general/bandages.json`<br>`assets/purposefulstorage/config/restrictions/general/butterflies.json`<br>`assets/purposefulstorage/config/restrictions/general/gears.json`<br>另有 44 个文件 |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**PurposefulStorage.dll**（`8931c7c5bb3937c7`）：106 个类型。

```text
Class <Module>
Class BEArrowRack
Class PurposefulStorage.BasePSContainer
Class PurposefulStorage.BEBasePSAnimatable
Class PurposefulStorage.BEBasePSContainer
Class PurposefulStorage.BEBeltHooks
Class PurposefulStorage.BEBlanketRack
Class PurposefulStorage.BEGloveRack
Class PurposefulStorage.BEHatRack
Class PurposefulStorage.BENecklaceStand
Class PurposefulStorage.BEPantsRack
Class PurposefulStorage.BEShoeRack
Class PurposefulStorage.BEWardrobe
Class PurposefulStorage.BEApothecaryCabinet
Class PurposefulStorage.BEButterflyDisplayPanel
Class PurposefulStorage.BEGearRack
Class PurposefulStorage.BEGliderMount
Class PurposefulStorage.BEJonasPartsCabinet
Class PurposefulStorage.BEMedallionRack
Class PurposefulStorage.BESaddleRack
Class PurposefulStorage.BESchematicRack
Class PurposefulStorage.BETuningCylinderRack
Class PurposefulStorage.BEClothRack
Class PurposefulStorage.BEPeltRack
Class PurposefulStorage.BEResourceBin
Class PurposefulStorage.BERopeRack
Class PurposefulStorage.BESpearRack
Class PurposefulStorage.BESwordPedestal
Class PurposefulStorage.BESwordPlaque
Class PurposefulStorage.BEWeaponRack
Class PurposefulStorage.BlockHatRack
Class PurposefulStorage.BlockWardrobe
Class PurposefulStorage.BlockApothecaryCabinet
Class PurposefulStorage.BlockGliderMount
Class PurposefulStorage.BlockJonasPartsContainer
Class PurposefulStorage.BlockPeltRack
Class PurposefulStorage.BlockSpearRack
Class PurposefulStorage.BlockWeaponRack
Class PurposefulStorage.AnimationData
Class PurposefulStorage.ShapeReferences
```

其余 66 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 26 个配方文件与 0 个手册章节](/reference/recipes/purposefulstorage)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
