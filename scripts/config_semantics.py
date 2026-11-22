"""Resolve server fields in their owning config type, never by first name match."""
import html, re
from wiki_content import write_generated

GROUP_FILES={
 'DiseaseExposure':('Seraph.Core/Framework/DiseaseSyndromes.cs','DiseaseExposureOptions','疾病暴露'),
 'SurfaceWater':('Seraph.Core/Framework/SurfaceWater.cs','SurfaceWaterOptions','地表水'),
 'Sanitation':('Seraph.Core/Framework/Sanitation.cs','SanitationOptions','卫生'),
 'ThermalAdaptation':('Seraph.Core/Framework/ThermalAdaptation.cs','ThermalAdaptationOptions','冷热适应'),
 'Pain':('Seraph.Core/Framework/WoundPain.cs','PainOptions','疼痛'),
 'Circulation':('Seraph.Core/Framework/BloodCirculation.cs','CirculationOptions','血液循环'),
 'Exertion':('Seraph.Core/Framework/Exertion.cs','ExertionOptions','体力'),
 'Digestion':('Seraph.Core/Framework/DigestionOptions.cs','DigestionOptions','消化')
}
LABELS={
 'BurstTransitionSeconds':'疾跑转为快跑的过渡时间（现实秒）','BurstRearmSeconds':'疾跑爆发再次就绪的间隔（现实秒）','RunningSpeedGain':'快跑速度增益参数','RunningStaminaPerSecond':'快跑每现实秒耐力消耗','JoggingSpeedGain':'慢跑速度增益参数','RunningSlowdownStamina':'快跑降速的耐力阈值','RestDelaySeconds':'停止强动作后的体力恢复等待时间（现实秒）',
 'EnableDrowsyMovement':'困倦时单次合眼转向开关（旧字段名）','EnableClinicalEffects':'临床效果开关','EnableSymptomVisuals':'症状视觉效果开关',
 'WoundInfectionHazardPerSecond':'伤口感染危险率／秒','RespiratoryTransmissionUnitsPerSecond':'呼吸道传播单位／秒',
 'RespiratoryProtectionByCode':'物品呼吸防护比例表','RespiratorySourcesByBlockCode':'方块呼吸道病原来源表',
 'BathWaterCoolingHalfLifeSeconds':'浴水降温半衰期（秒）','BathWaterThermalKillPerDegreeSecond':'浴水热灭活系数／度秒',
 'HandToFoodTransferFraction':'手部污染转入食物的比例','CleanWaterHandRetention':'洁净水清洗后的手部污染保留比例','DirtyWaterHandRetention':'脏水清洗后的手部污染保留比例',
 'IndirectHazardPerGameHour':'间接暴露危险率／游戏小时','VectorLandingHazardPerGameHour':'虫媒附着危险率／游戏小时','VectorMaturationGameHours':'虫媒成熟时间（游戏小时）','VectorInfectiousChance':'虫媒带病概率参数','VectorBiteHazard':'虫媒叮咬危险参数','BiteHazard':'咬伤危险参数',
 'SepsisHpPerTenGameMinutes':'败血症每 10 游戏分钟伤害','SepsisOnsetHours':'败血症危险条件持续时间（小时）','SepsisRecoveryHours':'败血症恢复条件持续时间（小时）',
 'PondTurbidity':'池塘浑浊度','LakeTurbidity':'湖泊浑浊度','RiverTurbidity':'河流浑浊度','PondShigellaPerL':'池塘每升志贺菌负荷','LakeShigellaPerL':'湖泊每升志贺菌负荷','RiverShigellaPerL':'河流每升志贺菌负荷','Valid':'配置有效性计算结果（非独立玩法开关）',
 'DirtyGroundPerGameHour':'脏污地面引起的脏污增量／游戏小时','PollutionPerPointPerGameHour':'每污染点的脏污增量／游戏小时','DirtyWaterRisePerGameHour':'脏水造成的脏污增量／游戏小时','CleanWaterFallPerGameHour':'洁净水清洁速率／游戏小时','RainWashPerGameHour':'雨水清洗速率／游戏小时','CleanGameHours':'清洁状态时长（游戏小时）','BathedGameHours':'洗浴状态时长（游戏小时）',
 'TrainingHours':'冷热适应训练时间（小时）','DecayHalfLifeHours':'适应衰减半衰期（小时）','AcuteHalfLifeHours':'急性疼痛半衰期（小时）','SlowAcuteHalfLifeHours':'慢速急性疼痛半衰期（小时）',
 'RegenerationMlPerGameHour':'基础造血速率（毫升／游戏小时）','FiltrationMlPerGameHour':'基础过滤速率（毫升／游戏小时）','LactateClearanceGPerGameHour':'乳酸清除参数（克／游戏小时）','LactateStandingHalfLifeSeconds':'站立乳酸半衰期（现实秒）','LactateWalkingHalfLifeSeconds':'步行乳酸半衰期（现实秒）','LactateSeatedHalfLifeSeconds':'坐姿乳酸半衰期（现实秒）','RenalToxicityThreshold':'肾脏反应毒性阈值','RenalBasalMultiplier':'肾脏反应基础倍率','RenalClearanceMultiplier':'肾脏反应清除倍率','RenalElectrolytesMgPerExtraMl':'额外清除量的电解质参数（毫克／毫升；实际结算需看调用）',
 'BurstSeconds':'疾跑爆发时长（现实秒）','TransitionSeconds':'爆发后过渡时长（现实秒）','RecoveryDelaySeconds':'体力恢复等待时间（现实秒）','SeatedRecoverySeconds':'坐姿恢复时间（现实秒）','StandingRecoverySeconds':'站立恢复时间（现实秒）','WalkingRecoverySeconds':'步行恢复时间（现实秒）','UnlockStamina':'解除体力锁定的耐力阈值','ExhaustedJumpCooldownSeconds':'力竭跳跃冷却（现实秒）','UnlockLactateRatio':'解除锁定的乳酸比例阈值',
 'WaterHalfLifeHours':'胃水排空半衰期（小时）','CarbohydrateHalfLifeHours':'碳水排空半衰期（小时）','ProteinHalfLifeHours':'蛋白质排空半衰期（小时）','FatHalfLifeHours':'脂肪排空半衰期（小时）','ResidueHalfLifeHours':'残渣排空半衰期（小时）','WaterMlPerHour':'水吸收速率上限（毫升／小时）','DigestionGPerGameHour':'消化吞吐量（克／游戏小时）','BasalWaterLossGPerGameHour':'基础失水量（克／游戏小时）','EntericWaterLossLPerHour':'肠道疾病失水参数（升／小时）',
 'ClinicalDamageMultiplier':'临床伤害倍率','EnableInjuryActionEffects':'伤势行动效果开关','Format':'配置格式标识','ConfigVersion':'配置格式版本','Mode':'运行模式','PhysiologySpeed':'生理时间速度倍率','TelemetryEnabled':'遥测开关','CheckpointSeconds':'检查点间隔（秒）','EnableMovementEffects':'移动效果开关','EnableWoundTracking':'伤口追踪开关','EnableGroundWaterDrinking':'地面水源饮用开关','EnableMedicalActions':'护理动作开关','EnableEstimatedFoodEnergy':'食物能量估算开关','EstimatedKJPerSaturation':'每饱食度的估算能量（千焦）','DrinkServingL':'单次饮水份量（升）','DrinkCooldownRealSeconds':'饮水冷却（现实秒）','EnableDefecation':'排泄开关','BowelUnitsPerSaturation':'饱食度到排泄游戏单位的换算',
 'FreshWaterHazardPerL':'淡水每升危险参数','RainWaterHazardPerL':'雨水每升危险参数','FecalWaterHazardPerL':'粪便污染水每升危险参数','WaterPollutionHazardPerLByBlockCode':'方块水污染来源映射','AnimalWastePathogens':'动物排泄物病原组成','CarrionPathogens':'腐肉病原组成','DefaultRelativeHumidity':'默认相对湿度','DefaultClothingClo':'默认服装保温值（clo）','WindGameUnitToMps':'风速游戏单位到米／秒换算','HeatCacheToRadiantC':'附近热源到辐射温度换算','RoomHeatMaxBonusC':'室内增温上限（摄氏度）','RoomHeatCelsiusPerStrength':'每热源强度的室内增温（摄氏度）','RoomHeatHalfLifeHours':'室内热量半衰期（小时）','RainGameUnitToFilmKgPerSecond':'雨量到表面水膜质量速率换算','ClothingCloByCode':'物品保温值表（clo）','HeadgearShadeByCode':'头部装备遮阳比例表','CsvMaximumMiB':'遥测文件容量上限（MiB）','BedSleepPressureRecoveryMultiplier':'床上睡眠的睡压恢复倍率'
}
for stem,label in [('SleepPressureRise','睡压上升'),('SleepPressureRecovery','睡压恢复'),('FatigueRise','疲劳上升'),('FatigueSleepRecovery','睡眠恢复疲劳'),('FatigueSeatedRecovery','坐姿恢复疲劳')]:
    LABELS[stem+'GameHours']=label+'时间（显式游戏小时，非空时覆盖秒值）'
    LABELS[stem+'Seconds']=label+'时间（规范化游戏秒）'

