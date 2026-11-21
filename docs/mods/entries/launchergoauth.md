# 启动器认证

ServerAuth · 模组代码：launchergoauth

> 来源：整合包安装包 `ServerAuth-1.1.1` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `launchergoauth` |
| 版本 | 1.1.1 |
| 类型 | 含程序代码 |
| 运行端 | universal |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

服务器认证模组，提供注册登录、会话记住、Discourse SSO 与 OAuth2/OIDC 认证能力。

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

```text
ServerAuth（内嵌模组）

Author: VSCN-Studio
Copyright (C) 2026 HansJack, LauncherGo project owner (VSCN-Studio team)
License: MIT. See LICENSE.txt when this
mod is distributed as a standalone package, or the repository LICENSE file when
distributed with LauncherGo.

该目录由 LauncherGo 自动维护，请勿手动修改。

功能：
- 约束玩家先完成认证再进入游戏
- 提供密码注册、密码登录、Discourse SSO 与 OAuth2/OIDC 授权码认证
- OAuth2/OIDC 支持 Discovery、PKCE S256、Token 与 UserInfo 端点
- 为 LauncherGo 认证中心与 QQ 密码管理提供玩家与会话数据
- 支持 /serverauth reload，LauncherGo 保存配置后自动重载，无需轮询配置文件
```

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `serverauth.dll` |
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

**serverauth.dll**（`1769317a9d245ee4`）：39 个类型。

```text
Class <Module>
Class VsslAuth.VsslAuthModSystem
Class VsslAuth.Server.VsslAuthServerSystem
Class VsslAuth.Network.AuthChallengePacket
Class VsslAuth.Network.AuthStatePacket
Class VsslAuth.Client.VsslAuthClientSystem
Class <PrivateImplementationDetails>
Class VsslAuth.Server.VsslAuthServerSystem.PendingAuthState
Class VsslAuth.Server.VsslAuthServerSystem.DiscourseChallengeState
Class VsslAuth.Server.VsslAuthServerSystem.OAuth2ChallengeState
Class VsslAuth.Server.VsslAuthServerSystem.OAuth2Endpoints
Class VsslAuth.Server.VsslAuthServerSystem.OAuth2Identity
Class VsslAuth.Server.VsslAuthServerSystem.PlayerStore
Class VsslAuth.Server.VsslAuthServerSystem.ServerAuthSettings
Class VsslAuth.Server.VsslAuthServerSystem.ServerAuthDiscourseSettings
Class VsslAuth.Server.VsslAuthServerSystem.ServerAuthOAuth2Settings
Class VsslAuth.Server.VsslAuthServerSystem.ServerAuthPlayerRecord
Class VsslAuth.Server.VsslAuthServerSystem.ServerAuthSessionRecord
Class VsslAuth.Server.VsslAuthServerSystem.PasswordHasher
Class VsslAuth.Server.VsslAuthServerSystem.DiscourseConnect
Class VsslAuth.Server.VsslAuthServerSystem.<>c
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass33_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass39_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass49_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass51_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass53_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass54_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass55_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass56_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass58_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass65_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass67_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass68_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass72_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass73_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass82_0
Class VsslAuth.Server.VsslAuthServerSystem.<>c__DisplayClass83_0
Class VsslAuth.Client.VsslAuthClientSystem.<>c
Class VsslAuth.Client.VsslAuthClientSystem.<>c__DisplayClass7_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
