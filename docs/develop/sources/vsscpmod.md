<!-- generated:start -->
# 文明补丁源码索引

[返回模组介绍](/mods/entries/vsscpmod)

## 源码实现矩阵（当前源码树）

以下 49 个 C# 文件从 `E:\vintagestory\Seraph Civilization Patches` 的 `src` 目录逐文件扫描生成。每行给出声明类型、前若干可见方法和 SHA-256 前 12 位；完整文件清单与核验状态见[源码盘点](/develop/source-inventory)。源码文件存在不代表该路径在当前配置中启用，运行时仍需看依赖检测、能力所有权和配置校验。

### 如何从矩阵定位功能

| 玩家看到的系统 | 源码目录/文件前缀 | 服务器/开发者关注点 |
| --- | --- | --- |
| 石板搬运/货舱 | `Quarry*.cs`、`EntityQuarryDrag.cs` | 石板内容统计、负重阈值、拖拽实体与船货舱布局 |
| 制作与容器兼容 | `RknCrafting*.cs`、`ChiselTools*.cs`、`Toolsmith*.cs`、`*Cooking*.cs` | 目标模组检测、配方/容器匹配和恢复命令 |
| 地图、坐标与信息 | `Information*.cs`、`CoordinateDisplay.cs`、`ImmersiveMapWaypointRenderer.cs` | 服务端信息限制、地图航点和客户端渲染 |
| 载具、外观和绘图 | `Cape*.cs`、`VintageCanvas*.cs`、`QuarryShip*.cs` | 网格恢复、纹理/绘制兼容和船体面片 |
| 等级、体能与快捷键 | `Leveling*.cs`、`Jaunt*.cs`、`Komet*.cs` | 技能面板/效果、耐力 HUD、字体与按键 |

### 逐文件索引

#### `根目录/`

