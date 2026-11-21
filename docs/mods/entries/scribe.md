# 书写

Scribe · 模组代码：scribe

> 来源：整合包安装包 `Scribe-1.4.4.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `scribe` |
| 版本 | 1.4.4 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0, gui 3.1.0 |
| 作者 | RaptorKhan |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Items & stations to keep notes and manage tasks.

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
| 程序集 | 2 | `Scribe.Core.dll`<br>`Scribe.dll` |
| 方块定义 | 5 | `assets/scribe/blocktypes/assignmentdesk.json`<br>`assets/scribe/blocktypes/chalkboard.json`<br>`assets/scribe/blocktypes/inbox.json`<br>`assets/scribe/blocktypes/lectern.json`<br>`assets/scribe/blocktypes/scriptorium.json` |
| 物品定义 | 5 | `assets/scribe/itemtypes/clockmakerschematic.json`<br>`assets/scribe/itemtypes/scribeclockmakernotebook.json`<br>`assets/scribe/itemtypes/scribenotebook.json`<br>`assets/scribe/itemtypes/scribetablet.json`<br>`assets/scribe/itemtypes/tasknotice.json` |
| 实体定义 | 0 | — |
| 配方定义 | 11 | `assets/scribe/recipes/grid/assignmentdesk.json`<br>`assets/scribe/recipes/grid/chalkboard.json`<br>`assets/scribe/recipes/grid/inbox.json`<br>`assets/scribe/recipes/grid/scribeclockmakernotebook-schematic.json`<br>`assets/scribe/recipes/grid/scribeclockmakernotebook.json`<br>`assets/scribe/recipes/grid/scribelectern.json`<br>`assets/scribe/recipes/grid/scribenotebook.json`<br>`assets/scribe/recipes/grid/scribetablet-clay.json`<br>`assets/scribe/recipes/grid/scribetablet-wax.json`<br>`assets/scribe/recipes/grid/scriptorium.json`<br>`assets/scribe/recipes/grid/tasknotice.json` |
| 资产补丁 | 1 | `assets/scribe/patches/trader-clockmakerschematic.json` |
| 语言资源 | 26 | `assets/game/lang/cs.json`<br>`assets/game/lang/de.json`<br>`assets/game/lang/en.json`<br>`assets/game/lang/es-es.json`<br>`assets/game/lang/fr.json`<br>`assets/game/lang/it.json`<br>`assets/game/lang/ja.json`<br>`assets/game/lang/pl.json`<br>`assets/game/lang/pt-br.json`<br>`assets/game/lang/ru.json`<br>`assets/game/lang/sv-se.json`<br>`assets/game/lang/uk.json`<br>另有 14 个文件 |
| 手册资源 | 9 | `assets/scribe/config/handbook/00-getting-started.json`<br>`assets/scribe/config/handbook/01-editor-reference.json`<br>`assets/scribe/config/handbook/02-pinned-hud.json`<br>`assets/scribe/config/handbook/03-task-types.json`<br>`assets/scribe/config/handbook/04-transcribe.json`<br>`assets/scribe/config/handbook/05-views.json`<br>`assets/scribe/config/handbook/06-assignments.json`<br>`assets/scribe/config/handbook/07-quests.json`<br>`assets/scribe/config/handbook/08-delivery.json` |
| 包内配置数据 | 1 | `assets/scribe/config/configlib-patches.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Scribe.dll**（`d7011843074f4ba9`）：498 个类型。

