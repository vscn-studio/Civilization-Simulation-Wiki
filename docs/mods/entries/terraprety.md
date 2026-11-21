# 地形生成

Terra Prety · 模组代码：terraprety

> 来源：整合包安装包 `Terra Prety-7.11.2-pre.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `terraprety` |
| 版本 | 7.11.2-pre.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 否 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Nephelangelo, Darkluke1111, JonR, Algernon |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“世界、气候与环境”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

A redesign of worldgen to feel more natural, beautiful and enjoyable to traverse.

</details>

作者提供的链接：https://mods.vintagestory.at/terraprety

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `TerraPrety.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 5 | `assets/terraprety/patches/survival-worldgen-landforms.json`<br>`assets/terraprety/patches/survival-worldgen-reducedferns.json`<br>`assets/terraprety/patches/survival-worldgen-storystructures.json`<br>`assets/terraprety/patches/survival-worldgen-tileddungeons.json`<br>`assets/terraprety/patches/survival-worldgen-treengenproperties.json` |
| 语言资源 | 1 | `assets/terraprety/lang/en.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**TerraPrety.dll**（`81dfd6e32e730dff`）：36 个类型。

```text
Class <Module>
Class MapLayer.MapLayerOceansSmooth
Class TerraPrety.NoiseRemapper
Class TerraPrety.Patch
Class TerraPrety.TerraPretyModSystem
Class TerraPrety.WorldGenConfig
Class TerraPrety.Noise.VoronoiNoise
Class TerraPrety.Noise.VoronoiRidgeNoise
Class TerraPrety.Rivers.CoastMap
Class TerraPrety.Rivers.GenRivers
Class TerraPrety.Rivers.GenTerraPrety
Class TerraPrety.Rivers.RiverData
Class TerraPrety.Rivers.PrimaryRiverLogic
Class TerraPrety.Rivers.TributaryRiverLogic
Class TerraPrety.Rivers.RiverPlottingLogic
Class TerraPrety.Rivers.RiverMap
Class TerraPrety.Rivers.RiverRegion
Class TerraPrety.Rivers.RiverSegment
Class TerraPrety.Rivers.RiverPoint
Class TerraPrety.LandformHeights.LandformGenHeight
Class TerraPrety.LandformHeights.LandformHeightNoise
Class TerraPrety.LandformHeights.LandformsHeightsWorldProperty
Class TerraPrety.LandformHeights.MapLayerLandformsSmooth
Class TerraPrety.LandformHeights.MidpointDistFromPointNoise
Class TerraPrety.LandformHeights.WeightedNormalizedSimplexNoise
Class TerraPrety.ContinentalUpheaval.ContinentalUpheavalHandler
Class TerraPrety.ContinentalUpheaval.ContinentalUpheavalPatches
Class TerraPrety.ContinentalUpheaval.MoreContinentalUpheavalPatches
Class TerraPrety.ContinentalUpheaval.AttemptSmoothingPatch
Class TerraPrety.ContinentalUpheaval.MapLayerContinentalUpheaval
Class <PrivateImplementationDetails>
Class TerraPrety.TerraPretyModSystem.<>O
Class TerraPrety.TerraPretyModSystem.<>c__DisplayClass13_0
Class TerraPrety.Rivers.GenTerraPrety.<>c__DisplayClass35_0
Class TerraPrety.LandformHeights.LandformHeightNoise.<>c__DisplayClass25_0
Class TerraPrety.ContinentalUpheaval.MoreContinentalUpheavalPatches.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
