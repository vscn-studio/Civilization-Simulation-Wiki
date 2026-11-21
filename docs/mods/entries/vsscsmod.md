# 文明模拟

Seraph Civilization Simulation · 模组代码：vsscsmod

> 来源：整合包安装包 `Seraph Civilization Simulation-1.0.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vsscsmod` |
| 版本 | 1.0.0 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.3 |
| 作者 | HansJack |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

文明模拟提供多人世界中的身份、部落与公共生活系统。源码把功能拆为聚落/部落、领地授权、集群玩家、公告与教程、交易/经济、地图信息和管理员设置；服务端保存世界状态，客户端窗口只提交经过权限检查的请求。

### 玩家操作

- 进入世界后用文明窗口查看名称、部落和集群状态；领地、部落授权和锁具操作由服务器判定，客户端显示失败原因。
- 公告与教程由管理员发布，按世界保存；地图和信息显示可能受 `InformationRestrictions` 与服务器权限限制。
- 交易、货币和 Vinconomy 等功能依赖安装包中相应兼容模组，不存在依赖时不会凭页面名称生成物品或命令。

### 管理员与开发者入口

完整命令见[管理员指令](/admin/commands-full)，配置字段见[当前配置表](/admin/config-tables)中的 `SeraphCivilizationSimulation.json`；源码控制流核验见[文明源码专题](/guide/civilization-source)，API/事件所有权见[开发者 API](/develop/api)。`/vsscsmod reload config` 和内容热重载仍受权限和配置校验约束，重载失败保留上一份有效状态。

[返回整合包图鉴](/mods/)

## 源码实现矩阵（当前源码树）

逐文件类型、方法及哈希已集中到[开发者源码索引](/develop/sources/vsscsmod)。

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 3 | `AngleSharp.dll`<br>`Markdig.dll`<br>`vsscsmod.dll` |
| 方块定义 | 3 | `assets/vscncivilizationsimulation/blocktypes/groundmaps.json`<br>`assets/vsscmmod/blocktypes/groundmaps.json`<br>`assets/vsscsmod/blocktypes/groundmaps.json` |
| 物品定义 | 1 | `assets/vsscsmod/itemtypes/civilizationcore.json` |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 4 | `assets/vsscsmod/patches/animal-passage.json`<br>`assets/vsscsmod/patches/chiseltools-survival.json`<br>`assets/vsscsmod/patches/player.json`<br>`assets/vsscsmod/patches/wildlife.json` |
| 语言资源 | 4 | `assets/game/lang/en.json`<br>`assets/game/lang/zh-cn.json`<br>`assets/vsscsmod/lang/en.json`<br>`assets/vsscsmod/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**AngleSharp.dll**（`3b957dcbc83e406e`）：593 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>f__AnonymousType1
Class <>f__AnonymousType2
Class AngleSharp.BrowsingContext
Class AngleSharp.BrowsingContextExtensions
Class AngleSharp.Configuration
Class AngleSharp.ConfigurationExtensions
Class AngleSharp.FormatExtensions
Class AngleSharp.MarkupReadStream
Class AngleSharp.Xhtml.XhtmlMarkupFormatter
Class AngleSharp.Text.ByteOrderMark
Class AngleSharp.Text.CharArrayTextSource
Class AngleSharp.Text.CharExtensions
Class AngleSharp.Text.Punycode
Class AngleSharp.Text.ReadOnlyByteTextSource
Class AngleSharp.Text.ReadOnlyMemoryTextSource
Class AngleSharp.Text.StreamingTextSource
Class AngleSharp.Text.StringBuilderPool
Class AngleSharp.Text.StringExtensions
Class AngleSharp.Text.StringSource
Class AngleSharp.Text.StringSourceExtensions
Class AngleSharp.Text.StringTextSource
Class AngleSharp.Text.Symbols
Class AngleSharp.Text.TextEncoding
Class AngleSharp.Text.TextSource
Class AngleSharp.Text.TextView
Class AngleSharp.Text.WritableTextSource
Class AngleSharp.Text.XmlExtensions
Class AngleSharp.Svg.SvgElementFactory
Class AngleSharp.Svg.Dom.SvgCircleElement
Class AngleSharp.Svg.Dom.SvgDescElement
Class AngleSharp.Svg.Dom.SvgElement
Class AngleSharp.Svg.Dom.SvgForeignObjectElement
Class AngleSharp.Svg.Dom.SvgStyleElement
Class AngleSharp.Svg.Dom.SvgSvgElement
Class AngleSharp.Svg.Dom.SvgTitleElement
Class AngleSharp.Scripting.ScriptOptions
Class AngleSharp.Mathml.MathElementFactory
Class AngleSharp.Mathml.Dom.MathAnnotationXmlElement
```

其余 553 个类型未在此列出；可按维护说明重新分析程序集。

**Markdig.dll**（`419844b384f1e7e2`）：337 个类型。

