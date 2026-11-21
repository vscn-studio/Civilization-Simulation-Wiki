# 绘画画布

VintageCanvas · 模组代码：vintagecanvas

> 来源：整合包安装包 `VintageCanvas-1.4.2.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vintagecanvas` |
| 版本 | 1.4.2 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Tony Murchison |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

In-world painting mod

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
| 程序集 | 4 | `Microsoft.Win32.SystemEvents.dll`<br>`Mixbox.dll`<br>`System.Drawing.Common.dll`<br>`VintageCanvas.dll` |
| 方块定义 | 9 | `assets/vintagecanvas/blocktypes/canvas.json`<br>`assets/vintagecanvas/blocktypes/easel.json`<br>`assets/vintagecanvas/blocktypes/frescoplaster.json`<br>`assets/vintagecanvas/blocktypes/heasel.json`<br>`assets/vintagecanvas/blocktypes/jarbrush.json`<br>`assets/vintagecanvas/blocktypes/largecanvas.json`<br>`assets/vintagecanvas/blocktypes/paintjar.json`<br>`assets/vintagecanvas/blocktypes/palette.json`<br>`assets/vintagecanvas/blocktypes/wallpaint.json` |
| 物品定义 | 11 | `assets/vintagecanvas/itemtypes/brush.json`<br>`assets/vintagecanvas/itemtypes/liquid/paint.json`<br>`assets/vintagecanvas/itemtypes/liquid/tempera.json`<br>`assets/vintagecanvas/itemtypes/liquid/turpentine.json`<br>`assets/vintagecanvas/itemtypes/pastel.json`<br>`assets/vintagecanvas/itemtypes/pigment.json`<br>`assets/vintagecanvas/itemtypes/rag.json`<br>`assets/vintagecanvas/itemtypes/raw/paintjar.json`<br>`assets/vintagecanvas/itemtypes/roller.json`<br>`assets/vintagecanvas/itemtypes/vellum.json`<br>`assets/vintagecanvas/itemtypes/wearable/seraph/head.json` |
| 实体定义 | 0 | — |
| 配方定义 | 22 | `assets/vintagecanvas/recipes/barrel/brazilwood.json`<br>`assets/vintagecanvas/recipes/barrel/leadwhite.json`<br>`assets/vintagecanvas/recipes/barrel/ultramarine.json`<br>`assets/vintagecanvas/recipes/barrel/verdigris.json`<br>`assets/vintagecanvas/recipes/barrel/vermillion.json`<br>`assets/vintagecanvas/recipes/barrel/woadpigment.json`<br>`assets/vintagecanvas/recipes/clayforming/fourpaintjars.json`<br>`assets/vintagecanvas/recipes/clayforming/paintjar.json`<br>`assets/vintagecanvas/recipes/cooking/turpentine.json`<br>`assets/vintagecanvas/recipes/grid/beret.json`<br>`assets/vintagecanvas/recipes/grid/brush.json`<br>`assets/vintagecanvas/recipes/grid/canvas-vellum.json`<br>另有 10 个文件 |
| 资产补丁 | 3 | `assets/vintagecanvas/patches/artistclassdisable.json`<br>`assets/vintagecanvas/patches/emcompat.json`<br>`assets/vintagecanvas/patches/grinderrecipes.json` |
| 语言资源 | 3 | `assets/vintagecanvas/lang/en.json`<br>`assets/vintagecanvas/lang/uk.json`<br>`assets/vintagecanvas/lang/worldconfig-en.json` |
| 手册资源 | 5 | `assets/vintagecanvas/config/handbook/1-basics.json`<br>`assets/vintagecanvas/config/handbook/2-painting.json`<br>`assets/vintagecanvas/config/handbook/3-frescos.json`<br>`assets/vintagecanvas/config/handbook/4-largepaintings.json`<br>`assets/vintagecanvas/config/handbook/5-finitepaint.json` |
| 包内配置数据 | 2 | `assets/vintagecanvas/config/characterclasses.json`<br>`assets/vintagecanvas/config/traits.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Microsoft.Win32.SystemEvents.dll**（`d27ecc9df37937ae`）：11 个类型。

```text
Class <Module>
Class FxResources.Microsoft.Win32.SystemEvents.SR
Class Microsoft.Win32.PowerModeChangedEventArgs
Class Microsoft.Win32.SessionEndedEventArgs
Class Microsoft.Win32.SessionEndingEventArgs
Class Microsoft.Win32.SessionSwitchEventArgs
Class Microsoft.Win32.SystemEvents
Class Microsoft.Win32.TimerElapsedEventArgs
Class Microsoft.Win32.UserPreferenceChangedEventArgs
Class Microsoft.Win32.UserPreferenceChangingEventArgs
Class System.SR
```

**Mixbox.dll**（`c38ecc2a2966e70a`）：5 个类型。

```text
Class <Module>
Class Scrtwpns.Mixbox.Mixbox
Class Scrtwpns.Mixbox.ZlibDecoder
Class <PrivateImplementationDetails>
Class Scrtwpns.Mixbox.ZlibDecoder.Huffman
```

**System.Drawing.Common.dll**（`f644932baa643d31`）：150 个类型。

```text
Class <Module>
Class Interop
Class FXAssembly
Class AssemblyRef
Class FxResources.System.Drawing.Common.SR
Class System.LocalAppContextSwitches
Class System.SR
Class System.Runtime.InteropServices.Marshalling.HandleRefMarshaller
Class System.Windows.Forms.DpiHelper
Class System.Drawing.SRDescriptionAttribute
Class System.Drawing.Bitmap
Class System.Drawing.BitmapSuffixInSameAssemblyAttribute
Class System.Drawing.BitmapSuffixInSatelliteAssemblyAttribute
Class System.Drawing.BufferedGraphics
Class System.Drawing.BufferedGraphicsContext
Class System.Drawing.Brushes
Class System.Drawing.SafeNativeMethods
Class System.Drawing.Graphics
Class System.Drawing.IconConverter
Class System.Drawing.Image
Class System.Drawing.ImageAnimator
Class System.Drawing.ImageConverter
Class System.Drawing.ImageFormatConverter
Class System.Drawing.NumericsExtensions
Class System.Drawing.Pen
Class System.Drawing.Pens
Class System.Drawing.StringFormat
Class System.Drawing.SystemFonts
Class System.Drawing.SystemPens
Class System.Drawing.Region
Class System.Drawing.ClientUtils
Class System.Drawing.NativeMethods
Class System.Drawing.Brush
Class System.Drawing.Font
Class System.Drawing.FontConverter
Class System.Drawing.FontFamily
Class System.Drawing.SolidBrush
Class System.Drawing.SystemBrushes
Class System.Drawing.TextureBrush
Class System.Drawing.BitmapSelector
```

其余 110 个类型未在此列出；可按维护说明重新分析程序集。

**VintageCanvas.dll**（`fbac105bfe8f64cc`）：59 个类型。

```text
Class <Module>
Class <>z__ReadOnlySingleElementList
Class VintageCanvas.VintageCanvasModSystem
Class VintageCanvas.PaintSavePacket
Class VintageCanvas.PaletteSavePacket
Class VintageCanvas.FrameSavePacket
Class VintageCanvas.FrescoPushPacket
Class VintageCanvas.FrescoRequestPacket
Class VintageCanvas.CanvasNameSavePacket
Class VintageCanvas.src.Utility.CanvasExport
Class VintageCanvas.src.Utility.FrescoStore
Class VintageCanvas.src.Utility.GuiPaintingSigning
Class VintageCanvas.src.Utility.IdRegistry
Class VintageCanvas.src.Utility.MessageForms
Class VintageCanvas.src.Utility.CanvasNetworkHandler
Class VintageCanvas.src.Utility.MultiblockSelectionOutlinePatch
Class VintageCanvas.src.Utility.LoadDecorPatch
Class VintageCanvas.src.Utility.ScrapeFrescoPatch
Class VintageCanvas.src.Utility.CancelArtistHunger
Class VintageCanvas.src.Utility.ChiselInfoPatch
Class VintageCanvas.src.Utility.FrescoRemovedPatch
Class VintageCanvas.src.Utility.FrescoFromTreePatch
Class VintageCanvas.src.Utility.TextureUtil
Class VintageCanvas.src.Utility.VintageCanvasConfig
Class VintageCanvas.src.Items.CollectibleBehaviorDecorTool
Class VintageCanvas.src.Items.CollectibleBehaviorPaintTool
Class VintageCanvas.src.Items.ItemBrush
Class VintageCanvas.src.Items.ItemPastel
Class VintageCanvas.src.Items.ItemPigment
Class VintageCanvas.src.Entities.BlockEntityCanvas
Class VintageCanvas.src.Entities.BlockEntityEasel
Class VintageCanvas.src.Entities.BlockEntityEaselH
Class VintageCanvas.src.Entities.BlockEntityFrescoPlaster
Class VintageCanvas.src.Entities.BlockEntityLargeCanvas
Class VintageCanvas.src.Entities.BlockEntityPalette
Class VintageCanvas.src.Blocks.BlockCanvas
Class VintageCanvas.src.Blocks.BlockEasel
Class VintageCanvas.src.Blocks.BlockEaselH
Class VintageCanvas.src.Blocks.BlockFrescoPlaster
Class VintageCanvas.src.Blocks.BlockLargeCanvas
```

其余 19 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 22 个配方文件与 5 个手册章节](/reference/recipes/vintagecanvas)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
