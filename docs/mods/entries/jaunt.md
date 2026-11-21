# 旅行与移动

Jaunt: Extended Riding System · 模组代码：jaunt

> 来源：整合包安装包 `Jaunt_ Extended Riding System-3.3.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `jaunt` |
| 版本 | 3.3.1 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | safwyl, sekelsta, Shintharo12, Freakyuser396, dinolord919 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Library providing an extended rideable system with additional control patterns and stamina

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
| 程序集 | 1 | `Jaunt.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 1 | `assets/jaunt/itemtypes/instrument.json` |
| 实体定义 | 2 | `assets/jaunt/sample/entities/wildhorse.json`<br>`assets/jaunt/sample/entities/wyvern.json` |
| 配方定义 | 1 | `assets/jaunt/recipes/grid/jauntflute.json` |
| 资产补丁 | 1 | `assets/jaunt/patches/instrument.json` |
| 语言资源 | 2 | `assets/jaunt/lang/en.json`<br>`assets/jaunt/lang/ru.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 1 | `assets/jaunt/config/imm.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Jaunt.dll**（`4aa21c271432960f`）：25 个类型。

```text
Class <Module>
Class Jaunt.WalkSpeedMultiplierPatch
Class Jaunt.HarmonyGuiDialogCreatureContentsPatch
Class Jaunt.JauntModSystem
Class Jaunt.Systems.FatigueSource
Class Jaunt.Items.ItemJauntInstrument
Class Jaunt.Hud.HudElementStaminaBar
Class Jaunt.Hud.HudIconRenderer
Class Jaunt.Entities.EntityFlyingAgent
Class Jaunt.Entities.EntityJauntAgent
Class Jaunt.Config.JauntConfig
Class Jaunt.Behaviors.CollectibleBehaviorJauntAttachments
Class Jaunt.Behaviors.EntityBehaviorJauntAiControl
Class Jaunt.Behaviors.EntityBehaviorJauntArmor
Class Jaunt.Behaviors.JauntGaitMeta
Class Jaunt.Behaviors.EntityBehaviorJauntGait
Class Jaunt.Behaviors.EntityBehaviorJauntRevivable
Class Jaunt.Behaviors.EntityBehaviorJauntRideable
Class Jaunt.Behaviors.EntityBehaviorJauntStamina
Class Jaunt.Behaviors.EntityBehaviorJauntWalkspeed
Class <PrivateImplementationDetails>
Class Jaunt.JauntModSystem.<>c__DisplayClass34_0
Class Jaunt.Items.ItemJauntInstrument.<>c
Class Jaunt.Behaviors.EntityBehaviorJauntRideable.<>c__DisplayClass16_0
Class Jaunt.Behaviors.EntityBehaviorJauntStamina.<>c
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 1 个配方文件与 0 个手册章节](/reference/recipes/jaunt)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
