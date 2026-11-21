# 锻造改进

SmithingPlus · 模组代码：smithingplusplus

> 来源：整合包安装包 `SmithingPlus-1.10.7.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `smithingplusplus` |
| 版本 | 1.10.7 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | jayu, theysa |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Metal tool repair, smithing tweaks and quality of life improvements. Bug and performance fork

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
| 程序集 | 1 | `SmithingPlus.dll` |
| 方块定义 | 1 | `assets/smithingplus/blocktypes/stoneanvil.json` |
| 物品定义 | 2 | `assets/smithingplus/itemtypes/forlonblade.json`<br>`assets/smithingplus/itemtypes/stonehammer.json` |
| 实体定义 | 0 | — |
| 配方定义 | 9 | `assets/smithingplus/compatibility/alchemy/recipes/smithing/smithingplus/1hook.json`<br>`assets/smithingplus/compatibility/butchering/recipes/smithing/smithingplus/1hook.json`<br>`assets/smithingplus/recipes/grid/chiselworkitem.json`<br>`assets/smithingplus/recipes/grid/forlornestoc.json`<br>`assets/smithingplus/recipes/smithing/bits/1arrowhead.json`<br>`assets/smithingplus/recipes/smithing/bits/3arrowhead.json`<br>`assets/smithingplus/recipes/smithing/bits/nails.json`<br>`assets/smithingplus/recipes/smithing/forlornblade.json`<br>`assets/smithingplus/recipes/smithing/ingot.json` |
| 资产补丁 | 5 | `assets/smithingplus/patches/compatibility/rustboundmagic/rod.json`<br>`assets/smithingplus/patches/compatibility/xskills-metalbit.json`<br>`assets/smithingplus/patches/forlornestocrepair.json`<br>`assets/smithingplus/patches/metalbit.json`<br>`assets/smithingplus/patches/rod.json` |
| 语言资源 | 13 | `assets/game/lang/be.json`<br>`assets/game/lang/en.json`<br>`assets/game/lang/it.json`<br>`assets/game/lang/pl.json`<br>`assets/game/lang/ru.json`<br>`assets/game/lang/zh-cn.json`<br>`assets/smithingplus/compatibility/rustboundmagic/lang/en.json`<br>`assets/smithingplus/lang/be.json`<br>`assets/smithingplus/lang/en.json`<br>`assets/smithingplus/lang/it.json`<br>`assets/smithingplus/lang/pl.json`<br>`assets/smithingplus/lang/ru.json`<br>另有 1 个文件 |
| 手册资源 | 1 | `assets/smithingplus/config/handbook/smithingplusguide.json` |
| 包内配置数据 | 2 | `assets/smithingplus/config/configlib-patches.json`<br>`assets/smithingplus/config/traits.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**SmithingPlus.dll**（`f7e6aedac21f5053`）：137 个类型。

```text
Class <Module>
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F2ABA42597B6A052A0EBE3671CF289745B2ADBFCDD1F0BCD00781B1A37CD25EBE__TemperatureValueRegex_0
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F2ABA42597B6A052A0EBE3671CF289745B2ADBFCDD1F0BCD00781B1A37CD25EBE__TemperatureRangeRegex_1
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F2ABA42597B6A052A0EBE3671CF289745B2ADBFCDD1F0BCD00781B1A37CD25EBE__Utilities
Class SmithingPlus.Core
Class SmithingPlus.PatchExtensions
Class SmithingPlus.Util.ApiExtensions
Class SmithingPlus.Util.CacheHelper
Class SmithingPlus.Util.CollectibleExtensions
Class SmithingPlus.Util.Constants
Class SmithingPlus.Util.ModStackAttributes
Class SmithingPlus.Util.ModAttributes
Class SmithingPlus.Util.ModRecipeAttributes
Class SmithingPlus.Util.ModStats
Class SmithingPlus.Util.HammerExtensions
Class SmithingPlus.Util.ItemExtensions
Class SmithingPlus.Util.ItemStackExtensions
Class SmithingPlus.Util.ReflectionExtensions
Class SmithingPlus.Util.SmithingRecipeLookups
Class SmithingPlus.Util.TreeAttributeExtensions
Class SmithingPlus.Util.VoxelExtensions
Class SmithingPlus.ToolRecovery.CollectibleBehaviorBrokenToolHead
Class SmithingPlus.ToolRecovery.CollectibleBehaviorRepairableTool
Class SmithingPlus.ToolRecovery.CollectibleBehaviorRepairableToolHead
Class SmithingPlus.ToolRecovery.RecyclableArrowBehavior
Class SmithingPlus.ToolRecovery.ItemDamagedPatches
Class SmithingPlus.ToolRecovery.ItemDestroyedPatches
Class SmithingPlus.ToolRecovery.ItemWorkItemPatches
Class SmithingPlus.ToolRecovery.ToolHeadRepairPatches
Class SmithingPlus.Test.AnvilActionTrace
Class SmithingPlus.Test.TestCommands
Class SmithingPlus.StoneSmithing.AnvilHitDisplayPatch
Class SmithingPlus.StoneSmithing.AnvilPartHitDisplayPatch
Class SmithingPlus.StoneSmithing.BlockEntityStoneAnvil
Class SmithingPlus.StoneSmithing.ItemStoneHammer
Class SmithingPlus.StoneSmithing.XHammer
Class SmithingPlus.StoneSmithing.RegenMeshPostfixPatch
Class SmithingPlus.SmithWithBits.CollectibleBehaviorWorkableNugget
Class SmithingPlus.SmithWithBits.SmithingRecipeAttributesPatch
Class SmithingPlus.SkillfulSmithing.SkillfulSmithingPatches
```

其余 97 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 9 个配方文件与 1 个手册章节](/reference/recipes/smithingplusplus)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
