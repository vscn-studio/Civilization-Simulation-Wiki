# 束缚交互

VS Restraints · 模组代码：vsrestraints

> 来源：整合包安装包 `VS Restraints-1.0.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vsrestraints` |
| 版本 | 1.0.0 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0, survival 1.22.0 |
| 作者 | HansJack |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Extends restraint gameplay and tools.

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
| 程序集 | 1 | `VSRestraints.dll` |
| 方块定义 | 1 | `assets/vsrestraints/blocktypes/pillory.json` |
| 物品定义 | 3 | `assets/vsrestraints/itemtypes/handcuffs.json`<br>`assets/vsrestraints/itemtypes/ironchain.json`<br>`assets/vsrestraints/itemtypes/legshackles.json` |
| 实体定义 | 0 | — |
| 配方定义 | 4 | `assets/vsrestraints/recipes/grid/handcuffs.json`<br>`assets/vsrestraints/recipes/grid/ironchain.json`<br>`assets/vsrestraints/recipes/grid/legshackles.json`<br>`assets/vsrestraints/recipes/grid/pillory.json` |
| 资产补丁 | 1 | `assets/vsrestraints/patches/creativetab.json` |
| 语言资源 | 2 | `assets/vsrestraints/lang/en.json`<br>`assets/vsrestraints/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**VSRestraints.dll**（`7b470375a3759fb9`）：66 个类型。

```text
Class <Module>
Class VSRestraints.ItemIronChain
Class VSRestraints.ChainCorrection
Class VSRestraints.IronChainSystem
Class VSRestraints.ChainEndpoint
Class VSRestraints.PlacedIronChain
Class VSRestraints.ChainConnectionsPacket
Class VSRestraints.IronChainConnections
Class VSRestraints.BlockBehaviorChainAnchor
Class VSRestraints.IronChainPhysics
Class VSRestraints.IronChainRenderer
Class VSRestraints.ChainMesh
Class VSRestraints.PendingRestraintRequests
Class VSRestraints.BlockPillory
Class VSRestraints.BlockEntityPillory
Class VSRestraints.PilloryCombatSystem
Class VSRestraints.PilloryGeometry
Class VSRestraints.RestraintPoses
Class VSRestraints.RestraintRequestPacket
Class VSRestraints.RestraintResponsePacket
Class VSRestraints.RestraintRequestClosedPacket
Class VSRestraints.RestraintRequestDialog
Class VSRestraints.RestraintRules
Class VSRestraints.RestraintSounds
Class VSRestraints.ItemRestraint
Class VSRestraints.RestraintBehavior
Class VSRestraints.RestraintSystem
Class VSRestraints.RestraintView
Class VSRestraints.RestraintGeometry
Class <PrivateImplementationDetails>
Class VSRestraints.ItemIronChain.<>c__DisplayClass2_0
Class VSRestraints.IronChainSystem.<>c__DisplayClass20_0
Class VSRestraints.IronChainConnections.<>c__DisplayClass12_0
Class VSRestraints.IronChainConnections.<>c__DisplayClass29_0
Class VSRestraints.IronChainRenderer.Entry
Class VSRestraints.IronChainRenderer.<>c__DisplayClass12_0
Class VSRestraints.ChainMesh.LinkTextures
Class VSRestraints.ChainMesh.<>c
Class VSRestraints.ChainMesh.<>c__DisplayClass2_0
Class VSRestraints.PendingRestraintRequests.Entry
```

其余 26 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 4 个配方文件与 0 个手册章节](/reference/recipes/vsrestraints)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
