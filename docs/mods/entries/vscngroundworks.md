# 地面施工

Ground Works · 模组代码：vscngroundworks

> 来源：整合包安装包 `Ground Works-1.0.4.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vscngroundworks` |
| 版本 | 1.0.4 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.3, survival 1.22.3 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Build paths and work the ground in place: compact soil with a shovel, loosen soil and reshape stone paths with a hoe, polish rock with a hammer and chisel, and saw planks into wooden paths using existing recipes. Native animations, sounds, and progress bars. No new items or recipes.

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
| 程序集 | 1 | `VscnGroundWorks.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/vscngroundworks/lang/en.json`<br>`assets/vscngroundworks/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**VscnGroundWorks.dll**（`2c5968f4eec6cbb6`）：36 个类型。

```text
Class <Module>
Class <>z__ReadOnlySingleElementList
Class VscnGroundWorks.ChiselWorkModePacket
Class VscnGroundWorks.ChiselSettings
Class VscnGroundWorks.ChiselWizCompat
Class VscnGroundWorks.GroundWorksSystem
Class VscnGroundWorks.RammedTypeDialog
Class VscnGroundWorks.RammedTypePacket
Class VscnGroundWorks.RammedTypes
Class VscnGroundWorks.RecipeWork
Class VscnGroundWorks.RoadTypes
Class VscnGroundWorks.ToolModes
Class VscnGroundWorks.WorkActions
Class VscnGroundWorks.WorkConfig
Class VscnGroundWorks.WorkDiagnostics
Class VscnGroundWorks.WorkPatches
Class VscnGroundWorks.WorkPlan
Class VscnGroundWorks.WorkSounds
Class <PrivateImplementationDetails>
Class <>z__ReadOnlySingleElementList.Enumerator
Class VscnGroundWorks.ChiselWizCompat.PolishingMode
Class VscnGroundWorks.ChiselWizCompat.<>c__DisplayClass14_0
Class VscnGroundWorks.GroundWorksSystem.<>O
Class VscnGroundWorks.GroundWorksSystem.<>c
Class VscnGroundWorks.GroundWorksSystem.<>c__DisplayClass17_0
Class VscnGroundWorks.GroundWorksSystem.<>c__DisplayClass20_0
Class VscnGroundWorks.RammedTypeDialog.<>c__DisplayClass0_0
Class VscnGroundWorks.RammedTypeDialog.<>c__DisplayClass0_1
Class VscnGroundWorks.RammedTypeDialog.<>c__DisplayClass1_0
Class VscnGroundWorks.RammedTypeDialog.<>c__DisplayClass1_1
Class VscnGroundWorks.RammedTypes.<>c
Class VscnGroundWorks.RammedTypes.<>c__DisplayClass5_0
Class VscnGroundWorks.RecipeWork.<>c
Class VscnGroundWorks.RecipeWork.<>c__DisplayClass22_0
Class VscnGroundWorks.RoadTypes.<>c__DisplayClass23_0
Class VscnGroundWorks.WorkActions.Session
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
