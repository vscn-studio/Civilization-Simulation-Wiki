# 经济系统

Vinconomy · 模组代码：vinconomy

> 来源：整合包安装包 `Vinconomy-6.0.3.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vinconomy` |
| 版本 | 6.0.3 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0, commercially 0.1.1 |
| 作者 | Severed Skullz |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

An Economy Mod allowing players to establish their own shops and sell goods to other players

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
| 程序集 | 1 | `Vinconomy.dll` |
| 方块定义 | 16 | `assets/vinconomy/blocktypes/autoteller.json`<br>`assets/vinconomy/blocktypes/buffettable.json`<br>`assets/vinconomy/blocktypes/clothingstall.json`<br>`assets/vinconomy/blocktypes/couponsslicer.json`<br>`assets/vinconomy/blocktypes/crate.json`<br>`assets/vinconomy/blocktypes/gachastall.json`<br>`assets/vinconomy/blocktypes/purchasestall.json`<br>`assets/vinconomy/blocktypes/sculpturepad.json`<br>`assets/vinconomy/blocktypes/shopbarrel.json`<br>`assets/vinconomy/blocktypes/shopdispenser.json`<br>`assets/vinconomy/blocktypes/shopmat.json`<br>`assets/vinconomy/blocktypes/shopmatdouble.json`<br>另有 4 个文件 |
| 物品定义 | 8 | `assets/vinconomy/itemtypes/catalog.json`<br>`assets/vinconomy/itemtypes/coupon.json`<br>`assets/vinconomy/itemtypes/gachaball.json`<br>`assets/vinconomy/itemtypes/ledger.json`<br>`assets/vinconomy/itemtypes/sculpturebundle.json`<br>`assets/vinconomy/itemtypes/shopcoupon.json`<br>`assets/vinconomy/itemtypes/stallcoupon.json`<br>`assets/vinconomy/itemtypes/tenretnibook.json` |
| 实体定义 | 0 | — |
| 配方定义 | 21 | `assets/vinconomy/recipes/disabled_recipies/reimbursement-shop.json`<br>`assets/vinconomy/recipes/disabled_recipies/reimbursement-stall.json`<br>`assets/vinconomy/recipes/disabled_recipies/tenretni.json`<br>`assets/vinconomy/recipes/grid/catalog.json`<br>`assets/vinconomy/recipes/grid/clothingstall.json`<br>`assets/vinconomy/recipes/grid/couponcutter.json`<br>`assets/vinconomy/recipes/grid/gachastall.json`<br>`assets/vinconomy/recipes/grid/ledger.json`<br>`assets/vinconomy/recipes/grid/mealtable.json`<br>`assets/vinconomy/recipes/grid/producecrate.json`<br>`assets/vinconomy/recipes/grid/purchasecrate.json`<br>`assets/vinconomy/recipes/grid/sculpturestand.json`<br>另有 9 个文件 |
| 资产补丁 | 1 | `assets/vinconomy/patches/toolrack-display-fix.json` |
| 语言资源 | 7 | `assets/vinconomy/lang/en.json`<br>`assets/vinconomy/lang/fr.json`<br>`assets/vinconomy/lang/pl.json`<br>`assets/vinconomy/lang/ru.json`<br>`assets/vinconomy/lang/uk.json`<br>`assets/vinconomy/lang/zh-cn.json`<br>`assets/vinconomy/lang/zh-tw.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Vinconomy.dll**（`9bb586b8c33aa0fd`）：123 个类型。

```text
Class <Module>
Class Vinconomy.Network.Packets.LedgerEntryRequestPacket
Class Vinconomy.Network.Packets.LedgerEntryResponsePacket
Class Vinconomy.Network.Packets.LedgerEntry
Class Vinconomy.Network.Packets.LedgerReadRequestPacket
Class Vinconomy.Network.Packets.LedgerReadResponsePacket
Class Vinconomy.Map.ShopMapComponent
Class Vinconomy.Map.ShopMapLayer
Class Vinconomy.ItemTypes.ItemCatalog
Class Vinconomy.ItemTypes.ItemCoupon
Class Vinconomy.ItemTypes.ItemGachaBall
Class Vinconomy.ItemTypes.ItemLedger
Class Vinconomy.ItemTypes.ItemSculptureBundle
Class Vinconomy.ItemTypes.ItemTenretniBook
Class Vinconomy.Inventory.Slots.CurrencySlot
Class Vinconomy.Inventory.Slots.DecoBlockSlot
Class Vinconomy.Inventory.Slots.GachaStockItemSlot
Class Vinconomy.Inventory.Slots.ProductSlot
Class Vinconomy.Inventory.Slots.StockItemSlot
Class Vinconomy.Inventory.Slots.VinconCloningSlot
Class Vinconomy.Inventory.Impl.VinconGenericInventory
Class Vinconomy.GUI.GuiVinconCatalog
Class Vinconomy.GUI.GuiVinconLedger
Class Vinconomy.GUI.GuiVinconShopCatalog
Class Commercially.Common.Interactions.OpenRegisterInteraction
Class Commercially.Common.Interactions.OpenStallInteraction
Class Commercially.Vinconomy.Util.LiquidUtils
Class Commercially.Vinconomy.Util.VinConstants
Class Commercially.Vinconomy.Util.VinUtils
Class Commercially.Vinconomy.Trading.PurchaseRequest
Class Commercially.Vinconomy.Trading.PurchaseResult
Class Commercially.Vinconomy.Trading.TradeInfo
Class Commercially.Vinconomy.Trading.TradeRequest
Class Commercially.Vinconomy.Trading.TradeResult
Class Commercially.Vinconomy.Trading.TradingConstants
Class Commercially.Vinconomy.Trading.TradingUtil
Class Commercially.Vinconomy.Trading.Processor.GenericPurchaseProcessor
Class Commercially.Vinconomy.Trading.Processor.GenericTradingProcessor
Class Commercially.Vinconomy.Registry.ShopConfiguration
Class Commercially.Vinconomy.Network.Packets.CatalogRequestPacket
```

其余 83 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 21 个配方文件与 0 个手册章节](/reference/recipes/vinconomy)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
