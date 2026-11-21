# 渐进出血

Progressive Bleeding · 模组代码：progressivebleeding

> 来源：整合包安装包 `Progressive Bleeding-1.7.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `progressivebleeding` |
| 版本 | 1.7.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 否 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.7 |
| 作者 | DAplayerGAMES |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“身体、战斗与成长”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Lanças e espadas causam sangramento contínuo e lentidão progressiva nas criaturas.

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
| 程序集 | 1 | `ProgressiveBleeding.dll` |
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

**ProgressiveBleeding.dll**（`fd98943c886f57d2`）：28 个类型。

```text
Class <Module>
Class ProgressiveBleeding.BleedFeedbackPatch
Class ProgressiveBleeding.BleedDamageSource
Class ProgressiveBleeding.BleedingBehavior
Class ProgressiveBleeding.TargetBalance
Class ProgressiveBleeding.BleedingConfig
Class ProgressiveBleeding.BleedingConfigDialog
Class ProgressiveBleeding.BleedingSystem
Class ProgressiveBleeding.DamagePatch
Class ProgressiveBleeding.OtherMovementPatch
Class ProgressiveBleeding.BloodTrail
Class ProgressiveBleeding.ConfigMessage
Class ProgressiveBleeding.ConfigEditing
Class ProgressiveBleeding.ConfigGuiSystem
Class ProgressiveBleeding.WeaponBleeding
Class ProgressiveBleeding.BleedFeedbackPatch.<Transpiler>d__0
Class ProgressiveBleeding.BleedingBehavior.<>c__DisplayClass17_0
Class ProgressiveBleeding.BleedingConfig.<>c
Class ProgressiveBleeding.BleedingConfig.<>c__DisplayClass85_0
Class ProgressiveBleeding.BleedingConfigDialog.<>c__DisplayClass20_0
Class ProgressiveBleeding.BleedingConfigDialog.<>c__DisplayClass20_1
Class ProgressiveBleeding.BleedingConfigDialog.<>c__DisplayClass22_0
Class ProgressiveBleeding.BleedingConfigDialog.<>c__DisplayClass22_1
Class ProgressiveBleeding.BleedingConfigDialog.<>c__DisplayClass31_0
Class ProgressiveBleeding.OtherMovementPatch.<TargetMethods>d__0
Class ProgressiveBleeding.ConfigGuiSystem.<>c__DisplayClass4_0
Class ProgressiveBleeding.ConfigGuiSystem.<>c__DisplayClass5_0
Class ProgressiveBleeding.ConfigGuiSystem.<>c__DisplayClass5_1
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
