# 生存配置字段（源码默认值）

> 从 `SeraphServerConfig.cs` 顶层属性声明提取；嵌套 `SurfaceWater`、`DiseaseExposure`、`Sanitation`、`Exertion`、`ThermalAdaptation`、`Pain`、`Circulation`、`Digestion` 仍需展开对应类型的 `Validate` 与默认值。

| 类型 | 字段 | 默认表达式 |
| --- | --- | --- |
| `bool` | `EnableDrowsyMovement` | `true` |
| `bool` | `EnableClinicalEffects` | `true` |
| `bool` | `EnableSymptomVisuals` | `true` |
| `double` | `WoundInfectionHazardPerSecond` | `0.00005` |
| `double` | `RespiratoryTransmissionUnitsPerSecond` | `0.005` |
| `double` | `BathWaterCoolingHalfLifeSeconds` | `5400` |
| `double` | `BathWaterThermalKillPerDegreeSecond` | `0.00002` |
| `double` | `HandToFoodTransferFraction` | `.2` |
| `double` | `CleanWaterHandRetention` | `.1` |
| `double` | `DirtyWaterHandRetention` | `.5` |
| `DiseaseExposureOptions` | `DiseaseExposure` | `new()` |
| `SurfaceWaterOptions` | `SurfaceWater` | `new()` |
| `SanitationOptions` | `Sanitation` | `new()` |
| `ThermalAdaptationOptions` | `ThermalAdaptation` | `new()` |
| `PainOptions` | `Pain` | `new()` |
| `CirculationOptions` | `Circulation` | `new()` |
| `ExertionOptions` | `Exertion` | `new()` |
| `double` | `DigestionGPerGameHour` | `1667` |
| `DigestionOptions` | `Digestion` | `new()` |
| `double` | `BasalWaterLossGPerGameHour` | `75` |
| `double` | `UrineProductionMlPerGameHour` | `60` |
| `double` | `EntericWaterLossLPerHour` | `0.5` |
| `double` | `ClinicalDamageMultiplier` | `1` |
| `bool` | `EnableInjuryActionEffects` | `true` |
| `string` | `Format` | `"seraph.release.config"` |
| `int` | `ConfigVersion` | `1` |
| `string` | `Mode` | `"survival"` |
| `double` | `PhysiologySpeed` | `1` |
| `double` | `FatigueRiseSeconds` | `172800` |
| `double` | `FatigueSleepRecoverySeconds` | `28800` |
| `double` | `FatigueSeatedRecoverySeconds` | `28800 / .385` |
| `double` | `SleepPressureRiseSeconds` | `90000` |
| `double` | `SleepPressureRecoverySeconds` | `28800` |
| `double` | `BedSleepPressureRecoveryMultiplier` | `2` |
| `int` | `CheckpointSeconds` | `30` |
| `bool` | `EnableMovementEffects` | `true` |
| `bool` | `EnableWoundTracking` | `true` |
| `bool` | `EnableGroundWaterDrinking` | `true` |
| `bool` | `EnableMedicalActions` | `true` |
| `double` | `EstimatedKJPerSaturation` | `8` |
| `double` | `DrinkServingL` | `0.25` |
| `double` | `DrinkCooldownRealSeconds` | `3` |
| `bool` | `EnableDefecation` | `true` |
| `double` | `BowelUnitsPerSaturation` | `0.2` |
| `double` | `FreshWaterHazardPerL` | `0.02` |
| `double` | `RainWaterHazardPerL` | `0.005` |
| `double` | `FecalWaterHazardPerL` | `0.5` |
| `double` | `DefaultRelativeHumidity` | `0.5` |
| `double` | `DefaultClothingClo` | `0.6` |
| `double` | `WindGameUnitToMps` | `1` |
| `double` | `HeatCacheToRadiantC` | `4` |
| `double` | `SolarPowerWAtFullExposure` | `500` |
| `double` | `RoomHeatMaxBonusC` | `18` |
| `double` | `RoomHeatCelsiusPerStrength` | `1.8` |
| `double` | `RoomHeatHalfLifeHours` | `4` |
| `double` | `RainGameUnitToFilmKgPerSecond` | `0.0001` |
| `int` | `CsvMaximumMiB` | `16` |

## 校验边界

