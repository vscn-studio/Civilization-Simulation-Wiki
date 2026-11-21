# 死亡扩展

Dead · 模组代码：dead

> 来源：整合包安装包 `Dead-2.9.8.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `dead` |
| 版本 | 2.9.8 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game * |
| 作者 | SiiMeR |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“身体、战斗与成长”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Leaves a lootable corpse of the player (with their exact skin and worn gear) at the death spot on respawn.

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
| 程序集 | 1 | `Dead.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 1 | `assets/dead/entities/playercorpse.json` |
| 配方定义 | 0 | — |
| 资产补丁 | 12 | `assets/dead/patches/clutter-carving.json`<br>`assets/dead/patches/crouch-animation.json`<br>`assets/dead/patches/deadcrawl-animation.json`<br>`assets/dead/patches/drag-shape.json`<br>`assets/dead/patches/elk-stowage.json`<br>`assets/dead/patches/hide-tint.json`<br>`assets/dead/patches/horse-stowage.json`<br>`assets/dead/patches/kneel-animation.json`<br>`assets/dead/patches/player-drag-animation.json`<br>`assets/dead/patches/playermodellib-compat.json`<br>`assets/dead/patches/skeleton-headless.json`<br>`assets/dead/patches/stow-animation.json` |
| 语言资源 | 2 | `assets/dead/lang/en.json`<br>`assets/dead/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 2 | `assets/dead/config/configlib-patches.json`<br>`assets/dead/config/imm.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Dead.dll**（`4b343b8e9e6bdfb5`）：75 个类型。

```text
Class <Module>
Class Dead.DeadCommands
Class Dead.DeadConfig
Class Dead.DeadDragController
Class Dead.DeadModSystem
Class Dead.Rendering.CorpseCubeParticles
Class Dead.Rendering.EntityDeadShapeRenderer
Class Dead.Persistence.CorpseRecord
Class Dead.Persistence.CorpseStore
Class Dead.Patches.DragYawLockPatch
Class Dead.Patches.HangRenderOffsetPatch
Class Dead.Patches.HiddenBodyRenderPatch
Class Dead.Patches.HiddenBodyInteractPatch
Class Dead.Patches.HideNamePatch
Class Dead.Patches.SkullNamePatch
Class Dead.Patches.HideTintPatch
Class Dead.Patches.HideGroundStorageTintPatch
Class Dead.Patches.HideTint
Class Dead.Patches.ReviveCancelPatch
Class Dead.Patches.StowAttachBlockPatch
Class Dead.Patches.StowSlotUnstowPatch
Class Dead.Patches.StowSlotHelpPatch
Class Dead.Patches.TeleporterMountPatch
Class Dead.Patches.WoundLogPatch
Class Dead.Network.ConfigSyncPacket
Class Dead.Network.DragStartPacket
Class Dead.Network.DragStopPacket
Class Dead.Network.HangCorpsePacket
Class Dead.Network.StowCorpsePacket
Class Dead.Inventories.InventoryDeadBackpacks
Class Dead.Inventories.InventoryDeadGear
Class Dead.Inventories.InventoryDeadGeneric
Class Dead.Inventories.ItemSlotDeadArmor
Class Dead.Inventories.ItemSlotDeadGear
Class Dead.Gui.GuiDialogCarving
Class Dead.Gui.GuiDialogCorpse
Class Dead.Entities.CorpseDragSeat
Class Dead.Entities.CorpseStowSeat
Class Dead.Entities.EntityPlayerCorpse
Class Dead.Behaviors.BEBehaviorDeadCarving
```

其余 35 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
