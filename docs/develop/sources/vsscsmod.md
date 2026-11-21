<!-- generated:start -->
# 文明模拟源码索引

[返回模组介绍](/mods/entries/vsscsmod)

## 源码实现矩阵（当前源码树）

以下 136 个 C# 文件从 `E:\vintagestory\Seraph Civilization Simulation` 的 `src` 目录逐文件扫描生成。每行给出声明类型、前若干可见方法和 SHA-256 前 12 位；完整文件清单与核验状态见[源码盘点](/develop/source-inventory)。源码文件存在不代表该路径在当前配置中启用，运行时仍需看依赖检测、能力所有权和配置校验。

### 如何从矩阵定位功能

| 玩家看到的系统 | 源码目录/文件前缀 | 服务器/开发者关注点 |
| --- | --- | --- |
| 文明核心、身份、复活 | `CivilizationCore.cs`、`CivilizationLifeState.cs`、`VscnRespawnBehavior.cs` | 状态持久化、生命计数、重生保护与名称校验 |
| 部落、授权、领地 | `CivilizationTribes.cs`、`Tribe*.cs`、`*Territory*.cs` | 成员/角色/授权分离，领地检测和加固恢复 |
| 聚落与地图 | `ClusterSpawning.cs`、`GroundMap*.cs`、`MapDrawing*.cs` | 出生点分配、纸图拼接、闭合范围与权限 |
| 公告、教程、HTML | `Announcement*.cs`、`Guidance*.cs`、`CivilizationContent*.cs` | 世界内容文件、资源白名单、分页和管理员编辑 |
| 经济与科技 | `CivilizationEconomy*.cs`、`Economy*.cs`、`Technology*.cs` | 报价快照、库存匹配、铸币/交易历史和科技状态 |
| 兼容、策略与日志 | `*Compatibility.cs`、`ModPolicy*.cs`、`ClientLog*.cs` | 依赖握手、保护策略、客户端日志上传边界 |

### 逐文件索引

#### `根目录/`

