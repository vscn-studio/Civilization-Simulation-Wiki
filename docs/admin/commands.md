# 指令与排障

下表为常用入口，完整参数、权限和效果分别见[文明模拟](/guide/civilization)、[文明补丁](/guide/patches)及[生存模拟](/guide/survival)。文明模拟的 `/vscncs` 是 `/vsscsmod` 的兼容别名；文明管理员命令需要 `controlserver` 权限或由服务器控制台执行。

| 场景 | 指令 | 对象与用途 |
| --- | --- | --- |
| 玩家出生 | `/vsscsmod cluster info` | 查看自己的出生聚落 |
| 玩家诊断 | `/vsscsmod statuscopy`、`/vsslssmod check` | 导出文明状态、查看生存状态 |
| 配置 | `/vsscsmod reload config` | 重载文明主配置 |
| 部落 | `/vsscsmod tribe list`、`tribe delete <部落名>` | 管理员列出或删除部落 |
| 聚落 | `/vsscsmod cluster list`、`who <玩家名>` | 管理员查看聚落或查询玩家分配 |
| 信息限制 | `/vsscpmod info status`、`info reload` | 管理员玩家查看或重载信息限制 |
| 物品修复 | `/vsscpmod fixstack`、`trunkrelease` | 解决特定 RKN 或 Logging 搬运问题，需启用对应兼容 |
| 生存模式 | `/vsslssmod mode survival` | 管理员切换模式，也可选择 `shadow` 或 `observe` |
| 生存诊断 | `/vsslssmod compat`、`/vsslssmod probe` | 管理员检查兼容和运行状态 |
| 客户端 | `.vsslssmodhud`、`.slssperf start` | 切换身体图、开始性能采样 |

## 常见问题

- **无法进入或版本不匹配**：核对客户端、服务端、游戏版本、模组 ID 和依赖，检查文明模组的白名单或黑名单规则。
- **与朋友出生位置不同**：查看各自聚落，管理员可使用文明模组的 `cluster assign`、`reset`；改配置不会自动重新生成已有布局。
- **地图、坐标或时间不可见**：先核对文明补丁的信息限制及地图兼容设置；管理员的 `info off` 仅影响其本次连接。
- **配置未生效**：确认文件位于正确的数据目录、JSON 格式有效，并按对应模组要求重载或重启。生存模拟配置无效时拒绝加载。
- **异常搬运或石板限制**：检查对应第三方模组是否启用及补丁配置；石板的限制以实际包含的岩石块数计算。
- **提交问题**：记录发生时间、版本、具体操作及重现步骤；按需使用诊断命令，检查日志中个人信息后再分享。客户端库存诊断使用 `.vsscpmod inventory start` 和 `stop`。

聚落重新生成、重置玩家和删除部落等操作可能改变存档状态，执行前先备份并确认影响。
