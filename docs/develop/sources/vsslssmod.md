<!-- generated:start -->
# 生存模拟源码索引

[返回模组介绍](/mods/entries/vsslssmod)

## 源码实现矩阵（当前源码树）

以下 249 个 C# 文件从 `E:\vintagestory\Seraph Living Survival Simulation` 的 `src` 目录逐文件扫描生成。每行给出声明类型、前若干可见方法和 SHA-256 前 12 位；完整文件清单与核验状态见[源码盘点](/develop/source-inventory)。源码文件存在不代表该路径在当前配置中启用，运行时仍需看依赖检测、能力所有权和配置校验。

### 如何从矩阵定位功能

| 玩家看到的系统 | 源码目录/文件前缀 | 服务器/开发者关注点 |
| --- | --- | --- |
| 核心生理 | `Seraph.Core/Framework/*.cs`、`Simulation/*.cs`、`State/*.cs` | 纯模拟状态、时间步、摄入/能量/体温/血液账本 |
| 服务端桥接 | `Seraph/Server/*.cs` | 原版事件转为已验证适配器输入，所有生理写入在服务端完成 |
| 水、污染与设施 | `Seraph/World/Water*.cs`、`Block*.cs`、`Pollution*.cs`、`Latrine*.cs` | 水批次、处理设备、井/浴缸/厕所、污染路径 |
| 玩家窗口与 HUD | `Seraph/Client/*.cs` | C 键面板、营养手册、趋势、固定窗口、症状与调试显示 |
| API 与能力 | `Seraph.Application/*.cs`、`TreatmentApi.cs` | 治疗注册、能力所有权、适配器证据、设置修订号 |
| 诊断与性能 | `Seraph/Diagnostics/*.cs`、`Seraph.DebugUI/*.cs` | `.slssperf`、调试窗口、性能采样和管理员诊断 |

### 逐文件索引

#### `Seraph/`

