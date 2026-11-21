# 服务器管理与配置

<PortalCards :items='[{&quot;title&quot;: &quot;命令与排障&quot;, &quot;description&quot;: &quot;按实际操作查命令和权限。&quot;, &quot;link&quot;: &quot;/admin/commands-full&quot;}, {&quot;title&quot;: &quot;配置当前值&quot;, &quot;description&quot;: &quot;查看指定服务器全部配置字段。&quot;, &quot;link&quot;: &quot;/admin/config-tables&quot;}, {&quot;title&quot;: &quot;核心模组配置&quot;, &quot;description&quot;: &quot;查已安装 Seraph 配置实值。&quot;, &quot;link&quot;: &quot;/admin/installed-configs&quot;}, {&quot;title&quot;: &quot;修改配置的步骤&quot;, &quot;description&quot;: &quot;备份、修改、重载与验证。&quot;, &quot;link&quot;: &quot;/pack/configuration&quot;}]' />

本页说明配置文件与运行流程；字段表会另行标注源码默认值和当前服务器配置快照。配置路径相对于游戏数据目录；首次启动后模组会生成相应文件。升级或更改规则前备份世界存档与配置，先在测试环境验证。

## 文明模拟

`ModConfig/SeraphCivilizationSimulation.json` 为主配置，`SeraphCivilizationLoreRestrictions.json` 为传说限制。主配置可通过管理员界面或 `/vsscsmod reload config` 应用；传说限制需重启。旧版 `VscnCivilizationSimulation.json` 和 `VscnCivilizationLoreRestrictions.json` 仅在对应新文件不存在时迁移。详细默认样例见[文明配置](/admin/civilization-config)。

出生聚落坐标与分配保存在世界状态中，重载配置不会重新生成；部落、领地和生命也属于世界存档，删除配置不会重置。公告和教程分别保存在 `ModData/vscncs-content/worlds/<世界标识哈希>/` 下。

## 文明补丁

`ModConfig/vsscpmod-privacy.json` 控制时间、坐标、调试及相关查询限制；修改后运行 `/vsscpmod info reload`。`vsscpmod-quarry-carry.json` 在启用石板兼容时生成，修改后重启。各字段默认值参见[兼容补丁](/guide/patches)。旧 BodyPhys 迁移备份位于 `ModData/vsscpmod-bodyphys-backups/`。

## 生存模拟

`ModConfig/vsslssmod.Server.json` 首次运行生成，修改后重启。`vsslssmod.Foods.json` 为可选食物数据覆盖，以包内 `assets/vsslssmod/config/foods.json` 为模板。旧测试版配置和存档不会自动迁移；无效配置拒绝加载并保留原文件。参阅[生存配置](/admin/survival-config)。

## 操作顺序

1. 备份世界存档、模组数据与配置，并确认客户端和服务端安装的版本。
2. 修改前记录原值，逐项修改；不要把客户端布局或日志文件当成服务端玩法配置。
3. 根据各配置的要求重载或重启，检查服务端日志及实际效果。
4. 遇到问题先还原最近的变更并检查依赖；涉及聚落重生成、玩家重置或删除部落时，先确认备份可恢复。

[指令与排障](/admin/commands) · [开发者手册](/develop/)
