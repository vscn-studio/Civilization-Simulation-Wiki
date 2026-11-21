# 火箭矢

VSCN Fire Arrows · 模组代码：vscnfirearrows

> 来源：整合包安装包 `VSCN Fire Arrows-1.0.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vscnfirearrows` |
| 版本 | 1.0.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0, survival 1.22.0 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“身体、战斗与成长”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Fire arrow recipes, torch ignition and weather-sensitive single-use burning for vanilla and modded arrows.

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
| 程序集 | 1 | `VscnFireArrows.dll` |
| 方块定义 | 1 | `assets/vscnfirearrows/blocktypes/arrowfire.json` |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/vscnfirearrows/lang/en.json`<br>`assets/vscnfirearrows/lang/zh-cn.json` |
| 手册资源 | 1 | `assets/vscnfirearrows/config/handbook/firearrows.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**VscnFireArrows.dll**（`c6f6b3b553c4fd8d`）：38 个类型。

```text
Class <Module>
Class Vscn.FireArrows.ArrowBurning
Class Vscn.FireArrows.ArrowFuelDurationPatch
Class Vscn.FireArrows.ArrowCanBurnPatch
Class Vscn.FireArrows.FireArrowsSystem
Class Vscn.FireArrows.FireCatalog
Class Vscn.FireArrows.FireConfig
Class Vscn.FireArrows.BurnRules
Class Vscn.FireArrows.FireEntityBehavior
Class Vscn.FireArrows.FireEnvironment
Class Vscn.FireArrows.FireMaterials
Class Vscn.FireArrows.FireRecipes
Class Vscn.FireArrows.FireState
Class Vscn.FireArrows.FireVisuals
Class Vscn.FireArrows.HeldArrowFirePatch
Class Vscn.FireArrows.EntityInitializePatch
Class Vscn.FireArrows.FireNamePatch
Class Vscn.FireArrows.FireInfoPatch
Class Vscn.FireArrows.SpentArrowRenderPatch
Class Vscn.FireArrows.FireStackEqualityPatch
Class Vscn.FireArrows.FireStackMergePatch
Class Vscn.FireArrows.FireHandbookPagePatch
Class Vscn.FireArrows.BetterHandbookFireGroupingPatch
Class Vscn.FireArrows.BurningAmmoPatch
Class Vscn.FireArrows.FireDamagePatch
Class Vscn.FireArrows.ArrowBurning.<>c__DisplayClass1_0
Class Vscn.FireArrows.FireCatalog.<>c
Class Vscn.FireArrows.FireEnvironment.<>c
Class Vscn.FireArrows.FireEnvironment.<>c__DisplayClass6_0
Class Vscn.FireArrows.FireEnvironment.<>c__DisplayClass8_0
Class Vscn.FireArrows.FireRecipes.<>c
Class Vscn.FireArrows.FireState.<>c
Class Vscn.FireArrows.FireVisuals.<>c
Class Vscn.FireArrows.HeldArrowFirePatch.Emission
Class Vscn.FireArrows.HeldArrowFirePatch.<>c
Class Vscn.FireArrows.EntityInitializePatch.<TargetMethods>d__0
Class Vscn.FireArrows.FireInfoPatch.<TargetMethods>d__0
Class Vscn.FireArrows.BurningAmmoPatch.<>c__DisplayClass0_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 0 个配方文件与 1 个手册章节](/reference/recipes/vscnfirearrows)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