| 文件 | 类型声明 | 主要方法（索引） | SHA-256 前 12 位 |
| --- | --- | --- | --- |
| `Seraph/Client/ActionProgressPresentation.cs` | `ActionProgressPresentation` | `Update, Reset` | `5f3bb75d4a6a` |
| `Seraph/Client/ActionRingRenderer.cs` | `ActionRingRenderer` | `Render, EnsureResources, Reload, ClearText, Dispose` | `920778540445` |
| `Seraph/Client/ActivityHud.cs` | `ActivityHud` | `ActivityHud, ShouldReceiveKeyboardEvents, ShouldReceiveMouseEvents, ToggleDebug, ResetDebug, CreateBounds, LedgerFont, FormatLedger` | `5090f5407dd8` |
| `Seraph/Client/AdrenalineAudio.cs` | `AdrenalineAudio` | `DangerSound, Gain, Tick, Reset, Dispose` | `74004d91500a` |
| `Seraph/Client/AdrenalineHud.cs` | `AdrenalineHud, AdrenalineDisplay` | `ShouldReceiveKeyboardEvents, ShouldReceiveMouseEvents, CaptureAllInputs, TryClose, Remaining, Prepare, OnRenderGUI, Reset` | `9bee406d5095` |
| `Seraph/Client/BedRestText.cs` | `BedRestText` | `Describe` | `9bf564d8ed55` |
| `Seraph/Client/BodyRenderer.cs` | `BodyStage, BodyRenderer, Artwork` | `Dispose, Release, VisualKey, Stage, HitTest, Draw` | `fe008a3ee025` |
| `Seraph/Client/BodyStatusHud.cs` | `BodyStatusHud` | `BodyStatusHud, ShouldReceiveKeyboardEvents, ShouldReceiveMouseEvents, ToggleVisibility, Update, IsVisibleByDefault, Refresh, Compose` | `386920d5bc4a` |
| `Seraph/Client/CairoTextureUpload.cs` | `CairoTextureUpload` | `Update` | `accc6b2f068f` |
| `Seraph/Client/CharacterImmunePanel.cs` | `CharacterPanelIntegration` | `DiseaseRows, ComposeMetricGrid, ComposeImmuneSystem, PositionImmuneContent, RefreshImmuneSystem` | `491a35981d2d` |
| `Seraph/Client/CharacterMetricsPanel.cs` | `CharacterPanelIntegration` | `MetricKeys, FunctionColumns, MetricRowHeight, Metrics, Metric, ComposeMetrics, ComposeBloodCirculation, ComposeEnergyBalance` | `7c1b430eecb9` |
| `Seraph/Client/CharacterPanelIntegration.cs` | `CharacterPanelIntegration, Panel, PanelHeights` | `DetailsKey, OnLevelReady, OnLeaveWorld, TryRegister, ClearCaches, RemoveOwnedPanels, ComposeExtraPanels, PanelHeights` | `3ceeef33732e` |
| `Seraph/Client/ClosedEyeOrientation.cs` | `ClosedEyeOrientation` | `ClosedEyeOrientation, TryTurn` | `dd71c13c7445` |
| `Seraph/Client/ClosedEyeRestBehavior.cs` | `ClosedEyeRestBehavior` | `ClosedEyeRestBehavior, PropertyName, OnGameTick, OnEntityDespawn, Stop` | `8b94d587dda3` |
| `Seraph/Client/ClosedEyeRestDisplay.cs` | `ClosedEyeRestDisplay` | `Values, Create` | `91358c357f60` |
| `Seraph/Client/DarkAdaptationRenderer.cs` | `DarkAdaptationRenderer` | `Sample, Brightness, Reset, OnRenderFrame, Draw, Restore, EnsureResources, Reload` | `0f156d8e221b` |
| `Seraph/Client/DarkAdaptationSparkles.cs` | `DarkAdaptationSparkles` | `DarkAdaptationSparkles, Reset, Render, Dispose` | `c15d49c33fe4` |
| `Seraph/Client/DarkAdaptationState.cs` | `DarkAdaptationState` | `Advance, Strength, Reset` | `71e97027e24c` |
| `Seraph/Client/ExertionPrediction.cs` | `SeraphClientBridge` | `DiscreteWorkAllowed, PredictDiscreteWork, ResetWorkPrediction, ReceiveExertion, PredictedFunctions, ProjectFunctions, PredictWork, PredictHeldWork` | `8c0ea45bef1b` |
| `Seraph/Client/EyeClosureCycle.cs` | `EyeClosureCycle` | `（无可索引的显式方法）` | `857ee166fcad` |
| `Seraph/Client/FoodInfoBehavior.cs` | `FoodInfoBehavior` | `GetHeldItemInfo, AppendWaterInfo, AppendFoodInfo, N, L` | `8cd0b21f8ca2` |
| `Seraph/Client/FoodKnowledgeCompatibility.cs` | `FoodKnowledgeCompatibility` | `IsKnownToPlayer, ShouldList` | `cdde13d4f469` |
| `Seraph/Client/GroundwaterParticleRenderer.cs` | `GroundwaterParticleRenderer, RevealKey, GroundwaterRevealState, Face` | `RevealKey, Reveal, Clear, Tick, SpawnExcavationParticles, Face, Dispose` | `1b70fe26d855` |
| `Seraph/Client/LoadVisuals.cs` | `LoadVisuals` | `LoadVisuals, readonly, Evaluate, Curve, Approach` | `21a22ce5f2fd` |
| `Seraph/Client/MetricTrendDisplay.cs` | `MetricTrendDisplay, Binding` | `Binding, For, Bind, Tick, Reset, Direction, Symbol, AfterBar` | `1af4156a158d` |
| `Seraph/Client/NativeCharacterScrollbars.cs` | `NativeCharacterScrollbars` | `HideUnused, HasOverflow, Dispose` | `055fe4dfc1e5` |
| `Seraph/Client/NativeFoodTooltips.cs` | `NativeFoodTooltips` | `Ready, BandageInfo, Pattern, StripBase, StripMeal, Dispose` | `88ea09518102` |
| `Seraph/Client/NativeHudReplacement.cs` | `NativeHudReplacement` | `RenderNative, Dispose` | `cb710cbc37b7` |
| `Seraph/Client/NativeProgressDisplay.cs` | `NativeProgressDisplay, NativeProgressApi` | `NativeProgressDisplay, Update, Render, Dispose, Wrap, Invoke` | `77ac9c5115fa` |
| `Seraph/Client/NativeWaterInfoHud.cs` | `NativeWaterInfoHud` | `RefreshSoon, RegisterContainers, RegisterContainerTypes, FindField, FindMethod, Every15Prefix, ComposePrefix, ComposePostfix` | `2bc57b0bf0d8` |
| `Seraph/Client/NativeWorkTransport.cs` | `SeraphClientBridge` | `AcceptedMining, AcceptedAttack, FlushMining` | `706e5759b297` |
| `Seraph/Client/NutritionHandbookDialog.cs` | `NutritionHandbookDialog, Entry, CategoryTabs` | `Entry, OnGuiClosed, BuildEntries, Compose, Filter, Sort, OnMouseDown, OnMouseUp` | `6b14a4cd057c` |
| `Seraph/Client/NutritionItemSlot.cs` | `NutritionItemSlot` | `NutritionItemSlot, OnMouseDownOnElement, ComposeElements, RenderInteractiveElements, Dispose` | `59cab897f9e0` |
| `Seraph/Client/NutritionPanel.cs` | `CharacterPanelIntegration` | `DigestionRadius, DigestionHeight, ComposeNutritionModel, ComposeNutritionDetails, NutrientText, ScoreText, DisplayNutrient, NutrientHelp` | `0e658dd188ea` |
| `Seraph/Client/PinnedCharacterPanels.cs` | `CharacterPanelIntegration, PinnedCharacterPanelsHud, PinnedPanelTitleBar, CharacterPanelHoverText, CharacterPanelHoverExtensions` | `OwnedComposer, IsPanelVisible, CanRenderPinnedPanels, AddPinnedTitleBar, TogglePinnedPanel, UpdatePinnedHud, OnCharacterClosed, RenderPinnedPanels` | `4c4935d0843d` |
| `Seraph/Client/PlayerPhysicsCompatibility.cs` | `PlayerPhysicsCompatibility` | `HasWalkableEntities, SimPhysicsFinalizer, RenderFrameFinalizer, SuppressTransitionNullReference, Dispose` | `abcc3d849374` |
| `Seraph/Client/PollutionDebugHighlights.cs` | `PollutionDebugHighlights` | `Update, Clear, Dispose` | `c19a63dd672d` |
| `Seraph/Client/SeraphClientBridge.cs` | `SeraphClientBridge` | `WarnExhaustion, GetSymptomSnapshot, OnLevelReady, RegisterAction, OnLeaveWorld, OpenNutritionHandbook, LogWaterInfo, WaterBlockChanged` | `db4714461335` |
| `Seraph/Client/SmithingTooltipCompatibility.cs` | `SmithingTooltipCompatibility` | `ReplaceMatcher, Match, Compile, Dispose` | `201d1267eb34` |
| `Seraph/Client/StatusIconLayout.cs` | `StatusIconLayout, Obstacle, Placement` | `Obstacle, Placement, ActiveMask, Place, Shake` | `b5ee3c4d98c7` |
| `Seraph/Client/StatusIconsHud.cs` | `SurvivalHud` | `ComposeStatusIcons, IconHover, DrawStatusIcon, RefreshStatusIcons, PositionStatusIcons, ReleaseStatusArt, RenderDarkAdaptationSparkles` | `7f4b60a21991` |
| `Seraph/Client/SurvivalHud.cs` | `SurvivalHud` | `SurvivalHud, UpdatePressure, ShouldReceiveKeyboardEvents, OnMouseDown, OnMouseUp, OnMouseMove, ToggleVisibility, Update` | `0292ed232870` |
| `Seraph/Client/SymptomPostProcess.cs` | `SymptomPostProcess` | `Render, SetEnabled, NeedsSceneCopy, DrawDefocus, DrawRest, ClearRest, PrepareNotice, DrawNotice` | `efbe3904aeca` |
| `Seraph/Client/SymptomRegions.cs` | `ScreenRegion, SymptomRegions` | `ScreenRegion, Intersect, IsProtected, HasMenu, Menus, Outside` | `be369749e26a` |
| `Seraph/Client/SymptomRenderer.cs` | `SymptomRenderer` | `RenderGuis, AfterPerception, AfterWindowRender, Reset, Advance, TurnAtClosure, Severity, RenderFinalFrame` | `02d61e24547e` |
| `Seraph/Client/TooltipText.cs` | `TooltipText, PanelKey` | `PanelKey, Help, Panel, ClearPanelCache, Item, InitializeMainThread, Wrap, WrapApprox` | `97742849fc76` |
| `Seraph/Diagnostics/KometTimingBridge.cs` | `KometTimingBridge, ITimer, Timer, Scope` | `Initialize, Bind, Begin, End, Scope, Dispose` | `e7059a34061e` |
| `Seraph/Diagnostics/LatencyTracker.cs` | `LatencyTracker` | `Begin, Expire, Complete, Clear` | `019979eec75d` |
| `Seraph/Diagnostics/PerformanceCapture.cs` | `PerformanceContext, PerformanceCapture, PerformanceMetric, PerformanceEvent, PerformanceReport` | `Get, Start, Stop, Dispose, PerformanceCapture, Add, Finish, PerformanceEvent` | `f9bfdaea9e73` |
| `Seraph/Diagnostics/PerformanceClient.cs` | `PerformanceClient` | `Start, Ready, Leave, ResetSamples, Tick, OnRenderFrame, SnapshotReceived, WaterReceived` | `7fd622042777` |
| `Seraph/Diagnostics/PerformanceRecorder.cs` | `PerformanceRecorder` | `Start, RenewLease, Tick, Stop, Dispose` | `9c14a53f61b3` |
| `Seraph/LocalizedText.cs` | `LocalizedText, owns` | `Get, GetL, TryGet, TryGetL` | `0ba147abb5b1` |
| `Seraph/Network/PerformanceProtocol.cs` | `PerformancePing, PerformancePong` | `（无可索引的显式方法）` | `43821423067b` |
| `Seraph/Network/Protocol.cs` | `Protocol, OrganicMistParticle, NativeWorkReceipt, WaterInfoRequest, WaterInfoResponse, GroundwaterReveal, FoodCatalogMessage, ClientHello` | `（无可索引的显式方法）` | `27ba7f03c64b` |
| `Seraph/Properties/AssemblyInfo.cs` | `（顶层注册/补丁逻辑）` | `（无可索引的显式方法）` | `481343b905c2` |
| `Seraph/SeraphModSystem.cs` | `SeraphModSystem` | `OpenNutritionHandbook, Start, AssetsFinalize, DrinkFromContainer, StartPre, StartServerSide, StartClientSide, Dispose` | `e1561a3d2284` |
| `Seraph/Server/ActivityCompatibility.cs` | `ActivityObservation, ActivityBridgeStatus, ActivityCompatibility` | `ActivityObservation, ActivityBridgeStatus, ControllerSeat, TriggerHeld, Observe, Idle, Status` | `d06b041a2828` |
| `Seraph/Server/AdrenalineAttackTiming.cs` | `AdrenalineAttackTiming` | `Tag, TagCode, Progress` | `64215c6cb793` |
| `Seraph/Server/BleedingVisualBridge.cs` | `BleedingVisualBridge` | `AllowExternal, Owns, AttachParticles, InitializeParticles, Sync, Dispose` | `6dde2ece7237` |
| `Seraph/Server/CalendarSettlement.cs` | `ServerCoordinator, NativeCalendarBridge` | `NotifySleepDanger, ObserveNativeSleep, ResetSleepTimeline, RestoreNativeTiredness, ResetCalendarBaseline, SleepRisks, ProjectSleep, ProjectBedRest` | `22021f73f17b` |
| `Seraph/Server/CharacterMetrics.cs` | `ServerCoordinator` | `Metric, StatusMetrics, FunctionMetrics, MobilityMetric, TemperatureMetrics, ClothingMetric, RecoveryMetrics, DescribeDisease` | `9f167a9dcc5c` |
| `Seraph/Server/CharacterPanelProjection.cs` | `ServerCoordinator` | `NutrientProjection, PanelNumber, Indicator, PanelNutritionLines, PanelHydrationLines, PanelWoundLines` | `68a13ffc7da8` |
| `Seraph/Server/ClinicalCoordinator.cs` | `ServerCoordinator, HeldPressure, PendingWash` | `HeldPressure, PendingWash, WashActionKey, WashAction, WashMessage, WashBusy, WashKind, OwnsThermal` | `21d61faa4822` |
| `Seraph/Server/ClosedEyeRest.cs` | `ServerCoordinator` | `ToggleClosedEyeRest, ValidateClosedEyeRest, ClearClosedEyeRest` | `e7a9718dcce4` |
| `Seraph/Server/CraftedFoodNutrition.cs` | `CraftedFoodNutrition` | `Supported, Read, Capture, Combine, Transfer, Write` | `aa8aee7fae09` |
| `Seraph/Server/ExertionCoordinator.cs` | `ServerCoordinator` | `Moving, SprintIntent, WorkInterval, JumpAllowed, DiscreteWorkAllowed, EffectiveFunctions, OwnsOxygen, RecordHeldWork` | `28ad1a786cfa` |
| `Seraph/Server/FoodCalibration.cs` | `FoodCalibration` | `Apply, CalibrateAnimal` | `81650cda1b7c` |
| `Seraph/Server/FoodCatalog.cs` | `FoodProfile, provenance, FoodCatalog, FoodDose, ServerCoordinator` | `Excluded, ReviewedFallback, Validate, Find, Composition, MealComposition, SpoilageFraction, SpoilageHazard` | `88ed3a0691e6` |
| `Seraph/Server/FoodCoverage.cs` | `ServerCoordinator` | `ExportFoodCoverage` | `a5b532c4097d` |
| `Seraph/Server/FoodGroupFallback.cs` | `FoodGroupFallback` | `Defaults, Provenance, Profile, EnergyPer100G` | `8b8df5c2d4fd` |
| `Seraph/Server/FoodMicronutrients.cs` | `FoodMicronutrients` | `ValidReserveScale, CombineReserveScales, PointsPer100G` | `3b2e161c642a` |
| `Seraph/Server/FrameworkCoordinator.cs` | `ServerCoordinator` | `StartFramework, ReportRuntimeCompatibility, RefreshCapabilities, AttachObserver, OnSaturation, ApplyIntake, ObserveConfirmedHurt, AdvanceFramework` | `ecf750af28c5` |
| `Seraph/Server/GasTransport.cs` | `IGasTransport, GasTransport` | `Create` | `7cf87e17fbd0` |
| `Seraph/Server/InjuryActions.cs` | `ServerCoordinator` | `ActionFunctions, ExhaustionReason, DeniedLabor, DeniedJump, ClosedEyeTurnEnabled, ClosedEyeAwake, CheckInjuryBlockBreak` | `667e8fe44531` |
| `Seraph/Server/MeasuredSmokeAdapter.cs` | `MeasuredSmokeAdapter` | `Diagnostics, BindQuery, TrySample, Ownership, BeginFirepit, EndFirepit, AllowDrain, Dispose` | `7220e2338e71` |
| `Seraph/Server/MicroclimateAdapter.cs` | `MicroclimateResult, MicroclimateAdapter, RoomCache` | `MicroclimateResult, RoomAirTemperature, Sample, SolarExposure, HeadgearShade, IsHeadgear, AttributeShade, RegionalColdExposure` | `4fa26eb5b668` |
| `Seraph/Server/NativeBandageBridge.cs` | `NativeBandageBridge, Use` | `Use, Started, SuppressesHealing, Owner, Begin, Complete, Finish, Restore` | `ee20537a5067` |
| `Seraph/Server/NativeColdVisuals.cs` | `ServerCoordinator, NativeColdVisuals` | `ProjectColdVisuals, Strength` | `79025ceea6e0` |
| `Seraph/Server/NativeDownedBridge.cs` | `NativeDownedBridge` | `Behavior, Owner, IsActive, Floor, TryEnter, Damage, Healing, RescueAfterConsumedTreatment` | `e613e5187274` |
| `Seraph/Server/NativeFoodBridge.cs` | `NativeFoodBridge, SolidContext, DrinkContext, MealContext, CookingState` | `SolidContext, DrinkContext, MealContext, Owner, SolidStart, SolidStop, ItemReceived, MealStart` | `8aa7d1e2cb2c` |
| `Seraph/Server/NativeInjuryActionBridge.cs` | `NativeInjuryActionBridge, GroundState, HitCycle` | `GroundState, Patch, Functions, Server, Denied, AppliedJumpMultiplier, GroundStart, GroundEnd` | `68a8d080a119` |
| `Seraph/Server/NativeLaborBridge.cs` | `NativeLaborBridge, ChiselTransaction` | `Server, Client, Accepted, Held, End, Allowed, DiscreteAllowed, Speed` | `a361dc4098fa` |
| `Seraph/Server/NativePhysiologyBridge.cs` | `NativePhysiologyBridge, DamageContext` | `DamageContext, CurrentRegion, Patch, Owner, Owned, GetHealth, GetMaximum, SetHealth` | `af7915dd0b32` |
| `Seraph/Server/NativeStatInputs.cs` | `NativeStatInputs` | `Multiplier, PhysiologyMultiplier, SetOwned, ExternalHealth, SourceLabel` | `6e67ab51123e` |
| `Seraph/Server/NativeVehicleBridge.cs` | `NativeVehicleBridge, Permissions, ShipAdapter` | `ShipAdapter, ResolveOptional, ResolveJaunt, JauntInputs, JauntInput, JauntDescending, Patch, Warn` | `a018b8859ace` |
| `Seraph/Server/NativeWorkTransport.cs` | `ServerCoordinator` | `RecordNativeBlockBreak, OnNativeWork` | `f6bb76bf6aba` |
| `Seraph/Server/PathogenExposure.cs` | `ServerCoordinator` | `ExposeIngestion` | `f7c5b0e9a844` |
| `Seraph/Server/PhysiologyObserver.cs` | `PhysiologyObserver` | `PhysiologyObserver, PropertyName, OnEntityReceiveSaturation, OnEntityReceiveDamage` | `c32ebdbcb426` |
| `Seraph/Server/ProduceWashing.cs` | `ServerCoordinator, PendingProduceWash` | `PendingProduceWash, BeginProduceWash, TickProduceWash, CommitProduceWash` | `766ead5c6fa4` |
| `Seraph/Server/ProspectingCompatibility.cs` | `ProspectingCompatibility` | `AfterProbe, Dispose` | `d86de7a01d65` |
| `Seraph/Server/RealSmokeGasTransport.cs` | `RealSmokeGasTransport, FuelMemory` | `Store, BeforeVent, AfterVent, AfterPoint, EmitCombustion, Emit, Sample, Tick` | `acb7a09bee3d` |
| `Seraph/Server/ReleaseConfigFile.cs` | `ReleaseConfigFile` | `（无可索引的显式方法）` | `a9ffa91f0d9b` |
| `Seraph/Server/RuntimeDiagnostics.cs` | `CompatibilityArchive, RuntimeFeature, OneOrManyStringsConverter, RuntimeDiagnostics` | `CompatibilityArchive, RuntimeFeature, Read, Write, RecordRound, WritePerformance, RuntimeFeatures, WriteCompatibility` | `6e676c792269` |
| `Seraph/Server/RusticFoodBridge.cs` | `RusticFoodBridge` | `Install, BeginServing, EndServing, Roux, Root, Set, Main, Liquid` | `c801dc57a68f` |
| `Seraph/Server/SanitationCoordinator.cs` | `ServerCoordinator, NativeSanitationBridge` | `ObserveSanitation, RecordButchering, Before, After, Dispose` | `070d4a254284` |
| `Seraph/Server/ServerCoordinator.cs` | `ClosedEyeRestMode, ServerCoordinator, GroundwaterRevealKey, SessionFaultKind, Session, GroundwaterFace` | `GroundwaterRevealKey, Session, LogProspectingWarning, LogProspectingInfo, TryGetWellSupply, TryExtractWell, TryRefillWell, FindWell` | `180885ed5732` |
| `Seraph/Server/ServerCoordinator.DebugValues.cs` | `ServerCoordinator` | `DebugValues, OnDebugValue, HandleDebugValue, ApplyDebugValue` | `00f00aa50925` |
| `Seraph/Server/ServerCoordinator.Performance.cs` | `ServerCoordinator` | `StartPerformance` | `379783ed93f0` |
| `Seraph/Server/SleepEyes.cs` | `ServerCoordinator` | `AdvanceSleepEyes, EyesClosed, SleepEyeProjection` | `a46120951506` |
| `Seraph/Server/SmokeDoseCoordinator.cs` | `ServerCoordinator` | `TickSmoke, SettleSmokeInjury` | `022a18b92431` |
| `Seraph/Server/TreatmentCoordinator.cs` | `ServerCoordinator, PendingTreatment` | `PendingTreatment, BeginTreatment, QueryTreatment, ContinueTreatment, TreatmentStillValid, CompleteTreatment, CancelTreatment, MedicineSpoiled` | `c079e426f09a` |
| `Seraph/Server/VanillaEnvironmentProbe.cs` | `VanillaEnvironmentProbe` | `Capture, ReadClothing, UsesNativeWearable, ReadCachedHeat, DressName, Local, Number, Clip` | `b79dd3039ead` |
| `Seraph/Server/VitalCoordinator.cs` | `ServerCoordinator` | `OwnsPhysiology, AllowsBedWithoutNativeTiredness, SessionFor, OwnHealth, SyncExternalMaximum, OwnMaxHealth, IsOwnedDowned, CompleteDownedRescue` | `188cf384d091` |
| `Seraph/Server/WaterImmersion.cs` | `WaterImmersion` | `Conductance` | `38748709523a` |
| `Seraph/Server/WorldInteractions.cs` | `ServerCoordinator, PendingDefecation, PendingLatrineDefecation, PendingGroundDrink, PendingWellBucketRaise, WaterSource` | `PendingDefecation, PendingLatrineDefecation, PendingGroundDrink, PendingWellBucketRaise, WaterSource, PreferredManureStorage, HasNaturalFertilizer, OnWorldAction` | `369dddebc00c` |
| `Seraph/SlowCallbackProbe.cs` | `SlowCallbackProbe, Measurement` | `SlowCallbackProbe, Measure, Record, Dispose` | `18252c16f100` |
| `Seraph/TreatmentApi.cs` | `TreatmentUseResult, SeraphModSystem` | `TreatmentUseResult, ReadHerbalWater, RegisterTreatment, RegisterTreatmentV1, QueryTreatment, BeginTreatment, ContinueTreatment, CompleteTreatment` | `dba6d0b35a81` |
| `Seraph/World/BedRestProperties.cs` | `BedRestProperties` | `Quality` | `2debe46cddf5` |
| `Seraph/World/BlockBathtub.cs` | `BlockBathtub, PlacementSnapshot, BlockEntityBathtub` | `GetPlacedBlockInteractionHelp, CreateInteractionHelp, OnUnloaded, IsCopper, PartCode, Direction, GetCollisionBoxes, GetSelectionBoxes` | `4434bcf684d0` |
| `Seraph/World/BlockEntityChimney.cs` | `BlockChimney, BlockChimneyPart, BlockEntityChimney` | `OnHeldInteractStart, TryPlaceBlock, CanPlaceBlock, CanEmbedAt, IsFullSolidCube, GetDrops, GetHeldItemInfo, GetPlacedBlockInfo` | `035ee5f3fe46` |
| `Seraph/World/BlockEntityWaterTreatment.cs` | `BlockEntityWaterTreatment` | `Initialize, Changed, Interact, TransferHeld, Liquid, Tick, HasPipe, DirectBathBelow` | `7107a33ce494` |
| `Seraph/World/BlockEntityWellWall.cs` | `BlockEntityWellWall` | `Initialize, RefreshServerState, OnTesselation, ToTreeAttributes, FromTreeAttributes, OnBlockRemoved, OnBlockUnloaded` | `33020df2ba4b` |
| `Seraph/World/BlockLatrine.cs` | `BlockLatrine, BlockEntityLatrine` | `GetCollisionBoxes, TryPlaceBlock, GetSelectionBoxes, DoPartialSelection, GetPlacedBlockName, OnBlockInteractStart, GetPlacedBlockInfo, OnTesselation` | `be851c76d8e4` |
| `Seraph/World/BlockWaterTreatment.cs` | `BlockWaterTreatment` | `readonly, PipePos, BasinPos, Half, TryPlaceBlock, Place, Bounds, GetSelectionBoxes` | `d5418908916f` |
| `Seraph/World/BlockWellHead.cs` | `BlockWellHead, BlockEntityWellHead` | `TryPlaceBlock, GetPlacedBlockInteractionHelp, OnUnloaded, OnBlockInteractStart, OnBlockInteractStep, OnBlockInteractStop, OnBlockInteractCancel, GetPlacedBlockInfo` | `942c25fcbe75` |
| `Seraph/World/ChimneyHost.cs` | `ChimneyHost` | `Set, Resolve, Read, Write, Drops, Render` | `3937c3d675c4` |
| `Seraph/World/ChimneyInstallation.cs` | `ChimneyInstallationPlan, ChimneyGeometry` | `ChimneyInstallationPlan, Execute, Opening, FullHost` | `41fecb20eb9e` |
| `Seraph/World/ChunkPollutionStore.cs` | `PollutionChunk, PollutionSnapshot, ChunkPollutionStore, LocalSource, Residue, Column, Scan, BlockSource` | `PollutionChunk, PollutionSnapshot, LocalSource, Residue, Scan, BlockSource, OnSourceEntity, OnSourceDespawn` | `e1112e7c3071` |
| `Seraph/World/ChunkPollutionStore.Ponds.cs` | `ChunkPollutionStore, PondCell` | `PondCell, PondAt, AdvancePonds, MixPonds, TransferToPonds, RestorePonds` | `635d1975ec98` |
| `Seraph/World/ClosedEyePose.cs` | `ClosedEyePose` | `Create` | `b285d8ba5e26` |
| `Seraph/World/CottageWaterCompatibility.cs` | `CottageWaterCompatibility, Binding, Transfer` | `Binding, Get, Set, Transfer, Attach, Enabled, BeginHeld, BeginPoured` | `71f2296248c3` |
| `Seraph/World/DefecationPose.cs` | `DefecationPose` | `Create` | `9fb509fd7177` |
| `Seraph/World/FixtureInteriorSurface.cs` | `FixtureInteriorSurface` | `Build` | `21498c1123a9` |
| `Seraph/World/FixtureOrientation.cs` | `FixtureOrientation, PlacementScope` | `Placement, Dispose, Facing, Rotate, Boxes, Mesh, BathPartner, BathOffset` | `3aa14d49315a` |
| `Seraph/World/FixtureWaterMesh.cs` | `FixtureWaterMesh` | `Finish` | `eef28c32439a` |
| `Seraph/World/GroundwaterExposureScan.cs` | `GroundwaterExposureScan` | `Visit` | `911f510c8bc3` |
| `Seraph/World/GroundwaterWorldStore.cs` | `GroundwaterWorldStore, RegionKey, Entry, SaveEnvelope, SaveEntry, TerrainMetrics` | `RegionKey, TerrainMetrics, Loaded, Unloaded, ResetColumn, Dispose, Query, TryExtract` | `addb0b4a5a7d` |
| `Seraph/World/ItemManure.cs` | `ItemManure` | `GetMergableQuantity, TryMergeStacks, GetHeldItemInfo` | `b637e3235ec1` |
| `Seraph/World/LatrineSeat.cs` | `BlockEntityLatrine` | `AnyMounted, CanMount, CanUnmount, Initialize, OnSeatAction, DidMount, DidUnmount, MountableToTreeAttributes` | `5ee6b42717dc` |
| `Seraph/World/LatrineWasteStorage.cs` | `LatrineWasteStorage` | `LatrineWasteStorage, IsManure, Read, FindBarrel, Matches, Add` | `bc080a48f2e5` |
| `Seraph/World/ManureGroundStorage.cs` | `ManureGroundStorage` | `ManureGroundStorage, Resolve, ResolveFallback, InventoryQuantity, TryRead, Add, ContainsManure` | `125522d83e8e` |
| `Seraph/World/ManureMass.cs` | `ManureMass` | `PerItem, Total, Mix` | `3e8ffa08e13c` |
| `Seraph/World/NativeAshGeneration.cs` | `NativeAshGeneration` | `EnsureSlot, NewSlot, BurnTick, AfterFuelDecrement, Dialog, AddSlot, Authorize, Dispose` | `b58c5b35bbbb` |
| `Seraph/World/NativeCropPollution.cs` | `NativeCropPollution, Cursor` | `Growth, Interval, Read, ReadForInfo, InfoLevel, Write, Harvest, Edible` | `3fe7e8b3c10e` |
| `Seraph/World/NativeManureFertilizer.cs` | `NativeManureFertilizer` | `Inputs, Scale, Dispose` | `7f8db7d730d4` |
| `Seraph/World/NativeStoneFirepit.cs` | `NativeStoneFirepit, UpgradeState` | `IsStoneBlock, Installed, State, Interact, IsLooseStone, AddInteractionHelp, Notify, BurnDuration` | `7d70b6b5db78` |
| `Seraph/World/NativeWaterDistillation.cs` | `NativeWaterDistillation` | `Enabled, Receive, BoilerInteract, FirepitInteract, GiveSalt, Drops, Dispose` | `1f303036bea6` |
| `Seraph/World/NativeWaterHeating.cs` | `NativeWaterHeating` | `Dispose, Vessel, Enabled, CanHeat, Heat, Temperature` | `eeda758b4639` |
| `Seraph/World/NativeWaterInventoryTransfer.cs` | `NativeWaterTransfer` | `WaterStackMerge, DrawFromCookingSlot, PourIntoCookingSlot` | `6976af661377` |
| `Seraph/World/NativeWaterTransfer.cs` | `NativeWaterTransfer, WellFillContext` | `WellFillContext, WaterStackMergableQuantity, ComparableWater, RegisterBlocks, Dispose, Enabled, BathtubInteract, DrinkableWater` | `ef7cafe0244b` |
| `Seraph/World/OrganicPollutionSource.cs` | `OrganicPollutionSource` | `IsFantasy, IsPlayerCorpse, IsRot, IsButcherCorpse, IsButcherRemains, Kind, Containment, DecayQuantity` | `2005910e79f8` |
| `Seraph/World/PathogenMetadata.cs` | `PathogenMetadata` | `Read, Write, Shed` | `531223cb0f37` |
| `Seraph/World/PathogenStackMerging.cs` | `PathogenStackMerging, MergeState` | `MergeState, MergableQuantity, HasPathogenData, MergeStart, MergeDone, Dispose` | `3995571f26bb` |
| `Seraph/World/PollutionChangeBridge.cs` | `PollutionChangeBridge` | `Dirty, BeforeMove, AfterMove, Dispose` | `55725aff7212` |
| `Seraph/World/PollutionMapLayer.cs` | `PollutionMapLayer, MapSample, View` | `MapSample, View, OnLoaded, OnMapOpenedClient, OnMapClosedClient, OnTick, AfterWorldMapMouseMove, OnMapOpenedServer` | `392ca44e7eef` |
| `Seraph/World/PollutionPlantCache.cs` | `PollutionPlantCache, Contact, Key, Job` | `PollutionPlantCache, Contact, Key, Job, At, Advance, Invalidate` | `4d68cd46bd97` |
| `Seraph/World/PollutionRouteCache.cs` | `PollutionRouteCache, Cell, Route` | `PollutionRouteCache, Cell, Route, Key, Request, Weight, Invalidate, Advance` | `4ae54306a88c` |
| `Seraph/World/PollutionText.cs` | `PollutionText` | `Agent, Water, MapWaterStatus, Levels, Sources, Region` | `4bf37da4b068` |
| `Seraph/World/PollutionVegetation.cs` | `PollutionPlant, PollutionVegetation` | `PollutionPlant, Bind, Classify` | `91e012e45546` |
| `Seraph/World/RecipeMetadataCompatibility.cs` | `RecipeMetadataCompatibility` | `HandbookTypes, Comparable, CookingEquals, IngredientEquals, HandbookEquals, Report, UnknownKeys, CookingComparisons` | `8ee00477da9b` |
| `Seraph/World/SaltResidueBehavior.cs` | `SaltResidueBehavior` | `SaltResidueBehavior, ToTreeAttributes, FromTreeAttributes, OnBlockPlaced, GetBlockInfo, Safe` | `f93748e7b0c4` |
| `Seraph/World/SurfaceWaterClassifier.cs` | `SurfaceWaterClassifier, Pond, Job` | `Pond, PondAt, Job, Query, IsMappedRiver, InvalidateAt, Invalidate, IsRiver` | `89cc75f2b22f` |
| `Seraph/World/TreatmentSlot.cs` | `TreatmentKind, FilterMaterial, TreatmentSlot` | `FilterMaterial, Resolve, Valid, Matches, TryInsert, Product, Consume, Accept` | `66c852284d46` |
| `Seraph/World/VomitPose.cs` | `VomitPose` | `Create` | `ff65d4948e5e` |
| `Seraph/World/WaterInfoBehavior.cs` | `WaterInfoBehavior` | `WaterInfoBehavior, GetPlacedBlockInfo` | `562d4ab18057` |
| `Seraph/World/WaterInfoText.cs` | `WaterInfoText, on` | `Lines` | `6060db7e3203` |
| `Seraph/World/WaterInteractionTarget.cs` | `WaterInteractionTarget` | `Find, IsWaterBucket, IsWaterContainer, IsSurfaceWater, FindForHover, IsWaterBed, FindSurfaceWaterAlongLook, FindWaterInLookDirection` | `84db53648f8c` |
| `Seraph/World/WaterQuality.cs` | `WaterQuality, WorldCache, StoredWaterCooling, WaterMetadata` | `BindClassifier, Classifier, BindPollution, PollutionAt, DiseaseSourcesAt, ConfiguredRespiratorySourcesAt, RegionAt, ExtractionRollback` | `ad337c9101dd` |
| `Seraph/World/WellStructureResolver.cs` | `WellStructureResolver, Bounds` | `Bounds, TryFromHead, TryFromWall, IsWall, ProtectedIntake, HasFoundation, IsHead` | `60032b775f2a` |
| `Seraph/World/WorldCalendarTime.cs` | `WorldCalendarTime, Clock` | `Seconds, Hours, Reset` | `4fb6aaf57b34` |

