# 遗传系统依赖库

Genelib · 模组代码：genelib

> 来源：整合包安装包 `Genelib-3.2.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `genelib` |
| 版本 | 3.2.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | sekelsta |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“依赖、兼容与管理工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Calculates genetic inheritance for other mods.

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
| 程序集 | 1 | `Genelib.dll` |
| 方块定义 | 2 | `assets/genelib/blocktypes/nest-ground.json`<br>`assets/genelib/blocktypes/nestbox.json` |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 1 | `assets/genelib/patches/egg.json` |
| 语言资源 | 9 | `assets/genelib/lang/de.json`<br>`assets/genelib/lang/en.json`<br>`assets/genelib/lang/es-419.json`<br>`assets/genelib/lang/es-es.json`<br>`assets/genelib/lang/fr.json`<br>`assets/genelib/lang/pl.json`<br>`assets/genelib/lang/pt-br.json`<br>`assets/genelib/lang/ru.json`<br>`assets/genelib/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Genelib.dll**（`29773f973b482186`）：40 个类型。

```text
Class <Module>
Class Genelib.Array2DAttribute
Class Genelib.ByteArray2DAttribute
Class Genelib.BehaviorAnimalInfo
Class Genelib.GeneticMultiply
Class Genelib.EntityBehaviorGenetics
Class Genelib.AiTaskMate
Class Genelib.GenelibConfig
Class Genelib.GenelibSystem
Class Genelib.DictionaryTextureSource
Class Genelib.GeneInitializer
Class Genelib.Genome
Class Genelib.GenomeType
Class Genelib.ProtoArrayString
Class Genelib.PolygeneInterpreter
Class Genelib.SexDeterminationExtensions
Class Genelib.TextureOverlayInterpreter
Class Genelib.GuiDialogAnimal
Class Genelib.JsonTweakingSystem
Class Genelib.GeneticNest
Class Genelib.ItemGeneticEgg
Class Genelib.Network.GenomeTypesMessage
Class Genelib.Network.SetNameMessage
Class Genelib.Network.SetNoteMessage
Class Genelib.Network.ToggleBreedingMessage
Class Genelib.Extensions.EntityExtensions
Class Genelib.Extensions.ListExtensions
Class Genelib.Extensions.RandomExtensions
Class Genelib.Extensions.VSExtensions
Class Genelib.EntityBehaviorGenetics.<>c__DisplayClass18_0
Class Genelib.EntityBehaviorGenetics.<>c__DisplayClass18_1
Class Genelib.GenelibSystem.<>O
Class Genelib.GenelibSystem.<>c
Class Genelib.Genome.<>c__DisplayClass38_0
Class Genelib.Genome.<>c__DisplayClass40_0
Class Genelib.Genome.<>c__DisplayClass41_0
Class Genelib.Genome.<>c__DisplayClass42_0
Class Genelib.GenomeType.<>c
Class Genelib.NameMapping.<>c
Class Genelib.TextureOverlayInterpreter.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
