# 字体设置

字体设置 · 模组代码：fontsettings

> 来源：整合包安装包 `字体设置-1.3.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `fontsettings` |
| 版本 | 1.3.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.3 |
| 作者 | 神麤詭末 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

允许为游戏选择已安装的字体，兼容vsimgui。

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 2 | `FontSettings.dll`<br>`SixLabors.Fonts.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/fontsettings/lang/en.json`<br>`assets/fontsettings/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**SixLabors.Fonts.dll**（`e661c6ac204861ea`）：296 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.IsUnmanagedAttribute
Class System.Runtime.CompilerServices.NullableAttribute
Class System.Runtime.CompilerServices.NullableContextAttribute
Class UnicodeTrieGenerator.StateAutomation.StateMachine
Class UnicodeTrieGenerator.StateAutomation.StateMatch
Class UnicodeTrieGenerator.StateAutomation.Node
Class UnicodeTrieGenerator.StateAutomation.Variable
Class UnicodeTrieGenerator.StateAutomation.Comment
Class UnicodeTrieGenerator.StateAutomation.Assignment
Class UnicodeTrieGenerator.StateAutomation.Alternation
Class UnicodeTrieGenerator.StateAutomation.Concatenation
Class UnicodeTrieGenerator.StateAutomation.Repeat
Class UnicodeTrieGenerator.StateAutomation.Leaf
Class UnicodeTrieGenerator.StateAutomation.Literal
Class UnicodeTrieGenerator.StateAutomation.EndMarker
Class UnicodeTrieGenerator.StateAutomation.Tag
Class UnicodeTrieGenerator.StateAutomation.NodeUtilities
Class UnicodeTrieGenerator.StateAutomation.SymbolTable
Class SixLabors.DebugGuard
Class SixLabors.Guard
Class SixLabors.ThrowHelper
Class SixLabors.Fonts.BigEndianBinaryReader
Class SixLabors.Fonts.ByteMemoryManager
Class SixLabors.Fonts.FontException
Class SixLabors.Fonts.FontFamilyNotFoundException
Class SixLabors.Fonts.FontsThrowHelper
Class SixLabors.Fonts.GlyphMissingException
Class SixLabors.Fonts.InvalidFontFileException
Class SixLabors.Fonts.InvalidFontTableException
Class SixLabors.Fonts.MissingFontTableException
Class SixLabors.Fonts.FileFontMetrics
Class SixLabors.Fonts.Font
Class SixLabors.Fonts.FontCollection
Class SixLabors.Fonts.FontCollectionExtensions
Class SixLabors.Fonts.FontDescription
Class SixLabors.Fonts.FontMetrics
Class SixLabors.Fonts.FontReader
Class SixLabors.Fonts.GlyphMetrics
```

其余 256 个类型未在此列出；可按维护说明重新分析程序集。

**FontSettings.dll**（`b1052bfd8372e71e`）：15 个类型。

```text
Class <Module>
Class FontSettings.CairoFont_SetupContext_Patch
Class FontSettings.FontRunSplitterPatch
Class FontSettings.FontSettingsModSystem
Class FontSettings.GuiCompositeSettings_OnInterfaceOptions_Patch
Class FontSettings.ImGuiCompat
Class FontSettings.ImGuiControllerSingletonPatch
Class FontSettings.ImmersiveMapsCompat
Class FontSettings.LibGuiCompat
Class FontSettings.XSkillsGildedCompat
Class <PrivateImplementationDetails>
Class FontSettings.FontRunSplitterPatch.<ResolveTypefaceTranspiler>d__3
Class FontSettings.FontSettingsModSystem.<>c
Class FontSettings.GuiCompositeSettings_OnInterfaceOptions_Patch.<Transpiler>d__0
Class FontSettings.ImmersiveMapsCompat.<Transpiler>d__1
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