#### `Seraph.Application/`

| 文件 | 类型声明 | 主要方法（索引） | SHA-256 前 12 位 |
| --- | --- | --- | --- |
| `Seraph.Application/Capabilities.cs` | `CapabilityOwner, Capability, CapabilityAssignment, CapabilityRegistry, SideEffectKind, SideEffectBarrier, IntegrationStatus` | `CapabilityAssignment, Register, MayWrite, Create, SideEffectBarrier, Allows, IntegrationStatus` | `6ee924d6b208` |
| `Seraph.Application/ClinicalWarnings.cs` | `ClinicalWarning, ClinicalWarningPolicy, ClinicalWarningTracker, Episode` | `ClinicalWarning, Evaluate, BloodStage, Episode, Seed, Reset, Advance` | `0b0d0efe50bc` |
| `Seraph.Application/InboundGate.cs` | `InboundGate, Bucket` | `InboundGate, Bucket, TryAccept, Remove` | `d4964d31c570` |
| `Seraph.Application/IntegrationContracts.cs` | `AdapterEvidence, RoomSample, ExposureSample, InjurySample, IRoomEnvironmentAdapter, IExposureAdapter, IVerifiedInjuryLocation, IInjuryAdapter` | `AdapterEvidence, RoomSample, ExposureSample, InjurySample, FoodPortion, In, Receipt` | `907e00c87368` |
| `Seraph.Application/MedicalActions.cs` | `MedicalActionPhase, MedicalAction, MedicalActionCoordinator, IInventoryMedicalTransaction, IIntakeAdapter` | `MedicalAction, Get, Begin, Advance, Cancel` | `63e3ac48fa54` |
| `Seraph.Application/MetricTrends.cs` | `MetricTrends, Series` | `Series, Advance, Clear, Record` | `4d80bed46c65` |
| `Seraph.Application/SeraphServerConfig.cs` | `SeraphServerConfig, TargetVersion, SettingsAuthority` | `ResolveUnits, Validate, IsSupported, ValidateChange, Commit, CommitMode` | `055b24d31536` |
| `Seraph.Application/ShadowSaveCodec.cs` | `ShadowSave, SaveDecodeResult, ShadowSaveCodec, Envelope` | `SaveDecodeResult, Envelope, Encode, Decode, MigrateNutrition, Validate` | `dd500021ff37` |

