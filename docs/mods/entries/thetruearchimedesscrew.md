# 阿基米德螺旋提水

Archimedes Screw · 模组代码：thetruearchimedesscrew

> 来源：整合包安装包 `Archimedes Screw-0.2.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `thetruearchimedesscrew` |
| 版本 | 0.2.0 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | 未声明 |
| 作者 | Grym7er |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds a mechanically powered Archimedes screw that can pump water against gravity.

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
| 程序集 | 1 | `archimedes_screw.dll` |
| 方块定义 | 1 | `assets/archimedes_screw/blocktypes/metal/waterarchimedesscrew.json` |
| 物品定义 | 1 | `assets/archimedes_screw/itemtypes/resource/chutesection.json` |
| 实体定义 | 0 | — |
| 配方定义 | 3 | `assets/archimedes_screw/recipes/grid/waterarchimedesscrew-ported.json`<br>`assets/archimedes_screw/recipes/grid/waterarchimedesscrew-straight.json`<br>`assets/archimedes_screw/recipes/smithing/chutesection-lead.json` |
| 资产补丁 | 0 | — |
| 语言资源 | 1 | `assets/archimedes_screw/lang/en.json` |
| 手册资源 | 1 | `assets/archimedes_screw/config/handbook/101-overview.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**archimedes_screw.dll**（`acfa565abc021d90`）：12 个类型。

```text
Class <Module>
Class ArchimedesScrew.BlockEntityWaterArchimedesScrew
Class ArchimedesScrew.BlockWaterArchimedesScrew
Class ArchimedesScrew.RealisticWaterCompatBridge
Class ArchimedesScrew.RealisticWaterOutletSustainPatch
Class ArchimedesScrew.ArchimedesScrewModSystem
Class ArchimedesScrew.ArchimedesScrewAssemblyAnalyzer
Class ArchimedesScrew.ArchimedesWaterFamilies
Class ArchimedesScrew.ArchimedesFluidHostValidator
Class ArchimedesScrew.ArchimedesScrewAssemblyAnalyzer.AssemblyStatus
Class ArchimedesScrew.ArchimedesScrewAssemblyAnalyzer.<>c
Class ArchimedesScrew.ArchimedesWaterFamilies.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 3 个配方文件与 1 个手册章节](/reference/recipes/thetruearchimedesscrew)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
