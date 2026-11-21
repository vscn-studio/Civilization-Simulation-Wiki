# 雕刻工具

chiseltools · 模组代码：chiseltools

> 来源：整合包安装包 `chiseltools-1.17.9.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `chiseltools` |
| 版本 | 1.17.9 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | 未声明 |
| 作者 | QPTech |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Quentin's Chiseling Tools'

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
| 程序集 | 2 | `VoxReader.dll`<br>`chiseltools.dll` |
| 方块定义 | 32 | `assets/chiseltools/blocktypes/blank.json`<br>`assets/chiseltools/blocktypes/chiseledanvil.json`<br>`assets/chiseltools/blocktypes/chiseledbarrel.json`<br>`assets/chiseltools/blocktypes/chiseledbed.json`<br>`assets/chiseltools/blocktypes/chiseledbookshelf.json`<br>`assets/chiseltools/blocktypes/chiseledchest.json`<br>`assets/chiseltools/blocktypes/chiseledchestnerfed.json`<br>`assets/chiseltools/blocktypes/chiseledchimney.json`<br>`assets/chiseltools/blocktypes/chiseleddisplaycase.json`<br>`assets/chiseltools/blocktypes/chiseledfence-free.json`<br>`assets/chiseltools/blocktypes/chiseledfirepit.json`<br>`assets/chiseltools/blocktypes/chiseledflowerpot.json`<br>另有 20 个文件 |
| 物品定义 | 16 | `assets/chiseltools/itemtypes/blockswapper.json`<br>`assets/chiseltools/itemtypes/doortool.json`<br>`assets/chiseltools/itemtypes/handplaner.json`<br>`assets/chiseltools/itemtypes/handwedge.json`<br>`assets/chiseltools/itemtypes/jonaspaintbrush.json`<br>`assets/chiseltools/itemtypes/laddermaker.json`<br>`assets/chiseltools/itemtypes/locktool.json`<br>`assets/chiseltools/itemtypes/megapantograph.json`<br>`assets/chiseltools/itemtypes/paintbrush.json`<br>`assets/chiseltools/itemtypes/paintscraper.json`<br>`assets/chiseltools/itemtypes/palette.json`<br>`assets/chiseltools/itemtypes/pantograph.json`<br>另有 4 个文件 |
| 实体定义 | 0 | — |
| 配方定义 | 56 | `assets/chiseltools/recipes/grid/chiseledanvil-true.json`<br>`assets/chiseltools/recipes/grid/chiseledbarrel-true.json`<br>`assets/chiseltools/recipes/grid/chiseledbarrel.json`<br>`assets/chiseltools/recipes/grid/chiseledbed - true.json`<br>`assets/chiseltools/recipes/grid/chiseledbed.json`<br>`assets/chiseltools/recipes/grid/chiseledbookshelf.json`<br>`assets/chiseltools/recipes/grid/chiseledchest - true.json`<br>`assets/chiseltools/recipes/grid/chiseledchest.json`<br>`assets/chiseltools/recipes/grid/chiseledchestbig - true - fromdeco.json`<br>`assets/chiseltools/recipes/grid/chiseledchestbig - true.json`<br>`assets/chiseltools/recipes/grid/chiseledchestbig.json`<br>`assets/chiseltools/recipes/grid/chiseledchimney - true.json`<br>另有 44 个文件 |
| 资产补丁 | 0 | — |
| 语言资源 | 6 | `assets/chiseltools/lang/de.json`<br>`assets/chiseltools/lang/en.json`<br>`assets/chiseltools/lang/ja.json`<br>`assets/chiseltools/lang/pl.json`<br>`assets/chiseltools/lang/zh-cn.json`<br>`assets/game/lang/en.json` |
| 手册资源 | 1 | `assets/chiseltools/config/handbook/chiseltools.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**chiseltools.dll**（`2c55e6d6397b9465`）：90 个类型。

```text
Class <Module>
Class chisel.src.BEFunctionChiseled
Class chisel.src.DoorData
Class chisel.src.TriggerSettings
Class chisel.src.BELockedMicroblock
Class chisel.src.BlockFunctionalChiseled
Class chisel.src.ChiselToolLoader
Class chisel.src.GUIShapeBrowser
Class chisel.src.ItemBlockSwapper
Class chisel.src.ItemChiselBlockController
Class chisel.src.ItemDoorPart
Class chisel.src.ItemHandPlaner
Class chisel.src.ItemLadderMaker
Class chisel.src.ItemPaintBrush
Class chisel.src.ItemPantograph
Class chisel.src.ItemPathMaker
Class chisel.src.ItemWedge
Class chisel.src.PantographData
Class chiseltools.GUIElementClickableText
Class chiseltools.src.BBBarrelCover
Class chiseltools.src.BBChiseledCover
Class chiseltools.src.BEBBarrelCover
Class chiseltools.src.BEBChiseledCover
Class chiseltools.src.BEChiselProjector
Class chiseltools.src.ChiselProjectorData
Class chiseltools.src.BEDecoAnvil
Class chiseltools.src.BEDecoBarrel
Class chiseltools.src.BEDecoBookShelf
Class chiseltools.src.BEDecoContainer
Class chiseltools.src.BEDecoDisplayCase
Class chiseltools.src.BEDecoFirepit
Class chiseltools.src.BEDecoForge
Class chiseltools.src.BEDecoGeneric
Class chiseltools.src.BEDecoPlantContainer
Class chiseltools.src.BEDecoShelf
Class chiseltools.src.BEDecoSign
Class chiseltools.src.BEDecoToolRack
Class chiseltools.src.BETestDummy
Class chiseltools.src.BlockChiselProjector
Class chiseltools.src.BlockDeco
```

其余 50 个类型未在此列出；可按维护说明重新分析程序集。

**VoxReader.dll**（`eba5bd936745375b`）：33 个类型。

```text
Class <Module>
Class Microsoft.CodeAnalysis.EmbeddedAttribute
Class System.Runtime.CompilerServices.IsReadOnlyAttribute
Class VoxReader.ChunkFactory
Class VoxReader.ChunkTypeMapping
Class VoxReader.FormatParser
Class VoxReader.Helper
Class VoxReader.Model
Class VoxReader.Palette
Class VoxReader.VoxFile
Class VoxReader.VoxReader
Class VoxReader.Extensions.ByteArrayExtension
Class VoxReader.Exceptions.InvalidDataException
Class VoxReader.Chunks.Chunk
Class VoxReader.Chunks.GroupNodeChunk
Class VoxReader.Chunks.IndexMapChunk
Class VoxReader.Chunks.NodeChunk
Class VoxReader.Chunks.NoteChunk
Class VoxReader.Chunks.PackChunk
Class VoxReader.Chunks.PaletteChunk
Class VoxReader.Chunks.ShapeNodeChunk
Class VoxReader.Chunks.SizeChunk
Class VoxReader.Chunks.TransformNodeChunk
Class VoxReader.Chunks.VoxelChunk
Class <PrivateImplementationDetails>
Class VoxReader.FormatParser.<>c
Class VoxReader.Helper.<>c__DisplayClass1_0
Class VoxReader.Helper.<>c__DisplayClass1_1
Class VoxReader.Helper.<ExtractModels>d__1
Class VoxReader.Palette.<GetNoteIndices>d__10
Class VoxReader.Chunks.Chunk.<>c__14
Class VoxReader.Chunks.Chunk.<>c__16
Class VoxReader.Chunks.Chunk.<>c__DisplayClass15_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 56 个配方文件与 1 个手册章节](/reference/recipes/chiseltools)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
