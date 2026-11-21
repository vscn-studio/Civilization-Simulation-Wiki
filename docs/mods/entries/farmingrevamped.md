# 农业改造

FarmingRevamped · 模组代码：farmingrevamped

> 来源：整合包安装包 `FarmingRevamped-2.1.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `farmingrevamped` |
| 版本 | 2.1.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | 未声明 |
| 作者 | 8eiosMpyras |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

A mod to make farming more challenging and realistic.

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
| 程序集 | 1 | `FarmingOverhaul.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 1 | `assets/farmingoverhaul/recipes/grid/seed.json` |
| 资产补丁 | 21 | `assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-amaranth.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-cabbage.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-carrot.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-cassava.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-fennel.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-flax.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-licorice.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-onion.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-parsnip.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-peanut.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-pineapple.json`<br>`assets/farmingoverhaul/patches/survival-blocktypes-plant-crop-rice.json`<br>另有 9 个文件 |
| 语言资源 | 1 | `assets/farmingoverhaul/lang/en.json` |
| 手册资源 | 1 | `assets/farmingoverhaul/config/handbook/FarmingRevampedGuide.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**FarmingOverhaul.dll**（`598598ba9027049d`）：14 个类型。

```text
Class <Module>
Class FarmingOverhaul.SoilNoTime
Class FarmingOverhaul.NutrientYieldSystem
Class FarmingOverhaul.NutrientYieldModSystem
Class FarmingOverhaul.PatchClampMoistureField
Class FarmingOverhaul.PatchClampMoistureFieldOverload
Class FarmingOverhaul.PatchClampMoistureFieldHelper
Class FarmingOverhaul.PatchSwapMoistureFromWaterAndRain
Class FarmingOverhaul.SoilNoTimeModSystem
Class FarmingOverhaul.PatchGetGrowthRate
Class FarmingOverhaul.Patches.MoistureDamage
Class FarmingOverhaul.NutrientYieldModSystem.PatchCropGrowth
Class FarmingOverhaul.NutrientYieldModSystem.PatchFarmlandHarvest
Class FarmingOverhaul.Patches.MoistureDamage.<>c__DisplayClass2_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 1 个配方文件与 1 个手册章节](/reference/recipes/farmingrevamped)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
