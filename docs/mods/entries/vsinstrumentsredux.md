# 乐器

VSInstrumentsRedux · 模组代码：vsinstrumentsredux

> 来源：整合包安装包 `VSInstrumentsRedux-2.3.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vsinstrumentsredux` |
| 版本 | 2.3.0 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | KaiserConman, Poyomi |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Bring your world to life! Play ABC and MIDI files on working in-game instruments, and more!

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
| 程序集 | 2 | `Melanchall.DryWetMidi.dll`<br>`VSInstrumentsRedux.dll` |
| 方块定义 | 5 | `assets/vsinstrumentsredux/blocktypes/musicbox.json`<br>`assets/vsinstrumentsredux/blocktypes/musiclectern.json`<br>`assets/vsinstrumentsredux/blocktypes/musicward.json`<br>`assets/vsinstrumentsredux/blocktypes/phonograph.json`<br>`assets/vsinstrumentsredux/blocktypes/pianobench.json` |
| 物品定义 | 13 | `assets/vsinstrumentsredux/itemtypes/headphonograph.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-drum-machine.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-erhu.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-flute.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-resonance-blaster.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-saw-synth.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-saxophone.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-square-synth.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-synth-bass.json`<br>`assets/vsinstrumentsredux/itemtypes/instrument-warm-pad.json`<br>`assets/vsinstrumentsredux/itemtypes/phonographcylinder.json`<br>`assets/vsinstrumentsredux/itemtypes/portablephonograph.json`<br>另有 1 个文件 |
| 实体定义 | 0 | — |
| 配方定义 | 15 | `assets/vsinstrumentsredux/recipes/grid/drum-machine.json`<br>`assets/vsinstrumentsredux/recipes/grid/erhu.json`<br>`assets/vsinstrumentsredux/recipes/grid/flute.json`<br>`assets/vsinstrumentsredux/recipes/grid/headphonograph.json`<br>`assets/vsinstrumentsredux/recipes/grid/musicbox.json`<br>`assets/vsinstrumentsredux/recipes/grid/musiclectern.json`<br>`assets/vsinstrumentsredux/recipes/grid/phonograph.json`<br>`assets/vsinstrumentsredux/recipes/grid/phonographcylinder.json`<br>`assets/vsinstrumentsredux/recipes/grid/pianobench.json`<br>`assets/vsinstrumentsredux/recipes/grid/portablephonograph.json`<br>`assets/vsinstrumentsredux/recipes/grid/saw-synth.json`<br>`assets/vsinstrumentsredux/recipes/grid/saxophone.json`<br>另有 3 个文件 |
| 资产补丁 | 3 | `assets/vsinstrumentsredux/patches/expansion_toggles.json`<br>`assets/vsinstrumentsredux/patches/purposefulstorage_compat.json`<br>`assets/vsinstrumentsredux/patches/recipe_toggles.json` |
| 语言资源 | 2 | `assets/vsinstrumentsredux/lang/en.json`<br>`assets/vsinstrumentsredux/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 2 | `assets/vsinstrumentsredux/config/drum-durations.json`<br>`assets/vsinstrumentsredux/config/imm.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Melanchall.DryWetMidi.dll**（`08cf63e1c2587748`）：694 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>f__AnonymousType1
Class <>f__AnonymousType2
Class <>f__AnonymousType3
Class Melanchall.DryWetMidi.Tools.TimeProcessingInstruction
Class Melanchall.DryWetMidi.Tools.CsvError
Class Melanchall.DryWetMidi.Tools.CsvException
Class Melanchall.DryWetMidi.Tools.CsvFormattingUtilities
Class Melanchall.DryWetMidi.Tools.CsvDeserializationSettings
Class Melanchall.DryWetMidi.Tools.CsvReader
Class Melanchall.DryWetMidi.Tools.CsvRecord
Class Melanchall.DryWetMidi.Tools.CsvSerializer
Class Melanchall.DryWetMidi.Tools.EventParser
Class Melanchall.DryWetMidi.Tools.Record
Class Melanchall.DryWetMidi.Tools.TypeParser
Class Melanchall.DryWetMidi.Tools.CsvChord
Class Melanchall.DryWetMidi.Tools.CsvEvent
Class Melanchall.DryWetMidi.Tools.CsvNote
Class Melanchall.DryWetMidi.Tools.CsvObject
Class Melanchall.DryWetMidi.Tools.CsvSerializationSettings
Class Melanchall.DryWetMidi.Tools.CsvWriter
Class Melanchall.DryWetMidi.Tools.EventParametersProvider
Class Melanchall.DryWetMidi.Tools.Merger
Class Melanchall.DryWetMidi.Tools.ObjectsMerger
Class Melanchall.DryWetMidi.Tools.ObjectsMergingSettings
Class Melanchall.DryWetMidi.Tools.SequentialMergingSettings
Class Melanchall.DryWetMidi.Tools.SimultaneousMergingSettings
Class Melanchall.DryWetMidi.Tools.ConstantBounds
Class Melanchall.DryWetMidi.Tools.QuantizedTime
Class Melanchall.DryWetMidi.Tools.Quantizer
Class Melanchall.DryWetMidi.Tools.QuantizerUtilities
Class Melanchall.DryWetMidi.Tools.QuantizingSettings
Class Melanchall.DryWetMidi.Tools.RandomizingSettings
Class Melanchall.DryWetMidi.Tools.PartProcessingContext
Class Melanchall.DryWetMidi.Tools.Repeater
Class Melanchall.DryWetMidi.Tools.RepeaterUtilities
Class Melanchall.DryWetMidi.Tools.RepeatingSettings
Class Melanchall.DryWetMidi.Tools.ObjectsGroupResizingSettings
Class Melanchall.DryWetMidi.Tools.Resizer
```

其余 654 个类型未在此列出；可按维护说明重新分析程序集。

**VSInstrumentsRedux.dll**（`10c1ce27d50b56d5`）：185 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class MeltySynth.ArrayMath
Class MeltySynth.AudioRendererEx
Class MeltySynth.BinaryReaderEx
Class MeltySynth.BiQuadFilter
Class MeltySynth.Channel
Class MeltySynth.Chorus
Class MeltySynth.Instrument
Class MeltySynth.InstrumentInfo
Class MeltySynth.InstrumentRegion
Class MeltySynth.Lfo
Class MeltySynth.MidiFile
Class MeltySynth.MidiFileSequencer
Class MeltySynth.ModulationEnvelope
Class MeltySynth.Modulator
Class MeltySynth.Oscillator
Class MeltySynth.Preset
Class MeltySynth.PresetInfo
Class MeltySynth.PresetRegion
Class MeltySynth.RegionEx
Class MeltySynth.Reverb
Class MeltySynth.SampleHeader
Class MeltySynth.SoundFont
Class MeltySynth.SoundFontInfo
Class MeltySynth.SoundFontMath
Class MeltySynth.SoundFontParameters
Class MeltySynth.SoundFontSampleData
Class MeltySynth.Synthesizer
Class MeltySynth.SynthesizerSettings
Class MeltySynth.Voice
Class MeltySynth.VoiceCollection
Class MeltySynth.VolumeEnvelope
Class MeltySynth.ZoneInfo
Class VSInstrumentsRedux.AbcParser
Class VSInstrumentsRedux.BlockInstrument
Class VSInstrumentsRedux.BlockEntityInstrument
Class VSInstrumentsRedux.BlockLectern
Class VSInstrumentsRedux.BlockEntityLectern
Class VSInstrumentsRedux.GuiDialogLectern
```

其余 145 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 15 个配方文件与 0 个手册章节](/reference/recipes/vsinstrumentsredux)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
