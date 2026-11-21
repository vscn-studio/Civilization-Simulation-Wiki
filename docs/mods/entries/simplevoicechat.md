# 语音聊天

Simple Voice Chat · 模组代码：simplevoicechat

> 来源：整合包安装包 `Simple Voice Chat-1.3.7.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `simplevoicechat` |
| 版本 | 1.3.7 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.3 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Proximity voice chat and player channels for Vintage Story.

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
| 程序集 | 5 | `Concentus.dll`<br>`RNNoise.NET.dll`<br>`SimpleVoiceChat.dll`<br>`native/runtimes/win-x64/rnnoise.dll`<br>`native/runtimes/win-x86/rnnoise.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/simplevoicechat/lang/en.json`<br>`assets/simplevoicechat/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Concentus.dll**（`3a1dcfcfaf86b90f`）：151 个类型。

```text
Class <Module>
Class Concentus.OpusCodecFactory
Class Concentus.Analysis
Class Concentus.CodecHelpers
Class Concentus.Downmix
Class Concentus.MultiLayerPerceptron
Class Concentus.OpusCompare
Class Concentus.OpusConstants
Class Concentus.OpusException
Class Concentus.OpusMultistream
Class Concentus.Tables
Class Concentus.ResamplerFactory
Class Concentus.Silk.ApplySineWindow
Class Concentus.Silk.BurgModified
Class Concentus.Silk.BWExpander
Class Concentus.Silk.CNG
Class Concentus.Silk.CodeSigns
Class Concentus.Silk.CorrelateMatrix
Class Concentus.Silk.DecodeAPI
Class Concentus.Silk.DecodeCore
Class Concentus.Silk.DecodeIndices
Class Concentus.Silk.DecodeParameters
Class Concentus.Silk.DecodePitch
Class Concentus.Silk.DecodePulses
Class Concentus.Silk.EncodeAPI
Class Concentus.Silk.EncodeIndices
Class Concentus.Silk.EncodePulses
Class Concentus.Silk.Filters
Class Concentus.Silk.FindLPC
Class Concentus.Silk.FindLTP
Class Concentus.Silk.FindPitchLags
Class Concentus.Silk.FindPredCoefs
Class Concentus.Silk.GainQuantization
Class Concentus.Silk.HPVariableCutoff
Class Concentus.Silk.K2A
Class Concentus.Silk.LinearAlgebra
Class Concentus.Silk.LPCInversePredGain
Class Concentus.Silk.LTPAnalysisFilter
Class Concentus.Silk.LTPScaleControl
Class Concentus.Silk.NLSF
```

其余 111 个类型未在此列出；可按维护说明重新分析程序集。

**RNNoise.NET.dll**（`f1798d0e9992d153`）：3 个类型。

```text
Class <Module>
Class RNNoise.NET.Denoiser
Class RNNoise.NET.Native
```

**SimpleVoiceChat.dll**（`279956f9e033acc3`）：309 个类型。

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
Class <>f__AnonymousType9
Class <>f__AnonymousType10
Class <>f__AnonymousType11
Class <>f__AnonymousType12
Class <>f__AnonymousType13
Class <>f__AnonymousType14
Class <>f__AnonymousType15
Class <>f__AnonymousType16
Class <>f__AnonymousType17
Class SimpleVoiceChat.ClientVoiceController
Class SimpleVoiceChat.ControllerLifecycle
Class SimpleVoiceChat.SVCLang
Class SimpleVoiceChat.ServerVoiceController
Class SimpleVoiceChat.SimpleVoiceChatModSystem
Class SimpleVoiceChat.VoiceConstants
Class SimpleVoiceChat.Server.ChannelService
Class SimpleVoiceChat.Server.VoiceChannel
Class SimpleVoiceChat.Server.ListenerEgressBudget
Class SimpleVoiceChat.Server.ListenerStreamArbiter
Class SimpleVoiceChat.Server.ServerAdaptiveBitrateController
Class SimpleVoiceChat.Server.VoiceAuditLog
Class SimpleVoiceChat.Server.VoiceAuditConfig
Class SimpleVoiceChat.Server.VoiceAuditEntry
Class SimpleVoiceChat.Server.VoiceMetrics
Class SimpleVoiceChat.Server.VoiceModerationService
Class SimpleVoiceChat.Server.VoiceSpatialIndex
Class SimpleVoiceChat.Server.VoiceTokenBucket
Class SimpleVoiceChat.Networking.MonotonicClock
Class SimpleVoiceChat.Networking.ServerClockEstimator
Class SimpleVoiceChat.Networking.PacketMapper
```

其余 269 个类型未在此列出；可按维护说明重新分析程序集。

以下程序集未能解析：`native/runtimes/win-x64/rnnoise.dll`, `native/runtimes/win-x86/rnnoise.dll`。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
