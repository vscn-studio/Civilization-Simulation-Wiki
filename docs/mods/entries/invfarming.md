# 无脊椎动物养殖

Involved Farming · 模组代码：invfarming

> 来源：整合包安装包 `Involved Farming-1.0.7.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `invfarming` |
| 版本 | 1.0.7 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | Kappir |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds fallow farmland state to the game!

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
| 程序集 | 1 | `invfarming.dll` |
| 方块定义 | 1 | `assets/invfarming/blocktypes/fallow.json` |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 15 | `assets/invfarming/patches/FallowPlacerAoG.json`<br>`assets/invfarming/patches/FallowPlacerAoGBA.json`<br>`assets/invfarming/patches/FallowPlacerBiodiversityCrops.json`<br>`assets/invfarming/patches/FallowPlacerBiodiversityHerbs.json`<br>`assets/invfarming/patches/FallowPlacerBrazil.json`<br>`assets/invfarming/patches/FallowPlacerCropsV2.json`<br>`assets/invfarming/patches/FallowPlacerDebeReBullshit.json`<br>`assets/invfarming/patches/FallowPlacerDruuuuuugs.json`<br>`assets/invfarming/patches/FallowPlacerFloralZones.json`<br>`assets/invfarming/patches/FallowPlacerLongTermFood.json`<br>`assets/invfarming/patches/FallowPlacerNewWorld.json`<br>`assets/invfarming/patches/FallowPlacerSeafarer.json`<br>另有 3 个文件 |
| 语言资源 | 1 | `assets/invfarming/lang/en.json` |
| 手册资源 | 1 | `assets/invfarming/config/handbook/farming-fallow.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**invfarming.dll**（`861bdc573df9dd3c`）：7 个类型。

```text
Class <Module>
Class invfarming.Patches.SafeRemoveFallow
Class invfarming.Fallowing.BEFallow
Class invfarming.Fallowing.FallowPilePlacer
Class invfarming.Fallowing.FallowPlacer
Class InvolvedFarming.InvolvedFarmingModSystem
Class invfarming.Patches.SafeRemoveFallow.RemoveFallow
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 0 个配方文件与 1 个手册章节](/reference/recipes/invfarming)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
