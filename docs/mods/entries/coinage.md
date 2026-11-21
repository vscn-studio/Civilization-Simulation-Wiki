# 铸币

Coinage · 模组代码：coinage

> 来源：整合包安装包 `Coinage-2.4.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `coinage` |
| 版本 | 2.4.0 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | xel |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds customizable coins and coinmaking tools to the game

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
| 程序集 | 2 | `Clipper2Lib.dll`<br>`Coinage.dll` |
| 方块定义 | 6 | `assets/coinage/blocktypes/coinbag.json`<br>`assets/coinage/blocktypes/mechanical/pressautofeed.json`<br>`assets/coinage/blocktypes/wood/coinpress.json`<br>`assets/coinage/blocktypes/wood/coinpresstop.json`<br>`assets/coinage/blocktypes/wood/displaystand.json`<br>`assets/coinage/blocktypes/wood/pile.json` |
| 物品定义 | 7 | `assets/coinage/itemtypes/resource/coin.json`<br>`assets/coinage/itemtypes/resource/planchet.json`<br>`assets/coinage/itemtypes/tool/anvildie.json`<br>`assets/coinage/itemtypes/tool/punch.json`<br>`assets/coinage/itemtypes/tool/punchpart.json`<br>`assets/coinage/itemtypes/tool/trussell.json`<br>`assets/coinage/itemtypes/wearable/coinpouch.json` |
| 实体定义 | 0 | — |
| 配方定义 | 10 | `assets/coinage/recipes/grid/block/displaystand.json`<br>`assets/coinage/recipes/grid/coinbag.json`<br>`assets/coinage/recipes/grid/coinpress.json`<br>`assets/coinage/recipes/grid/coinpressfeeder.json`<br>`assets/coinage/recipes/grid/pile.json`<br>`assets/coinage/recipes/grid/resource/planchet.json`<br>`assets/coinage/recipes/grid/tool/anvildie.json`<br>`assets/coinage/recipes/grid/tool/punch.json`<br>`assets/coinage/recipes/grid/tool/trussell.json`<br>`assets/coinage/recipes/smithing/punchpart.json` |
| 资产补丁 | 6 | `assets/coinage/patches/compat/xskills/smeltingratios.json`<br>`assets/coinage/patches/config/tradelists/trader-artisan.json`<br>`assets/coinage/patches/config/tradelists/trader-clothing.json`<br>`assets/coinage/patches/entities/player.json`<br>`assets/coinage/patches/remaps.json`<br>`assets/coinage/patches/shapes/seraph-faceless.json` |
| 语言资源 | 7 | `assets/coinage/lang/en.json`<br>`assets/coinage/lang/fr.json`<br>`assets/coinage/lang/pl.json`<br>`assets/coinage/lang/ru.json`<br>`assets/game/lang/en.json`<br>`assets/game/lang/pl.json`<br>`assets/game/lang/ru.json` |
| 手册资源 | 1 | `assets/game/config/handbook/56-guide-coins.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Clipper2Lib.dll**（`e9bf01e01f494ef6`）：47 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.IsReadOnlyAttribute
Class System.Runtime.CompilerServices.NullableAttribute
Class System.Runtime.CompilerServices.NullableContextAttribute
Class Clipper2Lib.Path64
Class Clipper2Lib.Paths64
Class Clipper2Lib.PathD
Class Clipper2Lib.PathsD
Class Clipper2Lib.InternalClipper
Class Clipper2Lib.Clipper
Class Clipper2Lib.Vertex
Class Clipper2Lib.OutPt
Class Clipper2Lib.OutRec
Class Clipper2Lib.HorzSegment
Class Clipper2Lib.HorzJoin
Class Clipper2Lib.Active
Class Clipper2Lib.ClipperEngine
Class Clipper2Lib.ReuseableDataContainer64
Class Clipper2Lib.ClipperBase
Class Clipper2Lib.Clipper64
Class Clipper2Lib.ClipperD
Class Clipper2Lib.PolyPathBase
Class Clipper2Lib.PolyPath64
Class Clipper2Lib.PolyPathD
Class Clipper2Lib.PolyTree64
Class Clipper2Lib.PolyTreeD
Class Clipper2Lib.ClipperLibException
Class Clipper2Lib.Minkowski
Class Clipper2Lib.ClipperOffset
Class Clipper2Lib.OutPt2
Class Clipper2Lib.RectClip64
Class Clipper2Lib.RectClipLines64
Class Clipper2Lib.Vertex2
Class Clipper2Lib.Edge
Class Clipper2Lib.Triangle
Class Clipper2Lib.Delaunay
Class Clipper2Lib.VertexPoolList
Class Clipper2Lib.OutPtPoolList
Class Clipper2Lib.OutRecPoolList
```

其余 7 个类型未在此列出；可按维护说明重新分析程序集。

**Coinage.dll**（`ad8c7db343bed491`）：122 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>f__AnonymousType1
Class Coinage.CoinageModSystem
Class Coinage.Constants
Class Coinage.Util.CoinTesselator
Class Coinage.Util.CollectibleUtils
Class Coinage.Util.GeometryUtils
Class Coinage.Util.LangUtils
Class Coinage.Util.LegacyCoinShapes
Class Coinage.Util.Logger
Class Coinage.Util.MeshUtils
Class Coinage.Util.Polylabel
Class Coinage.Systems.CoinageCommandSystem
Class Coinage.Systems.CoinageMeshCacheSystem
Class Coinage.Systems.CoinagePatchSystem
Class Coinage.Patches.BlockEntityContainer_InitializePatch
Class Coinage.Patches.BlockEntityGroundStorage_OnTesselationPatch
Class Coinage.Patches.CharacterSystem_OnMatchesGridRecipePatch
Class Coinage.Patches.InventoryBase_OpenPatch
Class Coinage.Packets.CoinpressAnimPacket
Class Coinage.Packets.NetworkCreateCoinType
Class Coinage.Packets.NetworkOpenDialog
Class Coinage.Packets.NetworkRequestAllData
Class Coinage.Packets.NetworkRequestCoinTypes
Class Coinage.Packets.NetworkResponseAllData
Class Coinage.Packets.NetworkResponseCoinTypes
Class Coinage.Packets.NetworkResponseConfig
Class Coinage.Items.ItemAnvilDie
Class Coinage.Items.ItemCoin
Class Coinage.Items.ItemPlanchet
Class Coinage.Items.ItemPunch
Class Coinage.Items.ItemShapable
Class Coinage.Items.ItemShapableMetalDisc
Class Coinage.Items.ItemTrussell
Class Coinage.Inventory.InventoryAnvilPile
Class Coinage.Gui.GuiAnvilPile
Class Coinage.Gui.GuiCoinAdmin
Class Coinage.Gui.GuiCoinDesigner
Class Coinage.Gui.GuiCoinShaper
```

其余 82 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 10 个配方文件与 1 个手册章节](/reference/recipes/coinage)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
