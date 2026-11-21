# 信封与邮件

Envelopes · 模组代码：envelopes

> 来源：整合包安装包 `Envelopes-3.9.2.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `envelopes` |
| 版本 | 3.9.2 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | SiiMeR |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds envelopes and parcels to the game, sealable with wax

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
| 程序集 | 1 | `Envelopes.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 5 | `assets/envelopes/itemtypes/envelope.json`<br>`assets/envelopes/itemtypes/parcel.json`<br>`assets/envelopes/itemtypes/sealstamp.json`<br>`assets/envelopes/itemtypes/signetring.json`<br>`assets/envelopes/itemtypes/waxstick.json` |
| 实体定义 | 0 | — |
| 配方定义 | 14 | `assets/envelopes/recipes/grid/add-letter.json`<br>`assets/envelopes/recipes/grid/add-parchment-to-parcel.json`<br>`assets/envelopes/recipes/grid/envelope.json`<br>`assets/envelopes/recipes/grid/parcel.json`<br>`assets/envelopes/recipes/grid/remove-wax-parcel.json`<br>`assets/envelopes/recipes/grid/remove-wax.json`<br>`assets/envelopes/recipes/grid/repair-stamp.json`<br>`assets/envelopes/recipes/grid/seal-parcel.json`<br>`assets/envelopes/recipes/grid/signetring-disassemble.json`<br>`assets/envelopes/recipes/grid/signetring-engrave.json`<br>`assets/envelopes/recipes/grid/stamp-reengrave.json`<br>`assets/envelopes/recipes/grid/wax-seal-stamp.json`<br>另有 2 个文件 |
| 资产补丁 | 1 | `assets/envelopes/patches/compatibility/writtenword.json` |
| 语言资源 | 4 | `assets/envelopes/lang/en.json`<br>`assets/envelopes/lang/ru.json`<br>`assets/envelopes/lang/uk.json`<br>`assets/game/lang/en.json` |
| 手册资源 | 1 | `assets/envelopes/config/handbook/envelopesguide.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Envelopes.dll**（`36d8fa3ce59c4d77`）：60 个类型。

```text
Class <Module>
Class Envelopes.EnvelopesModSystem
Class Envelopes.Util.BooleanArrayPacker
Class Envelopes.Util.Helpers
Class Envelopes.Util.EnvelopeAttributes
Class Envelopes.Util.StampAttributes
Class Envelopes.Patches.PatchGridRecipeMatches
Class Envelopes.Patches.PatchCollectibleHeldInteractStart
Class Envelopes.Patches.PatchGroundStorableHeldInteract
Class Envelopes.Patches.PatchBlockTryPlaceOnGroundStorage
Class Envelopes.Patches.PatchGroundStorageInteractStart
Class Envelopes.Messages.AddStampDesignAttributePacket
Class Envelopes.Messages.OpenEnvelopePacket
Class Envelopes.Messages.RemapSealerIdPacket
Class Envelopes.Messages.SaveStampDesignPacket
Class Envelopes.Messages.SealEnvelopePacket
Class Envelopes.Messages.SetEnvelopeFromToPacket
Class Envelopes.Items.ItemSealableContainer
Class Envelopes.Items.ItemSealableEnvelope
Class Envelopes.Items.ItemSealableParcel
Class Envelopes.Items.ItemSignetRing
Class Envelopes.Items.ItemWaxSealStamp
Class Envelopes.Items.ItemWaxStick
Class Envelopes.Gui.Constants
Class Envelopes.Gui.GuiDialogEnvelopeHeadersEditor
Class Envelopes.Gui.GuiElementHelpers
Class Envelopes.Gui.GuiElementTextInputNoBackground
Class Envelopes.Gui.GuiSealStampDesigner
Class Envelopes.Database.EnvelopeContents
Class Envelopes.Database.EnvelopeContentsDatabase
Class Envelopes.Database.Stamp
Class Envelopes.Database.StampDatabase
Class Envelopes.Behaviors.AddressableBehavior
Class Envelopes.Behaviors.HurtOnConsume
Class Envelopes.Behaviors.RenderStampEmblem
Class Envelopes.Behaviors.SetSealColorFromAttributes
Class <PrivateImplementationDetails>
Class Envelopes.EnvelopesModSystem.<>c
Class Envelopes.EnvelopesModSystem.<>c__DisplayClass10_0
Class Envelopes.EnvelopesModSystem.<>c__DisplayClass12_0
```

其余 20 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 13 个配方文件与 1 个手册章节](/reference/recipes/envelopes)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
