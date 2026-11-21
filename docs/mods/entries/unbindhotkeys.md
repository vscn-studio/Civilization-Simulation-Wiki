# 快捷键解绑

Unbind Hot Keys · 模组代码：unbindhotkeys

> 来源：整合包安装包 `Unbind Hot Keys-1.0.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `unbindhotkeys` |
| 版本 | 1.0.1 |
| 类型 | 含程序代码 |
| 运行端 | client |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | Primer81 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“界面、汉化与客户端工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Hovering over a hot key and pressing the 'Delete' key (or more simply the 'D' key) will now unbind the hot key.

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
| 程序集 | 4 | `System.Collections.Immutable.dll`<br>`System.Text.Encodings.Web.dll`<br>`System.Text.Json.dll`<br>`UnbindHotKeys.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 1 | `assets/unbindhotkeys/lang/en.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**System.Collections.Immutable.dll**（`624a6c98adadb059`）：136 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.NullableAttribute
Class System.Runtime.CompilerServices.NullableContextAttribute
Class System.Runtime.CompilerServices.NullablePublicOnlyAttribute
Class System.Runtime.CompilerServices.RefSafetyRulesAttribute
Class FxResources.System.Collections.Immutable.SR
Class System.SR
Class System.Linq.ImmutableArrayExtensions
Class System.Linq.ImmutableArrayExtensions.<SelectManyIterator>d__36
Class System.Runtime.Versioning.NonVersionableAttribute
Class System.Runtime.InteropServices.ImmutableCollectionsMarshal
Class System.Runtime.CompilerServices.CollectionBuilderAttribute
Class System.Collections.ThrowHelper
Class System.Collections.HashHelpers
Class System.Collections.Immutable.AllocFreeConcurrentStack
Class System.Collections.Immutable.DictionaryEnumerator
Class System.Collections.Immutable.ImmutableHashSet
Class System.Collections.Immutable.ImmutableHashSet.HashBucketByValueEqualityComparer
Class System.Collections.Immutable.ImmutableHashSet.HashBucketByRefEqualityComparer
Class System.Collections.Immutable.ImmutableHashSet.Builder
Class System.Collections.Immutable.ImmutableHashSet.<>c
Class System.Collections.Immutable.ImmutableArray
Class System.Collections.Immutable.ImmutableArray.Builder
Class System.Collections.Immutable.ImmutableArray.Builder.<GetEnumerator>d__66
Class System.Collections.Immutable.ImmutableArray.EnumeratorObject
Class System.Collections.Immutable.ImmutableArrayBuilderDebuggerProxy
Class System.Collections.Immutable.ImmutableDictionary
Class System.Collections.Immutable.ImmutableDictionary.<>c__12
Class System.Collections.Immutable.ImmutableDictionary.<>c__13
Class System.Collections.Immutable.ImmutableDictionary.<>c__DisplayClass9_0
Class System.Collections.Immutable.ImmutableDictionary
Class System.Collections.Immutable.ImmutableDictionary.Builder
Class System.Collections.Immutable.ImmutableDictionary.Builder.<get_Keys>d__18
Class System.Collections.Immutable.ImmutableDictionary.Builder.<get_Values>d__22
Class System.Collections.Immutable.ImmutableDictionary.Comparers
Class System.Collections.Immutable.ImmutableDictionary.<>c
Class System.Collections.Immutable.ImmutableDictionary.<get_Keys>d__25
Class System.Collections.Immutable.ImmutableDictionary.<get_Values>d__27
Class System.Collections.Immutable.ImmutableDictionaryBuilderDebuggerProxy
```

其余 96 个类型未在此列出；可按维护说明重新分析程序集。

