# 时钟显示补丁

HUD Clock · 模组代码：hudclockpatch

> 来源：整合包安装包 `HUD Clock-4.5.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `hudclockpatch` |
| 版本 | 4.5.0 |
| 类型 | 含程序代码 |
| 运行端 | 客户端 |
| 客户端必需 | 是 |
| 服务端必需 | 否 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Elocrypt |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“界面、汉化与客户端工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

A client-side HUD displaying in-game time, weather, storms, rifts, rooms, and claims.

</details>

作者提供的链接：https://github.com/Elocrypt/HudClock

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `HudClock.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 13 | `assets/hudclock/lang/de.json`<br>`assets/hudclock/lang/en.json`<br>`assets/hudclock/lang/es-419.json`<br>`assets/hudclock/lang/es-es.json`<br>`assets/hudclock/lang/fr.json`<br>`assets/hudclock/lang/it.json`<br>`assets/hudclock/lang/ja.json`<br>`assets/hudclock/lang/ko.json`<br>`assets/hudclock/lang/pl.json`<br>`assets/hudclock/lang/pt-br.json`<br>`assets/hudclock/lang/pt-pt.json`<br>`assets/hudclock/lang/ru.json`<br>另有 1 个文件 |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**HudClock.dll**（`f0e39821fcd5c720`）：63 个类型。

```text
Class <Module>
Class HudClock.HudClockModSystem
Class HudClock.Resources.AssetPaths
Class HudClock.Resources.EnumLangKeys
Class HudClock.Resources.LangKeys
Class HudClock.Presentation.StormHud.StormHudController
Class HudClock.Presentation.StormHud.StormHudStateMachine
Class HudClock.Presentation.StormHud.StormHudView
Class HudClock.Presentation.Shared.BoundsBuilder
Class HudClock.Presentation.Shared.HudAnchorMapper
Class HudClock.Presentation.Shared.HudAnchorOffsets
Class HudClock.Presentation.Shared.HudFonts
Class HudClock.Presentation.SettingsDialog.SettingsDialogController
Class HudClock.Presentation.SettingsDialog.SettingsDialogView
Class HudClock.Presentation.MainHud.MainHudController
Class HudClock.Presentation.MainHud.MainHudView
Class HudClock.Presentation.MainHud.MainHudViewModel
Class HudClock.Presentation.ClaimHud.ClaimHudController
Class HudClock.Presentation.ClaimHud.ClaimHudView
Class HudClock.Infrastructure.Settings.JsonSettingsStore
Class HudClock.Infrastructure.Reflection.FieldAccessor
Class HudClock.Infrastructure.Integration.HudShelfBridge
Class HudClock.Infrastructure.Integration.HudShelfCall
Class HudClock.Infrastructure.Input.KeybindRegistry
Class HudClock.Infrastructure.Assets.IconCache
Class HudClock.Domain.Weather.BeaufortScale
Class HudClock.Domain.Weather.RainfallFrequency
Class HudClock.Domain.Weather.WeatherService
Class HudClock.Domain.Time.TimeFormatter
Class HudClock.Domain.Storms.StormService
Class HudClock.Domain.Rooms.RoomService
Class HudClock.Domain.Rifts.RiftService
Class HudClock.Domain.Player.PlayerStatsService
Class HudClock.Domain.Claims.ClaimService
Class HudClock.Domain.Calendar.CalendarService
Class HudClock.Domain.Calendar.SeasonWording
Class HudClock.Core.ModLog
Class HudClock.Configuration.AppearanceOptions
Class HudClock.Configuration.ClaimOptions
Class HudClock.Configuration.DisplayOptions
```

其余 23 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
