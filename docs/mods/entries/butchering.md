# 屠宰与肉类加工

Butchering · 模组代码：butchering

> 来源：整合包安装包 `Butchering-1.14.3.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `butchering` |
| 版本 | 1.14.3 |
| 类型 | 含程序代码 |
| 运行端 | universal |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | G3rste, CaptainOats |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Carry animals back to your place for proper butchering.

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
| 程序集 | 1 | `Butchering.dll` |
| 方块定义 | 6 | `assets/butchering/blocktypes/butcherhook.json`<br>`assets/butchering/blocktypes/butcherhookceiling.json`<br>`assets/butchering/blocktypes/butchertable.json`<br>`assets/butchering/blocktypes/resource/ivoryblock.json`<br>`assets/butchering/blocktypes/smokingrack.json`<br>`assets/butchering/blocktypes/temporalbutcherbox.json` |
| 物品定义 | 69 | `assets/butchering/itemtypes/butchercreatures/bear.json`<br>`assets/butchering/itemtypes/butchercreatures/bovinae/bovinae.json`<br>`assets/butchering/itemtypes/butchercreatures/caninae/caninae.json`<br>`assets/butchering/itemtypes/butchercreatures/capreolinae/alceini.json`<br>`assets/butchering/itemtypes/butchercreatures/capreolinae/capreolini.json`<br>`assets/butchering/itemtypes/butchercreatures/capreolinae/odocoileini.json`<br>`assets/butchering/itemtypes/butchercreatures/casuariidae/casuariidae.json`<br>`assets/butchering/itemtypes/butchercreatures/casuariidae/cereopsisnovaehollandiae.json`<br>`assets/butchering/itemtypes/butchercreatures/casuariidae/dromornithidae.json`<br>`assets/butchering/itemtypes/butchercreatures/casuariidae/rallidae.json`<br>`assets/butchering/itemtypes/butchercreatures/cervinae/cervini.json`<br>`assets/butchering/itemtypes/butchercreatures/chicken.json`<br>另有 57 个文件 |
| 实体定义 | 1 | `assets/butchering/entities/arrow.json` |
| 配方定义 | 33 | `assets/butchering/recipes/barrel/cleanoffal.json`<br>`assets/butchering/recipes/barrel/curedhealingprimemeat.json`<br>`assets/butchering/recipes/cooking/fatrender.json`<br>`assets/butchering/recipes/cooking/glue.json`<br>`assets/butchering/recipes/grid/blackpudding.json`<br>`assets/butchering/recipes/grid/bloodbait.json`<br>`assets/butchering/recipes/grid/blooddough.json`<br>`assets/butchering/recipes/grid/bloodsausage.json`<br>`assets/butchering/recipes/grid/bone.json`<br>`assets/butchering/recipes/grid/boneneedle.json`<br>`assets/butchering/recipes/grid/bonetools.json`<br>`assets/butchering/recipes/grid/butcherhook.json`<br>另有 21 个文件 |
| 资产补丁 | 55 | `assets/butchering/patches/blocktypes/trough-large.json`<br>`assets/butchering/patches/compatibility/caninae/canina.json`<br>`assets/butchering/patches/compatibility/caninae/cerdocyonina.json`<br>`assets/butchering/patches/compatibility/caninae/urocyonini.json`<br>`assets/butchering/patches/compatibility/caninae/vulpini.json`<br>`assets/butchering/patches/compatibility/capreolinae/alceini.json`<br>`assets/butchering/patches/compatibility/capreolinae/capreolini.json`<br>`assets/butchering/patches/compatibility/capreolinae/odocoileini.json`<br>`assets/butchering/patches/compatibility/combatoverhaul/arrow.json`<br>`assets/butchering/patches/compatibility/equusferus/equusferus.json`<br>`assets/butchering/patches/compatibility/equushorses/equushorse.json`<br>`assets/butchering/patches/compatibility/expandedfoods/dough.json`<br>另有 43 个文件 |
| 语言资源 | 15 | `assets/butchering/lang/cs.json`<br>`assets/butchering/lang/de.json`<br>`assets/butchering/lang/en.json`<br>`assets/butchering/lang/eo.json`<br>`assets/butchering/lang/es-419.json`<br>`assets/butchering/lang/es-es.json`<br>`assets/butchering/lang/fr.json`<br>`assets/butchering/lang/it.json`<br>`assets/butchering/lang/ja.json`<br>`assets/butchering/lang/ko.json`<br>`assets/butchering/lang/pl.json`<br>`assets/butchering/lang/pt-br.json`<br>另有 3 个文件 |
| 手册资源 | 2 | `assets/butchering/config/handbook/01_butcheringguide.json`<br>`assets/butchering/config/handbook/02_butcheringinfo.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Butchering.dll**（`db5a4ae6efdd85b1`）：35 个类型。

```text
Class <Module>
Class Butchering.src.system.BMReferences
Class Butchering.src.system.ButcheringSystem
Class Butchering.src.system.ButcheringConfig
Class Butchering.src.system.HarvestablePatch
Class Butchering.src.system.XSkillsCompatibilitySystem
Class Butchering.src.common.item.ItemButcherable
Class Butchering.src.common.entitybehavior.EntityBehaviorButcherable
Class Butchering.src.common.entitybehavior.EntityBehaviorButcheringStats
Class Butchering.src.common.block.BlockButcherHook
Class Butchering.src.common.block.BlockButcherTable
Class Butchering.src.common.block.BlockButcherWorkstation
Class Butchering.src.common.block.BlockMeatHook
Class Butchering.src.common.blockentity.BlockEntityButcherHook
Class Butchering.src.common.blockentity.BlockEntityButcherTable
Class Butchering.src.common.blockentity.BlockEntityButcherWorkstation
Class Butchering.src.common.blockentity.BlockEntityMeatHook
Class butchering.src.Client.GuiComposerHelpers
Class butchering.src.Client.GuiDialogTemporalButcherBox
Class butchering.src.Client.GuiElementImage
Class <PrivateImplementationDetails>
Class Butchering.src.system.ButcheringSystem.<>c__DisplayClass11_0
Class Butchering.src.system.ButcheringSystem.<>c__DisplayClass13_0
Class Butchering.src.common.block.BlockButcherTable.<>c
Class Butchering.src.common.block.BlockButcherWorkstation.<>c
Class Butchering.src.common.block.BlockMeatHook.<>c
Class Butchering.src.common.blockentity.BlockEntityButcherHook.<>c__DisplayClass13_0
Class Butchering.src.common.blockentity.BlockEntityButcherHook.<>c__DisplayClass13_1
Class Butchering.src.common.blockentity.BlockEntityButcherHook.<>c__DisplayClass13_2
Class Butchering.src.common.blockentity.BlockEntityButcherTable.<>c__DisplayClass4_0
Class Butchering.src.common.blockentity.BlockEntityButcherTable.<>c__DisplayClass4_1
Class Butchering.src.common.blockentity.BlockEntityButcherTable.<>c__DisplayClass4_2
Class Butchering.src.common.blockentity.BlockEntityButcherWorkstation.<>c
Class Butchering.src.common.blockentity.BlockEntityButcherWorkstation.<>c__DisplayClass28_0
Class Butchering.src.common.blockentity.BlockEntityMeatHook.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 33 个配方文件与 2 个手册章节](/reference/recipes/butchering)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
