<!-- generated:start -->
# SimpleVoiceChat.Server.json

[返回全部配置表](/admin/config-tables)

来源：指定服务器 `ModConfig/SimpleVoiceChat.Server.json`；路径以 `/` 分隔，数字是数组索引。

| 字段路径 | 类型 | 当前值 |
| --- | --- | --- |
| <code>/ConfigVersion</code> | number | <code>12</code> |
| <code>/ServerInstanceId</code> | string | <code>"85a7c67f5fbc49259b5dcef50ba44186"</code> |
| <code>/Enabled</code> | boolean | <code>true</code> |
| <code>/AllowAdpcmFallback</code> | boolean | <code>true</code> |
| <code>/DefaultOpusBitrateKbps</code> | number | <code>24</code> |
| <code>/MaxOpusBitrateKbps</code> | number | <code>48</code> |
| <code>/EnableAdaptiveBitrate</code> | boolean | <code>true</code> |
| <code>/AllowWhisper</code> | boolean | <code>true</code> |
| <code>/AllowShout</code> | boolean | <code>true</code> |
| <code>/ForceImmersive</code> | boolean | <code>false</code> |
| <code>/MaxRange</code> | number | <code>80</code> |
| <code>/WhisperRange</code> | number | <code>5</code> |
| <code>/TalkRange</code> | number | <code>20</code> |
| <code>/ShoutRange</code> | number | <code>40</code> |
| <code>/EnableProximityChatText</code> | boolean | <code>false</code> |
| <code>/ProximityChatRange</code> | number | <code>6</code> |
| <code>/EnableOcclusion</code> | boolean | <code>true</code> |
| <code>/EnableWeatherEffects</code> | boolean | <code>true</code> |
| <code>/EnableEnvironmentalVoiceEffects</code> | boolean | <code>true</code> |
| <code>/ApplyUnderwaterEffectsToChannels</code> | boolean | <code>false</code> |
| <code>/EnableDownedVoiceSilence</code> | boolean | <code>true</code> |
| <code>/EquipmentVoiceEffectRules/0/Slot</code> | number | <code>2</code> |
| <code>/EquipmentVoiceEffectRules/0/ItemCodePattern</code> | string | <code>"armor-head-*"</code> |
| <code>/EquipmentVoiceEffectRules/0/Effect</code> | number | <code>0</code> |
| <code>/EquipmentVoiceEffectRules/1/Slot</code> | number | <code>1</code> |
| <code>/EquipmentVoiceEffectRules/1/ItemCodePattern</code> | string | <code>"clothes-face-*mask*"</code> |
| <code>/EquipmentVoiceEffectRules/1/Effect</code> | number | <code>1</code> |
| <code>/EnableHudIndicators</code> | boolean | <code>true</code> |
| <code>/MaxVoicePacketsPerSecond</code> | number | <code>60</code> |
| <code>/MaxVoiceBytesPerSecond</code> | number | <code>32768</code> |
| <code>/MaxVoicePayloadBytes</code> | number | <code>444</code> |
| <code>/MaxServerEgressKbps</code> | number | <code>30000</code> |
| <code>/MaxListenerEgressKbps</code> | number | <code>2048</code> |
| <code>/MaxDirectorEgressKbps</code> | number | <code>1024</code> |
| <code>/SpatialCellSize</code> | number | <code>16</code> |
| <code>/MaxStreamsPerListener</code> | number | <code>8</code> |
| <code>/MaxProximityStreams</code> | number | <code>6</code> |
| <code>/MaxChannelTalkers</code> | number | <code>3</code> |
| <code>/MaxChannelMembers</code> | number | <code>10</code> |
| <code>/MaxChannelsPerPlayer</code> | number | <code>1</code> |
| <code>/MaxChannels</code> | number | <code>16</code> |
| <code>/MaxChannelNameLength</code> | number | <code>24</code> |
| <code>/ChannelMemberPageSize</code> | number | <code>20</code> |
| <code>/AuditRetention</code> | number | <code>1000</code> |
| <code>/EnableChannels</code> | boolean | <code>false</code> |
| <code>/AllowPlayerChannelCreation</code> | boolean | <code>false</code> |
| <code>/EnableDirectorProximityCapture</code> | boolean | <code>false</code> |
| <code>/MaxDirectorListeners</code> | number | <code>8</code> |
| <code>/MaxDirectorStreamsPerListener</code> | number | <code>16</code> |
| <code>/EnableRecorderCapture</code> | boolean | <code>false</code> |
| <code>/MaxRecorderListeners</code> | number | <code>1</code> |
| <code>/MaxRecorderEgressKbps</code> | number | <code>1024</code> |
| <code>/RecorderCheckpointSeconds</code> | number | <code>5</code> |
| <code>/MaxRecorderSessionMinutes</code> | number | <code>180</code> |
| <code>/MaxRecorderClockSkewMilliseconds</code> | number | <code>2000</code> |
| <code>/MaxRecorderDownloadKbps</code> | number | <code>2048</code> |
| <code>/NextChannelNumber</code> | number | <code>4</code> |
| <code>/GloballyMutedPlayerUids</code> | 敏感字段 | <code>已隐藏</code> |
| <code>/ForceBlockedPlayerUids</code> | 敏感字段 | <code>已隐藏</code> |
| <code>/PersistentChannels</code> | array | <code>[]</code> |

配置表没有列为默认值的内容均来自当前实例；不应直接照搬到另一个服务器。Seraph 的已核验含义、范围和生效方式见[管理员入口](/admin/)。
<!-- generated:end -->
