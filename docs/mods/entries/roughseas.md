# 海浪

Rough Seas · 模组代码：roughseas

> 来源：整合包安装包 `Rough Seas-5.0.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `roughseas` |
| 版本 | 5.0.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.4 |
| 作者 | hoblin |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Makes the ocean dangerous and worth going out on.

</details>

作者提供的链接：https://github.com/hoblin/rough-seas

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `RoughSeas.dll` |
| 方块定义 | 3 | `assets/roughseas/blocktypes/debarkedtrunk.json`<br>`assets/roughseas/blocktypes/reedbundle.json`<br>`assets/roughseas/blocktypes/wedge.json` |
| 物品定义 | 13 | `assets/roughseas/itemtypes/anchorwarp.json`<br>`assets/roughseas/itemtypes/resource/bark.json`<br>`assets/roughseas/itemtypes/resource/lath.json`<br>`assets/roughseas/itemtypes/resource/lathbundle.json`<br>`assets/roughseas/itemtypes/resource/pole.json`<br>`assets/roughseas/itemtypes/tool/paddle.json`<br>`assets/roughseas/itemtypes/tool/tholeoar.json`<br>`assets/roughseas/itemtypes/vessel/barkcanoe.json`<br>`assets/roughseas/itemtypes/vessel/coracle.json`<br>`assets/roughseas/itemtypes/vessel/currach.json`<br>`assets/roughseas/itemtypes/vessel/dugout.json`<br>`assets/roughseas/itemtypes/vessel/outrigger.json`<br>另有 1 个文件 |
| 实体定义 | 7 | `assets/roughseas/entities/lathbundle.json`<br>`assets/roughseas/entities/vessel/barkcanoe.json`<br>`assets/roughseas/entities/vessel/coracle.json`<br>`assets/roughseas/entities/vessel/currach.json`<br>`assets/roughseas/entities/vessel/dugout.json`<br>`assets/roughseas/entities/vessel/outrigger.json`<br>`assets/roughseas/entities/vessel/reedboat.json` |
| 配方定义 | 6 | `assets/roughseas/recipes/barrel/lath.json`<br>`assets/roughseas/recipes/grid/anchorwarp.json`<br>`assets/roughseas/recipes/grid/lathbundles.json`<br>`assets/roughseas/recipes/grid/laths.json`<br>`assets/roughseas/recipes/grid/propulsion.json`<br>`assets/roughseas/recipes/grid/vessels.json` |
| 资产补丁 | 20 | `assets/roughseas/patches/boats-drift.json`<br>`assets/roughseas/patches/compat-shipwright.json`<br>`assets/roughseas/patches/player-barkcanoe.json`<br>`assets/roughseas/patches/player-coracle.json`<br>`assets/roughseas/patches/player-currach.json`<br>`assets/roughseas/patches/player-dugout.json`<br>`assets/roughseas/patches/player-outrigger.json`<br>`assets/roughseas/patches/player-poses.json`<br>`assets/roughseas/patches/player-raft.json`<br>`assets/roughseas/patches/player-reedboat.json`<br>`assets/roughseas/patches/player-tying.json`<br>`assets/roughseas/patches/propulsion-oar.json`<br>另有 8 个文件 |
| 语言资源 | 66 | `assets/game/lang/worldconfig-ar.json`<br>`assets/game/lang/worldconfig-be.json`<br>`assets/game/lang/worldconfig-bg.json`<br>`assets/game/lang/worldconfig-cs.json`<br>`assets/game/lang/worldconfig-da.json`<br>`assets/game/lang/worldconfig-de.json`<br>`assets/game/lang/worldconfig-en.json`<br>`assets/game/lang/worldconfig-eo.json`<br>`assets/game/lang/worldconfig-es-419.json`<br>`assets/game/lang/worldconfig-es-es.json`<br>`assets/game/lang/worldconfig-fi.json`<br>`assets/game/lang/worldconfig-fr.json`<br>另有 54 个文件 |
| 手册资源 | 6 | `assets/roughseas/config/handbook/00-goingtosea.json`<br>`assets/roughseas/config/handbook/01-weather.json`<br>`assets/roughseas/config/handbook/02-vessels.json`<br>`assets/roughseas/config/handbook/03-surf.json`<br>`assets/roughseas/config/handbook/04-mooring.json`<br>`assets/roughseas/config/handbook/05-swimming.json` |
| 包内配置数据 | 22 | `assets/roughseas/config/compat/extremeweather.json`<br>`assets/roughseas/config/person.json`<br>`assets/roughseas/config/propulsion.json`<br>`assets/roughseas/config/remapentities.json`<br>`assets/roughseas/config/remaps.json`<br>`assets/roughseas/config/sailing.json`<br>`assets/roughseas/config/seaweather.json`<br>`assets/roughseas/config/shore.json`<br>`assets/roughseas/config/soundscape.json`<br>`assets/roughseas/config/storms.json`<br>`assets/roughseas/config/vessels/canoebarks.json`<br>`assets/roughseas/config/vessels/damage.json`<br>另有 10 个文件 |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**RoughSeas.dll**（`d0fac1965cb3c991`）：856 个类型。

```text
Class <Module>
Class <>z__ReadOnlyArray
Class <>z__ReadOnlyList
Class <>z__ReadOnlySingleElementList
Class RoughSeas.ReachedAtRuntimeAttribute
Class RoughSeas.ReliesOnAttribute
Class RoughSeas.ReliesOnTextAttribute
Class RoughSeas.RoughSeasModSystem
Class RoughSeas.Wind.BodyInWind
Class RoughSeas.Wind.EntityBehaviorWindage
Class RoughSeas.Wind.VesselInWind
Class RoughSeas.Wind.WindConfig
Class RoughSeas.Wind.WindModSystem
Class RoughSeas.Wind.WindSurface
Class RoughSeas.Wind.BluffSurface
Class RoughSeas.Water.AddedMass
Class RoughSeas.Water.Band
Class RoughSeas.Water.Beds
Class RoughSeas.Water.BoxAverage
Class RoughSeas.Water.EnteringWaves
Class RoughSeas.Water.CoarseBed
Class RoughSeas.Water.FaceBuilder
Class RoughSeas.Water.OpenWater
Class RoughSeas.Water.PhaseField
Class RoughSeas.Water.RunUp
Class RoughSeas.Water.SeabedMap
Class RoughSeas.Water.Seabeds
Class RoughSeas.Water.ShoreConfig
Class RoughSeas.Water.FacesConfig
Class RoughSeas.Water.RunUpConfig
Class RoughSeas.Water.SheetConfig
Class RoughSeas.Water.BedConfig
Class RoughSeas.Water.BandConfig
Class RoughSeas.Water.ShoreGround
Class RoughSeas.Water.SlippingBlade
Class RoughSeas.Water.SurfaceConfig
Class RoughSeas.Water.ShortWavesConfig
Class RoughSeas.Water.ShortBandConfig
Class RoughSeas.Water.TessellationConfig
Class RoughSeas.Water.SurfaceTrainConfig
```

其余 816 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 6 个配方文件与 6 个手册章节](/reference/recipes/roughseas)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
