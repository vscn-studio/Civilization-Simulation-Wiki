# 盐田

Fields of Salt · 模组代码：fieldsofsalt

> 来源：整合包安装包 `Fields of Salt-1.2.5.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `fieldsofsalt` |
| 版本 | 1.2.5 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Xytabich |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds ponds to evaporate seawater and produce salt

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
| 程序集 | 1 | `fieldsofsalt.dll` |
| 方块定义 | 5 | `assets/fieldsofsalt/blocktypes/channel.json`<br>`assets/fieldsofsalt/blocktypes/connector.json`<br>`assets/fieldsofsalt/blocktypes/pondmain.json`<br>`assets/fieldsofsalt/blocktypes/source.json`<br>`assets/fieldsofsalt/blocktypes/surrogate.json` |
| 物品定义 | 1 | `assets/fieldsofsalt/itemtypes/pondtemplate.json` |
| 实体定义 | 0 | — |
| 配方定义 | 5 | `assets/fieldsofsalt/recipes/evaporationpond/salt.json`<br>`assets/fieldsofsalt/recipes/grid/channel.json`<br>`assets/fieldsofsalt/recipes/grid/connector.json`<br>`assets/fieldsofsalt/recipes/grid/pondtemplate.json`<br>`assets/fieldsofsalt/recipes/grid/source.json` |
| 资产补丁 | 0 | — |
| 语言资源 | 4 | `assets/fieldsofsalt/lang/en.json`<br>`assets/fieldsofsalt/lang/fr.json`<br>`assets/fieldsofsalt/lang/ja.json`<br>`assets/fieldsofsalt/lang/pt-br.json` |
| 手册资源 | 1 | `assets/fieldsofsalt/config/handbook/evaporation.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**fieldsofsalt.dll**（`5065a923dd9f243c`）：37 个类型。

```text
Class <Module>
Class FieldsOfSalt.FieldsOfSaltMod
Class FieldsOfSalt.HandbookItemInfoEvent
Class FieldsOfSalt.HandbookItemInfoPatch
Class FieldsOfSalt.Utils.BitPackUtil
Class FieldsOfSalt.Utils.BlockPosExt
Class FieldsOfSalt.Utils.GraphicUtil
Class FieldsOfSalt.Utils.ModConfig
Class FieldsOfSalt.Utils.SerializationUtils
Class FieldsOfSalt.Utils.TreeAttributeUtils
Class FieldsOfSalt.Renderer.TemplateAreaRenderer
Class FieldsOfSalt.Recipes.EvaporationRecipe
Class FieldsOfSalt.Recipes.LiquidIngredient
Class FieldsOfSalt.Multiblock.BlockMultiblockMain
Class FieldsOfSalt.Multiblock.BlockMultiblockSurrogate
Class FieldsOfSalt.Multiblock.MultiblockManager
Class FieldsOfSalt.Items.ItemPondTemplate
Class FieldsOfSalt.Handbook.EvaporationInfo
Class FieldsOfSalt.Blocks.BlockChannel
Class FieldsOfSalt.Blocks.BlockConnector
Class FieldsOfSalt.Blocks.BlockPond
Class FieldsOfSalt.Blocks.BlockRenderSurrogate
Class FieldsOfSalt.Blocks.BlockSource
Class FieldsOfSalt.Blocks.Entities.BlockEntityPond
Class FieldsOfSalt.Blocks.Entities.BlockEntitySource
Class FieldsOfSalt.HandbookItemInfoPatch.<>c
Class FieldsOfSalt.Utils.GraphicUtil.<>c__DisplayClass11_0
Class FieldsOfSalt.Items.ItemPondTemplate.TemplateInfo
Class FieldsOfSalt.Items.ItemPondTemplate.MultiblockInfo
Class FieldsOfSalt.Items.ItemPondTemplate.<>c__DisplayClass11_0
Class FieldsOfSalt.Handbook.EvaporationInfo.<>c__DisplayClass4_0
Class FieldsOfSalt.Blocks.BlockChannel.<>c__DisplayClass6_0
Class FieldsOfSalt.Blocks.Entities.BlockEntityPond.<>c
Class FieldsOfSalt.Blocks.Entities.BlockEntityPond.<>c__DisplayClass55_0
Class FieldsOfSalt.Blocks.Entities.BlockEntityPond.<>c__DisplayClass57_0
Class FieldsOfSalt.Blocks.Entities.BlockEntitySource.LiquidGraphicProps
Class FieldsOfSalt.Items.ItemPondTemplate.TemplateInfo.BlockTemplate
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 5 个配方文件与 1 个手册章节](/reference/recipes/fieldsofsalt)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