| 文件 | 类型声明 | 主要方法（索引） | SHA-256 前 12 位 |
| --- | --- | --- | --- |
| `BillpostingFontCompatibility.cs` | `BillpostingFontCompatibility` | `TryCreate, SetTextFont, UseClientFormatFont, ClientFontName, Dispose` | `a4c2d0004a8c` |
| `BillpostingInteractionCompatibility.cs` | `BillpostingInteractionCompatibility` | `TryCreate, Place, Initialized, RefreshText, Take, Dispose` | `23a3824fab2b` |
| `BodyPhysMigration.cs` | `BodyPhysMigration` | `readonly, TryCreate, BeforeReady, Migrate, ReadNutrients, NewSave, Validate, Get` | `dff471bdd184` |
| `CandelaClickUpTorchesCompatibility.cs` | `CandelaClickUpTorchesCompatibility` | `TryCreate, UseDropsForTorchPickup, RestorePickupMode, Dispose` | `f09759941735` |
| `CapeRecipePatchCompatibilitySystem.cs` | `CapeRecipePatchCompatibilitySystem` | `ExecuteOrder, ShouldLoad, AssetsLoaded` | `d4a82732a91e` |
| `CapeRenderCompatibility.cs` | `CapeRenderCompatibility, RetryState, RenderState` | `RenderState, TryCreate, BeforeRegenMipMaps, BeforeRender, AfterRender, Dispose` | `1f1e7eda93c9` |
| `ChiselToolsHandPlanerCompatibility.cs` | `ChiselToolsHandPlanerCompatibility` | `TryCreate, AfterSetToolMode, BeforeUse, PreparePlaneHit, Dispose` | `62cac1ff890f` |
| `ChromiumSulfateCookingCompatibility.cs` | `ChromiumSulfateCookingCompatibility` | `TryCreate, UseCookingTemperature, Dispose` | `5c1865967c46` |
| `ClientMeshRecovery.cs` | `ClientMeshRecovery, RetryState, ToolState` | `ToolState, Usable, TryCreate, BeforeDeadHide, BeforeTool, RejectEmptyMesh, AfterTool, TrackTesselation` | `aed8e9abe99d` |
| `CoordinateDisplayCompatibility.cs` | `CoordinateDisplayCompatibility` | `TryCreate, HideMapDescription, HideMapFields, HideMapDebugInfo, MarkMapCoordinateInput, HideMapCoordinateInput, BlockHiddenMapInput, FindType` | `2744688828e0` |
| `CraftingCountRenderer.cs` | `CraftingCountRenderer` | `CraftingCountRenderer, OnRenderFrame, RenderCounts, Scan, GetTexture, Dispose` | `451fd76299ec` |
| `CraftingSurfaceAccess.cs` | `CraftingSurfaceAccess` | `TryCreate, GetInventory, GetMatrices, GetAnchor` | `eaffcee73afc` |
| `CreativeTabSelector.cs` | `CreativeTabSelector, ScrollableTabs, CategoryScrollbar` | `OnMouseWheel, TryCreate, Compose, AfterComposeGui, RouteMouseWheel, SyncSelection, Remove, Dispose` | `7ed9692cb6bb` |
| `EntityQuarryDrag.cs` | `EntityQuarryDrag` | `Initialize, UpdateBounds, ReceiveDamage, CanCollect, GetName, GetInfoText, GetInteractionHelp, OnInteract` | `e1b86f0e0534` |
| `EnvelopeEngravingCompatibility.cs` | `EnvelopeEngravingCompatibility` | `TryCreate, UseEngravingMetal, Dispose` | `5ef252cdfd0b` |
| `FenceReinforcementCompatibility.cs` | `FenceReinforcementCompatibility` | `TryCreate, PreserveReinforcement, Dispose` | `923d74bc5189` |
| `FromGoldenCombsCompatibilitySystem.cs` | `FromGoldenCombsCompatibilitySystem` | `ExecuteOrder, Start, BeforeClimate, Dispose` | `4031c5e8e46a` |
| `ImmersiveFibercraftCompatibilitySystem.cs` | `ImmersiveFibercraftCompatibilitySystem` | `ExecuteOrder, AssetsLoaded` | `3be8c22d2571` |
| `ImmersiveMapWaypointRenderer.cs` | `ImmersiveMapWaypointRenderer` | `OnRenderFrame, RenderWaypoints, FindHeldMap, GetIcon, GetFallbackIcon, GetLabel, Draw, LoadIconLocations` | `f61d22a531e2` |
| `InformationDisplayPatches.cs` | `InformationDisplayPatches, TrackedText` | `TrackedText, Patch, KeepMonthAndDay, MonthAndDay, TextKind, FilterInitialText, TrackDynamicText, FilterDynamicText` | `0442822aa6c9` |
| `InformationRestrictions.cs` | `InformationAccessPacket, InformationRestrictionsConfig, InformationRestrictions, Feature` | `PatchCommands, IsRestricted, IsFeatureRestricted, LoadConfig, ChangeAccess, PlayerNowPlaying, PlayerDisconnected, SendAccess` | `501c2cc771eb` |
| `InventoryInputDiagnostics.cs` | `InventoryInputDiagnostics, Frame` | `RunCommand, Start, PatchDialogs, BeginRoute, BeginDialog, EndDialog, EndRoute, RecordRoute` | `1e9f3025e4b7` |
| `JauntStaminaHudCompatibility.cs` | `JauntStaminaHudCompatibility` | `TryCreate, HideHorizontalBar, RenderFilledIcon, RenderPercentage, DisplayOnly, Dispose` | `f849fb8219e0` |
| `KometFontCompatibility.cs` | `KometFontCompatibility, SavedFace` | `SavedFace, TryCreate, FontProperties, ChineseFace, UseChineseFace, UpdateHudFonts, UpdateUiFonts, SetFonts` | `96a83394cdbd` |
| `KometHotkeyCompatibility.cs` | `KometHotkeyCompatibility` | `TryCreate, CaptureHoveredKey, HoveredKey, OnKeyDown, HideClearedMapping, Dispose` | `a2b93a9af419` |
| `KometPrimitiveSurvivalCompatibilitySystem.cs` | `KometPrimitiveSurvivalCompatibilitySystem` | `ExecuteOrder, ShouldLoad, StartPre, KeepGameplayMod, Dispose` | `a533586d79dd` |
| `LevelingEffects.cs` | `LevelingEffects, Definition, Result` | `Definition, Result, Bind, Read, ReadOne, SourceKind, Format, N` | `f0f0d9f18740` |
| `LevelingSkillPanel.cs` | `LevelingSkillPanel, ScrollState, WindowState` | `readonly, ScrollState, WindowState, TryCreate, Validate, WindowHeight, ComposeWindow, RefreshWindow` | `f116a2408ddb` |
| `LevelingSurvivalCompatibility.cs` | `LevelingSurvivalCompatibility` | `Enabled, TryCreate, Append, CreateMetric, RequireMethod, RequireProperty, Dispose` | `cfe72ae694e0` |
| `LoggingCarryOnCompatibility.cs` | `LoggingCarryOnCompatibility` | `TryCreate, IsTrunk, CheckPlayerAttachment, InventoryStack, HasContents, CanPlace, CopyInventory, RepairCarried` | `3ad55c1408b2` |
| `LoggingProgressCompatibility.cs` | `LoggingProgressCompatibility, ActiveInteraction` | `ActiveInteraction, TryCreate, AfterStep, AfterClear, OnTick, Clear, Dispose` | `a3b986351e7f` |
| `LongTermFoodMealCompatibilitySystem.cs` | `LongTermFoodMealCompatibilitySystem` | `ExecuteOrder, AssetsLoaded, Parse, PreparePorridge` | `e07f2cbab004` |
| `ModCommands.cs` | `ModCommands` | `Root` | `d6391cebe440` |
| `PieBarrelTextureCompatibility.cs` | `PieBarrelTextureCompatibility` | `TryCreate, UsePieCrust, Dispose` | `deb78dfdf5fc` |
| `QuarryCargoLayout.cs` | `QuarryCargoLayout, Cell, Footprint, CargoShape` | `Cell, Footprint, Register, TryGet, HasLayout, AccurateRearOccupancy, Plan, OccupiedBy` | `49dfa46719a3` |
| `QuarryCarryCompatibility.cs` | `QuarryCarryConfig, QuarryCarryCompatibility, LoadCache` | `Normalize, TryCreate, CountBlocks, SpeedFactor, StorageFlags, CountCarried, ReadLoad, AddStack` | `906c9536e312` |
| `QuarryContainerRecovery.cs` | `QuarryContainerRecovery, State` | `Queue, BeforeOpen, Recover` | `65bce1989883` |
| `QuarryDragCompatibility.cs` | `QuarryDragCompatibility, Binding` | `Binding, TryCreate, FreeBinding, EmptyHands, SelectThroughGrass, CoveredPlant, SolidCollision, ClipSolid` | `9f0058e2ea81` |
| `QuarryDragRenderer.cs` | `QuarryDragRenderer` | `QuarryDragRenderer, DoRender3DOpaque, SetShadowMatrix, EnsureLayout, EnsureWrapping, ChainClearance, BuildWrapping, Tube` | `01fcf053bc56` |
| `QuarryLoadShaders.cs` | `QuarryLoadShaders` | `Get, Create, Prepare, Reload, Dispose` | `6df05b41c958` |
| `QuarryShipCompatibility.cs` | `QuarryShipCargoBehavior, QuarryShipCompatibility, VehicleCargoSlot, QuarryShipCargoSlot` | `QuarryShipCargoBehavior, OnLoaded, IsSlab, IsShip, IsCart, IsAttachable, GetCategoryCode, GetAttachedShape` | `6aef7d7e5358` |
| `QuarrySlabLayout.cs` | `QuarrySlabLayout, MeasurementTextures` | `QuarrySlabLayout, Measure, StoneFaces, Bounds` | `d9de68bbf689` |
| `RknCraftingCompatibility.cs` | `RknCraftingCompatibility, Snapshot` | `TryCreate, Install, RequireMethod, For, RememberStartedCrafting, RememberClientCrafting, CheckHotbarChange, StopChangedCraftingStep` | `08bb95f67bc4` |
| `RknFloatingCountCompatibility.cs` | `RknFloatingCountCompatibility` | `TryCreate, RenderBuiltin, Dispose` | `ca3fe9eec2e7` |
| `SeaweedPatchCompatibilitySystem.cs` | `SeaweedPatchCompatibilitySystem` | `ExecuteOrder, ShouldLoad, AssetsLoaded` | `ba57ffe7147d` |
| `SeraphCivilizationPatchesSystem.cs` | `SeraphCivilizationPatchesSystem` | `ExecuteOrder, UseIndependentMaps, Start, StartServerSide, StartClientSide, Dispose` | `073ba22fdd18` |
| `ToolsmithCraftingCompatibility.cs` | `ToolsmithCraftingCompatibility` | `TryCreate, Ignored, FilterHandleInputs, ValidateRknHandle, SafeHandleRecipe, Lookup, TextField, Dispose` | `f70de41e2c57` |
| `VintageCanvasPaintCompatibility.cs` | `VintageCanvasPaintCompatibility` | `TryCreate, Patch, PrepareHeldSelection, PrepareEndSelection, InteractStep, PrepareSelection, ResolveBlock, ValidateDecorSurface` | `d6fe3fefb684` |
| `VintageCanvasTextureCompatibility.cs` | `VintageCanvasTextureCompatibility` | `TryCreate, CanUpdateAtlas, Dispose` | `def7ec1be3b2` |
<!-- generated:end -->
