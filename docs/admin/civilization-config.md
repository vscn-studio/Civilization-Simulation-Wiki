# 文明模组默认配置

以下是文明模组 1.0.0 配置示例，不是服务器当前值。配置和迁移方式见[文明模组手册](/guide/civilization)。主配置可在管理员界面保存或通过指令重载；传说限制修改后需重启。

## SeraphCivilizationLoreRestrictions.example.json

```json
{
  "Enabled": true,
  "OnlyWhenLoreDisabled": true,
  "RemoveExistingRestrictedEntities": true,
  "LivingDeadSpawns": true,
  "GreenWillowispSpawns": true,
  "WhiteWillowispSpawns": true,
  "YellowWillowispSpawns": true,
  "LivingDeadTemporalGearDrops": true,
  "SkullOfTheDead": true,
  "HandOfTheDead": true,
  "BoneSoilTemporalGearDrops": true,
  "BoneSoilLoreBookDrops": true,
  "BoneSoilLoreCylinderDrops": true,
  "TemporalAmuletTeleport": true,
  "TemporalWinterSkip": true,
  "EquusRevival": true,
  "ImmersiveTemporalMaps": true,
  "TemporalTemperatureForecaster": true,
  "ScribeClockmakerNotebookRecipe": true,
  "VinconomyCatalogRecipe": true,
  "CaravanTemporalGearSign": true,
  "ExpandedMatterTemporalMaterials": true,
  "ShipwrightLoreFigureheads": true,
  "HeraldryDrifterPattern": true,
  "HeraldryEidolonPattern": true
}
```

## SeraphCivilizationSimulation.example.json

```json
{
  "DisableVintageCanvasArtistClass": true,
  "PaperMaps": {
    "MaxSheets": 49
  },
  "ModPolicy": {
    "Enabled": true,
    "Mode": "Whitelist",
    "IncludeServerMods": true,
    "ReportTimeoutSeconds": 30,
    "Mods": []
  },
  "Respawn": {
    "Enabled": true,
    "ProtectionSeconds": 10,
    "InitialLives": 3,
    "NewbornMinimumLivingMembers": 5,
    "ReincarnationChance": 1.0,
    "HomecomingMinimumChance": 0.5,
    "HomecomingChancePerExtraLivingMember": 0.1,
    "ReincarnationLives": 3,
    "ReincarnationOutsideRange": 10
  },
  "Sleep": {
    "Enabled": true
  },
  "Tribes": {
    "AllowSoloCreation": false
  },
  "Territory": {
    "BoundaryDisplayEnabled": true,
    "CenterCooldownMinutes": 60,
    "FirstOutpostMembers": 4,
    "SecondOutpostMembers": 6,
    "MaxOutposts": 2,
    "HealthBonus": 0,
    "ReinforcementPerLivingMember": 10,
    "ReinforcementMaximum": 200,
    "ReinforcementRecoveryPerMemberPerMinute": 0.2,
    "ReinforcementRecoveryMaximumPerMinute": 4,
    "ReinforcementRecoveryDelaySeconds": 600
  },
  "TribeAuthorization": {
    "Enabled": true,
    "ConstructionEnabled": true,
    "BenefitsEnabled": true,
    "BlockUnauthorizedReinforcement": true,
    "BlockUnauthorizedLocks": true,
    "ReinforcementExclusionsEnabled": true,
    "ReinforcementExcludedBlocks": [
      "*:ladder*",
      "*:crudeladder*",
      "*:ropeladder*",
      "*:rope-ladder*",
      "*:scaffold*",
      "*:torch*",
      "*:lantern*",
      "*:paperlantern*",
      "*:candle*",
      "*:oillamp*",
      "*:carpet*",
      "*:rug-*",
      "*:snowlayer*",
      "*:loosestones*",
      "*:loosestick*",
      "*:leaflitter*",
      "*:tallgrass*",
      "*:flower-*",
      "*:fern-*",
      "*:mushroom-*",
      "*:crop-*",
      "*:sapling-*",
      "*:vine-*",
      "*:ivy-*",
      "*:reeds-*",
      "*:cattail-*"
    ],
    "OutsiderPlacementCooldownEnabled": false,
    "OutsiderPlacementCooldownSeconds": 2,
    "OutsiderBlockQuotaEnabled": false,
    "OutsiderBlockQuota": 64,
    "ProtectCriticalAreas": false,
    "CriticalAreaRadius": 5
  },
  "BuildingProtection": {
    "Enabled": true,
    "FireProtectionDamagePerSecond": 0.2,
    "ArrowContactSeconds": 12,
    "CoolingPerSecond": 0.5,
    "ManualFireDelayMaximumSeconds": 120,
    "ManualFireStrengthForMaximum": 200,
    "GrassIgnitionSeconds": 2,
    "GrassFailureSeconds": 15,
    "ClothIgnitionSeconds": 4,
    "ClothFailureSeconds": 25,
    "WoodIgnitionSeconds": 45,
    "WoodFailureSeconds": 120,
    "TimberIgnitionSeconds": 90,
    "TimberFailureSeconds": 240
  },
  "Clusters": {
    "Enabled": true,
    "TotalClusters": 10,
    "GlobalRadius": 10000,
    "ClusterRadius": 250,
    "MinDistanceBetween": 1000,
    "MaxPlayersPerCluster": 15,
    "LandValidationRadius": 150,
    "MinLandRatio": 0.6,
    "AvoidOceans": true,
    "AvoidExtremeClimate": true,
    "MinTemperature": -5.0,
    "MaxTemperature": 35.0,
    "AssignmentMode": "Sequential",
    "ManualClusters": []
  },
  "Roster": {
    "HeaderSvg": "<svg viewBox=\"0 0 700 120\" xmlns=\"http://www.w3.org/2000/svg\" preserveAspectRatio=\"xMidYMid meet\">\n  <rect x=\"32\" y=\"24\" width=\"36\" height=\"36\" rx=\"4\" fill=\"#6b8e23\"/>\n  <rect x=\"104\" y=\"24\" width=\"36\" height=\"36\" rx=\"4\" fill=\"#8b5a2b\"/>\n  <rect x=\"68\" y=\"60\" width=\"36\" height=\"36\" rx=\"4\" fill=\"#555\"/>\n  <text x=\"164\" y=\"78\" font-size=\"50\" font-family=\"Inter, Arial, Helvetica, sans-serif\" font-weight=\"600\" textLength=\"504\" lengthAdjust=\"spacingAndGlyphs\" fill=\"#fff\">复古物语中文社区</text>\n</svg>"
  }
}
```
