# 灯具

Candela · 模组代码：candela

> 来源：整合包安装包 `Candela-1.0.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `candela` |
| 版本 | 1.0.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | DizzyD |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Candle-making beyond the cooking pot - tallow, wicks and dipping - and candles that burn down and need tending

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
| 程序集 | 1 | `candela.dll` |
| 方块定义 | 2 | `assets/candela/blocktypes/tallowcandle.json`<br>`assets/candela/blocktypes/tallowcandles.json` |
| 物品定义 | 9 | `assets/candela/itemtypes/beeswax-molten.json`<br>`assets/candela/itemtypes/candle-tallow.json`<br>`assets/candela/itemtypes/candlemould.json`<br>`assets/candela/itemtypes/candlestub.json`<br>`assets/candela/itemtypes/dippingrod.json`<br>`assets/candela/itemtypes/oilburner.json`<br>`assets/candela/itemtypes/powder-verdigris.json`<br>`assets/candela/itemtypes/tallow-molten.json`<br>`assets/candela/itemtypes/wick.json` |
| 实体定义 | 0 | — |
| 配方定义 | 8 | `assets/candela/recipes/clayforming/candlemould.json`<br>`assets/candela/recipes/cooking/beeswax-molten.json`<br>`assets/candela/recipes/cooking/stubs-molten.json`<br>`assets/candela/recipes/cooking/tallow-molten.json`<br>`assets/candela/recipes/grid/dippingrod.json`<br>`assets/candela/recipes/grid/lantern-tallow.json`<br>`assets/candela/recipes/grid/oilburner.json`<br>`assets/candela/recipes/grid/wick.json` |
| 资产补丁 | 7 | `assets/candela/patches/candles-burn.json`<br>`assets/candela/patches/chandelier-burn.json`<br>`assets/candela/patches/lamp-oil.json`<br>`assets/candela/patches/lantern-fuel.json`<br>`assets/candela/patches/player-dip.json`<br>`assets/candela/patches/pot-of-wax.json`<br>`assets/candela/patches/verdigris.json` |
| 语言资源 | 68 | `assets/candela/lang/ar.json`<br>`assets/candela/lang/be.json`<br>`assets/candela/lang/bg.json`<br>`assets/candela/lang/cs.json`<br>`assets/candela/lang/da.json`<br>`assets/candela/lang/de.json`<br>`assets/candela/lang/en.json`<br>`assets/candela/lang/eo.json`<br>`assets/candela/lang/es-419.json`<br>`assets/candela/lang/es-es.json`<br>`assets/candela/lang/fi.json`<br>`assets/candela/lang/fr.json`<br>另有 56 个文件 |
| 手册资源 | 2 | `assets/candela/config/handbook/60-candela-dipping.json`<br>`assets/candela/config/handbook/61-candela-upkeep.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**candela.dll**（`440c48ea54a391ac`）：86 个类型。

```text
Class <Module>
Class <>z__ReadOnlyArray
Class candela.BlockCandelaCandles
Class candela.BlockCandelaChandelier
Class candela.BlockCandelaLantern
Class candela.CandleMeshes
Class candela.ColouredCandleMeshes
Class candela.CandleHolders
Class candela.LanternFlamePatch
Class candela.PartBurned
Class candela.TorchTime
Class candela.BEBehaviorTorchHolderTime
Class candela.TorchTimePatches
Class candela.BlockBehaviorDipVat
Class candela.BEBehaviorLanternFuel
Class candela.LanternStack
Class candela.BECandles
Class candela.CandleInfo
Class candela.Flame
Class candela.Relight
Class candela.Weather
Class candela.CandelaConfig
Class candela.CandleWax
Class candela.CandelaModSystem
Class candela.ItemCandelaCandle
Class candela.ItemPlaceableCandle
Class candela.CandlePlacement
Class candela.CarriedWax
Class candela.CollectibleBehaviorPotOfWax
Class candela.OneTexture
Class candela.DyedItems
Class candela.FlameColours
Class candela.ItemCandleMould
Class candela.ItemDippingRod
Class candela.ItemMoltenWax
Class candela.LampOil
Class candela.BurnerStack
Class candela.ItemOilBurner
Class candela.SettingBar
Class candela.StoneBakeOvenCompat
```

其余 46 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 8 个配方文件与 2 个手册章节](/reference/recipes/candela)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