`Format` 必须为 `seraph.release.config`，`ConfigVersion=1`；`Mode` 只能 `survival`、`shadow`、`observe`；`PhysiologySpeed` 只能 0.1–20；检查点 10–300 秒；饮水份量 0.01–1 L；所有对象和映射都有数量/数值上限。修改后使用 `/vsscsmod reload config` 仅适用于文明配置；生存配置由 `vsslssmod.Server.json` 启动时读取，重启后验证。

## 嵌套选项默认值与校验

以下表格直接来自配置属性所引用的 record 类型；范围来自各类型的 `Validate()`。

### `DiseaseExposure`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `IndirectHazardPerGameHour` | `.1` |
| `double` | `VectorLandingHazardPerGameHour` | `.05` |
| `double` | `VectorMaturationGameHours` | `2` |
| `double` | `VectorInfectiousChance` | `.1` |
| `double` | `VectorBiteHazard` | `.2` |
| `double` | `BiteHazard` | `.8` |
| `double` | `SepsisHpPerTenGameMinutes` | `5` |
| `double` | `SepsisOnsetHours` | `2` |
| `double` | `SepsisRecoveryHours` | `2` |
### `SurfaceWater`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `PondTurbidity` | `.30` |
| `double` | `LakeTurbidity` | `.16` |
| `double` | `RiverTurbidity` | `.1` |
| `double` | `PondShigellaPerL` | `50` |
| `double` | `LakeShigellaPerL` | `35` |
| `double` | `RiverShigellaPerL` | `20` |
### `Sanitation`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `DirtyGroundPerGameHour` | `.0025` |
| `double` | `PollutionPerPointPerGameHour` | `.00025` |
| `double` | `DirtyWaterRisePerGameHour` | `.006` |
| `double` | `CleanWaterFallPerGameHour` | `.5` |
| `double` | `RainWashPerGameHour` | `.1` |
| `double` | `CleanGameHours` | `24` |
| `double` | `BathedGameHours` | `72` |
### `ThermalAdaptation`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `TrainingHours` | `168` |
| `double` | `DecayHalfLifeHours` | `72` |
### `Pain`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `AcuteHalfLifeHours` | `2` |
| `double` | `SlowAcuteHalfLifeHours` | `6` |
### `Circulation`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `RegenerationMlPerGameHour` | `180` |
| `double` | `FiltrationMlPerGameHour` | `72` |
| `double` | `LactateClearanceGPerGameHour` | `400` |
| `double` | `LactateStandingHalfLifeSeconds` | `180` |
| `double` | `LactateWalkingHalfLifeSeconds` | `300` |
| `double` | `LactateSeatedHalfLifeSeconds` | `150` |
| `double` | `RenalToxicityThreshold` | `.5` |
| `double` | `RenalBasalMultiplier` | `1.55` |
| `double` | `RenalClearanceMultiplier` | `2` |
| `double` | `RenalElectrolytesMgPerExtraMl` | `0` |
### `Exertion`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `BurstSeconds` | `3` |
| `double` | `BurstTransitionSeconds` | `1` |
| `double` | `BurstRearmSeconds` | `2` |
| `double` | `RunningSpeedGain` | `.8` |
| `double` | `RunningStaminaPerSecond` | `.009` |
| `double` | `JoggingSpeedGain` | `.25` |
| `double` | `RunningSlowdownStamina` | `.20` |
| `double` | `RestDelaySeconds` | `2` |
| `double` | `SeatedRecoverySeconds` | `25` |
| `double` | `StandingRecoverySeconds` | `50` |
| `double` | `WalkingRecoverySeconds` | `100` |
| `double` | `UnlockStamina` | `.20` |
| `double` | `ExhaustedJumpCooldownSeconds` | `3` |
| `double` | `UnlockLactateRatio` | `.6` |
### `Digestion`

| 类型 | 字段 | 默认值 |
| --- | --- | --- |
| `double` | `WaterHalfLifeHours` | `1d / 3` |
| `double` | `CarbohydrateHalfLifeHours` | `1.5` |
| `double` | `ProteinHalfLifeHours` | `2` |
| `double` | `FatHalfLifeHours` | `3` |
| `double` | `ResidueHalfLifeHours` | `3` |
| `double` | `MicronutrientHalfLifeHours` | `2` |
| `double` | `ProteinDigestSlowMul` | `2.25` |
| `double` | `WaterMlPerHour` | `2000` |
