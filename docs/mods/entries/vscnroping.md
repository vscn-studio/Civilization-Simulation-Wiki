# 绳索交互

VSCN Roping · 模组代码：vscnroping

> 来源：整合包安装包 `VSCN Roping-1.1.15.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vscnroping` |
| 版本 | 1.1.15 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Throwable lassos, binding and tethering for players and creatures.

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
| 程序集 | 1 | `VSCN.Roping.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 2 | `assets/vscnroping/itemtypes/lasso-metal.json`<br>`assets/vscnroping/itemtypes/lasso-rope.json` |
| 实体定义 | 0 | — |
| 配方定义 | 2 | `assets/vscnroping/recipes/grid/lasso-metal.json`<br>`assets/vscnroping/recipes/grid/lasso-rope.json` |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/vscnroping/lang/en.json`<br>`assets/vscnroping/lang/zh-cn.json` |
| 手册资源 | 1 | `assets/vscnroping/config/handbook/roping.json` |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**VSCN.Roping.dll**（`c65fff0a74b6e36b`）：35 个类型。

```text
Class <Module>
Class VSCN.Roping.ItemLasso
Class VSCN.Roping.RopeSimulation
Class VSCN.Roping.ActiveCast
Class VSCN.Roping.LassoRenderer
Class VSCN.Roping.ModelWrap
Class VSCN.Roping.RopingHud
Class VSCN.Roping.RopingInteractionBehavior
Class VSCN.Roping.StrugglePacket
Class VSCN.Roping.LassoActionPacket
Class VSCN.Roping.EscapeStatusPacket
Class VSCN.Roping.HandworkPacket
Class VSCN.Roping.CastVisualPacket
Class VSCN.Roping.LassoLink
Class VSCN.Roping.PendingCast
Class VSCN.Roping.CutAttempt
Class VSCN.Roping.HandworkAttempt
Class VSCN.Roping.RopingSystem
Class <PrivateImplementationDetails>
Class VSCN.Roping.ItemLasso.HeldSway
Class VSCN.Roping.LassoRenderer.<>c
Class VSCN.Roping.ModelWrap.<>c
Class VSCN.Roping.RopingSystem.<>c__DisplayClass41_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass42_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass57_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass60_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass61_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass62_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass70_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass70_1
Class VSCN.Roping.RopingSystem.<>c__DisplayClass71_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass78_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass87_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass92_0
Class VSCN.Roping.RopingSystem.<>c__DisplayClass93_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 2 个配方文件与 1 个手册章节](/reference/recipes/vscnroping)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
