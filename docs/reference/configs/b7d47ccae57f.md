<!-- generated:start -->
# Watersheds/Braided/BraidedConfig.json

[返回全部配置表](/admin/config-tables)

来源：指定服务器 `ModConfig/Watersheds/Braided/BraidedConfig.json`；路径以 `/` 分隔，数字是数组索引。

| 字段路径 | 类型 | 当前值 |
| --- | --- | --- |
| <code>/Description</code> | string | <code>"Settings for the braided streams."</code> |
| <code>/EnabledChance</code> | number | <code>50</code> |
| <code>/EnabledChanceDescription</code> | string | <code>已隐藏地址</code> |
| <code>/HistoricalIterations</code> | number | <code>3</code> |
| <code>/HistoricalIterationsDescription</code> | string | <code>"Number of historical meandering iterations to render before the final.&lt;br&gt;Each appears at reduced opacity, creating faded historical stream channels.&lt;br&gt;For example, with 5 historical iterations, opacities are: 17%, 33%, 50%, 67%, 83%, then 100% for the final path."</code> |
| <code>/MinOpacity</code> | number | <code>0.35</code> |
| <code>/MinOpacityDescription</code> | string | <code>"Opacity for the oldest historical path.&lt;br&gt;Opacity scales linearly from MaxOpacity for the first historical path to this on the final historical path.&lt;br&gt;0.25 means the oldest historical opacity is at 25%, 0.5 means the oldest is at 50%."</code> |
| <code>/MaxOpacity</code> | number | <code>1</code> |
| <code>/MaxOpacityDescription</code> | string | <code>"Opacity for the historical path.&lt;br&gt;Opacity scales linearly from this for the first historical path to MinOpacity on the final historical path.&lt;br&gt;0.5 means the newest historical path's opacity is at 50%, 0.75 means the newest is at 75%."</code> |
| <code>/CaptureGap</code> | number | <code>2</code> |
| <code>/CaptureGapDescription</code> | string | <code>"Number of meandering iterations between each historical path capture.&lt;br&gt;A higher CaptureGap means more visual difference between historical paths.&lt;br&gt;With 29 iterations, 5 historical captures, and gap of 4: captures at iterations 8, 12, 16, 20, 24, final at 28."</code> |
| <code>/MeanderIterations</code> | number | <code>16</code> |
| <code>/MeanderIterationsDescription</code> | string | <code>"Number of iterative passes for the progressive meandering on braided streams.&lt;br&gt;Each iteration applies small displacements that accumulate over the iterations into larger meanders.&lt;br&gt;Not enough iterations and the streams will be basic, more closely resembling their base bezier curves.&lt;br&gt;After a certain point the iterations becomes meaningless. You can meander the streams forever."</code> |
| <code>/SinuosityAtSource</code> | number | <code>1.4</code> |
| <code>/SinuosityAtSourceDescription</code> | string | <code>"Sinuosity at the braided stream source.&lt;br&gt;Sinuosity scales the amplitude of the meandering sine-based curves per iteration.&lt;br&gt;The sinuosity lerps from the source to the anchor based on the distance along the stream.&lt;br&gt;Super volatile value, completely changes how meandering works with even a tiny change."</code> |
| <code>/SinuosityAtAnchor</code> | number | <code>1.4</code> |
| <code>/SinuosityAtAnchorDescription</code> | string | <code>"Sinuosity at the anchor point for braided streams.&lt;br&gt;Streams longer than anchor length continue extrapolating linearly.&lt;br&gt;1.0 means a straight line. 1.5+ gives massive meandering.&lt;br&gt;The sinuosity lerps from the source to the anchor based on the distance along the stream.&lt;br&gt;Super volatile value, completely changes how meandering works with even a tiny change."</code> |
| <code>/WavelengthMultiplierAtSource</code> | number | <code>6.6</code> |
| <code>/WavelengthMultiplierAtSourceDescription</code> | string | <code>"Wavelength multiplier at the braided stream source (thin end).&lt;br&gt;The meander wavelength (meander length down the stream) at each point is the streambed width at that point multiplied by this value.&lt;br&gt;Higher wavelength multiplier means longer, more gradual meanders.&lt;br&gt;Lower wavelength multiplier means tighter, more frequent bends.&lt;br&gt;You can use UseConstantBeltWidthRatio (on by default) instead of this for simpler but less fine tuned meander wavelengths."</code> |
| <code>/WavelengthMultiplierAtAnchor</code> | number | <code>1.39</code> |
| <code>/WavelengthMultiplierAtAnchorDescription</code> | string | <code>"Wavelength multiplier at the anchor point for braided streams.&lt;br&gt;Streams longer than anchor length continue growing the meander wavelength linearly.&lt;br&gt;The meander wavelength (meander length down the stream) at each point is the streambed width at that point multiplied by this value.&lt;br&gt;Higher wavelength multiplier means longer, more gradual meanders.&lt;br&gt;Lower wavelength multiplier means tighter, more frequent bends.&lt;br&gt;You can use UseConstantBeltWidthRatio (on by default) instead of this for simpler but less fine tuned meander wavelengths."</code> |
| <code>/UseConstantBeltWidthRatio</code> | boolean | <code>true</code> |
| <code>/UseConstantBeltWidthRatioDescription</code> | string | <code>"When true, automatically calculates wavelength multipliers to maintain a constant meander belt width to stream width ratio along all positions in the braided river.&lt;br&gt;The ratio is set by BeltWidthToStreamWidthRatio.&lt;br&gt;When false, the meandering uses the manually set WavelengthMultiplierAtSource and WavelengthMultiplierAtAnchor values instead."</code> |
| <code>/BeltWidthToStreamWidthRatio</code> | number | <code>6</code> |
| <code>/BeltWidthToStreamWidthRatioDescription</code> | string | <code>"Target ratio of meander belt width to stream bed width for braided streams. Only used when UseConstantBeltWidthRatio is true.&lt;br&gt;0.35 means the meander belt width is 35% of stream width. Higher that than means you get wider meander belts relative to the stream width.&lt;br&gt;The wavelength multipliers are automatically calculated from this ratio and the sinuosity values."</code> |
| <code>/MeanderFading/SourceDistanceAtAnchor</code> | number | <code>50</code> |
| <code>/MeanderFading/SourceDistanceAtAnchorDescription</code> | string | <code>"Distance from the braided stream source (in blocks) when the stream is at the anchor's stream length, over which to fade meandering back to the original path.&lt;br&gt;This distance scales with stream length: short streams have proportionally shorter fade distances, long streams have proportionally longer fade distances.&lt;br&gt;Basically, its how big the fadeout of meandering is near the stream source."</code> |
| <code>/MeanderFading/MouthDistanceAtAnchor</code> | number | <code>300</code> |
| <code>/MeanderFading/MouthDistanceAtAnchorDescription</code> | string | <code>"Distance from the braided stream drain/connection (in blocks) when the stream is at the anchor's stream length, over which to fade meandering back to a straight connection.&lt;br&gt;This distance scales with stream length: short streams have proportionally shorter fade distances, long streams have proportionally longer fade distances.&lt;br&gt;Basically, its how big the fadeout of meandering is near the stream mouth."</code> |
| <code>/MeanderFadingDescription</code> | string | <code>"Configuration for fading out meandering into a smooth path at the braided stream source and mouth."</code> |
| <code>/CurvePointSmoothing/WindowRadius</code> | number | <code>8</code> |
| <code>/CurvePointSmoothing/WindowRadiusDescription</code> | string | <code>"Number of neighboring points on each side to include in smoothing window for braided streams.&lt;br&gt;Controls spatial extent of smoothing effect. Applied per iteration.&lt;br&gt;1 gives a 3-point window (current + 2 neighbors), 2 gives a 5-point window, 3 gives a 7-point window."</code> |
| <code>/CurvePointSmoothing/Strength</code> | number | <code>1</code> |
| <code>/CurvePointSmoothing/StrengthDescription</code> | string | <code>"Controls the intensity of the smoothing within the smoothing window for braided streams.&lt;br&gt;0.0 to 1.0 is no smoothing to full smoothing, and 1.0+ is even more smoothing.&lt;br&gt;Adjust together with WindowRadius."</code> |
| <code>/CurvePointSmoothingDescription</code> | string | <code>"Configuration for smoothing out the braided stream path (the curve points) inbetween the iterations of meandering."</code> |
| <code>/SteepTerrainStraightening/BlendStrength</code> | number | <code>0.5</code> |
| <code>/SteepTerrainStraightening/BlendStrengthDescription</code> | string | <code>"Maximum strength of blending the meandered path back to original bezier curve path in and around steep terrain.&lt;br&gt;0 means no blending (full meandering everywhere). 1 means a hard switch to the bezier curve when the path gets to an area with the max steepness.&lt;br&gt;This prevents streams from meandering the path into nearby cliffs and hills, and keeps the stream path clean on mountains.&lt;br&gt;Use with HeightThreshold to define the relationship between terrain height and blend strength"</code> |
| <code>/SteepTerrainStraightening/HeightThreshold</code> | number | <code>60</code> |
| <code>/SteepTerrainStraightening/HeightThresholdDescription</code> | string | <code>"Height difference (in blocks) at which steep terrain blending reaches full strength.&lt;br&gt;The blending lerps from 0 blending at 0 height difference to the full blending strength (BlendStrength) at this configured threshold.&lt;br&gt;This prevents streams from meandering the path into nearby cliffs and hills, and keeps the stream path clean on mountains.&lt;br&gt;Use with BlendStrength to define the relationship between terrain height and blend strength"</code> |
| <code>/SteepTerrainStraightening/SearchRadius</code> | number | <code>0</code> |
| <code>/SteepTerrainStraightening/SearchRadiusDescription</code> | string | <code>"Manhattan distance radius (in chunks) for searching neighboring terrain when calculating max height difference.&lt;br&gt;0 means only use the current chunk. 1 means include immediate neighbors. 2+ means a larger search area.&lt;br&gt;A larger radius catches steep/rough terrain that is further from the stream path.Increase it if you find streams meandering into rough terrain, otherwise leave at 0"</code> |
| <code>/SteepTerrainStraighteningDescription</code> | string | <code>"Configuration for straightening streams around steep terrain to prevent meandering into cliffs and hills, and to keep mountain streams clean."</code> |
| <code>/OxbowCutoff/ProximityThreshold</code> | number | <code>0.75</code> |
| <code>/OxbowCutoff/ProximityThresholdDescription</code> | string | <code>"Minimum distance between meander curves as fraction of the local meander's amplitude for braided streams."</code> |
| <code>/OxbowCutoff/MinWavelengthArcLengthFraction</code> | number | <code>0.2</code> |
| <code>/OxbowCutoff/MinWavelengthArcLengthFractionDescription</code> | string | <code>"Minimum arc length gap between segments of the braided stream path, as a fraction of the local wavelength.&lt;br&gt;Only segment pairs separated by at least this fraction of the wavelength are checked for oxbow cutoffs."</code> |
| <code>/OxbowCutoff/MaxCutAttempts</code> | number | <code>100</code> |
| <code>/OxbowCutoff/MaxCutAttemptsDescription</code> | string | <code>"Maximum attempts to cut oxbows per iteration for braided streams."</code> |
| <code>/OxbowCutoffDescription</code> | string | <code>"Configuration for cutting off a braided stream as it intersects with itself via meandering, creating an oxbow lake."</code> |
| <code>/DrainMovement/DrainMigrateRadius</code> | number | <code>128</code> |
| <code>/DrainMovement/DrainMigrateRadiusDescription</code> | string | <code>"The stream mouths can migrate this amount of blocks away from it's original drain mouths, if their stream mouths can migrate.&lt;br&gt;At time of writing, this is for meandering and braided streams."</code> |
| <code>/DrainMovement/SlowdownInnerMigrateRadiusFraction</code> | number | <code>0.5</code> |
| <code>/DrainMovement/SlowdownInnerMigrateRadiusFractionDescription</code> | string | <code>"This is the fraction of DrainMigrateRadius where a strream mouth can migrate before getting slowed down."</code> |
| <code>/DrainMovement/DistributaryFanStrength</code> | number | <code>0.1</code> |
| <code>/DrainMovement/DistributaryFanStrengthDescription</code> | string | <code>"Strength of the fanning out effect on the original braided stream mouth positions."</code> |
| <code>/DrainMovement/DistributaryFanDistance</code> | number | <code>150</code> |
| <code>/DrainMovement/DistributaryFanDistanceDescription</code> | string | <code>"Distributary fanning effect starts this distance away from the original stream mouth."</code> |
| <code>/DrainMovement/DistributarySpreadAtAnchor</code> | number | <code>45</code> |
| <code>/DrainMovement/DistributarySpreadAtAnchorDescription</code> | string | <code>"How many blocks each braided distributary channel's mouth is fanned left&amp;right along the coastline at the anchor length."</code> |
| <code>/DrainMovement/MouthStraighteningStrength</code> | number | <code>0.1</code> |
| <code>/DrainMovement/MouthStraighteningStrengthDescription</code> | string | <code>"To prevent the stream meandering around/on the stream mouth we straighten it up between the stream mouth and (the scaled) mouthFadeAtAnchor.&lt;br&gt;0.0 is no straightening 1.0 is full strength straightening."</code> |
| <code>/DrainMovementDescription</code> | string | <code>"Configs for the moving the stream mouths/drain points along the coast."</code> |

配置表没有列为默认值的内容均来自当前实例；不应直接照搬到另一个服务器。Seraph 的已核验含义、范围和生效方式见[管理员入口](/admin/)。
<!-- generated:end -->
