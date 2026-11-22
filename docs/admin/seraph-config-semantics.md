<!-- generated:start -->
# 生存配置：中文含义、当前值与校验

这里列出服务器配置表中的当前值。修改文件后按[配置操作流程](/pack/configuration)重启并验证。

## 阅读方法

每项先给中文含义，再保留可搜索的原字段。危险参数、病原负荷和概率不是同一种数值，不能统一换算为百分比。

| 中文含义 | 原字段路径 | 当前值 | 校验说明 |
| --- | --- | --- | --- |
| 困倦时单次合眼转向开关（旧字段名） | <code>/EnableDrowsyMovement</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 临床效果开关 | <code>/EnableClinicalEffects</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 症状视觉效果开关 | <code>/EnableSymptomVisuals</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 伤口感染危险率／秒 | <code>/WoundInfectionHazardPerSecond</code> | <code>5e-05</code> | 直接数值边界：0～.01 |
| 呼吸道传播单位／秒 | <code>/RespiratoryTransmissionUnitsPerSecond</code> | <code>0.005</code> | 直接数值边界：0～1 |
| 物品呼吸防护比例表 | <code>/RespiratoryProtectionByCode</code> | <code>{}</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 方块呼吸道病原来源表 | <code>/RespiratorySourcesByBlockCode</code> | <code>{}</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 浴水降温半衰期（秒） | <code>/BathWaterCoolingHalfLifeSeconds</code> | <code>5400</code> | 直接数值边界：60～604800 |
| 浴水热灭活系数／度秒 | <code>/BathWaterThermalKillPerDegreeSecond</code> | <code>2e-05</code> | 直接数值边界：0～.01 |
| 手部污染转入食物的比例 | <code>/HandToFoodTransferFraction</code> | <code>0.2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 洁净水清洗后的手部污染保留比例 | <code>/CleanWaterHandRetention</code> | <code>0.1</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 脏水清洗后的手部污染保留比例 | <code>/DirtyWaterHandRetention</code> | <code>0.5</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 间接暴露危险率／游戏小时 | <code>/DiseaseExposure/IndirectHazardPerGameHour</code> | <code>0.1</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 虫媒附着危险率／游戏小时 | <code>/DiseaseExposure/VectorLandingHazardPerGameHour</code> | <code>0.05</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 虫媒成熟时间（游戏小时） | <code>/DiseaseExposure/VectorMaturationGameHours</code> | <code>2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 虫媒带病概率参数 | <code>/DiseaseExposure/VectorInfectiousChance</code> | <code>0.1</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 虫媒叮咬危险参数 | <code>/DiseaseExposure/VectorBiteHazard</code> | <code>0.2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 咬伤危险参数 | <code>/DiseaseExposure/BiteHazard</code> | <code>0.8</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 败血症每 10 游戏分钟伤害 | <code>/DiseaseExposure/SepsisHpPerTenGameMinutes</code> | <code>5</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 败血症危险条件持续时间（小时） | <code>/DiseaseExposure/SepsisOnsetHours</code> | <code>2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 败血症恢复条件持续时间（小时） | <code>/DiseaseExposure/SepsisRecoveryHours</code> | <code>2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 池塘浑浊度 | <code>/SurfaceWater/PondTurbidity</code> | <code>0.4</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 湖泊浑浊度 | <code>/SurfaceWater/LakeTurbidity</code> | <code>0.15</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 河流浑浊度 | <code>/SurfaceWater/RiverTurbidity</code> | <code>0.1</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 池塘每升志贺菌负荷 | <code>/SurfaceWater/PondShigellaPerL</code> | <code>50</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 湖泊每升志贺菌负荷 | <code>/SurfaceWater/LakeShigellaPerL</code> | <code>35</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 河流每升志贺菌负荷 | <code>/SurfaceWater/RiverShigellaPerL</code> | <code>20</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 配置有效性计算结果（非独立玩法开关） | <code>/SurfaceWater/Valid</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 脏污地面引起的脏污增量／游戏小时 | <code>/Sanitation/DirtyGroundPerGameHour</code> | <code>0.01</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 每污染点的脏污增量／游戏小时 | <code>/Sanitation/PollutionPerPointPerGameHour</code> | <code>0.001</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 脏水造成的脏污增量／游戏小时 | <code>/Sanitation/DirtyWaterRisePerGameHour</code> | <code>0.02</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 洁净水清洁速率／游戏小时 | <code>/Sanitation/CleanWaterFallPerGameHour</code> | <code>0.5</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 雨水清洗速率／游戏小时 | <code>/Sanitation/RainWashPerGameHour</code> | <code>0.1</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 清洁状态时长（游戏小时） | <code>/Sanitation/CleanGameHours</code> | <code>24</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 洗浴状态时长（游戏小时） | <code>/Sanitation/BathedGameHours</code> | <code>72</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 冷热适应训练时间（小时） | <code>/ThermalAdaptation/TrainingHours</code> | <code>168</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 适应衰减半衰期（小时） | <code>/ThermalAdaptation/DecayHalfLifeHours</code> | <code>72</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 急性疼痛半衰期（小时） | <code>/Pain/AcuteHalfLifeHours</code> | <code>2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 慢速急性疼痛半衰期（小时） | <code>/Pain/SlowAcuteHalfLifeHours</code> | <code>6</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 基础造血速率（毫升／游戏小时） | <code>/Circulation/RegenerationMlPerGameHour</code> | <code>180</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 基础过滤速率（毫升／游戏小时） | <code>/Circulation/FiltrationMlPerGameHour</code> | <code>72</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 乳酸清除参数（克／游戏小时） | <code>/Circulation/LactateClearanceGPerGameHour</code> | <code>400</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 站立乳酸半衰期（现实秒） | <code>/Circulation/LactateStandingHalfLifeSeconds</code> | <code>180</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 步行乳酸半衰期（现实秒） | <code>/Circulation/LactateWalkingHalfLifeSeconds</code> | <code>300</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 坐姿乳酸半衰期（现实秒） | <code>/Circulation/LactateSeatedHalfLifeSeconds</code> | <code>150</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 肾脏反应毒性阈值 | <code>/Circulation/RenalToxicityThreshold</code> | <code>0.5</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 肾脏反应基础倍率 | <code>/Circulation/RenalBasalMultiplier</code> | <code>1.55</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 肾脏反应清除倍率 | <code>/Circulation/RenalClearanceMultiplier</code> | <code>2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 额外清除量的电解质参数（毫克／毫升；实际结算需看调用） | <code>/Circulation/RenalElectrolytesMgPerExtraMl</code> | <code>50</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 疾跑爆发时长（现实秒） | <code>/Exertion/BurstSeconds</code> | <code>3</code> | 直接数值边界：1～10 |
| 疾跑转为快跑的过渡时间（现实秒） | <code>/Exertion/BurstTransitionSeconds</code> | <code>1</code> | 直接数值边界：.2～5 |
| 疾跑爆发再次就绪的间隔（现实秒） | <code>/Exertion/BurstRearmSeconds</code> | <code>2</code> | 直接数值边界：1～30 |
| 快跑速度增益参数 | <code>/Exertion/RunningSpeedGain</code> | <code>0.8</code> | 直接数值边界：.5～.95 |
| 快跑每现实秒耐力消耗 | <code>/Exertion/RunningStaminaPerSecond</code> | <code>0.009</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 慢跑速度增益参数 | <code>/Exertion/JoggingSpeedGain</code> | <code>0.25</code> | 直接数值边界：.05～.5 |
| 快跑降速的耐力阈值 | <code>/Exertion/RunningSlowdownStamina</code> | <code>0.2</code> | 直接数值边界：.1～.5 |
| 停止强动作后的体力恢复等待时间（现实秒） | <code>/Exertion/RestDelaySeconds</code> | <code>2</code> | 直接数值边界：0～60 |
| 坐姿恢复时间（现实秒） | <code>/Exertion/SeatedRecoverySeconds</code> | <code>25</code> | 直接数值边界：1～3600 |
| 站立恢复时间（现实秒） | <code>/Exertion/StandingRecoverySeconds</code> | <code>50</code> | 直接数值边界：1～3600 |
| 步行恢复时间（现实秒） | <code>/Exertion/WalkingRecoverySeconds</code> | <code>100</code> | 直接数值边界：1～3600 |
| 解除体力锁定的耐力阈值 | <code>/Exertion/UnlockStamina</code> | <code>0.2</code> | 直接数值边界：.1～1 |
| 力竭跳跃冷却（现实秒） | <code>/Exertion/ExhaustedJumpCooldownSeconds</code> | <code>3</code> | 直接数值边界：1～10 |
| 解除锁定的乳酸比例阈值 | <code>/Exertion/UnlockLactateRatio</code> | <code>0.6</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 消化吞吐量（克／游戏小时） | <code>/DigestionGPerGameHour</code> | <code>1000</code> | 直接数值边界：1～10000 |
| 胃水排空半衰期（小时） | <code>/Digestion/WaterHalfLifeHours</code> | <code>0.5</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 碳水排空半衰期（小时） | <code>/Digestion/CarbohydrateHalfLifeHours</code> | <code>1.5</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 蛋白质排空半衰期（小时） | <code>/Digestion/ProteinHalfLifeHours</code> | <code>2</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 脂肪排空半衰期（小时） | <code>/Digestion/FatHalfLifeHours</code> | <code>3</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 残渣排空半衰期（小时） | <code>/Digestion/ResidueHalfLifeHours</code> | <code>3</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 水吸收速率上限（毫升／小时） | <code>/Digestion/WaterMlPerHour</code> | <code>1000</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 基础失水量（克／游戏小时） | <code>/BasalWaterLossGPerGameHour</code> | <code>75</code> | 直接数值边界：0～10000 |
| 肠道疾病失水参数（升／小时） | <code>/EntericWaterLossLPerHour</code> | <code>0.5</code> | 直接数值边界：0～10 |
| 临床伤害倍率 | <code>/ClinicalDamageMultiplier</code> | <code>1</code> | 直接数值边界：0～10 |
| 伤势行动效果开关 | <code>/EnableInjuryActionEffects</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 配置格式标识 | <code>/Format</code> | <code>"seraph.release.config"</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 配置格式版本 | <code>/ConfigVersion</code> | <code>1</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 睡压上升时间（显式游戏小时，非空时覆盖秒值） | <code>/SleepPressureRiseGameHours</code> | <code>null</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 睡压恢复时间（显式游戏小时，非空时覆盖秒值） | <code>/SleepPressureRecoveryGameHours</code> | <code>null</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 疲劳上升时间（显式游戏小时，非空时覆盖秒值） | <code>/FatigueRiseGameHours</code> | <code>null</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 睡眠恢复疲劳时间（显式游戏小时，非空时覆盖秒值） | <code>/FatigueSleepRecoveryGameHours</code> | <code>null</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 坐姿恢复疲劳时间（显式游戏小时，非空时覆盖秒值） | <code>/FatigueSeatedRecoveryGameHours</code> | <code>null</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 运行模式 | <code>/Mode</code> | <code>"survival"</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 生理时间速度倍率 | <code>/PhysiologySpeed</code> | <code>1</code> | 直接数值边界：SchedulerOptions.MinimumPhysiologySpeed～SchedulerOptions.MaximumPhysiologySpeed |
| 疲劳上升时间（规范化游戏秒） | <code>/FatigueRiseSeconds</code> | <code>172800</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 睡眠恢复疲劳时间（规范化游戏秒） | <code>/FatigueSleepRecoverySeconds</code> | <code>28800</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 坐姿恢复疲劳时间（规范化游戏秒） | <code>/FatigueSeatedRecoverySeconds</code> | <code>74805.1948051948</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 睡压上升时间（规范化游戏秒） | <code>/SleepPressureRiseSeconds</code> | <code>90000</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 睡压恢复时间（规范化游戏秒） | <code>/SleepPressureRecoverySeconds</code> | <code>28800</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 床上睡眠的睡压恢复倍率 | <code>/BedSleepPressureRecoveryMultiplier</code> | <code>2</code> | 直接数值边界：1～8 |
| 遥测开关 | <code>/TelemetryEnabled</code> | <code>false</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 检查点间隔（秒） | <code>/CheckpointSeconds</code> | <code>30</code> | 直接数值边界：10～300 |
| 移动效果开关 | <code>/EnableMovementEffects</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 伤口追踪开关 | <code>/EnableWoundTracking</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 地面水源饮用开关 | <code>/EnableGroundWaterDrinking</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 护理动作开关 | <code>/EnableMedicalActions</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 食物能量估算开关 | <code>/EnableEstimatedFoodEnergy</code> | <code>false</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 每饱食度的估算能量（千焦） | <code>/EstimatedKJPerSaturation</code> | <code>8</code> | 直接数值边界：0～100 |
| 单次饮水份量（升） | <code>/DrinkServingL</code> | <code>0.25</code> | 直接数值边界：0.01～1 |
| 饮水冷却（现实秒） | <code>/DrinkCooldownRealSeconds</code> | <code>3</code> | 直接数值边界：1～60 |
| 排泄开关 | <code>/EnableDefecation</code> | <code>true</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 饱食度到排泄游戏单位的换算 | <code>/BowelUnitsPerSaturation</code> | <code>0.2</code> | 直接数值边界：0～2 |
| 淡水每升危险参数 | <code>/FreshWaterHazardPerL</code> | <code>0.02</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 雨水每升危险参数 | <code>/RainWaterHazardPerL</code> | <code>0.005</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 粪便污染水每升危险参数 | <code>/FecalWaterHazardPerL</code> | <code>0.5</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 方块水污染来源映射 | <code>/WaterPollutionHazardPerLByBlockCode</code> | <code>{}</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 动物排泄物病原组成 / ecoli | <code>/AnimalWastePathogens/ecoli</code> | <code>0.6</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 动物排泄物病原组成 / salmonella | <code>/AnimalWastePathogens/salmonella</code> | <code>0.4</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 腐肉病原组成 / salmonella | <code>/CarrionPathogens/salmonella</code> | <code>0.7</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 腐肉病原组成 / wound-staph | <code>/CarrionPathogens/wound-staph</code> | <code>0.3</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 默认相对湿度 | <code>/DefaultRelativeHumidity</code> | <code>0.5</code> | 直接数值边界：0～1 |
| 默认服装保温值（clo） | <code>/DefaultClothingClo</code> | <code>0.6</code> | 直接数值边界：0～10 |
| 风速游戏单位到米／秒换算 | <code>/WindGameUnitToMps</code> | <code>1</code> | 直接数值边界：0～20 |
| 附近热源到辐射温度换算 | <code>/HeatCacheToRadiantC</code> | <code>4</code> | 直接数值边界：0～30 |
| 室内增温上限（摄氏度） | <code>/RoomHeatMaxBonusC</code> | <code>18</code> | 直接数值边界：0～50 |
| 每热源强度的室内增温（摄氏度） | <code>/RoomHeatCelsiusPerStrength</code> | <code>1.8</code> | 直接数值边界：0～10 |
| 室内热量半衰期（小时） | <code>/RoomHeatHalfLifeHours</code> | <code>4</code> | 直接数值边界：0.1～48 |
| 雨量到表面水膜质量速率换算 | <code>/RainGameUnitToFilmKgPerSecond</code> | <code>0.0001</code> | 直接数值边界：0～0.01 |
| 物品保温值表（clo） | <code>/ClothingCloByCode</code> | <code>{}</code> | 未单独列出数值范围；仍需通过完整配置的联合校验。 |
| 遥测文件容量上限（MiB） | <code>/CsvMaximumMiB</code> | <code>16</code> | 直接数值边界：1～128 |

## 配置变更与单位

- 格式要求为 `Format=seraph.release.config` 和 `ConfigVersion=1`。
- `ResolveUnits()` 将五项非空的游戏小时字段乘 3600，覆盖对应秒字段；空值保留原秒值。
- 模式支持 `survival`、`shadow`、`observe`；生理速度必须为有限数，范围 0.1～20。
- 运行时设置会校验权限和修订号；无效变更不会提交。启动加载失败与运行时拒绝变更应分别排查。
- 字典项要求依各字段校验而定。水污染来源支持完整代码及末尾星号模式，不能笼统要求所有映射都必须是精确物品代码。

[全部配置表](/admin/config-tables) · [默认值](/admin/survival-config-full)
<!-- generated:end -->
