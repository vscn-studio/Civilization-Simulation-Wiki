# 采石工艺

Stone Quarry · 模组代码：stonequarryrepckfipil

> 来源：整合包安装包 `Stone Quarry-3.6.3.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `stonequarryrepckfipil` |
| 版本 | 3.6.3 |
| 类型 | 含程序代码 |
| 运行端 | universal |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | 未声明 |
| 作者 | DArkHekRoMaNT |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds stone quarrying mechanics with plug and feather, stone slabs, and rubble storage

</details>

作者提供的链接：https://github.com/DArkHekRoMaNT/StoneQuarry

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `StoneQuarry.dll` |
| 方块定义 | 3 | `assets/stonequarry/blocktypes/plugandfeather.json`<br>`assets/stonequarry/blocktypes/rubblestorage.json`<br>`assets/stonequarry/blocktypes/stoneslab.json` |
| 物品定义 | 6 | `assets/stonequarry/itemtypes/tool/adminhammer.json`<br>`assets/stonequarry/itemtypes/tool/chisel.json`<br>`assets/stonequarry/itemtypes/tool/rubblehammer.json`<br>`assets/stonequarry/itemtypes/toolhead/finishingchiselhead.json`<br>`assets/stonequarry/itemtypes/toolhead/rubblehammerhead.json`<br>`assets/stonequarry/itemtypes/toolhead/wedgechiselhead.json` |
| 实体定义 | 0 | — |
| 配方定义 | 10 | `assets/stonequarry/recipes/clayforming/mold/plugandfeather.json`<br>`assets/stonequarry/recipes/grid/rubblestorage.json`<br>`assets/stonequarry/recipes/grid/tool/finishingchisel.json`<br>`assets/stonequarry/recipes/grid/tool/rubblehammer.json`<br>`assets/stonequarry/recipes/grid/tool/wedgechisel.json`<br>`assets/stonequarry/recipes/smithing/plugandfeather.json`<br>`assets/stonequarry/recipes/smithing/tool/finishingchiselhead.json`<br>`assets/stonequarry/recipes/smithing/tool/roughcutchisel.json`<br>`assets/stonequarry/recipes/smithing/tool/rubblehammerhead.json`<br>`assets/stonequarry/recipes/smithing/tool/wedgechiselhead.json` |
| 资产补丁 | 6 | `assets/stonequarry/patches/config/rubblestorage.json`<br>`assets/stonequarry/patches/miningbagstorable.json`<br>`assets/stonequarry/patches/storageflags.json`<br>`assets/stonequarry/patches/toolmold.json`<br>`assets/stonequarry/patches/tools.json`<br>`assets/stonequarry/patches/usefulstuffrecycling.json` |
| 语言资源 | 15 | `assets/stonequarry/lang/cs.json`<br>`assets/stonequarry/lang/de.json`<br>`assets/stonequarry/lang/en.json`<br>`assets/stonequarry/lang/es-419.json`<br>`assets/stonequarry/lang/es-es.json`<br>`assets/stonequarry/lang/fr.json`<br>`assets/stonequarry/lang/it.json`<br>`assets/stonequarry/lang/ja.json`<br>`assets/stonequarry/lang/ko.json`<br>`assets/stonequarry/lang/pl.json`<br>`assets/stonequarry/lang/pt-br.json`<br>`assets/stonequarry/lang/ru.json`<br>另有 3 个文件 |
| 手册资源 | 3 | `assets/stonequarry/config/handbook/masonguide.json`<br>`assets/stonequarry/config/handbook/quarryguide.json`<br>`assets/stonequarry/config/handbook/rubblestorageguide.json` |
| 包内配置数据 | 1 | `assets/stonequarry/config/rockdata.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**StoneQuarry.dll**（`ca010476db029632`）：54 个类型。

```text
Class <Module>
Class StoneQuarry.BEPlugAndFeather
Class StoneQuarry.BERubbleStorage
Class StoneQuarry.BEStoneSlab
Class StoneQuarry.BlockPlugAndFeather
Class StoneQuarry.BlockRubbleStorage
Class StoneQuarry.BlockStoneSlab
Class StoneQuarry.MultiBlockBase
Class StoneQuarry.Config
Class StoneQuarry.Constants
Class StoneQuarry.SQSounds
Class StoneQuarry.Core
Class StoneQuarry.RubbleStorageInventory
Class StoneQuarry.RubbleStorageItemSlot
Class StoneQuarry.StoneSlabInventory
Class StoneQuarry.ItemRubbleHammer
Class StoneQuarry.PlugPreviewManager
Class StoneQuarry.RockData
Class StoneQuarry.RockManager
Class StoneQuarry.StoneSlabMeshCache
Class StoneQuarry.StoneSlabRenderPreset
Class StoneQuarry.Lib.Utils.WorldUtil
Class StoneQuarry.Lib.Extensions.ArrayExtensions
Class StoneQuarry.Lib.Extensions.InventoryExtensions
Class StoneQuarry.Lib.Extensions.Vec3iExtensions
Class StoneQuarry.Lib.Config.ClientOnlyAttribute
Class StoneQuarry.Lib.Config.ConfigAttribute
Class StoneQuarry.Lib.Config.ConfigIgnoreAttribute
Class StoneQuarry.Lib.Config.ConfigManager
Class StoneQuarry.Lib.Config.ConfigPropertyAttribute
Class StoneQuarry.Lib.Config.ConfigUtil
Class StoneQuarry.Lib.Config.DescriptionAttribute
Class StoneQuarry.Lib.Config.RangeAttribute
Class StoneQuarry.Lib.Config.ValueCheckerAttribute
Class <PrivateImplementationDetails>
Class StoneQuarry.BERubbleStorage.<>c
Class StoneQuarry.BERubbleStorage.<>c__DisplayClass19_0
Class StoneQuarry.BERubbleStorage.<>c__DisplayClass23_0
Class StoneQuarry.BlockRubbleStorage.<>c__DisplayClass9_0
Class StoneQuarry.BlockRubbleStorage.<>c__DisplayClass9_1
```

其余 14 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 10 个配方文件与 3 个手册章节](/reference/recipes/stonequarryrepckfipil)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
