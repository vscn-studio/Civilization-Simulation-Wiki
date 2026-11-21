# 储存调整

Storage Tweaks · 模组代码：storagetweaks

> 来源：整合包安装包 `Storage Tweaks-1.4.2.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `storagetweaks` |
| 版本 | 1.4.2 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game *, survival * |
| 作者 | Trojan96 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds compact/sort and quick-unload buttons to chests.

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
| 程序集 | 1 | `StorageTweaks.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 4 | `assets/storagetweaks/lang/en.json`<br>`assets/storagetweaks/lang/es-419.json`<br>`assets/storagetweaks/lang/es-es.json`<br>`assets/storagetweaks/lang/ru.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 1 | `assets/storagetweaks/config/configlib-patches.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**StorageTweaks.dll**（`425424aca84a57be`）：54 个类型。

```text
Class <Module>
Class StorageTweaks.ContainerWhitelist
Class StorageTweaks.FavoritesManager
Class StorageTweaks.FoodShelvesSegmentGuard
Class StorageTweaks.QuickStoreNearbyContainerSystem
Class StorageTweaks.SortResult
Class StorageTweaks.SortError
Class StorageTweaks.SortSuccess
Class StorageTweaks.SortSystem
Class StorageTweaks.SortInventoryPacket
Class StorageTweaks.UnloadInventoryPacket
Class StorageTweaks.QuickStoreNearbyContainersPacket
Class StorageTweaks.RemeshContainersPacket
Class StorageTweaks.UpdateFavoritesPacket
Class StorageTweaks.StorageTweaksClientConfig
Class StorageTweaks.StorageTweaksServerConfig
Class StorageTweaks.StorageTweaksModSystem
Class StorageTweaks.Util
Class StorageTweaks.Patches.CreativeInventoryContainerTabPatch
Class StorageTweaks.Patches.GuiDialogBlockEntityInventoryPatch
Class StorageTweaks.Patches.GuiDialogInventoryPatch
Class StorageTweaks.Patches.FavoritedSlot
Class StorageTweaks.Patches.GuiElementItemSlotGridPatch
Class StorageTweaks.Patches.InventoryBasePatch
Class StorageTweaks.Patches.MoreInventorysPatch
Class StorageTweaks.Patches.PatchUtils
Class StorageTweaks.Gui.ContainerActionButtons
Class StorageTweaks.Gui.InventoryActionButtons
Class StorageTweaks.Gui.SvgButton
Class StorageTweaks.Gui.SvgToggleButton
Class StorageTweaks.Extensions.InventoryExt
Class StorageTweaks.Extensions.ItemSlotExt
Class StorageTweaks.Extensions.OverhaullibLegacyInfo
Class StorageTweaks.ContainerWhitelist.<>c
Class StorageTweaks.ContainerWhitelist.<>c__DisplayClass2_0
Class StorageTweaks.QuickStoreNearbyContainerSystem.<>c__DisplayClass0_0
Class StorageTweaks.SortSystem.<>c
Class StorageTweaks.StorageTweaksModSystem.<>O
Class StorageTweaks.StorageTweaksModSystem.<>c__DisplayClass17_0
Class StorageTweaks.StorageTweaksModSystem.<>c__DisplayClass17_1
```

其余 14 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
