# 血迹追踪

BloodTrail · 模组代码：bloodtrail

> 来源：整合包安装包 `BloodTrail-1.2.13.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `bloodtrail` |
| 版本 | 1.2.13 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Aylor222 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“身体、战斗与成长”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Animals leave blood trails when wounded by a player.

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
| 程序集 | 1 | `BloodTrail.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 66 | `assets/bloodtrail/compatibility/abelisauridae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/ankylosauria/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/archosaurfixd/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/bovinae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/caninae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/capreolinae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/carcharodontosauridae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/casuariidae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/cats/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/ceratopsidae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/cervinae/patches/entities/various.json`<br>`assets/bloodtrail/compatibility/dinornithidae/patches/entities/various.json`<br>另有 54 个文件 |
| 语言资源 | 3 | `assets/bloodtrail/lang/en.json`<br>`assets/bloodtrail/lang/fr.json`<br>`assets/bloodtrail/lang/ru.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 1 | `assets/bloodtrail/config/imm.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**BloodTrail.dll**（`636ae76962124ffc`）：21 个类型。

```text
Class <Module>
Class MyColorUtil
Class BloodTrail.Core
Class BloodTrail.src.Server.BleedingEventArgs
Class BloodTrail.src.Server.EntityBleedingBehavior
Class BloodTrail.src.managers.BloodTrailTickManager
Class BloodTrail.src.Config.ClientServerConfigSync
Class BloodTrail.src.Config.ConfigClient
Class BloodTrail.src.Config.ConfigLibCompatibility
Class BloodTrail.src.Config.ConfigServer
Class BloodTrail.src.Config.IMMCompatibility
Class BloodTrail.src.Config.ModConfig
Class BloodTrail.src.Client.EntityBleedingBehaviorParticles
Class <PrivateImplementationDetails>
Class BloodTrail.Core.<>O
Class BloodTrail.Core.<>c
Class BloodTrail.Core.<>c__DisplayClass17_0
Class BloodTrail.src.managers.BloodTrailTickManager.<>c
Class BloodTrail.src.Config.ClientServerConfigSync.NetworkApiConfigClientServerSync
Class BloodTrail.src.Config.ConfigLibCompatibility.<>c__DisplayClass2_0
Class BloodTrail.src.Client.EntityBleedingBehaviorParticles.<>c__DisplayClass15_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
