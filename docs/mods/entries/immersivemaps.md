# 沉浸地图

Immersive Maps · 模组代码：immersivemaps

> 来源：整合包安装包 `Immersive Maps-1.2.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `immersivemaps` |
| 版本 | 1.2.1 |
| 类型 | 含程序代码 |
| 运行端 | universal |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.7 |
| 作者 | Woeful_Wolf |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds physical maps to the game with vanilla styled features and balancing.

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
| 程序集 | 1 | `ImmersiveMaps.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 7 | `assets/immersivemaps/itemtypes/charcoal-pencil.json`<br>`assets/immersivemaps/itemtypes/map-papyrus-temporal.json`<br>`assets/immersivemaps/itemtypes/map-papyrus.json`<br>`assets/immersivemaps/itemtypes/map-parchment-temporal.json`<br>`assets/immersivemaps/itemtypes/map-parchment.json`<br>`assets/immersivemaps/itemtypes/paper-papyrus.json`<br>`assets/immersivemaps/itemtypes/penner-and-inkhorn.json` |
| 实体定义 | 0 | — |
| 配方定义 | 6 | `assets/immersivemaps/recipes/grid/charcoal-pencil-recipe.json`<br>`assets/immersivemaps/recipes/grid/map-papyrus-recipe.json`<br>`assets/immersivemaps/recipes/grid/map-papyrus-temporal-recipe.json`<br>`assets/immersivemaps/recipes/grid/map-parchment-recipe.json`<br>`assets/immersivemaps/recipes/grid/map-parchment-temporal-recipe.json`<br>`assets/immersivemaps/recipes/grid/paper-papyrus-recipe.json` |
| 资产补丁 | 2 | `assets/immersivemaps/patches/game-entities-humanoid-player.json`<br>`assets/immersivemaps/patches/game-shapes-entity-humanoid-seraph.json` |
| 语言资源 | 1 | `assets/immersivemaps/lang/en.json` |
| 手册资源 | 1 | `assets/immersivemaps/config/handbook/maps.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ImmersiveMaps.dll**（`0c4aab5ec55c9860`）：85 个类型。

```text
Class <Module>
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FDC696C5685107DA959456553FBDFE24DEE151D4B47973DF39273B30C747E5247__Markup_0
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FDC696C5685107DA959456553FBDFE24DEE151D4B47973DF39273B30C747E5247__Whitespace_1
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FDC696C5685107DA959456553FBDFE24DEE151D4B47973DF39273B30C747E5247__OrderPrefix_2
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>FDC696C5685107DA959456553FBDFE24DEE151D4B47973DF39273B30C747E5247__Utilities
Class ImmersiveMaps.ImmersiveMapsModSystem
Class ImmersiveMaps.Waypoints.MapWaypoints
Class ImmersiveMaps.Waypoints.OreColors
Class ImmersiveMaps.Waypoints.Waypoint
Class ImmersiveMaps.Waypoints.WaypointCollection
Class ImmersiveMaps.Waypoints.WaypointPalette
Class ImmersiveMaps.Utils.CustomFonts
Class ImmersiveMaps.Utils.GeographicCoordinates
Class ImmersiveMaps.Utils.MapCoordinates
Class ImmersiveMaps.Utils.PlayerText
Class ImmersiveMaps.Rendering.ChunkMapLayerHost
Class ImmersiveMaps.Rendering.MapPainter
Class ImmersiveMaps.Rendering.MapRenderState
Class ImmersiveMaps.Rendering.MapRenderSystem
Class ImmersiveMaps.Rendering.MapTemplate
Class ImmersiveMaps.Rendering.PlayerMarker
Class ImmersiveMaps.Rendering.TemporalGlitch
Class ImmersiveMaps.Rendering.TemporalTint
Class ImmersiveMaps.Rendering.WaypointGlyphCache
Class ImmersiveMaps.Rendering.WaypointIconSet
Class ImmersiveMaps.Prospecting.ProspectingRecord
Class ImmersiveMaps.Prospecting.ProspectingReadings
Class ImmersiveMaps.Patches.ItemLocatorMapPatches
Class ImmersiveMaps.Patches.ItemProspectingPickPatches
Class ImmersiveMaps.Network.MapRequestHandler
Class ImmersiveMaps.Network.ModNetwork
Class ImmersiveMaps.Network.MapRotationPacket
Class ImmersiveMaps.Network.SaveWaypointPacket
Class ImmersiveMaps.Network.RemoveWaypointPacket
Class ImmersiveMaps.Network.PinWaypointPacket
Class ImmersiveMaps.Network.CopyWaypointsPacket
Class ImmersiveMaps.Network.RenameMapPacket
Class ImmersiveMaps.Network.AddReadingPacket
Class ImmersiveMaps.Network.SaveNotesPacket
Class ImmersiveMaps.Network.LockMapPacket
```

其余 45 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 6 个配方文件与 1 个手册章节](/reference/recipes/immersivemaps)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
