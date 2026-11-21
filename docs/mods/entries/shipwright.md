# 造船

Shipwright: Vessels of Distant Shores · 模组代码：shipwright

> 来源：整合包安装包 `Shipwright_ Vessels of Distant Shores-1.5.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `shipwright` |
| 版本 | 1.5.1 |
| 类型 | 含程序代码 |
| 运行端 | universal |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Freakyuser396, Pal_5000, Rivvion, Shintharo12 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds various sailed and rowed boats

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
| 程序集 | 1 | `shipwright.dll` |
| 方块定义 | 1 | `assets/shipwright/blocktypes/agedfigurehead.json` |
| 物品定义 | 29 | `assets/shipwright/itemtypes/artisanbrush.json`<br>`assets/shipwright/itemtypes/attachments/boatcover.json`<br>`assets/shipwright/itemtypes/attachments/boatdeco-punter.json`<br>`assets/shipwright/itemtypes/attachments/disabled/boatseat.json`<br>`assets/shipwright/itemtypes/attachments/disabled/drakkarflag.json`<br>`assets/shipwright/itemtypes/attachments/disabled/testpassenger.json`<br>`assets/shipwright/itemtypes/attachments/drakkartent.json`<br>`assets/shipwright/itemtypes/attachments/jibsail.json`<br>`assets/shipwright/itemtypes/attachments/oarset.json`<br>`assets/shipwright/itemtypes/attachments/ropeladder.json`<br>`assets/shipwright/itemtypes/attachments/saillogo.json`<br>`assets/shipwright/itemtypes/attachments/sailpatternbase.json`<br>另有 17 个文件 |
| 实体定义 | 21 | `assets/game/entities/nonliving/boat-sailed.json`<br>`assets/shipwright/compatibility/game/entities/nonliving/testboat-sailed.json`<br>`assets/shipwright/entities/nonliving/catboat-construction.json`<br>`assets/shipwright/entities/nonliving/catboat.json`<br>`assets/shipwright/entities/nonliving/coracle-construction.json`<br>`assets/shipwright/entities/nonliving/coracle.json`<br>`assets/shipwright/entities/nonliving/drakkar-construction.json`<br>`assets/shipwright/entities/nonliving/drakkar.json`<br>`assets/shipwright/entities/nonliving/faering-construction.json`<br>`assets/shipwright/entities/nonliving/faering.json`<br>`assets/shipwright/entities/nonliving/kayak-construction.json`<br>`assets/shipwright/entities/nonliving/kayak.json`<br>另有 9 个文件 |
| 配方定义 | 15 | `assets/shipwright/recipes/barrel/dyes.json`<br>`assets/shipwright/recipes/barrel/tannin.json`<br>`assets/shipwright/recipes/barrel/woad.json`<br>`assets/shipwright/recipes/grid/boatdeco.json`<br>`assets/shipwright/recipes/grid/dragonhorn.json`<br>`assets/shipwright/recipes/grid/drakkarflag.json`<br>`assets/shipwright/recipes/grid/drakkartent.json`<br>`assets/shipwright/recipes/grid/figurehead.json`<br>`assets/shipwright/recipes/grid/lanterns.json`<br>`assets/shipwright/recipes/grid/oars.json`<br>`assets/shipwright/recipes/grid/roller.json`<br>`assets/shipwright/recipes/grid/ropeladderswap.json`<br>另有 3 个文件 |
| 资产补丁 | 16 | `assets/shipwright/patches/carryon.json`<br>`assets/shipwright/patches/disabled/vanilla-chest.json`<br>`assets/shipwright/patches/disabled/vanilla-figurehead.json`<br>`assets/shipwright/patches/disabled/vanilla-linen.json`<br>`assets/shipwright/patches/draconis-horn.json`<br>`assets/shipwright/patches/game-entities-humanoid-player.json`<br>`assets/shipwright/patches/game-shapes-entity-humanoid-seraph-faceless.json`<br>`assets/shipwright/patches/heraldrybanners-banners.json`<br>`assets/shipwright/patches/physicslib.json`<br>`assets/shipwright/patches/sailboatbed.json`<br>`assets/shipwright/patches/sailrecolor.json`<br>`assets/shipwright/patches/shipwright-configpatches.json`<br>另有 4 个文件 |
| 语言资源 | 2 | `assets/shipwright/lang/en.json`<br>`assets/shipwright/lang/uk.json` |
| 手册资源 | 1 | `assets/shipwright/config/handbook/shipwrightguide.json` |
| 包内配置数据 | 1 | `assets/shipwright/config/configlib-patches.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**shipwright.dll**（`9a3471bb42b1b59b`）：34 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>f__AnonymousType1
Class <>f__AnonymousType2
Class <>f__AnonymousType3
Class shipwright.CollectibleBehaviorInteractibleAttachment
Class shipwright.CollectibleBehaviorTextureSwapper
Class shipwright.ModSystemShipwrightSounds
Class shipwright.EntityShipwrightBoat
Class shipwright.EntityShipwrightConstruction
Class shipwright.EntityShipwrightBoatSeat
Class shipwright.HarmonyGuiDialogCreatureContentsPatch
Class shipwright.ModSystemShipwrightConstructionSitePreview
Class shipwright.ItemShipwrightRoller
Class shipwright.TextureDebugNetPacket
Class shipwright.ModSystemShipwrightCommands
Class shipwright.ShipwrightTextureDebug
Class shipwright.ModSystemSailSwap
Class shipwright.shipwrightCore
Class shipwright.CollectibleBehaviorInteractibleAttachment.<>c__DisplayClass13_0
Class shipwright.EntityShipwrightBoat.<>c
Class shipwright.EntityShipwrightConstruction.<>c__DisplayClass11_0
Class shipwright.ItemShipwrightRoller.<>c
Class shipwright.ItemShipwrightRoller.<>c__DisplayClass13_0
Class shipwright.ModSystemShipwrightCommands.<>c
Class shipwright.ModSystemShipwrightCommands.<>c__DisplayClass2_0
Class shipwright.ShipwrightTextureDebug.Collector
Class shipwright.ShipwrightTextureDebug.LogEvent
Class shipwright.ShipwrightTextureDebug.<>O
Class shipwright.ModSystemSailSwap.ItemArtisanBrush
Class shipwright.ModSystemSailSwap.BehSailRecolor
Class shipwright.shipwrightCore.<>O
Class shipwright.ModSystemSailSwap.BehSailRecolor.BakedTexture
Class shipwright.ModSystemSailSwap.BehSailRecolor.<>c__DisplayClass13_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 15 个配方文件与 1 个手册章节](/reference/recipes/shipwright)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
