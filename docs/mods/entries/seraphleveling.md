# 技能成长

Seraph Leveling · 模组代码：seraphleveling

> 来源：整合包安装包 `Seraph Leveling-1.22.5.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `seraphleveling` |
| 版本 | 1.22.5 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0, survival 1.22.0 |
| 作者 | Soareverix |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“身体、战斗与成长”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

A progression system that improves player traits through gameplay. Mine blocks to increase your mining speed, deal damage to improve your combat prowess, and more!

</details>

作者提供的链接：https://github.com/Michael-Andrzejewski/Seraph-Leveling-Vintage-Story-Mod

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `SeraphLeveling.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 1 | `assets/seraphleveling/lang/en.json` |
| 手册资源 | 1 | `assets/seraphleveling/config/handbook/sl-guide.json` |
| 包内配置数据 | 1 | `assets/seraphleveling/config/traits.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**SeraphLeveling.dll**（`fc5771fbde2476fa`）：91 个类型。

```text
Class <Module>
Class SeraphLeveling.CharacterSystemPatches
Class SeraphLeveling.SeraphProgressPage
Class SeraphLeveling.SeraphReportRichtext
Class SeraphLeveling.SeraphLevelingClientSystem
Class SeraphLeveling.SeraphLevelingModSystem
Class SeraphLeveling.SeraphLevelingConfig
Class SeraphLeveling.COWeaponProgressData
Class SeraphLeveling.COProficiencyProgressData
Class SeraphLeveling.COPlayerProgressData
Class SeraphLeveling.PlayerProgressExport
Class SeraphLeveling.RangedWeaponProgressData
Class SeraphLeveling.RangedProgressData
Class SeraphLeveling.WalkingProgressData
Class SeraphLeveling.HungerProgressData
Class SeraphLeveling.ArmorPieceProgressData
Class SeraphLeveling.ArmorProgressData
Class SeraphLeveling.WeaponProgressData
Class SeraphLeveling.MeleeProgressData
Class SeraphLeveling.PickaxeProgressData
Class SeraphLeveling.MiningProgressData
Class SeraphLeveling.ClothierProgressData
Class SeraphLeveling.MenderProgressData
Class SeraphLeveling.PilfererProgressData
Class SeraphLeveling.ResourcefulProgressData
Class SeraphLeveling.ForagerProgressData
Class SeraphLeveling.FurtiveProgressData
Class SeraphLeveling.PreciseWeaponProgressData
Class SeraphLeveling.PreciseProgressData
Class SeraphLeveling.TechnicalProgressData
Class SeraphLeveling.HardyHealthProgressData
Class SeraphLeveling.BowyerProgressData
Class SeraphLeveling.ImproviserProgressData
Class SeraphLeveling.TinkererProgressData
Class SeraphLeveling.MercilessProgressData
Class SeraphLeveling.ClaustrophobicRemovalProgressData
Class SeraphLeveling.CachedVanillaTraits
Class SeraphLeveling.Position2D
Class SeraphLeveling.ProgressReportMessage
Class SeraphLeveling.ProgressReportRequestMessage
```

其余 51 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 0 个配方文件与 1 个手册章节](/reference/recipes/seraphleveling)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
