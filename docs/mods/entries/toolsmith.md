# 工具锻造

Toolsmith · 模组代码：toolsmith

> 来源：整合包安装包 `Toolsmith-1.2.19.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `toolsmith` |
| 版本 | 1.2.19 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | Jon |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Upgrade your tools with proper handles and bindings for durability and other buffs! Plus, returning the tool head when it wears out since they should last much longer then they do in vanilla.

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
| 程序集 | 1 | `Toolsmith.dll` |
| 方块定义 | 2 | `assets/toolsmith/blocktypes/grindstone.json`<br>`assets/toolsmith/blocktypes/workbench.json` |
| 物品定义 | 7 | `assets/toolsmith/itemtypes/fabricstrips.json`<br>`assets/toolsmith/itemtypes/handles/carpentedhandle.json`<br>`assets/toolsmith/itemtypes/handles/crudehandle.json`<br>`assets/toolsmith/itemtypes/handles/handle.json`<br>`assets/toolsmith/itemtypes/sandpaper.json`<br>`assets/toolsmith/itemtypes/tinkertoolparts.json`<br>`assets/toolsmith/itemtypes/whetstone.json` |
| 实体定义 | 0 | — |
| 配方定义 | 44 | `assets/toolsmith/compatibility/ancienttools/recipes/grid/fabricstrips-atleather-cloth.json`<br>`assets/toolsmith/compatibility/butchering/recipes/grid/sandpaper-from-glues.json`<br>`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-carpentedhandle.json`<br>`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-grindstone.json`<br>`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-handle.json`<br>`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-workbench.json`<br>`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-carpentedhandle.json`<br>`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-grindstone.json`<br>`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-handle.json`<br>`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-workbench.json`<br>`assets/toolsmith/compatibility/floralzonescentralaustralianregion/recipes/grid/centralaustralian-carpentedhandle.json`<br>`assets/toolsmith/compatibility/floralzonescentralaustralianregion/recipes/grid/centralaustralian-grindstone.json`<br>另有 32 个文件 |
| 资产补丁 | 82 | `assets/toolsmith/compatibility/ancienttools/patches/fabricstrips-additions.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-axe.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-hammer.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-hoe.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-knife.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-pickaxe.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-prospectingpick.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-saw.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-scythe.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/elementium/vanilla-shovel.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/manasteel/vanilla-axe.json`<br>`assets/toolsmith/compatibility/botaniastory/patches/partshapes/manasteel/vanilla-hammer.json`<br>另有 70 个文件 |
| 语言资源 | 7 | `assets/toolsmith/lang/be.json`<br>`assets/toolsmith/lang/en.json`<br>`assets/toolsmith/lang/es-419.json`<br>`assets/toolsmith/lang/es-es.json`<br>`assets/toolsmith/lang/fr.json`<br>`assets/toolsmith/lang/pt-br.json`<br>`assets/toolsmith/lang/ru.json` |
| 手册资源 | 7 | `assets/toolsmith/config/handbook/toolsmithing-craftingmethods.json`<br>`assets/toolsmith/config/handbook/toolsmithing-durabilityandwear.json`<br>`assets/toolsmith/config/handbook/toolsmithing-miscaddons.json`<br>`assets/toolsmith/config/handbook/toolsmithing-reforging.json`<br>`assets/toolsmith/config/handbook/toolsmithing-the-basics.json`<br>`assets/toolsmith/config/handbook/toolsmithing-toolhandles.json`<br>`assets/toolsmith/config/handbook/toolsmithing-tooltypes.json` |
| 包内配置数据 | 60 | `assets/toolsmith/compatibility/meteoricsteel/config/toolsmith/parts/bindings/bindings-meteoricsteel.json`<br>`assets/toolsmith/compatibility/meteoricsteel/config/toolsmith/stats/bindings/bindings-meteoricsteel.json`<br>`assets/toolsmith/compatibility/uraniumexpanded/config/toolsmith/parts/bindings/bindings-ferrousuranium.json`<br>`assets/toolsmith/compatibility/uraniumexpanded/config/toolsmith/parts/bindings/bindings-uraniumsteel.json`<br>`assets/toolsmith/compatibility/uraniumexpanded/config/toolsmith/stats/bindings/bindings-ferrousuranium.json`<br>`assets/toolsmith/compatibility/uraniumexpanded/config/toolsmith/stats/bindings/bindings-uraniumsteel.json`<br>`assets/toolsmith/config/toolsmith/parts/bindings/bindings-ancienttools.json`<br>`assets/toolsmith/config/toolsmith/parts/bindings/bindings-butchery.json`<br>`assets/toolsmith/config/toolsmith/parts/bindings/bindings-primitivesurvival.json`<br>`assets/toolsmith/config/toolsmith/parts/bindings/bindings-stringsense.json`<br>`assets/toolsmith/config/toolsmith/parts/bindings/bindings-tailorsdelight.json`<br>`assets/toolsmith/config/toolsmith/parts/bindings/bindings-vanilla.json`<br>另有 48 个文件 |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**Toolsmith.dll**（`95c25a86ffe83b56`）：83 个类型。

```text
Class <Module>
Class Toolsmith.RecipeRegisterModSystem
Class Toolsmith.ToolsmithModSystem
Class Toolsmith.Utils.ConfigUtility
Class Toolsmith.Utils.ItemStackExtensions
Class Toolsmith.Utils.MathUtility
Class Toolsmith.Utils.StringHelpers
Class Toolsmith.Utils.ToolsmithAttributes
Class Toolsmith.Utils.ToolsmithConstants
Class Toolsmith.ToolTinkering.TinkeringUtility
Class Toolsmith.ToolTinkering.ToolRenderingPatches
Class Toolsmith.ToolTinkering.ToolRenderingHoePatches
Class Toolsmith.ToolTinkering.ToolTinkeringTransitionalPropsPatches
Class Toolsmith.ToolTinkering.ToolTinkeringCraftingPatches
Class Toolsmith.ToolTinkering.ToolTinkeringRenderPatches
Class Toolsmith.ToolTinkering.OffhandDominantInteractionUsePatches
Class Toolsmith.ToolTinkering.ToolTinkeringGuiElementPatches
Class Toolsmith.ToolTinkering.ItemAxePatches
Class Toolsmith.ToolTinkering.Items.ItemTinkerToolParts
Class Toolsmith.ToolTinkering.Items.ItemWhetstone
Class Toolsmith.ToolTinkering.Items.ItemWorkableNugget
Class Toolsmith.ToolTinkering.Drawbacks.DrawbackUtility
Class Toolsmith.ToolTinkering.Drawbacks.ReforgingUtility
Class Toolsmith.ToolTinkering.Blocks.BlockEntityGrindstone
Class Toolsmith.ToolTinkering.Blocks.BlockEntityWorkbench
Class Toolsmith.ToolTinkering.Blocks.BlockGrindstone
Class Toolsmith.ToolTinkering.Blocks.BlockWorkbench
Class Toolsmith.ToolTinkering.Blocks.WorkbenchInventory
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorOffhandDominantInteraction
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorSmithedTools
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorTinkeredTools
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorToolBinding
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorToolBlunt
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorToolHandle
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorToolHead
Class Toolsmith.ToolTinkering.Behaviors.CollectibleBehaviorToolPartWithHealth
Class Toolsmith.Server.ServerCommands
Class Toolsmith.Properties.Resources
Class Toolsmith.Config.ToolsmithPart
Class Toolsmith.Config.HandlePartDefines
```

其余 43 个类型未在此列出；可按维护说明重新分析程序集。

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 44 个配方文件与 7 个手册章节](/reference/recipes/toolsmith)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
