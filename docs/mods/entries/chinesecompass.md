# 司南与罗盘

Chinese Compass — Sinan and Mariner's Compass · 模组代码：chinesecompass

> 来源：整合包安装包 `Chinese Compass — Sinan and Mariner's Compass-1.0.9.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `chinesecompass` |
| 版本 | 1.0.9 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Sinan and a wooden Chinese mariner's compass with a 24-mountain dial.

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
| 程序集 | 1 | `ChineseCompass.dll` |
| 方块定义 | 6 | `assets/chinesecompass/blocktypes/legacy-sinan-mold-fired.json`<br>`assets/chinesecompass/blocktypes/legacy-sinan-mold-raw.json`<br>`assets/chinesecompass/blocktypes/marinerscompass.json`<br>`assets/chinesecompass/blocktypes/sinan-mold-fired.json`<br>`assets/chinesecompass/blocktypes/sinan-mold-raw.json`<br>`assets/chinesecompass/blocktypes/sinan.json` |
| 物品定义 | 7 | `assets/chinesecompass/itemtypes/magnetic-needle.json`<br>`assets/chinesecompass/itemtypes/quartz-cover.json`<br>`assets/chinesecompass/itemtypes/sinan-blank-copper.json`<br>`assets/chinesecompass/itemtypes/sinan-blank-tinbronze.json`<br>`assets/chinesecompass/itemtypes/sinan-plate-copper.json`<br>`assets/chinesecompass/itemtypes/sinan-plate-tinbronze.json`<br>`assets/chinesecompass/itemtypes/sinan-spoon-magnetite.json` |
| 实体定义 | 0 | — |
| 配方定义 | 7 | `assets/chinesecompass/recipes/clayforming/sinan-mold.json`<br>`assets/chinesecompass/recipes/grid/compass-cover.json`<br>`assets/chinesecompass/recipes/grid/marinerscompass.json`<br>`assets/chinesecompass/recipes/grid/quartz-cover.json`<br>`assets/chinesecompass/recipes/grid/sinan-engrave.json`<br>`assets/chinesecompass/recipes/grid/sinan-spoon.json`<br>`assets/chinesecompass/recipes/grid/sinan.json` |
| 资产补丁 | 1 | `assets/chinesecompass/patches/panning-drops.json` |
| 语言资源 | 2 | `assets/chinesecompass/lang/en.json`<br>`assets/chinesecompass/lang/zh-cn.json` |
| 手册资源 | 1 | `assets/chinesecompass/config/handbook/chinesecompass.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ChineseCompass.dll**（`8af081b48ab3b50a`）：22 个类型。

```text
Class <Module>
Class ChineseCompass.CompassEnvironment
Class ChineseCompass.WindSample
Class ChineseCompass.CompassHudLayout
Class ChineseCompass.CompassHudRenderer
Class ChineseCompass.CompassMath
Class ChineseCompass.HandNeedleState
Class ChineseCompass.HeldCompassMeshes
Class ChineseCompass.RubbingSession
Class ChineseCompass.MagnetiteRubbing
Class ChineseCompass.RubbingFeedback
Class ChineseCompass.CompassModSystem
Class ChineseCompass.ItemQuartzCover
Class ChineseCompass.BlockMarinersCompass
Class ChineseCompass.BlockSinan
Class ChineseCompass.NeedleMotion
Class ChineseCompass.BEMarinersCompass
Class ChineseCompass.NeedleRenderer
Class ChineseCompass.TribeCenterNavigation
Class ChineseCompass.MagnetiteRubbing.<>c__DisplayClass6_0
Class ChineseCompass.CompassModSystem.CompassConfig
Class ChineseCompass.CompassModSystem.<>c__DisplayClass7_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 7 个配方文件与 1 个手册章节](/reference/recipes/chinesecompass)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