```text
Class <Module>
Class System.SpanExtensions
Class System.Text.UnicodeUtility
Class Markdig.Markdown
Class Markdig.MarkdownExtensions
Class Markdig.MarkdownParserContext
Class Markdig.MarkdownPipeline
Class Markdig.MarkdownPipelineBuilder
Class Markdig.Syntax.BlankLineBlock
Class Markdig.Syntax.Block
Class Markdig.Syntax.BlockExtensions
Class Markdig.Syntax.CharIteratorHelper
Class Markdig.Syntax.CodeBlock
Class Markdig.Syntax.ContainerBlock
Class Markdig.Syntax.FencedCodeBlock
Class Markdig.Syntax.HeadingBlock
Class Markdig.Syntax.HtmlBlock
Class Markdig.Syntax.LeafBlock
Class Markdig.Syntax.LinkReferenceDefinition
Class Markdig.Syntax.LinkReferenceDefinitionExtensions
Class Markdig.Syntax.LinkReferenceDefinitionGroup
Class Markdig.Syntax.ListBlock
Class Markdig.Syntax.ListItemBlock
Class Markdig.Syntax.MarkdownDocument
Class Markdig.Syntax.MarkdownObject
Class Markdig.Syntax.DataKey
Class Markdig.Syntax.MarkdownObjectDataExtensions
Class Markdig.Syntax.MarkdownObjectExtensions
Class Markdig.Syntax.EmptyBlock
Class Markdig.Syntax.ParagraphBlock
Class Markdig.Syntax.QuoteBlock
Class Markdig.Syntax.QuoteBlockLine
Class Markdig.Syntax.ThematicBreakBlock
Class Markdig.Syntax.Inlines.AutolinkInline
Class Markdig.Syntax.Inlines.CodeInline
Class Markdig.Syntax.Inlines.ContainerInline
Class Markdig.Syntax.Inlines.DelimiterInline
Class Markdig.Syntax.Inlines.EmphasisDelimiterInline
Class Markdig.Syntax.Inlines.EmphasisInline
Class Markdig.Syntax.Inlines.HtmlEntityInline
```

其余 297 个类型未在此列出；可按维护说明重新分析程序集。

**vsscsmod.dll**（`d54210bbffc7cb62`）：782 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>f__AnonymousType1
Class <>f__AnonymousType2
Class <>f__AnonymousType3
Class <>f__AnonymousType4
Class <>f__AnonymousType5
Class <>f__AnonymousType6
Class <>f__AnonymousType7
Class <>f__AnonymousType8
Class <>z__ReadOnlyArray
Class <>z__ReadOnlySingleElementList
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FB68D0955179F20FBC476A3D19CE9257BEAEEB8FE02D001B5D734B72E4E29EE33__HiddenContent_0
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FB68D0955179F20FBC476A3D19CE9257BEAEEB8FE02D001B5D734B72E4E29EE33__Tokens_1
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FB68D0955179F20FBC476A3D19CE9257BEAEEB8FE02D001B5D734B72E4E29EE33__TagName_2
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FB68D0955179F20FBC476A3D19CE9257BEAEEB8FE02D001B5D734B72E4E29EE33__Attributes_3
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FB68D0955179F20FBC476A3D19CE9257BEAEEB8FE02D001B5D734B72E4E29EE33__Whitespace_4
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FB68D0955179F20FBC476A3D19CE9257BEAEEB8FE02D001B5D734B72E4E29EE33__Utilities
Class SeraphCivilizationSimulation.AdminSettingsRequest
Class SeraphCivilizationSimulation.AdminSettingsPacket
Class SeraphCivilizationSimulation.AdminSettingsData
Class SeraphCivilizationSimulation.VscnCivilizationModSystem
Class SeraphCivilizationSimulation.AdminSettingsWindow
Class SeraphCivilizationSimulation.AdminSettingText
Class SeraphCivilizationSimulation.AnnouncementDom
Class SeraphCivilizationSimulation.AnnouncementFonts
Class SeraphCivilizationSimulation.AnnouncementGameResources
Class SeraphCivilizationSimulation.AnnouncementResourcePicker
Class SeraphCivilizationSimulation.AnnouncementState
Class SeraphCivilizationSimulation.TutorialState
Class SeraphCivilizationSimulation.AnnouncementEntry
Class SeraphCivilizationSimulation.AnnouncementHtml
Class SeraphCivilizationSimulation.AnnouncementInteraction
Class SeraphCivilizationSimulation.AnnouncementAnchor
Class SeraphCivilizationSimulation.AnnouncementBox
Class SeraphCivilizationSimulation.AnnouncementSwitch
Class SeraphCivilizationSimulation.AnnouncementDisclosure
Class SeraphCivilizationSimulation.AnnouncementRule
Class SeraphCivilizationSimulation.AnnouncementTable
Class SeraphCivilizationSimulation.AnnouncementHtmlTools
```

其余 742 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