| 文件 | 类型声明 | 主要方法（索引） | SHA-256 前 12 位 |
| --- | --- | --- | --- |
| `AdminSettings.cs` | `AdminSettingsRequest, AdminSettingsPacket, AdminSettingsData, VscnCivilizationModSystem` | `Document, Revision, OnAdminSettings, ApplyConfiguration, RefreshConfigurationClients` | `ba817332a383` |
| `AdminSettingsWindow.cs` | `AdminSettingsWindow` | `AdminSettingsWindow, Update, Request, Compose, OnRenderGUI, Dispose` | `328d03b31c38` |
| `AdminSettingText.cs` | `AdminSettingText` | `Title, Description` | `5e5c483c318c` |
| `AnnouncementDom.cs` | `AnnouncementDom` | `Markup, Encode, Decode, Parse, Styles, Value, Number, Dimension` | `0e5c179c1b3b` |
| `AnnouncementFonts.cs` | `AnnouncementFonts, Run` | `Run, SingleLine, Runs, Readable, WithFamily, Family` | `709869def3de` |
| `AnnouncementGameResources.cs` | `AnnouncementGameResources, Resource, ItemCell, AnnouncementInlineItemBox, AnnouncementResourcePicker` | `Resource, Esc, Resolve, ItemHtml, ItemAttributes, AttributeData, SlideshowHtml, ResolveElement` | `15d891b812ac` |
| `AnnouncementHtml.cs` | `AnnouncementState, TutorialState, AnnouncementEntry, AnnouncementHtml` | `Migrate, PendingNotification, ValidateSave, HiddenContent, Tokens, TagName, Attributes, Whitespace` | `733808034028` |
| `AnnouncementHtmlLayout.cs` | `AnnouncementInteraction, AnnouncementAnchor, AnnouncementBox, AnnouncementSwitch, AnnouncementDisclosure, AnnouncementRule, AnnouncementTable, Cell` | `AnnouncementAnchor, Position, StretchHeight, Measure, MeasureContent, CalcBounds, Align, ComposeElements` | `17b515e1ef22` |
| `AnnouncementHtmlTools.cs` | `AnnouncementHtmlTools` | `Format, Insert` | `389c7273e1b7` |
| `AnnouncementImages.cs` | `AnnouncementImages, CachedRequest` | `CachedRequest, NormalizeSource, IsPublicAddress, Request, Download, ReadBounded, Decode, Clear` | `4d69584faa20` |
| `AnnouncementMarkdown.cs` | `AnnouncementMarkdown, Edit` | `ToNativeMarkup, ToHtml, Edit, Format` | `3f9680462c9b` |
| `AnnouncementRecipes.cs` | `AnnouncementRecipes, RecipeRow, RecipeOutput` | `Signature, Html, Resolve, Component, RecipeRow, MeasureContent, ComposeElements, RenderInteractiveElements` | `fc32b8260c1d` |
| `AnnouncementTextLayout.cs` | `AnnouncementTextLayout, ImageBudget, BlockSpacing, DecorationMarker, NoticeText, NoticeLink` | `Components, Number, Measure, Layout, DecorationMarker, NoticeText, ComposeElements, CalcBounds` | `1aa08220906b` |
| `AnnouncementVisualComponents.cs` | `AnnouncementBlock, AnnouncementCard, AnnouncementImage` | `AnnouncementBlock, Anchor, FindAnchor, AnnouncementCard, CalcBounds, ComposeElements, RenderInteractiveElements, UseMouseOverCursor` | `57bb33e220de` |
| `ArtistClassRestriction.cs` | `ArtistClassRestrictionSystem, ArtistClassCompatibility, to, loading` | `Start, AssetsFinalize, Dispose, Restricted, AfterLoadClasses, BeforeSetClass, BeforePlayerJoin` | `c7d8f5e6c4a7` |
| `AssemblyInfo.cs` | `（顶层注册/补丁逻辑）` | `（无可索引的显式方法）` | `2ba80c3b13ba` |
| `AtlasViewportFit.cs` | `AtlasViewportFit` | `For, Valid, Local, World, Rectangle, Cross, DistanceSquared, InCoverage` | `7471813f1aa1` |
| `BearBlockBreakingBehavior.cs` | `BearBlockBreakingBehavior` | `BearBlockBreakingBehavior, AfterInitialized, RememberCombatTarget, OnGameTick, CanBreak, HasUnbreakableBarrier, OnEntityDespawn, CanScan` | `ceb77c2bfa9f` |
| `BuildingProtectionRules.cs` | `BuildingProtectionConfig, BuildingFireState, BuildingProtectionRules` | `Validate, RecoveryRate, Remaining, SetDamage, Consume` | `b0e6a684da07` |
| `BuildingTerritory.cs` | `TerritoryCell, TerritoryRun, BuildingTerritoryRegion, BuildingTerritoryConfig, TerritoryGeometry, BuildingTerritoryIndex, TerritoryRegionView, TerritoryCandidateView` | `TerritoryCell, Position, Neighbors, Invalidate, Validate, Encode, Decode, Connected` | `001a0eddf924` |
| `BuildingTerritoryDetection.cs` | `TerritoryDetectionException, BuildingTerritoryDetector, CourtyardScan` | `TerritoryDetectionException, BuildingTerritoryDetector, SolidFloor, RequireLoaded, Room, ClearBody, Safe, Make` | `bd244f23a54a` |
| `BuildingTerritoryServer.cs` | `VscnCivilizationModSystem` | `TribeSpawn, TrySaveTerritoryChange` | `b20edb4e6eb6` |
| `ChiselToolsSurvivalCompatibility.cs` | `ChiselToolsSurvivalCompatibility, OperationContext` | `OperationContext, Install, IsDisabled, FinalizeAssets, Notify, Deny, BeforeDisabledTool, BeforeWaterSource` | `3e2e685caa9c` |
| `CivilizationAuthorizationWindow.cs` | `VscnClusterWindow` | `CanManage, GrantScopes, ComposeTribe, HistoryDate, AuthorizationTime, TickAuthorizationClocks` | `4ec0a2afb14f` |
| `CivilizationBuildingProtection.cs` | `VscnCivilizationModSystem, FireExposure, MaterialFire` | `FireExposure, WearMatches, ProtectionSystem, ClearBuildingState, ClearBuildingDamage, ConsumeBuildingReserve, StartBuildingProtection, StopBuildingProtection` | `ce788beec113` |
| `CivilizationChat.cs` | `VscnCivilizationModSystem` | `GameNameKey, ChatPlayerName, UseGameNameInChat` | `652d1dea6daf` |
| `CivilizationContentCommands.cs` | `VscnCivilizationModSystem` | `HandleContentCommand, HandleAnnouncementCommand, HandleTutorialCommand, SaveAnnouncementState, SaveTutorialState, HandleReloadContent, NotifyCivilizationContentChanges, ListContent` | `6f6139a92085` |
| `CivilizationContentFiles.cs` | `VscnCivilizationModSystem` | `LoadCivilizationContent, ReloadAnnouncementContent, ReloadTutorialContent` | `a151bff5d732` |
| `CivilizationCore.cs` | `ItemCivilizationCore, CivilizationCoreInventory, CoreSlot, VscnClientModSystem, CivilizationCoreHud` | `OnBeforeRender, EnsureItem, DropAll, CoreSlot, CanTake, CanHold, CanTakeFrom, TryFlipWith` | `9d0a4884d288` |
| `CivilizationEconomy.cs` | `VscnCivilizationModSystem, TradeSession` | `StartEconomy, LoadEconomy, ValidExchange, ValidRequirement, SaveEconomy, StopEconomy, DisconnectEconomy, RegisterCoin` | `f4ab620991d9` |
| `CivilizationEconomyIssuance.cs` | `VscnCivilizationModSystem` | `DesignDesigner, CoinDesigner` | `fa71e76e9fb2` |
| `CivilizationEconomyWindow.cs` | `VscnClusterWindow` | `SetEconomySender, SetEconomyCatalog, UpdateEconomy, EconomyAction, ChangePage, CurrencyName, RecordedCurrency, OfferRequest` | `d858d44fcf49` |
| `CivilizationGuidance.cs` | `VscnCivilizationModSystem` | `Identity, RemainingLives, StartGuidance, BeforeRespawnKey, BeforeNativeRespawn, LoadCivilizationLives, SaveCivilizationLives, HandleNameCommand` | `d824bc99e836` |
| `CivilizationLifeState.cs` | `CivilizationLifeState, CivilizationIdentity, TerritoryWear, GuidancePacket, GuidanceDecision` | `Remaining, ValidName` | `3bd41300b3e2` |
| `CivilizationMapInventory.cs` | `CivilizationMapInventory, and, AtlasSlot` | `PageClass, GetPage, NewSlot, CanContain, Accepts, GetSuitability, FromTreeAttributes, ToTreeAttributes` | `0dc87f2309b3` |
| `CivilizationPages.cs` | `VscnCivilizationModSystem` | `ReturnLegacyMaps, PersistAnnouncements, SaveAnnouncement, SaveTutorial, PersistTutorials, SendLoginAnnouncement, AcknowledgeAnnouncement` | `eceb856b2e85` |
| `CivilizationTechnology.cs` | `VscnCivilizationModSystem` | `TechnologyAvailable, InitializeTechnologyMods, ScanOnlineTechnology, OnTechnologyBlockPlaced, OnTechnologyBlockBroken, RecordTechnologyAction, ScanTechnology, BuildTechnologyView` | `e353f44cbbb0` |
| `CivilizationTribes.cs` | `VscnCivilizationModSystem, PendingInvite, PendingFounding` | `PendingInvite, PendingFounding, ByUid, PlayerName, MemberDisplayName, Ui, DistanceTo, RemovePendingTribeActions` | `d33e8bc57d01` |
| `CivilizationTutorialPage.cs` | `VscnClusterWindow` | `ComposeTutorial, BeginTutorial, PublishTutorial, DeleteTutorial, ComposeTutorialReader, ComposeTutorialEditor, AddTutorialArticle, UpdateTutorialScroll` | `ec85f139e6bf` |
| `CivilizationWindowPages.cs` | `VscnClusterWindow, GuiElementPageTabs` | `StashAnnouncementDraft, SelectAnnouncement, OpenAnnouncementResource, OpenTutorialResource, AnnouncementResourceItems, ComposeAnnouncementResource, AnnouncementResourceBounds, CloseAnnouncementResource` | `f552db600500` |
| `ClientLogFiles.cs` | `ClientLogFiles, Snapshot, ClientLogIncoming` | `AllowedEntry, Snapshot, Capture, ValidateArchive, Append, Dispose` | `9e7c534c0149` |
| `ClientLogUploadClient.cs` | `ClientLogUploadSystem, ClientLogUploadDialog` | `StartClientSide, BeforeClientLogLeave, LogClientReady, ReceiveLogOffer, PrepareLogOffer, ReceiveLogReply, EndClientRequest, LogClientLeave` | `669d1c04a535` |
| `ClientLogUploadSystem.cs` | `ClientLogOffer, ClientLogUpload, ClientLogReply, ClientLogUploadSystem, LogIncident, LogRequest` | `LogRequest, Start, StartServerSide, BeforeLogLeave, BeforeLogDisconnect, LogPlayerPlaying, LogPlayerDisconnect, OfferLogs` | `f8516849757e` |
| `ClientOnlyModCatalog.cs` | `ClientOnlyModCatalog` | `Read, ReadInfo, ReadModInfo` | `99053bbaee7f` |
| `ClusterMessages.cs` | `ClusterMessages` | `For, Send` | `1670df32ef73` |
| `ClusterSpawning.cs` | `VscnCivilizationModSystem` | `InitializeClusters, CompleteInitialization, GenerateClusters, ValidateLand, RequiredLandSamples, LoadColumn, WithinWorld, Distance` | `b57c92be3aac` |
| `CoinageEconomyCompatibility.cs` | `CoinageEconomyCompatibility, HammerState, failed` | `Patch, HeldInteract, Server, PressedCoin, HammerState, BeforeHammer, AfterHammer, BeforeDesign` | `c10ae23293f0` |
| `Config.cs` | `ModPolicyMode, ClusterAssignmentMode, VscnConfig, PaperMapsConfig, TribeConfig, TerritoryConfig, ModPolicyConfig, ModRule` | `Validate, ShouldSerializeFirstOutpostMembers, ShouldSerializeSecondOutpostMembers, ShouldSerializeMaxOutposts, OutpostLimit, HomecomingChance` | `051a4165619a` |
| `ConfigMigration.cs` | `ConfigMigration` | `Read, LoadMain, LoadLore` | `c87f32c16621` |
| `EconomyBatchTrade.cs` | `VscnCivilizationModSystem, in` | `PurchaseGoods` | `a9fb86f6edea` |
| `EconomyCatalog.cs` | `EconomyCatalog, EconomyClientCatalog` | `Build, EconomyClientCatalog, Start, Receive, Advance, Dispose` | `730a5dc138aa` |
| `EconomyGuiFingerprint.cs` | `EconomyGuiFingerprint, DisplayContract` | `CreateProperty, Of` | `9abf1000a21e` |
| `EconomyGuiList.cs` | `EconomyGuiList, GuiElementEconomyItem, EconomyPreviewInventory, EconomyItemOverlay, GuiElementEconomyCoin, GuiElementEconomyArrow, GuiElementEconomyTaskEditor, GuiElementEconomyRule` | `Slot, CoinSlot, CurrencySelectors, CurrencyConversion, AddSlotButton, Exchange, CompleteRow, BeginRow` | `09140ce7a47b` |
| `EconomyInventory.cs` | `EconomyInventory, EconomyInventoryTrade, EconomyExchangeDelivery, EconomyExchangePlan` | `CoinKey, ItemKey, Slots, Count, Read, DisplayGroup, CoinBalances, PreviewStamp` | `9c6a54ad8d38` |
| `EconomyItemMatching.cs` | `EconomyItemMatching, EconomyItemRequirement, EconomyNestedItemMapping` | `Modern, Current, Attributes, Clean, Key, MatchingKey, Requirement, ResolveParts` | `d5345f7c56bb` |
| `EconomyOfferWindow.cs` | `EconomyOfferEditor, GuiElementEconomyPickerGrid` | `L, AddSlot, Build, BuildFooter, Clear, Pick, ClosePicker, Select` | `41840c9cb427` |
| `EconomyRateCalculator.cs` | `EconomyRateCalculator` | `FormatExact, FormatQuantity` | `1089fdc069bb` |
| `EconomyRefresh.cs` | `VscnCivilizationModSystem` | `ScheduleEconomyFlush, InitializeEconomyCatalog, InvalidateEconomyViews, WatchEconomyInventory, UnwatchEconomyInventory, FlushEconomyUpdates` | `4adb3caabd4b` |
| `EconomyState.cs` | `EconomyState, EconomyIssuer, EconomyMint, EconomyCoin, EconomyPolicy, EconomyOffer, EconomyTask, EconomyExchangeItem` | `Issuers, Active, Recognizes, MigrateIssuers, CanReadLedger, TribeHistory, TryRate, TryQuote` | `d88fed70dc77` |
| `EconomyTradeWindow.cs` | `EconomyTradeWindow` | `EconomyTradeWindow, L, Update, OnGuiClosed, OnMouseDown, OnMouseUp, OnRenderGUI, Compose` | `26a61374835a` |
| `FixedTerritoryRules.cs` | `FixedTerritoryRules` | `Members, Create, Apply, Validate` | `299ec811b3f3` |
| `GroundMapBlock.cs` | `GroundMapPlaceRequest, GroundMapTakeRequest, BlockGroundMap, BlockEntityGroundMap, VscnCivilizationModSystem` | `Text, Tell, Access, Give, PlaceOnWall, Place, OnBlockInteractStart, OnGettingBroken` | `ee3b139d9a63` |
| `GroundMapCompatibility.cs` | `GroundMapCompatibility` | `Install, DisableOldHud, CanRedraw, DrawStroke, ServerRotation, ClientRotation, Name, Info` | `da80ac106760` |
| `GroundMapData.cs` | `GroundMapData, MapPoint, AtlasViewport, MapPolygon, GroundMapLayout` | `IsAtlas, Sheets, Store, ReadSheets, CanAdd, CanPlace, DisplaySheets, Contains` | `e214229b23a1` |
| `GroundMapPaper.cs` | `GroundMapPaper` | `Meshes` | `a0e3e502edc5` |
| `GroundMapRendering.cs` | `MapCollage, GroundAtlasClient, AtlasEntry, GroundMapRenderer` | `GetModel, Dispose, AtlasEntry, GetTransparent, GetAtlas, OrientationKey, Orientation, TryGetHudTarget` | `d42f784e58a9` |
| `GroundMapSurface.cs` | `GroundMapPlacement, GroundMapVertex, GroundMapSurface` | `ToWorld, FromWorld, SetReference, FacePlayer, Ground, Map, Store, Read` | `b0e2c947676a` |
| `GuidanceClient.cs` | `VscnClientModSystem, TagState` | `StartGuidanceClient, OnGuidance, OnGuidancePauseResume, TryShowGuidance, LeaveGuidance, BeforeCharacterJoin, ResumeCharacterJoin, RequestTribeReinforcement` | `7328818df7f2` |
| `GuidanceWindow.cs` | `GuidanceWindow` | `CaptureAllInputs, TryClose, Update, Compose, Choose, Release, Suspend, OnRenderGUI` | `21d84caa6bca` |
| `GuiElementAnnouncement.cs` | `GuiElementAnnouncement` | `GuiElementAnnouncement, Anchor, BeforeCalcBounds, ComposeElements, RenderInteractiveElements, Dispose` | `8a284b096a5b` |
| `GuiElementAnnouncementContainer.cs` | `GuiElementAnnouncementContainer` | `GuiElementAnnouncementContainer, ComposeElements, RenderInteractiveElements` | `e8261d2cf527` |
| `GuiElementAnnouncementEditor.cs` | `GuiElementAnnouncementEditor` | `ScrollTo, LoadValue, ComposeTextElements, RenderInteractiveElements, WithScrolledBounds, OnMouseDownOnElement, OnMouseMove, OnMouseUp` | `5619ba24f1f5` |
| `GuiElementAnnouncementMenu.cs` | `GuiElementAnnouncementMenu` | `GuiElementAnnouncementMenu, ComposeElements, RenderInteractiveElements, Dispose` | `04d35dae5b08` |
| `GuiElementAnnouncementResourceList.cs` | `GuiElementAnnouncementResourceList, GuiElementAnnouncementResourceAlias` | `SetItems, RefreshScroll, ScrollTo, EnsureTexture, ComposeElements, RenderInteractiveElements, At, OnMouseMove` | `45eb4fc5baad` |
| `GuiElementAnnouncementTool.cs` | `GuiElementAnnouncementTool` | `GuiElementAnnouncementTool, BeforeCalcBounds, ComposeElements, DrawIcon, RenderInteractiveElements, OnKeyDown, Dispose` | `4835b2253c0e` |
| `GuiElementAutoScrollbar.cs` | `GuiElementAutoScrollbar` | `GuiElementAutoScrollbar, SetContentHeights, ComposeElements, RenderInteractiveElements, Dispose` | `7e23e09525aa` |
| `GuiElementFixedButton.cs` | `GuiElementFixedButton` | `GuiElementFixedButton, BeforeCalcBounds` | `07b8269aba14` |
| `GuiElementTribePortrait.cs` | `GuiElementTribePortrait` | `GuiElementTribePortrait, RenderInteractiveElements, Dispose` | `32f392000a1a` |
| `GuiElementTutorialLink.cs` | `GuiElementTutorialLink` | `ComposeElements, EnsureTexture, RenderInteractiveElements, OnMouseDownOnElement, OnMouseMove, IsExcluded, Dispose` | `d7381289b64a` |
| `GuiElementWrappedText.cs` | `GuiElementWrappedText` | `GuiElementWrappedText, ComposeTextElements` | `ec95db0eea17` |
| `HtmlDocumentApi.cs` | `HtmlDocumentApi` | `CreateEditor, CreateReader, InsertHtml, CreateDialog, CreateWorldTexture, PlainText` | `1aea7f84e7b0` |
| `HtmlDocumentDialog.cs` | `HtmlDocumentDialog` | `Compose, Submit, FocusEditor, Items, ClosePicker, OnRenderGUI, OnMouseDown, OnMouseMove` | `d0c2e6c936bc` |
| `HtmlDocumentWorldTexture.cs` | `HtmlDocumentWorldTexture` | `PrintHtml, Rebuild, Dispose` | `3494bb29f4d2` |
| `ImmersiveMapCompatibility.cs` | `MapMarkerClipboardRequest, ImmersiveMapCompatibility, VscnCivilizationModSystem, MarkerClipboard` | `Type, Field, Call, Static, Locked, CanDraw, TryGetDrawingMap, Fingerprint` | `e2beaab6b1e9` |
| `ImmersiveMapEditor.cs` | `ImmersiveMapCompatibility` | `ComposeMarkerEditor` | `fdd3947f92b4` |
| `InstalledModRecord.cs` | `InstalledModRecord` | `（无可索引的显式方法）` | `ec01e8947f94` |
| `LoreRestrictionCompatibility.cs` | `LoreRestrictionCompatibility` | `Install, FilterPan, AfterHarvestInitialized, BeforeRelicPlace, BeforeRestrictedBlockInteract, BeforeSkullTick, BeforeMapIdle, BeforeMapInteract` | `dc502ccc3e64` |
| `LoreRestrictionsConfig.cs` | `LoreRestrictionsConfig` | `Active, EntityRestricted, CollectibleRestricted, LivingDeadDropRestricted, PanDropRestricted, PatternRestricted` | `5fa6e9036b85` |
| `LoreRestrictionSystem.cs` | `LoreRestrictionSystem` | `ExecuteOrder, Start, AssetsFinalize, StartServerSide, StartClientSide, FinalizeClient, Bind, ParseConfig` | `1a5030404031` |
| `MapDrawingDocument.cs` | `MapDrawingDocument, MapDrawingLine, MapDrawingPoint, MapDrawingArea` | `Validate, ValidatePoint, Encode, Read, Decode` | `3048f0838cb7` |
| `MapDrawingFaces.cs` | `MapDrawingFaces, Point` | `Point, EnclosedWithBoundary, ClosedStroke, Extract` | `1d49b8f7ba93` |
| `MapDrawingNetwork.cs` | `MapDrawingSaveRequest, MapEditResult, VscnCivilizationModSystem` | `AllowMapEdit, MapEditReply, OnMapDrawingSave` | `60a44b023f33` |
| `MapDrawingProjection.cs` | `MapDrawingProjection` | `Cell, World, Faces, Territory, ValidateAreas` | `0781f685d761` |
| `MapDrawingRendering.cs` | `MapDrawingRendering, DrawingState` | `Install, Attach, Changed, Paint, Blit, Center, Draw` | `e6d72848014b` |
| `MapDrawingWindow.cs` | `GuiDialogMapDrawing, GuiDialogMapAreaNotes, GuiDialogMapAreaList, GuiDialogMapArea, MapDrawingCanvas, GuiDialogMapSettings, Settings` | `L, Compose, Status, Point, Snap, ShouldReceiveMouseEvents, OnRenderGUI, OnMouseDown` | `4c2b2e2d0edc` |
| `MapMarkerLayer.cs` | `MapMarkerLayer, Glyph` | `Glyph, Glyphs, Mesh, Cross` | `92324412d949` |
| `MapMarkerScales.cs` | `MapMarkerScales, MapMarkerScaleRequest, VscnCivilizationModSystem` | `Read, Write, OnMapMarkerScale` | `f02627b6dd1c` |
| `ModDataContentStore.cs` | `ModDataContentStore` | `RestoreBackup` | `3c13b100bc36` |
| `ModHandshakePolicy.cs` | `VscnCivilizationModSystem` | `InstallHandshakePolicy, AddHandshakePolicy, BuildServerBlacklist, BuildServerWhitelist` | `cb7c427044a3` |
| `ModPolicyEvaluator.cs` | `ModPolicyEvaluator` | `Validate` | `63a9f5364bd0` |
| `PaperMapAttributeStorage.cs` | `PaperMapAttributeStorage, LegacyImageStream` | `Pack, Read, ReadAttribute, LegacyReaderTranspiler, LegacyImageStream, Flush, Seek, SetLength` | `025c55d4763f` |
| `PaperMapStitching.cs` | `CivilizationMapInventory, Stitch` | `Stitch, Retire, SaveStitches, LoadStitches, SyncMasks, ReturnThread, UnstitchAll` | `13d8284c4923` |
| `ParchmentContracts.cs` | `ParchmentContract, VscnCivilizationModSystem, ParchmentBookCompatibility` | `ParchmentContract, Header, LooksLike, TryParse, ParseKeywords, ZeroTime, SignParchmentContract, SyncContractStack` | `980b78f325eb` |
| `PlayerStatusExport.cs` | `VscnCivilizationModSystem` | `ExportPlayerStatus, BuildPlayerStatusReport` | `f309cf505cdd` |
| `PlayerStatusLog.cs` | `PlayerStatusLog` | `CapturePlayer, CaptureAttribute, CaptureMods, Write` | `88b3d44477c4` |
| `PopulationTerritory.cs` | `PopulationTerritoryData, TerritoryShrinkView, TerritoryBoundaryEdge` | `（无可索引的显式方法）` | `09863b7ea0ef` |
| `RecordedPaperMap.cs` | `RecordedPaperMap, PaperMapDrawingCompatibility` | `IsPaperMap, Describe, Contains, Encode, Write, Read, Decode, AfterDraw` | `23f7532e5204` |
| `RectangularTerritory.cs` | `RectangularTerritoryConfig, TerritoryRectangle, TerritoryNamedArea, RectangularTerritorySite, TerritoryRoomObservation, TerritorySiteView, RectangularTerritoryRules` | `Validate, Contains, Same, Union, Pad, Around, Adjacent, ContainsColumn` | `5a3eff10742d` |
| `RectangularTerritoryLand.cs` | `VscnCivilizationModSystem` | `CheckFoundingTerritory, ValidateFixedTerritory, BeginFounding, RequestTerritoryDetection, SetFixedTerritory, ConfirmTerritory` | `133a34fb4dd1` |
| `RectangularTerritoryServer.cs` | `VscnCivilizationModSystem` | `TerritoryBudget, TerritoryArea, WithinTerritory, ReindexTerritories, CanManageTerritory, StartBuildingTerritories, StopBuildingTerritories, MigrateBuildingTerritories` | `4f8f530c1195` |
| `RectangularTerritoryViews.cs` | `VscnCivilizationModSystem` | `PreviewTerritory, FillBuildingTerritorySnapshot, FixedTerritoryEdges, RectangleBoundaries` | `9bc80fe8208c` |
| `RoofingPlacementCompatibility.cs` | `RoofingPlacementCompatibility` | `Install, ClearOrientation, BeforeGetToolModes, AfterGetToolModes, BeforeSetToolMode, BeforePlaceFrame, ReplacePlacementOrientation, RelativeOrientation` | `0f24c06413d8` |
| `ServerAnnouncementHud.cs` | `ServerAnnouncementHud` | `ServerAnnouncementHud, ShouldReceiveMouseEvents, OnEscapePressed, OnKeyDown, OnKeyPress, Show, Compose, SetScroll` | `a4569791b356` |
| `ServerAnnouncements.cs` | `ServerAnnouncementPacket, ServerAnnouncementRelay, VscnCivilizationModSystem` | `Install, Wrap, Dispose, StartAnnouncementRelay` | `271351e935eb` |
| `SleepInteractionGuard.cs` | `SleepInteractionGuard` | `IsSleeping` | `aef13122cb75` |
| `SleepInteractionRestrictions.cs` | `VscnCivilizationModSystem` | `InstallSleepInteractionRestrictions, HandleSleepCommand, SyncSleepInteractionSetting, SyncSleepInteractionSettings, IsPlayerSleeping, OnSleepingHandInteract, CanUseSleepingBlock, OnSleepingBlockAccess` | `0b4bbb175c71` |
| `State.cs` | `VscnState, ResetState, TribeState, TribeRecord, TribeMemberActivity, TribeOnlinePeriod, TribePermission, TribeAuthorization` | `Start, Stop, NeedsReset, Applied, FindMember, Find, RemoveMember, Active` | `ccf42f7d39a0` |
| `TechnologyCatalog.cs` | `TechnologyNode, TechnologyCatalog` | `TechnologyNode, Matches, CanComplete, ActionsMet, OutputsMet` | `36f05c8a96b5` |
| `TerritoryDebug.cs` | `VscnCivilizationModSystem` | `TerritoryOutpostLimit, HandleTerritoryDebug, TerritoryDebugInfo` | `88b9379e44e1` |
| `TerritoryEffects.cs` | `TerritoryDiscoveryPacket, VscnCivilizationModSystem` | `BuildTerritoryEffects, StartTerritoryEffects, UpdateTerritoryEffects, SetTerritoryStat` | `690fff6de54d` |
| `TerritoryNameHud.cs` | `TerritoryNameHud` | `Show, OnRenderGUI, ShouldReceiveMouseEvents, ShouldReceiveKeyboardEvents` | `a4165ca42723` |
| `TerritoryPatches.cs` | `TerritoryPatches` | `Area, Component, Covers, InComponent, Support` | `0b6a94ec2e90` |
| `TerritoryRenderer.cs` | `TerritoryRenderer` | `SetBoundaryVisibility, Update, OnRenderFrame, RenderBoundaries, BuildBoundaryMeshData, BuildBuildingMeshData, BuildPopulationMeshData, GetBoundarySegmentCount` | `e0735ad84f59` |
| `TradeHistory.cs` | `VscnCivilizationModSystem` | `TradeRecord` | `0b31040df7e5` |
| `TribeAuthorization.cs` | `TribeAuthorizationConfig, PlacedBuilding, VscnCivilizationModSystem` | `ShouldSerializeParchmentContractsEnabled, Validate, Authorized, TerritoryAt, CanBuildFor, AuthorizePlayer, RevokeAuthorization, PruneAuthorizations` | `8ab8aa95f9d6` |
| `TribeBuildingPlacement.cs` | `VscnCivilizationModSystem, PlacementContext` | `StartPlacementTracking, BeforeCarriedPlacement, BeforeBuildingPlacement, BeginBuildingPlacement, CheckPlacementFootprint, BeforeBuildingCanPlace, AfterBuildingPlacement, BeforeBuildingWrite` | `87978e76b346` |
| `TribeCompactWindow.cs` | `VscnClusterWindow` | `ScrollTribeFooter, MoveFooter, ComposeTribeDetails` | `d133bd367eee` |
| `TribeGovernance.cs` | `VscnCivilizationModSystem, in` | `PermissionsFor, HasTribePermission, OutpostWait, RemoveOutpost, TransferLeader, AdoptBuilding, NotifyAuthorization, NotifyPendingAuthorizations` | `ef03af550b50` |
| `TribeIcons.cs` | `TribeIcon, TribeIcons` | `CreateTexture, Draw, Home, Campfire, FillOutline, Stroke` | `4ea31148cfb7` |
| `TribeReinforcementCompatibility.cs` | `TribeReinforcementRequest, TribeReinforcementPacket, TribeReinforcementCompatibility, Scope` | `Scope, Install, Begin, End, CountdownInfo, NativeCalls, GetEffectiveReinforcement, Extra` | `988a9bb6ae66` |
| `TribeRoster.cs` | `TribeRosterConfig, TribeRosterPacket, TribeRosterMember, VscnCivilizationModSystem, RosterSvg, TribeRosterHud, CoreMenuKeyGesture, VscnClientModSystem` | `Validate, BuildTribeRoster, SendTribeRoster, Parse, Draw, TribeRosterHud, ShouldReceiveMouseEvents, OnEscapePressed` | `815f74696a74` |
| `TribeSuccession.cs` | `TribeSuccession, VscnCivilizationModSystem` | `Record, Successor, StartTribeSuccession, RecordTribeActivity, UpdateTribeSuccession, ChangeTribeLeader` | `d15a40d86ca2` |
| `VscnCivilizationModSystem.cs` | `VscnCivilizationModSystem` | `Start, AssetsFinalize, FinalizeClientChiselTools, StartServerSide, InstallRespawnIntegration, BeforeGetRespawnPosition, BeforeDeadCorpseHandling, BeforeDownedDeathDecision` | `c68e49751583` |
| `VscnClientModSystem.cs` | `VscnClientModSystem` | `ShouldLoad, StartClientSide, OnLevelFinalize, OpenSelectedPlayerTrade, OnSleepingBlockAccess, OnLeaveWorld, OnRequest, SendReport` | `4ceca1e338ec` |
| `VscnClusterWindow.cs` | `VscnClusterWindow` | `SelectWindowForTest, L, Esc, Action, Close, OnGuiOpened, OnGuiClosed, Update` | `8f4c630790ae` |
| `VscnRespawnBehavior.cs` | `VscnRespawnBehavior` | `PropertyName, Bind, Initialize, OnEntityRevive, OnGameTick, ProtectAfterRevive, OnEntityReceiveDamage` | `89f6ad24eba5` |
<!-- generated:end -->
