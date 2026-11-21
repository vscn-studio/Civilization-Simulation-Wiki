# 屋顶建造

VS Roofing Mod · 模组代码：vsroofing

> 来源：整合包安装包 `VS Roofing Mod-2.1.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vsroofing` |
| 版本 | 2.1.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | tui_smuggler |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Gridless roof crafting/building system with dynamic slopes and corners.

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
| 程序集 | 1 | `vsroofing.dll` |
| 方块定义 | 1 | `assets/vsroofing/blocktypes/roof.json` |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 21 | `assets/vsroofing/compatibility/bdtree/patches/roof.json`<br>`assets/vsroofing/compatibility/bricklayers/patches/roof.json`<br>`assets/vsroofing/compatibility/btrofuels/patches/bamboo.json`<br>`assets/vsroofing/compatibility/chiseltools/patches/items.json`<br>`assets/vsroofing/compatibility/clayworks/patches/roof.json`<br>`assets/vsroofing/compatibility/conquest/patches/roof.json`<br>`assets/vsroofing/compatibility/floralzonescaperegion/patches/roof.json`<br>`assets/vsroofing/compatibility/floralzonescaribbeanregion/patches/roof.json`<br>`assets/vsroofing/compatibility/floralzonescentralaustralianregion/patches/roof.json`<br>`assets/vsroofing/compatibility/floralzonescircumborealregion/patches/roof.json`<br>`assets/vsroofing/compatibility/floralzonesmediterraneanregion/patches/roof.json`<br>`assets/vsroofing/compatibility/floralzonesneozeylandicregion/patches/roof.json`<br>另有 9 个文件 |
| 语言资源 | 3 | `assets/vsroofing/lang/en.json`<br>`assets/vsroofing/lang/ru.json`<br>`assets/vsroofing/lang/uk.json` |
| 手册资源 | 2 | `assets/vsroofing/config/handbook/00-craftinginfo-guide.json`<br>`assets/vsroofing/config/handbook/01-craftinginfo-recipes.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**vsroofing.dll**（`7c350af951f20794`）：48 个类型。

```text
Class <Module>
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F989215DD7CBBD322B25CEA69ABC2E27D933D7F91BC0F9EF78AC2D1D35A21388F__VariantRegex_0
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F989215DD7CBBD322B25CEA69ABC2E27D933D7F91BC0F9EF78AC2D1D35A21388F__Utilities
Class VSRoofing.CollectibleBehaviorOffhand
Class VSRoofing.CollectibleBehaviorPlaceFrame
Class VSRoofing.CollectibleBehaviorRoofChisel
Class VSRoofing.Beam
Class VSRoofing.AutoRoofMaterialCollection
Class VSRoofing.AutoRoofData
Class VSRoofing.AutoRoofEntityChiseled
Class VSRoofing.AutoRoofEntity
Class VSRoofing.AutoRoofSlopeResolver
Class VSRoofing.AutoRoofBlockBrokenParticleProps
Class VSRoofing.AutoRoofMaterialInfo
Class VSRoofing.AutoRoofOffhandInfo
Class VSRoofing.AutoRoofMaterialInfoCollection
Class VSRoofing.AutoRoofSlope
Class VSRoofing.AutoRoofShape
Class VSRoofing.AutoRoofMaterialTexture
Class VSRoofing.AutoRoofFrame
Class VSRoofing.AutoRoofMaterialVariantTexture
Class VSRoofing.AutoRoofVariant
Class VSRoofing.AutoFence
Class VSRoofing.RoofBlock
Class VSRoofing.PatchedItemFirewood
Class VSRoofing.AutoRoofBeamHighlightRenderer
Class VSRoofing.CompositeTextureUtil
Class VSRoofing.MaterialsTextureSource
Class VSRoofing.FrameTextureSource
Class VSRoofing.Utils
Class VSRoofing.JsonObjectExtensions
Class VSRoofing.JsonObjectConverter
Class VSRoofing.ConfigData
Class VSRoofing.FramePlacementCheck
Class VSRoofing.VSRoofingModSystem
Class <PrivateImplementationDetails>
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F989215DD7CBBD322B25CEA69ABC2E27D933D7F91BC0F9EF78AC2D1D35A21388F__VariantRegex_0.RunnerFactory
Class VSRoofing.CollectibleBehaviorPlaceFrame.<>c__DisplayClass11_0
Class VSRoofing.CollectibleBehaviorPlaceFrame.<>c__DisplayClass14_0
Class VSRoofing.AutoRoofData.<>c__DisplayClass175_0
```

其余 8 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 0 个配方文件与 2 个手册章节](/reference/recipes/vsroofing)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
