# 纺纱与纤维工艺

Immersive Fibercraft · 模组代码：spinningwheel

> 来源：整合包安装包 `Immersive Fibercraft-1.2.14.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `spinningwheel` |
| 版本 | 1.2.14 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | 未声明 |
| 作者 | HeadPilgrim |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds immersive crafting mechanics for spinning and weaving.

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
| 程序集 | 1 | `SpinningWheel.dll` |
| 方块定义 | 2 | `assets/spinningwheel/blocktypes/flyshuttleloom.json`<br>`assets/spinningwheel/blocktypes/spinningwheel.json` |
| 物品定义 | 8 | `assets/spinningwheel/itemtypes/distafffibers.json`<br>`assets/spinningwheel/itemtypes/dropspindle.json`<br>`assets/spinningwheel/itemtypes/flyshuttleloombeater.json`<br>`assets/spinningwheel/itemtypes/flyshuttleloomframe.json`<br>`assets/spinningwheel/itemtypes/flyshuttleloomheddle.json`<br>`assets/spinningwheel/itemtypes/moaitem.json`<br>`assets/spinningwheel/itemtypes/spinningwheelframe.json`<br>`assets/spinningwheel/itemtypes/spinningwheelwheelitem.json` |
| 实体定义 | 0 | — |
| 配方定义 | 10 | `assets/spinningwheel/recipes/grid/dropspindle.json`<br>`assets/spinningwheel/recipes/grid/hpflyshuttleloom.json`<br>`assets/spinningwheel/recipes/grid/hpflyshuttleloombeater.json`<br>`assets/spinningwheel/recipes/grid/hpflyshuttleloomframe.json`<br>`assets/spinningwheel/recipes/grid/hpflyshuttleloomheddle.json`<br>`assets/spinningwheel/recipes/grid/hpmoaitem.json`<br>`assets/spinningwheel/recipes/grid/hpspinningwheel.json`<br>`assets/spinningwheel/recipes/grid/hpspinningwheelframe.json`<br>`assets/spinningwheel/recipes/grid/hpspinningwheelwheelitem.json`<br>`assets/spinningwheel/recipes/loompatterns/checkered.json` |
| 资产补丁 | 11 | `assets/spinningwheel/patches/floralzonescaribbeanregion-cotton.json`<br>`assets/spinningwheel/patches/game-cloth.json`<br>`assets/spinningwheel/patches/game-entities-humanoid-player.json`<br>`assets/spinningwheel/patches/game-flaxfibers.json`<br>`assets/spinningwheel/patches/game-flaxtwine.json`<br>`assets/spinningwheel/patches/game-seraph-faceless.json`<br>`assets/spinningwheel/patches/pemmican.json`<br>`assets/spinningwheel/patches/ruderalis.json`<br>`assets/spinningwheel/patches/rustbound-magic-shiftingfibers.json`<br>`assets/spinningwheel/patches/tailors-delight.json`<br>`assets/spinningwheel/patches/wool.json` |
| 语言资源 | 7 | `assets/spinningwheel/lang/be.json`<br>`assets/spinningwheel/lang/en.json`<br>`assets/spinningwheel/lang/fr.json`<br>`assets/spinningwheel/lang/is.json`<br>`assets/spinningwheel/lang/pl.json`<br>`assets/spinningwheel/lang/ru.json`<br>`assets/spinningwheel/lang/uk.json` |
| 手册资源 | 4 | `assets/spinningwheel/config/handbook/101-spinningwheel.json`<br>`assets/spinningwheel/config/handbook/102-flyshuttleloom.json`<br>`assets/spinningwheel/config/handbook/103-patternweaving.json`<br>`assets/spinningwheel/config/handbook/104-dropspidnle.json` |
| 包内配置数据 | 1 | `assets/spinningwheel/config/configlib-patches.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**SpinningWheel.dll**（`1d9361535f8991d4`）：37 个类型。

```text
Class <Module>
Class SpinningWheel.Utilities.InSpinningWheelProps
Class SpinningWheel.Utilities.ValuesByMultiblockOffset
Class SpinningWheel.ModSystem.SpinningWheelModSystem
Class SpinningWheel.ModSystem.SyncClientPacket
Class SpinningWheel.Recipes.LoomPatternRecipe
Class SpinningWheel.Recipes.LoomPatternRecipeLoader
Class SpinningWheel.Recipes.TemplatedRecipeJson
Class SpinningWheel.Recipes.TemplatedOutputJson
Class SpinningWheel.Recipes.VariantJson
Class SpinningWheel.Recipes.PatternRecipeJson
Class SpinningWheel.Recipes.PatternJson
Class SpinningWheel.Recipes.InputJson
Class SpinningWheel.Recipes.OutputJson
Class SpinningWheel.ModConfig.ModConfig
Class SpinningWheel.Items.ItemDropSpindle
Class SpinningWheel.Inventories.InventoryFlyshuttleLoom
Class SpinningWheel.Inventories.ItemSlotWeavingInput
Class SpinningWheel.Inventories.ItemSlotPatternInput
Class SpinningWheel.Inventories.InventorySpinningWheel
Class SpinningWheel.Inventories.ItemSlotSpinningInput
Class SpinningWheel.Inventories.ItemSlotOutput
Class SpinningWheel.GUIs.GuiDialogBlockEntityLoom
Class SpinningWheel.GUIs.GuiDialogBlockEntitySpinningWheel
Class SpinningWheel.Configuration.SpinningWheelConfigPatcher
Class SpinningWheel.Blocks.BlockFlyShuttleLoom
Class SpinningWheel.Blocks.BlockSpinningWheel
Class SpinningWheel.BLockEntityRenderer.SpinningWheelContentsRenderer
Class SpinningWheel.BlockEntityPackets.SetWeavingModePacket
Class SpinningWheel.BlockEntities.BlockEntityFlyShuttleLoom
Class SpinningWheel.BlockEntities.BlockEntitySpinningWheel
Class SpinningWheel.Utilities.ValuesByMultiblockOffset.<>c
Class SpinningWheel.ModSystem.SpinningWheelModSystem.<>O
Class SpinningWheel.ModSystem.SpinningWheelModSystem.<>c
Class SpinningWheel.BlockEntities.BlockEntityFlyShuttleLoom.<>c__DisplayClass117_0
Class SpinningWheel.BlockEntities.BlockEntitySpinningWheel.<>c
Class SpinningWheel.BlockEntities.BlockEntitySpinningWheel.<>c__DisplayClass95_0
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 10 个配方文件与 4 个手册章节](/reference/recipes/spinningwheel)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