def esc(s): return html.escape(str(s),quote=False).replace('|','&#124;').replace('`','&#96;')

def generate_config_semantics(root,src):
    rows=[]
    for line in (root/'docs/reference/configs/9ed44761146e.md').read_text(encoding='utf-8').splitlines():
        m=re.match(r'\| <code>(.*?)</code> \| (.*?) \| <code>(.*?)</code> \|',line)
        if m: rows.append(m.groups())
    out=['# 生存配置：中文含义、当前值与校验','','这里列出服务器配置表中的当前值。修改文件后按[配置操作流程](/pack/configuration)重启并验证。','',
      '## 阅读方法','','每项先给中文含义，再保留可搜索的原字段。危险参数、病原负荷和概率不是同一种数值，不能统一换算为百分比。','',
      '| 中文含义 | 原字段路径 | 当前值 | 校验说明 |','| --- | --- | --- | --- |']
    for path,typ,val in rows:
        parts=html.unescape(path).strip('/').split('/'); parent=parts[0]; name=parts[-1]
        filename,owner,group=GROUP_FILES.get(parent,('Seraph.Application/SeraphServerConfig.cs','SeraphServerConfig','基础配置'))
        text=(src/filename).read_text(encoding='utf-8-sig')
        match=re.search(r'\b(?:record|class)\s+'+owner+r'\b',text)
        start=match.start() if match else 0
        boundary=re.search(r'\npublic (?:sealed |static )?(?:record|class)\b',text[start+1:])
        body=text[start:start+1+boundary.start()] if boundary else text[start:]
        property_name=name if parent in GROUP_FILES else parent
        label=LABELS.get(property_name,'含义尚未逐项核实')
        if parent not in GROUP_FILES and name!=parent: label+=' / '+name
        validation=re.search(re.escape(property_name)+r' is < ([^\n?]+?) or > ([^\s?]+)',body)
        limits='直接数值边界：'+validation.group(1)+'～'+validation.group(2) if validation else '未单独列出数值范围；仍需通过完整配置的联合校验。'
        out.append(f'| {esc(label)} | <code>{path}</code> | <code>{val}</code> | {esc(limits)} |')
    out += ['', '## 配置变更与单位','','- 格式要求为 `Format=seraph.release.config` 和 `ConfigVersion=1`。','- `ResolveUnits()` 将五项非空的游戏小时字段乘 3600，覆盖对应秒字段；空值保留原秒值。','- 模式支持 `survival`、`shadow`、`observe`；生理速度必须为有限数，范围 0.1～20。','- 运行时设置会校验权限和修订号；无效变更不会提交。启动加载失败与运行时拒绝变更应分别排查。','- 字典项要求依各字段校验而定。水污染来源支持完整代码及末尾星号模式，不能笼统要求所有映射都必须是精确物品代码。','', '[全部配置表](/admin/config-tables) · [源码默认值](/admin/survival-config-full)']
    write_generated(root/'docs/admin/seraph-config-semantics.md','\n'.join(out))
