# 界面工具

Gui · 模组代码：gui

> 来源：整合包安装包 `Gui-4.0.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `gui` |
| 版本 | 4.0.0 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 否 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | ripls |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“界面、汉化与客户端工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Client-side GUI library

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
| 程序集 | 12 | `ExCSS.dll`<br>`Gui.dll`<br>`HarfBuzzSharp.dll`<br>`JetBrains.Annotations.dll`<br>`ShimSkiaSharp.dll`<br>`SkiaSharp.HarfBuzz.dll`<br>`Svg.Custom.dll`<br>`Svg.Model.dll`<br>`Svg.Skia.dll`<br>`native/win-arm64/native/libHarfBuzzSharp.dll`<br>`native/win-x64/native/libHarfBuzzSharp.dll`<br>`native/win-x86/native/libHarfBuzzSharp.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 0 | — |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ExCSS.dll**（`6b166e638181eba3`）：479 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class System.Threading.Tasks.TaskEx
Class ExCSS.DeclarationCondition
Class ExCSS.EmptyCondition
Class ExCSS.GroupCondition
Class ExCSS.NotCondition
Class ExCSS.OrCondition
Class ExCSS.Colors
Class ExCSS.Combinators
Class ExCSS.FeatureNames
Class ExCSS.FunctionNames
Class ExCSS.Keywords
Class ExCSS.PropertyNames
Class ExCSS.PseudoClassNames
Class ExCSS.PseudoElementNames
Class ExCSS.RuleNames
Class ExCSS.UnitNames
Class ExCSS.CharExtensions
Class ExCSS.CollectionExtensions
Class ExCSS.FormatExtensions
Class ExCSS.PortableExtensions
Class ExCSS.StringExtensions
Class ExCSS.ValueConverterExtensions
Class ExCSS.ValueExtensions
Class ExCSS.AttributeSelectorFactory
Class ExCSS.MediaFeatureFactory
Class ExCSS.PropertyFactory
Class ExCSS.PseudoClassSelectorFactory
Class ExCSS.PseudoElementSelectorFactory
Class ExCSS.CompressedStyleFormatter
Class ExCSS.DocumentFunction
Class ExCSS.DomainFunction
Class ExCSS.RegexpFunction
Class ExCSS.UrlFunction
Class ExCSS.UrlPrefixFunction
Class ExCSS.AspectRatioMediaFeature
Class ExCSS.ColorIndexMediaFeature
Class ExCSS.ColorMediaFeature
Class ExCSS.DeviceAspectRatioMediaFeature
```

其余 439 个类型未在此列出；可按维护说明重新分析程序集。

**Gui.dll**（`b8546b2c4f833779`）：628 个类型。

```text
Class <Module>
Class <>z__ReadOnlyArray
Class <>z__ReadOnlySingleElementList
Class Gui.GuiBase
Class Gui.GuiDialogBlockEntityBase
Class Gui.GuiGlobalOverlay
Class Gui.GuiModSystem
Class Gui.NativeLibraryLoader
Class Gui.GuiConfig
Class Gui.ThemeSection
Class Gui.WindowConfig
Class Gui.Vtml.VtmlConverter
Class Gui.Vtml.VtmlInlineElement
Class Gui.Vtml.VtmlTextRun
Class Gui.Vtml.VtmlIconRun
Class Gui.Vtml.VtmlItemStackRun
Class Gui.Vtml.VtmlHotkeyRun
Class Gui.Vtml.VtmlLineBreak
Class Gui.Vtml.VtmlClearFloat
Class Gui.Vtml.VtmlSpanBuilder
Class Gui.Theming.ThemeApplier
Class Gui.Theming.ColorOverrides
Class Gui.Theming.TypographyOverrides
Class Gui.Theming.ButtonVariantOverrides
Class Gui.Theming.ButtonOverrides
Class Gui.Theming.TextFieldOverrides
Class Gui.Theming.CheckboxOverrides
Class Gui.Theming.RadioButtonOverrides
Class Gui.Theming.SliderOverrides
Class Gui.Theming.DropdownOverrides
Class Gui.Theming.ProgressBarOverrides
Class Gui.Theming.FocusOverrides
Class Gui.Theming.ThemeOverrides
Class Gui.Theming.ColorOverrideSection
Class Gui.Theming.TypographyOverrideSection
Class Gui.Theming.ButtonVariantOverrideSection
Class Gui.Theming.ButtonOverrideSection
Class Gui.Theming.TextFieldOverrideSection
Class Gui.Theming.CheckboxOverrideSection
Class Gui.Theming.RadioButtonOverrideSection
```

其余 588 个类型未在此列出；可按维护说明重新分析程序集。

**HarfBuzzSharp.dll**（`55e72ac23263f8e1`）：34 个类型。

```text
Class <Module>
Class VersionConstants
Class HarfBuzzSharp.Blob
Class HarfBuzzSharp.Buffer
Class HarfBuzzSharp.DelegateProxies
Class HarfBuzzSharp.Face
Class HarfBuzzSharp.Font
Class HarfBuzzSharp.FontUserData
Class HarfBuzzSharp.FontFunctions
Class HarfBuzzSharp.HarfBuzzApi
Class HarfBuzzSharp.Language
Class HarfBuzzSharp.NativeObject
Class HarfBuzzSharp.OpenTypeMetrics
Class HarfBuzzSharp.UnicodeFunctions
Class HarfBuzzSharp.MonoPInvokeCallbackAttribute
Class HarfBuzzSharp.Internals.PlatformConfiguration
Class HarfBuzzSharp.Blob.StaticBlob
Class HarfBuzzSharp.Blob.<>c
Class HarfBuzzSharp.Blob.<>c__DisplayClass18_0
Class HarfBuzzSharp.DelegateProxies.<>c__DisplayClass44_0
Class HarfBuzzSharp.DelegateProxies.<>c__DisplayClass46_0
Class HarfBuzzSharp.DelegateProxies.<>c__DisplayClass47_0
Class HarfBuzzSharp.DelegateProxies.<>c__DisplayClass51_0
Class HarfBuzzSharp.DelegateProxies.<>c__DisplayClass52_0
Class HarfBuzzSharp.DelegateProxies.<>c__DisplayClass53_0
Class HarfBuzzSharp.Face.StaticFace
Class HarfBuzzSharp.Face.<>c
Class HarfBuzzSharp.FontFunctions.StaticFontFunctions
Class HarfBuzzSharp.FontFunctions.<>c
Class HarfBuzzSharp.Language.StaticLanguage
Class HarfBuzzSharp.Language.<>c
Class HarfBuzzSharp.NativeObject.<PtrToStringArray>d__12
Class HarfBuzzSharp.UnicodeFunctions.StaticUnicodeFunctions
Class HarfBuzzSharp.UnicodeFunctions.<>c
```

**JetBrains.Annotations.dll**（`8f2c837af3f4f61b`）：108 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.RefSafetyRulesAttribute
Class JetBrains.Annotations.CanBeNullAttribute
Class JetBrains.Annotations.NotNullAttribute
Class JetBrains.Annotations.ItemNotNullAttribute
Class JetBrains.Annotations.ItemCanBeNullAttribute
Class JetBrains.Annotations.StringFormatMethodAttribute
Class JetBrains.Annotations.StructuredMessageTemplateAttribute
Class JetBrains.Annotations.ValueProviderAttribute
Class JetBrains.Annotations.ValueRangeAttribute
Class JetBrains.Annotations.NonNegativeValueAttribute
Class JetBrains.Annotations.InvokerParameterNameAttribute
Class JetBrains.Annotations.NotifyPropertyChangedInvocatorAttribute
Class JetBrains.Annotations.ContractAnnotationAttribute
Class JetBrains.Annotations.LocalizationRequiredAttribute
Class JetBrains.Annotations.CannotApplyEqualityOperatorAttribute
Class JetBrains.Annotations.DefaultEqualityUsageAttribute
Class JetBrains.Annotations.BaseTypeRequiredAttribute
Class JetBrains.Annotations.UsedImplicitlyAttribute
Class JetBrains.Annotations.MeansImplicitUseAttribute
Class JetBrains.Annotations.PublicAPIAttribute
Class JetBrains.Annotations.InstantHandleAttribute
Class JetBrains.Annotations.PureAttribute
Class JetBrains.Annotations.MustUseReturnValueAttribute
Class JetBrains.Annotations.MustDisposeResourceAttribute
Class JetBrains.Annotations.HandlesResourceDisposalAttribute
Class JetBrains.Annotations.RequireStaticDelegateAttribute
Class JetBrains.Annotations.ProvidesContextAttribute
Class JetBrains.Annotations.PathReferenceAttribute
Class JetBrains.Annotations.SourceTemplateAttribute
Class JetBrains.Annotations.MacroAttribute
Class JetBrains.Annotations.CollectionAccessAttribute
Class JetBrains.Annotations.AssertionMethodAttribute
Class JetBrains.Annotations.AssertionConditionAttribute
Class JetBrains.Annotations.TerminatesProgramAttribute
Class JetBrains.Annotations.LinqTunnelAttribute
Class JetBrains.Annotations.NoEnumerationAttribute
Class JetBrains.Annotations.RegexPatternAttribute
Class JetBrains.Annotations.LanguageInjectionAttribute
```

