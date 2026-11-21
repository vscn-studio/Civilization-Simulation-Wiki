# 石砌烤炉

Stone Bake Oven · 模组代码：stonebakeoven

> 来源：整合包安装包 `Stone Bake Oven-1.4.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `stonebakeoven` |
| 版本 | 1.4.0 |
| 类型 | 含程序代码 |
| 运行端 | universal |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | Captain Oats, G3rste |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Creates a usable large stone oven for baking and more.

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
| 程序集 | 1 | `stonebakeoven.dll` |
| 方块定义 | 15 | `assets/stonebakeoven/blocktypes/ovenbakingtopbrick.json`<br>`assets/stonebakeoven/blocktypes/ovenbakingtopcobble.json`<br>`assets/stonebakeoven/blocktypes/ovenbakingtopplain.json`<br>`assets/stonebakeoven/blocktypes/ovencontrollerbrick.json`<br>`assets/stonebakeoven/blocktypes/ovencontrollercobble.json`<br>`assets/stonebakeoven/blocktypes/ovencontrollerplain.json`<br>`assets/stonebakeoven/blocktypes/ovencookingtopbrick.json`<br>`assets/stonebakeoven/blocktypes/ovencookingtopcobble.json`<br>`assets/stonebakeoven/blocktypes/ovencookingtopplain.json`<br>`assets/stonebakeoven/blocktypes/ovengrillbrick.json`<br>`assets/stonebakeoven/blocktypes/ovengrillbrickextra.json`<br>`assets/stonebakeoven/blocktypes/ovengrillcobble.json`<br>另有 3 个文件 |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 3 | `assets/stonebakeoven/recipes/grid/brick.json`<br>`assets/stonebakeoven/recipes/grid/cobble.json`<br>`assets/stonebakeoven/recipes/grid/plain.json` |
| 资产补丁 | 1 | `assets/stonebakeoven/patches/compatibility/realsmoke/realsmoke.json` |
| 语言资源 | 6 | `assets/stonebakeoven/lang/de.json`<br>`assets/stonebakeoven/lang/en.json`<br>`assets/stonebakeoven/lang/ja.json`<br>`assets/stonebakeoven/lang/pt-br.json`<br>`assets/stonebakeoven/lang/ru.json`<br>`assets/stonebakeoven/lang/uk.json` |
| 手册资源 | 1 | `assets/stonebakeoven/config/handbook/stone-bake-oven.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**stonebakeoven.dll**（`16903f1ef97b8b03`）：17 个类型。

```text
Class <Module>
Class StoneBakeOven.CookingTopPotRenderer
Class StoneBakeOven.GenericBlockInCookingTopRenderer
Class StoneBakeOven.GuiDialogBlockEntityCookingTop
Class StoneBakeOven.BlockEntityOvenBakingTop
Class StoneBakeOven.BlockEntityOvenController
Class StoneBakeOven.BlockEntityOvenCookingTop
Class StoneBakeOven.BlockEntityOvenGrill
Class StoneBakeOven.BlockOvenBakingTop
Class StoneBakeOven.BlockOvenController
Class StoneBakeOven.BlockOvenCookingTop
Class StoneBakeOven.ItemSlotCookingInput
Class StoneBakeOven.ItemSlotCookingOutput
Class StoneBakeOven.ItemSlotCookingIngredient
Class StoneBakeOven.ItemSlotUnused
Class StoneBakeOven.InventoryCookingTop
Class StoneBakeOven.OatsOven
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 3 个配方文件与 1 个手册章节](/reference/recipes/stonebakeoven)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