```text
Class <Module>
Class Scribe.AssignmentDisplay
Class Scribe.BlockAssignmentDesk
Class Scribe.BlockEntityAssignmentDesk
Class Scribe.BlockEntityInbox
Class Scribe.BlockEntityScribeChalkboard
Class Scribe.BlockEntityScribeInventoryStation
Class Scribe.BlockEntityScribeLectern
Class Scribe.BlockEntityScribeWritingStation
Class Scribe.BlockEntityScriptorium
Class Scribe.BlockInbox
Class Scribe.BlockScribeChalkboard
Class Scribe.BlockScribeLectern
Class Scribe.BlockScribeWritingStation
Class Scribe.BlockScriptorium
Class Scribe.CarryOnBridge
Class Scribe.CuneiformGlowMask
Class Scribe.CuneiformMetrics
Class Scribe.CuneiformTextRender
Class Scribe.CuneiformTextRenderWidget
Class Scribe.CuneiformText
Class Scribe.CuneiformTextState
Class Scribe.GuiDialogClockmakerNotebook
Class Scribe.GuiDialogScribeAssignmentDesk
Class Scribe.GuiDialogScribeChalkboard
Class Scribe.GuiDialogScribeInbox
Class Scribe.GuiDialogScribeLecternLibGui
Class Scribe.GuiDialogScribeNotebook
Class Scribe.ScribeManualHistoryRow
Class Scribe.ScribeManualHistoryRowState
Class Scribe.GuiDialogScribeQuestPrompt
Class Scribe.GuiDialogScribeScriptorium
Class Scribe.GuiDialogScribeTablet
Class Scribe.GuiDialogTaskNotice
Class Scribe.GuiDialogTaskNoticeRedirectConfirm
Class Scribe.HistoryDisplay
Class Scribe.HudPinsContent
Class Scribe.HudScribePins
Class Scribe.ItemClockmakerNotebook
Class Scribe.ItemScribeNotebook
```

其余 458 个类型未在此列出；可按维护说明重新分析程序集。

**Scribe.Core.dll**（`9b3da4994b00a229`）：74 个类型。

```text
Class <Module>
Class Scribe.Core.GuestbookEntry
Class Scribe.Core.GuestbookStore
Class Scribe.Core.HistoryEntry
Class Scribe.Core.HistoryEntryCodec
Class Scribe.Core.HistoryFlavor
Class Scribe.Core.HistoryPvpVerb
Class Scribe.Core.HistoryStore
Class Scribe.Core.PendingHistoryStore
Class Scribe.Core.ScribeArrowDigraph
Class Scribe.Core.ScribeAssignmentStateExtensions
Class Scribe.Core.ScribeAssignment
Class Scribe.Core.ScribeAssignmentTransitions
Class Scribe.Core.ScribeAssignmentStore
Class Scribe.Core.ScribeBlock
Class Scribe.Core.ScribeBlockKindToken
Class Scribe.Core.ScribeBrightnessCurve
Class Scribe.Core.ScribeCompletion
Class Scribe.Core.ScribeCraftMath
Class Scribe.Core.ScribeDeliveryPolicy
Class Scribe.Core.ScribeDocument
Class Scribe.Core.ScribeDocumentCodec
Class Scribe.Core.ScribeDocumentJsonCodec
Class Scribe.Core.ScribeDocumentTsvCodec
Class Scribe.Core.ScribeExternalTaskMapper
Class Scribe.Core.ScribeHudAnchorExtensions
Class Scribe.Core.ScribeKnownPlayersStore
Class Scribe.Core.ScribeQuestSource
Class Scribe.Core.ScribeLinkTarget
Class Scribe.Core.ScribeListDiff
Class Scribe.Core.ScribeMath
Class Scribe.Core.ScribePinCodec
Class Scribe.Core.ScribePinnedRef
Class Scribe.Core.ScribePinOrdering
Class Scribe.Core.ScribePlayerListBlob
Class Scribe.Core.ScribePlayerLocationStore
Class Scribe.Core.ScribePlayerSettings
Class Scribe.Core.ScribeQuestDecisionEntry
Class Scribe.Core.ScribeQuestDecisionSet
Class Scribe.Core.ScribeQuestDecisionCodec
```

其余 34 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 11 个配方文件与 9 个手册章节](/reference/recipes/scribe)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