#### `Seraph.Core/`

| 文件 | 类型声明 | 主要方法（索引） | SHA-256 前 12 位 |
| --- | --- | --- | --- |
| `Seraph.Core/BuildInfo.cs` | `BuildInfo` | `（无可索引的显式方法）` | `5ccd7b09ffb9` |
| `Seraph.Core/Framework/AdrenalineEffects.cs` | `AdrenalineEffects` | `AdvanceGameTimeCooldown, Level, AttackSpeed, Flow, Bleeding, Ventilation, Pain, Digestion` | `6aaa870dddac` |
| `Seraph.Core/Framework/AshAndFertilizer.cs` | `AshFertilizerDose, AshAndFertilizer` | `AshFertilizerDose, Validate, Ash, Manure` | `cd7f05cb8425` |
| `Seraph.Core/Framework/BathWaterTreatment.cs` | `BathWaterTreatment` | `Advance, IntegratedWarmth` | `84085a3b3489` |
| `Seraph.Core/Framework/BloodCirculation.cs` | `BloodState, CirculationOptions, CirculationResult, BloodCirculation` | `Validate, CirculationResult, AddWaste, LactateCapacityG, WasteCapacityMl, Toxicity, Pumping, Filtration` | `f6b8f61d4964` |
| `Seraph.Core/Framework/BodyFunctions.cs` | `InjuryEvent, HitRegion, Anatomy, BodyFunctions, BodyFunctionResolver, CombatFunctions` | `InjuryEvent, HitRegion, VitalIndex, Parent, Known, Locate, Remaining, Pain` | `e72a075aa26b` |
| `Seraph.Core/Framework/BowelSettlement.cs` | `BowelSettlement, DefecationPlan` | `Advance, PlanDefecation, DefecationPlan, Deconstruct` | `d8a19e3b576d` |
| `Seraph.Core/Framework/ClinicalEffects.cs` | `ClinicalEffect, ClinicalEffects, WoundCare, SoapCare` | `ClinicalEffect, Dehydration, HeatStress, Evaluate, DamagePerSecond, EntericBurden, EntericWaterLossLPerGameHour, DigestionEfficiency` | `f843e7658c13` |
| `Seraph.Core/Framework/ColdExposure.cs` | `ColdExposure` | `Advance` | `0fb6ac4e1d76` |
| `Seraph.Core/Framework/CropSurfaceContamination.cs` | `CropSurfaceContamination` | `Advance` | `72f3c6c78471` |
| `Seraph.Core/Framework/DietaryMetabolism.cs` | `DigestionFlux, DietaryMetabolism` | `DigestionFlux, Digest, DigestStep, Deposit, AvailableProtein, SpendProtein` | `8b0d46db96c5` |
| `Seraph.Core/Framework/DigestionOptions.cs` | `DigestionOptions` | `Validate, Empty` | `37d8804ee4f1` |
| `Seraph.Core/Framework/DiseaseExposure.cs` | `DiseaseExposure, per` | `RespiratoryContactUnits, AdvanceWounds, AnimalBitePathogen, Advance, AdvanceWithEvents` | `5365e5ebe4d5` |
| `Seraph.Core/Framework/DiseaseSyndromes.cs` | `SymptomKit, SyndromeState, DiseaseExposureOptions, SyndromeResult, DiseaseExposureResult, DiseaseSyndromes` | `Validate, SyndromeResult, DiseaseExposureResult, Kit, Severity, FoodPoisoning, FeverSetpointC, DivertMeal` | `e49939ecdf9c` |
| `Seraph.Core/Framework/DrinkingTemperature.cs` | `DrinkingTemperature` | `IsDrinkable, AbsorptionMultiplier, ThermalStimulusC` | `0c7f902fc6cf` |
| `Seraph.Core/Framework/EnvironmentalExposure.cs` | `EnvironmentalExposure, ExposurePreview` | `ChemicalInput, Preview, CombinedLoad, RespiratoryHazard, ExposurePreview` | `3654932d92d8` |
| `Seraph.Core/Framework/Exertion.cs` | `ExertionKind, ExertionResult, RecoveryStage, ExertionOptions, Exertion` | `ExertionResult, Validate, StaminaCapacity, WorkMultiplier, PowerW, RunningMovement, MovementPowerW, RunningLoad` | `0ac5d03f4cc2` |
| `Seraph.Core/Framework/ExposureBarriers.cs` | `AmbientExposureClock, ExposureLedgerEntry, ExposureBarrierState, ExposureBarriers` | `AmbientExposureClock, ExposureLedgerEntry, Validate, ContactUnits, Scale, Merge, Capacity, Loads` | `af304004ed79` |
| `Seraph.Core/Framework/FluxLedger.cs` | `FluxUnit, FluxEntry, FluxLedger` | `FluxEntry, Transfer, Net` | `c72eb52f7dcb` |
| `Seraph.Core/Framework/FrameworkKernel.cs` | `ActivityContext, FrameworkOptions, FrameworkResult, IntakeReceipt, DiseaseDefinition, FrameworkKernel, FunctionResolver` | `ActivityContext, Validate, FrameworkResult, IntakeReceipt, DiseaseDefinition, Advance, ImmuneSupport, WoundHealingRate` | `33e77e3aeb76` |
| `Seraph.Core/Framework/FrameworkState.cs` | `WoundKind, InjuryEvidence, DownedState, DiseasePhase, Wound, DiseaseState, ChronicEffect, ClinicalIndicators` | `Validate, ChronicEffect, Advance, Create, TreatmentsValidation, DeterministicRandom, NextUnit, Seed` | `4e8de7a51621` |
| `Seraph.Core/Framework/GroundwaterHydrology.cs` | `AquiferMaterialClass, GroundwaterType, AquiferMaterialProperties, AquiferMaterials, GroundwaterState, GroundwaterInputs, GroundwaterStep, GroundwaterTransfer` | `AquiferMaterialProperties, Validate, Properties, GroundwaterState, Finite, GroundwaterInputs, NonNegative, GroundwaterStep` | `03bf41cef549` |
| `Seraph.Core/Framework/HandContamination.cs` | `HandContamination` | `AfterDefecation, TransferToFood, AfterWashingProduce` | `71bd956dcf1a` |
| `Seraph.Core/Framework/HeldWorkLedger.cs` | `HeldWorkLedger` | `Advance, Finish, End` | `9f15bda7db89` |
| `Seraph.Core/Framework/HumidityModel.cs` | `HumidityModel` | `RelativeHumidity` | `624c1f9aadd3` |
| `Seraph.Core/Framework/Hydration.cs` | `Hydration` | `Stage, BloodMaximumFactor, PerformanceFactor, OrganFactor` | `70f924c59732` |
| `Seraph.Core/Framework/ImmuneSystem.cs` | `ImmuneSystem` | `Effective, Support, Susceptibility, Duration` | `2931ccb5ee18` |
| `Seraph.Core/Framework/Ketosis.cs` | `Ketosis` | `Symptomatic, Performance, Advance` | `8c48472e12d9` |
| `Seraph.Core/Framework/MicroNutrition.cs` | `MicroNutrition` | `Burden, Deficient, Gain, DailyPointsFor, HalfLifeHours, CumulativeAbsorption, ImmuneBonus` | `1f65245387d4` |
| `Seraph.Core/Framework/NativeWorkReceipts.cs` | `NativeWorkReceipts` | `Accept` | `2777f428206b` |
| `Seraph.Core/Framework/NutrientInteractions.cs` | `NutrientInteractions` | `AbsorptionFactor, RecoveryMultiplier, FatigueMultiplier, BleedingMultiplier, StaminaBonus, WaterAbsorptionSupport, InflammationTrend, Burden` | `4cc2611a80ec` |
| `Seraph.Core/Framework/NutritionState.cs` | `NutrientDefinition, Nutrients, NutrientStatus, NutrientStage, NutritionBands, NutritionAssessment, NutritionState` | `NutrientDefinition, IndexOf, NutrientStatus, Stage, Support, DeficiencyEffect, NutritionAssessment, ContentsMassG` | `eaeda3682dee` |
| `Seraph.Core/Framework/PathogenLoads.cs` | `PathogenLoads` | `Valid, Scale, Add, Mix, WithGenericEnteric` | `0063698572ed` |
| `Seraph.Core/Framework/Pathogens.cs` | `ExposureRoute, PathogenProfile, Pathogens` | `PathogenProfile, Enteric, Fecal, Wound, Airborne` | `c6cacf96b431` |
| `Seraph.Core/Framework/PlayerCondition.cs` | `EnergyReserves, PlayerCondition` | `EnergyReserves, From, PlayerCondition, Evaluate` | `b69efebb7e41` |
| `Seraph.Core/Framework/PollutionModel.cs` | `PollutionLoad, PollutionLevels, PollutionModel` | `PollutionLoad, Scale, PollutionLevels, Levels, WaterHazard, DoseRisk, Saturate, Positive` | `9d782c5a394e` |
| `Seraph.Core/Framework/PollutionTransport.cs` | `WasteContainment, OrganicWasteKind, PollutionTransport` | `GasEscape, WaterEscape, Leaks, OrganicGas, VegetationRetention, AquaticRetention, RiparianRetention, CompostActivity` | `685b07d9c9df` |
| `Seraph.Core/Framework/PondContamination.cs` | `PondContamination, PondContaminationModel` | `Valid, Scale, Add, Mean, AdvanceCell` | `857862f04400` |
| `Seraph.Core/Framework/RecoveryClock.cs` | `RecoveryClock` | `RecordWork, Seconds` | `b9208d67752e` |
| `Seraph.Core/Framework/RegionalEnvironment.cs` | `AirChemistry, BurningFuel, RegionalSources, RegionalEnvironment, RegionalEnvironmentModel` | `AirChemistry, Scale, Clamp, Unit, ChemicalWaterRisk, Valid, Combustion, Create` | `b119cfc6c39f` |
| `Seraph.Core/Framework/ReserveDisplay.cs` | `ReserveDisplay` | `Score, WholeScore, HydrationG` | `44769d5003f0` |
| `Seraph.Core/Framework/RestFeedback.cs` | `RestFeedback` | `Stress, FatigueRiseMultiplier, SleepRiseMultiplier, FatigueMovementPenalty, Advance, Relieve` | `243b333f0086` |
| `Seraph.Core/Framework/RunningPace.cs` | `RunningPace, ExerciseMuscles` | `Fraction, Gain, Advance, Restore, Burning, Charge, Recover` | `171c4038e081` |
| `Seraph.Core/Framework/Sanitation.cs` | `SanitationOptions, SanitationContext, Sanitation` | `Validate, GainMultiplier, Advance, WaterResidue` | `db2504c49ccc` |
| `Seraph.Core/Framework/SleepEyeCycle.cs` | `SleepEyeCycle, SleepEyeState` | `Capture, ClosureAfter, Restore, Coverage, Reset, Interval, Hold, Advance` | `b749a41d0fb4` |
| `Seraph.Core/Framework/SleepFeedback.cs` | `SleepCue, SleepFeedback` | `SleepCue, Evaluate` | `62f95bb45e2a` |
| `Seraph.Core/Framework/SmokeGasCoupling.cs` | `SmokeGasCoupling` | `Apply` | `9e5cc1f19116` |
| `Seraph.Core/Framework/SmokeInhalation.cs` | `SmokeInhalation` | `Ventilation, Advance, Capacity, Severity, DamagePerRealSecond` | `51836ea05ebc` |
| `Seraph.Core/Framework/SpoilageResponse.cs` | `VomitResult, SpoilageResponse` | `VomitResult, DirtinessGain, VomitProbability, TryVomit` | `a0dad1391cf0` |
| `Seraph.Core/Framework/SurfaceEcologySurvey.cs` | `EcologyCell, SurfaceEcologySurvey` | `Advance, Next` | `808b2e05d304` |
| `Seraph.Core/Framework/SurfaceWater.cs` | `SurfaceWaterOptions, SurfaceWater` | `TurbidityHazard, BaseTurbidity, Apply, ClarityTier` | `db0079529d6b` |
| `Seraph.Core/Framework/ThermalAdaptation.cs` | `ThermalAdaptationOptions, ThermalAdaptation` | `Validate, HotDemand, ColdDemand, Advance` | `411bc0c6f9aa` |
| `Seraph.Core/Framework/Treatments.cs` | `TreatmentRoute, TreatmentDefinition, ActiveTreatment, TreatmentDose, Complaint, Treatments` | `Validate, Key, ActiveTreatment, TreatmentDose, Complaint, Strength, Active, Relief` | `3776d9c07354` |
| `Seraph.Core/Framework/VitalState.cs` | `VitalState` | `MaximumFor, WithExternalMaximum, EffectiveMaximumFor, EffectiveFor, Deficits, WithNutrition, Validate, Restore` | `ef845e1cd5f2` |
| `Seraph.Core/Framework/WaterBatch.cs` | `WaterTreatmentStage, WaterBatch, InteractionState` | `PotentialBloodWasteMl, Validate, Mix, AfterDefecation` | `3507f352bcb1` |
| `Seraph.Core/Framework/WaterCycleModel.cs` | `GroundwaterCell, WaterCycleInputs, WaterCycleStep, WaterCycleModel, DesalinationResult, WaterTreatmentModel, RoomThermalInputs, RoomTemperatureModel` | `GroundwaterCell, Validate, Finite, WaterCycleInputs, WaterCycleStep, Advance, DeriveCell, EvaporationMultiplier` | `9748618d0bc9` |
| `Seraph.Core/Framework/WaterDistillation.cs` | `WaterDistillation` | `（无可索引的显式方法）` | `106eb5df9125` |
| `Seraph.Core/Framework/WaterFiltration.cs` | `WaterFiltration` | `Process, TransferVolume` | `f0012fcf4b1b` |
| `Seraph.Core/Framework/WaterHeating.cs` | `WaterHeating` | `AtTemperature, Evaporate` | `f57929b9b804` |
| `Seraph.Core/Framework/WaterQualityCompatibility.cs` | `WaterQualityCompatibility` | `Read, RequireCurrent` | `2b42bd72eef1` |
| `Seraph.Core/Framework/WellReservoir.cs` | `WellReservoir` | `Capacity, Height, InflowPerDay, Incoming` | `da27daf7870b` |
| `Seraph.Core/Framework/WorkIntervals.cs` | `WorkIntervals` | `Boundaries, Add, RestSeconds` | `d3420f1a9ee3` |
| `Seraph.Core/Framework/WorkPrediction.cs` | `PredictedWork, WorkAcknowledgements, WorkPrediction` | `PredictedWork, Credit, Notice, Settle, Trim, Advance, Reconcile, Add` | `b7a26396e4ad` |
| `Seraph.Core/Framework/WoundPain.cs` | `PainOptions, PainPools, WoundPain` | `Validate, PainPools, Pools, Contribution, Resolve, Advance, PaidHealing, Merge` | `04495c82b344` |
| `Seraph.Core/Framework/WoundRecovery.cs` | `WoundRecoveryResult, WoundRecovery` | `WoundRecoveryResult, DamagePoints, Settle` | `c38ec5a10213` |
| `Seraph.Core/Simulation/ActionEnergyBudget.cs` | `ActionEnergyBudget` | `Boundaries, Record, Consume` | `4ff53fffbf42` |
| `Seraph.Core/Simulation/BoundedTimeScheduler.cs` | `SchedulerOptions, TimeBudgetPlan, BoundedTimeScheduler` | `Validate, TimeBudgetPlan, Schedule` | `0326f741e773` |
| `Seraph.Core/Simulation/CalendarSleepTimeline.cs` | `CalendarSleepPeriod, CalendarSleepTimeline` | `CalendarSleepPeriod, Reset, Observe, Consume` | `e069cb53b018` |
| `Seraph.Core/Simulation/CalendarTimeScheduler.cs` | `CalendarTimeScheduler` | `Schedule, Reset` | `83935232ff7d` |
| `Seraph.Core/Simulation/Contracts.cs` | `StepInputs, IntakeEvent, StateChangeResult, StepResult, SimulationDiagnostics` | `Validate, StateChangeResult, StepResult, CreateFluxLedger` | `6ee328cab0e0` |
| `Seraph.Core/Simulation/ModelOptions.cs` | `ModelOptions` | `Validate` | `949c505efc7f` |
| `Seraph.Core/Simulation/PhysiologyFlowLedger.cs` | `PhysiologyFlowLedger` | `Hourly, KcalPerHour, Add` | `7a68b66f9da4` |
| `Seraph.Core/Simulation/SimulationKernel.cs` | `SimulationKernel, Ledger` | `ValidateState, DryHeatPowerW, EquivalentTemperatureC, Advance, ApplyIntake, Integrate, TryDryHeat, OutsideVaporFitDomain` | `c9d0e5b371b3` |
| `Seraph.Core/Simulation/ThermalLedger.cs` | `ThermalLedger` | `ThermalLedger, Add` | `1efaf7bc3765` |
| `Seraph.Core/State/BodyProfile.cs` | `BodyProfile` | `Validate, In` | `081fad1b4fa8` |
| `Seraph.Core/State/BodyState.cs` | `BodyState` | `Create, BloodVolumeL, Validate, AddUrine` | `c7e9aadce578` |
| `Seraph.Core/State/EnvironmentSample.cs` | `EnvironmentSourceQuality, EnvironmentSample` | `Validate` | `017441e29903` |

#### `Seraph.DebugUI/`

| 文件 | 类型声明 | 主要方法（索引） | SHA-256 前 12 位 |
| --- | --- | --- | --- |
| `Seraph.DebugUI/Client/DebugFont.cs` | `DebugFont` | `Push, Load, Dispose` | `48ff1a35df98` |
| `Seraph.DebugUI/Client/SeraphAdminDiagnosticsHud.cs` | `SeraphAdminDiagnosticsHud` | `SeraphAdminDiagnosticsHud, ShouldReceiveKeyboardEvents, Update, BuildText, Append, OnRenderGUI` | `10f4142f4667` |
| `Seraph.DebugUI/Client/SeraphDebugWindow.cs` | `SeraphDebugView, SeraphDebugWindow, SeraphDebugTheme, Scope` | `Toggle, OnDraw, Draw, Dispose, DrawContents, ResetPlayerEdit, DrawPlayerEdit, DrawLines` | `f3c69ed6cbc0` |
| `Seraph.DebugUI/DebugUiModSystem.cs` | `DebugUiModSystem` | `ShouldLoad, ExecuteOrder, StartClientSide, Toggle, ReconcileDiagnostics, ReadView, Dispose` | `10d975ed85e7` |
<!-- generated:end -->