**System.Text.Encodings.Web.dll**（`6ba46c1989be0429`）：31 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.NullableAttribute
Class System.Runtime.CompilerServices.NullableContextAttribute
Class System.Runtime.CompilerServices.NullablePublicOnlyAttribute
Class System.Runtime.CompilerServices.RefSafetyRulesAttribute
Class FxResources.System.Text.Encodings.Web.SR
Class System.HexConverter
Class System.SR
Class System.Text.UnicodeUtility
Class System.Text.Unicode.UnicodeHelpers
Class System.Text.Unicode.UnicodeRange
Class System.Text.Unicode.UnicodeRanges
Class System.Text.Encodings.Web.OptimizedInboxTextEncoder
Class System.Text.Encodings.Web.DefaultUrlEncoder
Class System.Text.Encodings.Web.DefaultUrlEncoder.EscaperImplementation
Class System.Text.Encodings.Web.DefaultJavaScriptEncoder
Class System.Text.Encodings.Web.DefaultJavaScriptEncoder.EscaperImplementation
Class System.Text.Encodings.Web.SpanUtility
Class System.Text.Encodings.Web.ScalarEscaperBase
Class System.Text.Encodings.Web.HtmlEncoder
Class System.Text.Encodings.Web.DefaultHtmlEncoder
Class System.Text.Encodings.Web.DefaultHtmlEncoder.EscaperImplementation
Class System.Text.Encodings.Web.JavaScriptEncoder
Class System.Text.Encodings.Web.TextEncoder
Class System.Text.Encodings.Web.TextEncoderSettings
Class System.Text.Encodings.Web.TextEncoderSettings.<GetAllowedCodePoints>d__14
Class System.Text.Encodings.Web.ThrowHelper
Class System.Text.Encodings.Web.UrlEncoder
Class System.IO.TextWriterExtensions
Class <PrivateImplementationDetails>
```

**System.Text.Json.dll**（`b10dcf464849d577`）：265 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.IsUnmanagedAttribute
Class System.Runtime.CompilerServices.NullableAttribute
Class System.Runtime.CompilerServices.NullableContextAttribute
Class System.Runtime.CompilerServices.NullablePublicOnlyAttribute
Class System.Runtime.CompilerServices.ScopedRefAttribute
Class System.Runtime.CompilerServices.RefSafetyRulesAttribute
Class FxResources.System.Text.Json.SR
Class System.HexConverter
Class System.SR
Class System.Text.Json.PooledByteBufferWriter
Class System.Text.Json.ThrowHelper
Class System.Text.Json.JsonCamelCaseNamingPolicy
Class System.Text.Json.JsonCamelCaseNamingPolicy.<>c
Class System.Text.Json.JsonNamingPolicy
Class System.Text.Json.JsonConstants
Class System.Text.Json.JsonHelpers
Class System.Text.Json.JsonKebabCaseLowerNamingPolicy
Class System.Text.Json.JsonKebabCaseUpperNamingPolicy
Class System.Text.Json.JsonSeparatorNamingPolicy
Class System.Text.Json.JsonSnakeCaseLowerNamingPolicy
Class System.Text.Json.JsonSnakeCaseUpperNamingPolicy
Class System.Text.Json.AppContextSwitchHelper
Class System.Text.Json.JsonDocument
Class System.Text.Json.JsonException
Class System.Text.Json.JsonPropertyDictionary
Class System.Text.Json.JsonPropertyDictionary.KeyCollection
Class System.Text.Json.JsonPropertyDictionary.KeyCollection.<GetEnumerator>d__14
Class System.Text.Json.JsonPropertyDictionary.KeyCollection.<System-Collections-IEnumerable-GetEnumerator>d__9
Class System.Text.Json.JsonPropertyDictionary.ValueCollection
Class System.Text.Json.JsonPropertyDictionary.ValueCollection.<GetEnumerator>d__14
Class System.Text.Json.JsonPropertyDictionary.ValueCollection.<System-Collections-IEnumerable-GetEnumerator>d__9
Class System.Text.Json.JsonReaderException
Class System.Text.Json.JsonReaderHelper
Class System.Text.Json.Arguments
Class System.Text.Json.ArgumentState
Class System.Text.Json.JsonSerializer
Class System.Text.Json.JsonSerializer.<<DeserializeAsyncEnumerableCore>g__CreateAsyncEnumerable|90_0>d
Class System.Text.Json.JsonSerializer.<>c__90
```

其余 225 个类型未在此列出；可按维护说明重新分析程序集。

**UnbindHotKeys.dll**（`5904294b5349b143`）：5 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.RefSafetyRulesAttribute
Class UnbindHotKeys.UnbindHotKeysModSystem
Class UnbindHotKeys.Patches
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
