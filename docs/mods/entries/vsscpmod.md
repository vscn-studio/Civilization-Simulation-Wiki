# 文明兼容补丁

Seraph Civilization Patches · 模组代码：vsscpmod

> 来源：整合包安装包 `Seraph Civilization Patches-1.0.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vsscpmod` |
| 版本 | 1.0.1 |
| 类型 | 含程序代码 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.3 |
| 作者 | HansJack |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

文明补丁处理制作、搬运、载具、地图和绘画之间的兼容。1.0.1 包内 DLL 类型和 13 个 patch 明确覆盖以下边界：

| 兼容组 | 实际证据 | 玩家影响 |
| --- | --- | --- |
| 制作与容器 | ChiselTools 手刨、Expanded Matter 硫酸盐烹饪、RKN 制作、签名戒指刻字、From Golden Combs 桶侧 | 保留原模组输入/输出并修复界面或容器匹配；配方仍以当前加载顺序为准。 |
| 搬运与车船 | Logging/Carry On、Quarry 货舱、Shipwright 面、Cart/Jaunt 兼容类型 | 搬运、采石货舱和船体面片由补丁接线，冲突时以 `/vsslssmod compat` 与日志的 capability owner 为准。 |
| 信息与渲染 | 地图航点、坐标、Komet 字体/快捷键、Billposting、Cape/Canvas | 客户端显示和网格恢复；不会改变服务器生理账本。 |

玩家遇到兼容问题时，先确认目标模组已加载、再查看[补丁源码专题](/guide/patches-source)和[管理员排障](/admin/commands-full)。补丁没有独立玩家指令来绕过目标模组权限；`.vsscpmod inventory start|stop` 只切换客户端库存诊断。

[返回整合包图鉴](/mods/)

## 源码实现矩阵（当前源码树）

逐文件类型、方法及哈希已集中到[开发者源码索引](/develop/sources/vsscpmod)。

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `vsscpmod.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 1 | `assets/vsscpmod/entities/quarrydrag.json` |
| 配方定义 | 0 | — |
| 资产补丁 | 13 | `assets/vsscpmod/patches/compatibility/billposting-texture.json`<br>`assets/vsscpmod/patches/compatibility/cape-shape-texture.json`<br>`assets/vsscpmod/patches/compatibility/chiseltools-container-spoilage.json`<br>`assets/vsscpmod/patches/compatibility/envelopes-signetring-engraving.json`<br>`assets/vsscpmod/patches/compatibility/envelopes-signetring-preview.json`<br>`assets/vsscpmod/patches/compatibility/fieldsofsalt-connector-rock.json`<br>`assets/vsscpmod/patches/compatibility/fromgoldencombs-barrel-side.json`<br>`assets/vsscpmod/patches/compatibility/immersive-fibercraft-game-twine.json`<br>`assets/vsscpmod/patches/compatibility/immersive-fibercraft-pemmican-twine.json`<br>`assets/vsscpmod/patches/compatibility/involved-farming-long-term-food.json`<br>`assets/vsscpmod/patches/compatibility/quarry-ship-cargo.json`<br>`assets/vsscpmod/patches/compatibility/shipwright-drakkar-faces.json`<br>另有 1 个文件 |
| 语言资源 | 2 | `assets/vsscpmod/lang/en.json`<br>`assets/vsscpmod/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**vsscpmod.dll**（`f498eedf58fba4a2`）：154 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>z__ReadOnlyArray
Class SeraphCivilizationPatches.BillpostingFontCompatibility
Class SeraphCivilizationPatches.BillpostingInteractionCompatibility
Class SeraphCivilizationPatches.BodyPhysMigration
Class SeraphCivilizationPatches.CandelaClickUpTorchesCompatibility
Class SeraphCivilizationPatches.CapeRecipePatchCompatibilitySystem
Class SeraphCivilizationPatches.CapeRenderCompatibility
Class SeraphCivilizationPatches.ChiselToolsHandPlanerCompatibility
Class SeraphCivilizationPatches.ChromiumSulfateCookingCompatibility
Class SeraphCivilizationPatches.ClientMeshRecovery
Class SeraphCivilizationPatches.CoordinateDisplayCompatibility
Class SeraphCivilizationPatches.CraftingCountRenderer
Class SeraphCivilizationPatches.CraftingSurfaceAccess
Class SeraphCivilizationPatches.CreativeTabSelector
Class SeraphCivilizationPatches.EntityQuarryDrag
Class SeraphCivilizationPatches.EnvelopeEngravingCompatibility
Class SeraphCivilizationPatches.FenceReinforcementCompatibility
Class SeraphCivilizationPatches.FromGoldenCombsCompatibilitySystem
Class SeraphCivilizationPatches.ImmersiveFibercraftCompatibilitySystem
Class SeraphCivilizationPatches.ImmersiveMapWaypointRenderer
Class SeraphCivilizationPatches.InformationDisplayPatches
Class SeraphCivilizationPatches.InformationAccessPacket
Class SeraphCivilizationPatches.InformationRestrictionsConfig
Class SeraphCivilizationPatches.InformationRestrictions
Class SeraphCivilizationPatches.InventoryInputDiagnostics
Class SeraphCivilizationPatches.JauntStaminaHudCompatibility
Class SeraphCivilizationPatches.KometFontCompatibility
Class SeraphCivilizationPatches.KometHotkeyCompatibility
Class SeraphCivilizationPatches.KometPrimitiveSurvivalCompatibilitySystem
Class SeraphCivilizationPatches.LevelingEffects
Class SeraphCivilizationPatches.LevelingSkillPanel
Class SeraphCivilizationPatches.LevelingSurvivalCompatibility
Class SeraphCivilizationPatches.LoggingCarryOnCompatibility
Class SeraphCivilizationPatches.LoggingProgressCompatibility
Class SeraphCivilizationPatches.LongTermFoodMealCompatibilitySystem
Class SeraphCivilizationPatches.ModCommands
Class SeraphCivilizationPatches.PieBarrelTextureCompatibility
Class SeraphCivilizationPatches.QuarryCargoLayout
```

其余 114 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