其余 68 个类型未在此列出；可按维护说明重新分析程序集。

**ShimSkiaSharp.dll**（`042fbc38db31f8c1`）：89 个类型。

```text
Class <Module>
Class ShimSkiaSharp.ClipPath
Class ShimSkiaSharp.ReferenceEqualityComparer
Class ShimSkiaSharp.CloneContext
Class ShimSkiaSharp.CloneHelpers
Class ShimSkiaSharp.PathClip
Class ShimSkiaSharp.CanvasCommand
Class ShimSkiaSharp.ClipPathCanvasCommand
Class ShimSkiaSharp.ClipRectCanvasCommand
Class ShimSkiaSharp.DrawImageCanvasCommand
Class ShimSkiaSharp.DrawPathCanvasCommand
Class ShimSkiaSharp.DrawTextBlobCanvasCommand
Class ShimSkiaSharp.DrawTextCanvasCommand
Class ShimSkiaSharp.DrawTextOnPathCanvasCommand
Class ShimSkiaSharp.RestoreCanvasCommand
Class ShimSkiaSharp.SaveCanvasCommand
Class ShimSkiaSharp.SaveLayerCanvasCommand
Class ShimSkiaSharp.SetMatrixCanvasCommand
Class ShimSkiaSharp.SKCanvas
Class ShimSkiaSharp.SKColorFilter
Class ShimSkiaSharp.BlendModeColorFilter
Class ShimSkiaSharp.ColorMatrixColorFilter
Class ShimSkiaSharp.LumaColorColorFilter
Class ShimSkiaSharp.TableColorFilter
Class ShimSkiaSharp.SKDrawable
Class ShimSkiaSharp.SKImage
Class ShimSkiaSharp.SKImageFilter
Class ShimSkiaSharp.ArithmeticImageFilter
Class ShimSkiaSharp.BlendModeImageFilter
Class ShimSkiaSharp.BlurImageFilter
Class ShimSkiaSharp.ColorFilterImageFilter
Class ShimSkiaSharp.DilateImageFilter
Class ShimSkiaSharp.DisplacementMapEffectImageFilter
Class ShimSkiaSharp.DistantLitDiffuseImageFilter
Class ShimSkiaSharp.DistantLitSpecularImageFilter
Class ShimSkiaSharp.ErodeImageFilter
Class ShimSkiaSharp.ImageImageFilter
Class ShimSkiaSharp.MatrixConvolutionImageFilter
Class ShimSkiaSharp.MergeImageFilter
Class ShimSkiaSharp.OffsetImageFilter
```

