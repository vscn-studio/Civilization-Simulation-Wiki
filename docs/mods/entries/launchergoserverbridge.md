# 启动器服务器桥接

LauncherGo Server Bridge · 模组代码：launchergoserverbridge

> 来源：整合包安装包 `LauncherGo Server Bridge-2.2.0` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `launchergoserverbridge` |
| 版本 | 2.2.0 |
| 类型 | 含程序代码 |
| 运行端 | server |
| 客户端必需 | 否 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“依赖、兼容与管理工具”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Authenticated local server bridge for LauncherGo. Queries state and executes commands on the Vintage Story server thread.

</details>

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

```text
LauncherGo Server Bridge

Author: VSCN-Studio
Copyright (C) 2026 HansJack, LauncherGo project owner (VSCN-Studio team)
License: MIT. See LICENSE.txt when this mod is distributed as a standalone
package, or the repository LICENSE file when distributed with LauncherGo.

This server-side mod is deployed by LauncherGo and listens only on 127.0.0.1. It uses the per-profile token in ModConfig/launchergoserverbridge.json.

Protocol version 2 supports authenticated queries, commands, and long-lived event subscriptions over NDJSON. OSQ HTTP clients are not compatible.
The bridge also exposes `players.history` and emits `player.count-changed`; player history is retained for seven days and only records changes in the online player count.
```

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `serverbridge.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 0 | — |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**serverbridge.dll**（`71445157f51ddeb7`）：30 个类型。

```text
Class <Module>
Class LauncherGo.Services.ServerDeathLogParser
Class LauncherGo.Services.ServerBroadcastLogParser
Class LauncherGoServerBridge.ServerBridgeEvent
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem
Class <PrivateImplementationDetails>
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.InventorySummaryEntry
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.ServerBridgeConfiguration
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.ServerBridgeRequest
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.ServerBridgeResponse
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.PlayerCountRecord
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.ServerBridgeEventRecord
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.BridgeSubscriber
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>O
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass43_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass44_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass46_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass47_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass47_1
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass49_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass50_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass50_1
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass57_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass57_1
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass58_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass69_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass73_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass74_0
Class LauncherGoServerBridge.LauncherGoServerBridgeModSystem.<>c__DisplayClass82_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
