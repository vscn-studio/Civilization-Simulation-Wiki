# 离线防腐

Offline No Spoil · 模组代码：offlinenospoil

> 来源：整合包安装包 `Offline No Spoil-1.6.1-pre.5.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `offlinenospoil` |
| 版本 | 1.6.1-pre.5 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“农业、饮食与卫生”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Preserves perishable food in offline player inventories and configured storage containers with bounded, persistent access policies.

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
| 程序集 | 1 | `VSCNStudio.OfflineNoSpoil.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/offlinenospoil/lang/en.json`<br>`assets/offlinenospoil/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**VSCNStudio.OfflineNoSpoil.dll**（`afc6c09683718b47`）：54 个类型。

```text
Class <Module>
Class VSCNStudio.OfflineNoSpoil.AccessPolicyTracker
Class VSCNStudio.OfflineNoSpoil.PersistedAccessPolicyState
Class VSCNStudio.OfflineNoSpoil.ContainerAccessPolicy
Class VSCNStudio.OfflineNoSpoil.GlobMatcher
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilConfig
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilContainerBehavior
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilCrockBehavior
Class VSCNStudio.OfflineNoSpoil.CrockUseRules
Class VSCNStudio.OfflineNoSpoil.CrockInteractionState
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilCrockPatch
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesCompatibility
Class VSCNStudio.OfflineNoSpoil.FoodShelvesInteractionState
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesMeshPatch
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilModSystem
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilTooltipBehavior
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilTooltipPacket
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilTooltipRuntime
Class VSCNStudio.OfflineNoSpoil.OfflinePlayerTracker
Class VSCNStudio.OfflineNoSpoil.OfflineStateStore
Class VSCNStudio.OfflineNoSpoil.PersistedPlayerState
Class VSCNStudio.OfflineNoSpoil.PerishReconciler
Class VSCNStudio.OfflineNoSpoil.AccessPolicyTracker.PolicyKeyCursor
Class VSCNStudio.OfflineNoSpoil.AccessPolicyTracker.AccessPolicyState
Class VSCNStudio.OfflineNoSpoil.AccessPolicyTracker.<>c
Class VSCNStudio.OfflineNoSpoil.AccessPolicyTracker.<>c__DisplayClass31_0
Class VSCNStudio.OfflineNoSpoil.AccessPolicyTracker.<>c__DisplayClass34_0
Class VSCNStudio.OfflineNoSpoil.AccessPolicyTracker.<>c__DisplayClass52_0
Class VSCNStudio.OfflineNoSpoil.ContainerAccessPolicy.<>c
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilConfig.<>c
Class VSCNStudio.OfflineNoSpoil.CrockUseRules.<>c__DisplayClass1_0
Class VSCNStudio.OfflineNoSpoil.CrockInteractionState.<>c
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilCrockPatch.CrockPatchState
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesCompatibility.FoodShelvesPatchState
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesCompatibility.<>c
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesCompatibility.<FindBlockInteractionMethods>d__11
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesCompatibility.<FindContainedInteractionMethods>d__12
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesCompatibility.<FindInteractionMethods>d__10
Class VSCNStudio.OfflineNoSpoil.FoodShelvesInteractionState.<>c
Class VSCNStudio.OfflineNoSpoil.OfflineNoSpoilFoodShelvesMeshPatch.<>c
```

其余 14 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