其余 49 个类型未在此列出；可按维护说明重新分析程序集。

**SkiaSharp.HarfBuzz.dll**（`993ac40cb1619ef2`）：9 个类型。

```text
Class <Module>
Class VersionConstants
Class SkiaSharp.HarfBuzz.BlobExtensions
Class SkiaSharp.HarfBuzz.CanvasExtensions
Class SkiaSharp.HarfBuzz.FontExtensions
Class SkiaSharp.HarfBuzz.SKShaper
Class SkiaSharp.HarfBuzz.BlobExtensions.<>c__DisplayClass0_0
Class SkiaSharp.HarfBuzz.BlobExtensions.<>c__DisplayClass0_1
Class SkiaSharp.HarfBuzz.SKShaper.Result
```

**Svg.Custom.dll**（`7db7962aaa3c9fa8`）：375 个类型。

```text
Class <Module>
Class Svg.SvgCircle
Class Svg.SvgEllipse
Class Svg.SvgLine
Class Svg.SvgMarkerElement
Class Svg.SvgPathBasedElement
Class Svg.SvgPolygon
Class Svg.SvgPolyline
Class Svg.SvgRectangle
Class Svg.SvgVisualElement
Class Svg.SvgClipPath
Class Svg.SvgMask
Class Svg.EnumBaseConverter
Class Svg.XmlSpaceHandlingConverter
Class Svg.SvgFillRuleConverter
Class Svg.SvgColourInterpolationConverter
Class Svg.SvgClipRuleConverter
Class Svg.SvgTextAnchorConverter
Class Svg.SvgStrokeLineCapConverter
Class Svg.SvgStrokeLineJoinConverter
Class Svg.SvgMarkerUnitsConverter
Class Svg.SvgFontStyleConverter
Class Svg.SvgOverflowConverter
Class Svg.SvgTextLengthAdjustConverter
Class Svg.SvgTextPathMethodConverter
Class Svg.SvgTextPathSpacingConverter
Class Svg.SvgShapeRenderingConverter
Class Svg.SvgTextRenderingConverter
Class Svg.SvgImageRenderingConverter
Class Svg.SvgFontVariantConverter
Class Svg.SvgCoordinateUnitsConverter
Class Svg.SvgGradientSpreadMethodConverter
Class Svg.SvgTextDecorationConverter
Class Svg.SvgFontStretchConverter
Class Svg.SvgFontWeightConverter
Class Svg.SvgTextTransformationConverter
Class Svg.SvgBlendModeConverter
Class Svg.SvgColourMatrixTypeConverter
Class Svg.SvgComponentTransferTypeConverter
Class Svg.SvgCompositeOperatorConverter
```

