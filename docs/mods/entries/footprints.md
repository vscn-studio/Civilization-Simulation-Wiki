# 足迹

Footprints · 模组代码：footprints

> 来源：整合包安装包 `Footprints-1.2.16.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `footprints` |
| 版本 | 1.2.16 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Aylor222 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“世界、气候与环境”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Animals and Players leave footprints when moving.

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
| 程序集 | 1 | `Footprints.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 62 | `assets/footprints/compatibility/archosaurfixd/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/bovinae/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/caninae/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/capreolinae/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/casuariidae/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/cats/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/cervinae/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/dinornithidae/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/draconis/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/elephantidae/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/elkvariants/patches/entities_footprints/various.json`<br>`assets/footprints/compatibility/equus/patches/entities_footprints/various.json`<br>另有 50 个文件 |
| 语言资源 | 3 | `assets/footprints/lang/en.json`<br>`assets/footprints/lang/fr.json`<br>`assets/footprints/lang/ru.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 12 | `assets/footprints/config/footprints/archosaur.json`<br>`assets/footprints/config/footprints/cats.json`<br>`assets/footprints/config/footprints/dino.json`<br>`assets/footprints/config/footprints/draconis.json`<br>`assets/footprints/config/footprints/equus.json`<br>`assets/footprints/config/footprints/fantasycreatures.json`<br>`assets/footprints/config/footprints/fauna.json`<br>`assets/footprints/config/footprints/medievalexpansionpatch.json`<br>`assets/footprints/config/footprints/playermodels.json`<br>`assets/footprints/config/footprints/thecritterpack.json`<br>`assets/footprints/config/footprints/vanilla.json`<br>`assets/footprints/config/imm.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Footprints.dll**（`d8dd07a14452c14e`）：43 个类型。

```text
Class <Module>
Class Core
Class components.Footprints.Footprint
Class Footprints.FootprintRenderer
Class Footprints.src.utils.DebugUtils
Class Footprints.src.managers.FootprintRegistry
Class Footprints.src.managers.FootprintTickManager
Class Footprints.src.managers.LODManager
Class Footprints.src.managers.LODStatsLogger
Class Footprints.src.managers.rendering.TexturesManager
Class Footprints.src.managers.rendering.UVCoordStorage
Class Footprints.src.eventsListeners.BlockChangeListener
Class Footprints.src.Config.ConfigClient
Class Footprints.src.Config.ConfigLibCompatibility
Class Footprints.src.Config.ConfigServer
Class Footprints.src.Config.IMMCompatibility
Class Footprints.src.Config.ModConfig
Class Footprints.src.configs.ClientServerConfigSync
Class Footprints.src.configs.ServerConfigsSync
Class Footprints.src.components.FootprintDefinition
Class Footprints.src.behaviors.server.EntityFootprintsBehaviorSync
Class Footprints.src.behaviors.server.PlayerFootprintsSync
Class Footprints.src.behaviors.client.EntityFootprintsBehavior
Class Footprints.src.behaviors.client.PlayerFootprintTracker
Class <PrivateImplementationDetails>
Class Core.<>O
Class Core.<>c
Class Core.<>c__DisplayClass20_0
Class Core.<>c__DisplayClass22_0
Class Footprints.FootprintRenderer.<>c__DisplayClass19_0
Class Footprints.src.utils.DebugUtils.<>c
Class Footprints.src.managers.FootprintTickManager.<>O
Class Footprints.src.managers.FootprintTickManager.<>c__DisplayClass6_0
Class Footprints.src.Config.ConfigLibCompatibility.<>c
Class Footprints.src.Config.ConfigLibCompatibility.<>c__DisplayClass6_0
Class Footprints.src.configs.ClientServerConfigSync.NetworkApiConfigClientServerSync
Class Footprints.src.configs.ServerConfigsSync.NetworkApiConfigServerSync
Class Footprints.src.behaviors.server.EntityFootprintsBehaviorSync.<>c__DisplayClass22_0
Class Footprints.src.behaviors.server.PlayerFootprintsSync.NetworkApiConfigAffectPlayerMsg
Class Footprints.src.behaviors.client.PlayerFootprintTracker.<>c__DisplayClass11_0
```

其余 3 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
