# 极端天气

Extreme Weather · 模组代码：extremeweather

> 来源：整合包安装包 `Extreme Weather-1.8.7.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `extremeweather` |
| 版本 | 1.8.7 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | 未声明 |
| 作者 | Tiggetagg |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“世界、气候与环境”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Are you ready for a true challenge against the elements? Weather events strike without warning - watch the skies: blinding blizzards that bury the world in deep snow, drenching summer monsoons, hurricanes that strip forests bare and tear roofs apart, tornadoes, sandstorms, heat waves and cold snaps that turn the climate deadly - shelter is no longer optional. Includes new weather patterns that join the natural rotation. Fully configurable. Recommended companion: Immersive Body Temperature, which reacts to the temperatures, wind and rain this mod drives.

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
| 程序集 | 1 | `ExtremeWeather.dll` |
| 方块定义 | 2 | `assets/extremeweather/blocktypes/icicle.json`<br>`assets/extremeweather/blocktypes/snowedclutter.json` |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 2 | `assets/extremeweather/patches/door-rattle-anim.json`<br>`assets/extremeweather/patches/snowblock-sticky.json` |
| 语言资源 | 2 | `assets/extremeweather/lang/en.json`<br>`assets/game/lang/worldconfig-en.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 11 | `assets/game/config/weatherevents/supercell.json`<br>`assets/game/config/weatherevents/torrential.json`<br>`assets/game/config/weatherpatterns/drizzle.json`<br>`assets/game/config/weatherpatterns/duststorm.json`<br>`assets/game/config/weatherpatterns/fogbank.json`<br>`assets/game/config/weatherpatterns/hurricanesky.json`<br>`assets/game/config/weatherpatterns/mackerelsky.json`<br>`assets/game/config/weatherpatterns/squall.json`<br>`assets/game/config/weatherpatterns/sunshower.json`<br>`assets/game/config/windpatterns/hurricane.json`<br>`assets/game/config/windpatterns/zephyr.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ExtremeWeather.dll**（`6511b61fd7a5965c`）：80 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class ExtremeWeather.AvalancheSystem
Class ExtremeWeather.BlizzardAudioSystem
Class ExtremeWeather.BlizzardVisionSystem
Class ExtremeWeather.BlockBehaviorStickyFalling
Class ExtremeWeather.BlockIcicle
Class ExtremeWeather.DeepSnowSystem
Class ExtremeWeather.DoorShakeSystem
Class ExtremeWeather.EventStatePacket
Class ExtremeWeather.EventDirectorSystem
Class ExtremeWeather.ExtremeWeatherConfig
Class ExtremeWeather.ExtremeWeatherModSystem
Class ExtremeWeather.HeatWaveSystem
Class ExtremeWeather.HurricaneSystem
Class ExtremeWeather.PaneShakeSystem
Class ExtremeWeather.ParticleStormSystem
Class ExtremeWeather.PerfTracker
Class ExtremeWeather.PerfMonitor
Class ExtremeWeather.PerfMonitorServer
Class ExtremeWeather.PerfMonitorClient
Class ExtremeWeather.RubbleUtil
Class ExtremeWeather.CropUtil
Class ExtremeWeather.SandstormClientSystem
Class ExtremeWeather.SandstormSystem
Class ExtremeWeather.BlockSnowedClutter
Class ExtremeWeather.BlockEntitySnowedClutter
Class ExtremeWeather.SnowfallRenderer
Class ExtremeWeather.StormThreatSystem
Class ExtremeWeather.TornadoRenderer
Class ExtremeWeather.TornadoPacket
Class ExtremeWeather.TornadoSystem
Class ExtremeWeather.WeatherRead
Class ExtremeWeather.WindUtil
Class ExtremeWeather.ConfigSyncPacket
Class <PrivateImplementationDetails>
Class ExtremeWeather.AvalancheSystem.<>c
Class ExtremeWeather.AvalancheSystem.<>c__DisplayClass10_0
Class ExtremeWeather.AvalancheSystem.<>c__DisplayClass15_0
Class ExtremeWeather.AvalancheSystem.<>c__DisplayClass15_1
```

其余 40 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
