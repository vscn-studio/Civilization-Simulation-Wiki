# 商业交易

Commercially · 模组代码：commercially

> 来源：整合包安装包 `Commercially-0.1.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `commercially` |
| 版本 | 0.1.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | Severed Skullz |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

To be added

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
| 程序集 | 1 | `Commercially.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 1 | `assets/commercially/lang/en.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Commercially.dll**（`eec6395c34997692`）：78 个类型。

```text
Class <Module>
Class Vinconomy.Filters.CommonFilters
Class Commercially.ConvivialityModSystem
Class Commercially.Conviviality.NPC.EntityCompanion
Class Commercially.Common.Util.CallerUtils
Class Commercially.Common.Util.CommercialConfig
Class Commercially.Common.Util.CommerciallyConstants
Class Commercially.Common.Util.CommUtils
Class Commercially.Common.Util.ComponentUtils
Class Commercially.Common.Util.TransformationData
Class Commercially.Common.Renderer.BlockRenderer
Class Commercially.Common.Renderer.ClutterBlockRenderer
Class Commercially.Common.Renderer.CoinItemRenderer
Class Commercially.Common.Renderer.ItemRenderer
Class Commercially.Common.Renderer.MicroBlockRenderer
Class Commercially.Common.Registry.OwnableClientRegistry
Class Commercially.Common.Registry.OwnableRegistration
Class Commercially.Common.Registry.OwnableServerRegistry
Class Commercially.Common.Registry.Packets.OwnableEntry
Class Commercially.Common.Registry.Packets.OwnableUpdatePacket
Class Commercially.Common.Registry.Packets.RegistryUpdatePacket
Class Commercially.Common.Networking.Packets.GUITabPacket
Class Commercially.Common.Networking.Packets.GUITabsPacket
Class Commercially.Common.ModSystems.CommerciallyModSystem
Class Commercially.Common.ModSystems.ModularGUIModSystem
Class Commercially.Common.Map.OwnableMapComponent
Class Commercially.Common.Map.OwnableMapLayer
Class Commercially.Common.Inventory.ConfigurableInventory
Class Commercially.Common.Inventory.Slots.AggregatedSlots
Class Commercially.Common.Inventory.Slots.GenericAggregatedSlots
Class Commercially.Common.Inventory.Slots.CompositeAggregatedSlots
Class Commercially.Common.Inventory.Slots.CapacityAggregatedSlots
Class Commercially.Common.Inventory.Slots.ServingCapacityAggregatedSlots
Class Commercially.Common.Inventory.Slots.LiquidCapacityAggregatedSlots
Class Commercially.Common.Inventory.Slots.DurabilityAggregatedSlots
Class Commercially.Common.Inventory.Slots.AggregatedStacks
Class Commercially.Common.Inventory.Slots.FilteredItemSlot
Class Commercially.Common.Inventory.Slots.ItemLockedSlot
Class Commercially.Common.Inventory.Slots.ToggledSlot
Class Commercially.Common.Interactions.OpenGuiInteraction
```

其余 38 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
