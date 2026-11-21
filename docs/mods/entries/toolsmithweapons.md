# 武器锻造

Weaponsmith a Toolsmith addon · 模组代码：toolsmithweapons

> 来源：整合包安装包 `Weaponsmith a Toolsmith addon-1.1.7.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `toolsmithweapons` |
| 版本 | 1.1.7 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0, toolsmith 1.2.19 |
| 作者 | MetaCalf |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“身体、战斗与成长”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

This mod adds vanilla weapons to use the same tikering features as tools have in Toolsmith. This mod requires Toolsmith to work since all functionality actually lives in that mod.

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
| 程序集 | 1 | `ToolsmithWeapons.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 0 | — |
| 手册资源 | 0 | — |
| 包内配置数据 | 3 | `assets/toolsmithweapons/config/toolsmith/regex/bluntheadedtools/bluntheadedtools-weapons.json`<br>`assets/toolsmithweapons/config/toolsmith/regex/partblacklist/partblacklist-weapons.json`<br>`assets/toolsmithweapons/config/toolsmith/regex/tinkerabletools/tinkerabletools-weapons.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ToolsmithWeapons.dll**（`3147ebfa1ad2f40c`）：15 个类型。

```text
Class <Module>
Class ToolsmithWeapons.ToolsmithWeaponsModSystem
Class ToolsmithWeapons.Fixes.AssemblyStaleInteractionFixPatch
Class ToolsmithWeapons.Fixes.ProjectileBrokenToolCleanupLogic
Class ToolsmithWeapons.Fixes.TerrainImpactCleanupPatch
Class ToolsmithWeapons.Fixes.EntityImpactCleanupPatch
Class ToolsmithWeapons.Fixes.SpearAssemblyEchoSuppression
Class ToolsmithWeapons.Fixes.SpearStartEchoSuppressionPatch
Class ToolsmithWeapons.Fixes.SpearStopEchoSuppressionPatch
Class ToolsmithWeapons.Fixes.SpearCancelEchoSuppressionPatch
Class ToolsmithWeapons.Fixes.SpearPartBundleRenderPatch
Class ToolsmithWeapons.Fixes.VanillaArmoryFinishedWeaponRenderPatch
Class ToolsmithWeapons.Fixes.WeaponNotAToolHeadPatch
Class ToolsmithWeapons.Fixes.WeaponNotBlacklistedPatch
Class ToolsmithWeapons.Fixes.SpearPartBundleRenderPatch.<>c__DisplayClass3_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