其余 335 个类型未在此列出；可按维护说明重新分析程序集。

**Svg.Model.dll**（`ea907e5b58585323`）：60 个类型。

```text
Class <Module>
Class Svg.Model.GradientMesh
Class Svg.Model.GradientMeshPoint
Class Svg.Model.SvgFilterContext
Class Svg.Model.SvgFilterPrimitiveContext
Class Svg.Model.SvgFilterResult
Class Svg.Model.Services.FilterEffectsService
Class Svg.Model.Services.GradientMeshService
Class Svg.Model.Services.HitTestService
Class Svg.Model.Services.MarkerService
Class Svg.Model.Services.MaskingService
Class Svg.Model.Services.PaintingService
Class Svg.Model.Services.PathingService
Class Svg.Model.Services.SvgService
Class Svg.Model.Services.TransformsService
Class Svg.Model.Services.VectorDrawableConverter
Class Svg.Model.Editing.DrawableEditingExtensions
Class Svg.Model.Editing.DrawableWalker
Class Svg.Model.Editing.SvgDocumentEditingExtensions
Class Svg.Model.Drawables.DrawableBase
Class Svg.Model.Drawables.DrawableContainer
Class Svg.Model.Drawables.DrawablePath
Class Svg.Model.Drawables.Factories.DrawableFactory
Class Svg.Model.Drawables.Elements.AnchorDrawable
Class Svg.Model.Drawables.Elements.CircleDrawable
Class Svg.Model.Drawables.Elements.EllipseDrawable
Class Svg.Model.Drawables.Elements.FragmentDrawable
Class Svg.Model.Drawables.Elements.GroupDrawable
Class Svg.Model.Drawables.Elements.ImageDrawable
Class Svg.Model.Drawables.Elements.LineDrawable
Class Svg.Model.Drawables.Elements.MarkerDrawable
Class Svg.Model.Drawables.Elements.MaskDrawable
Class Svg.Model.Drawables.Elements.PathDrawable
Class Svg.Model.Drawables.Elements.PolygonDrawable
Class Svg.Model.Drawables.Elements.PolylineDrawable
Class Svg.Model.Drawables.Elements.RectangleDrawable
Class Svg.Model.Drawables.Elements.SwitchDrawable
Class Svg.Model.Drawables.Elements.SymbolDrawable
Class Svg.Model.Drawables.Elements.TextDrawable
Class Svg.Model.Drawables.Elements.UseDrawable
```

其余 20 个类型未在此列出；可按维护说明重新分析程序集。

**Svg.Skia.dll**（`7c320221ef4d143a`）：26 个类型。

```text
Class <Module>
Class Svg.Skia.SkiaModel
Class Svg.Skia.SkiaSvgAssetLoader
Class Svg.Skia.SKPictureExtensions
Class Svg.Skia.SKSvg
Class Svg.Skia.SKSvgDrawEventArgs
Class Svg.Skia.SKSvgSettings
Class Svg.Skia.TypefaceProviders.CustomTypefaceProvider
Class Svg.Skia.TypefaceProviders.DefaultTypefaceProvider
Class Svg.Skia.TypefaceProviders.FontManagerTypefaceProvider
Class Svg.Skia.SkiaModel.PositionedTextCache
Class Svg.Skia.SkiaModel.<EnumerateFontFamilyCandidates>d__36
Class Svg.Skia.SkiaSvgAssetLoader.CachedSkPaint
Class Svg.Skia.SkiaSvgAssetLoader.<>c__DisplayClass17_0
Class Svg.Skia.SKSvg.<>O
Class Svg.Skia.SKSvg.<HitTestDrawables>d__0
Class Svg.Skia.SKSvg.<HitTestDrawables>d__1
Class Svg.Skia.SKSvg.<HitTestDrawables>d__6
Class Svg.Skia.SKSvg.<HitTestDrawables>d__7
Class Svg.Skia.SKSvg.<HitTestElements>d__2
Class Svg.Skia.SKSvg.<HitTestElements>d__3
Class Svg.Skia.SKSvg.<HitTestElements>d__8
Class Svg.Skia.SKSvg.<HitTestElements>d__9
Class Svg.Skia.TypefaceProviders.CustomTypefaceProvider.<>c
Class Svg.Skia.TypefaceProviders.DefaultTypefaceProvider.<>c
Class Svg.Skia.TypefaceProviders.FontManagerTypefaceProvider.<>c
```

以下程序集未能解析：`native/win-arm64/native/libHarfBuzzSharp.dll`, `native/win-x64/native/libHarfBuzzSharp.dll`, `native/win-x86/native/libHarfBuzzSharp.dll`。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
