# 整合包配置文件操作

配置文件位于实例的 `Logs/服务器相关/ModConfig` 目录（实际文件名以启动器生成结果为准）。字段、默认值和校验范围见[完整生存配置](/admin/survival-config-full)。

## 安全修改顺序

1. 停服并备份配置与世界。
2. 只修改一个逻辑组，保持 JSON 类型不变。
3. 先校验顶层 `Format`、`ConfigVersion`、`Mode` 和 `PhysiologySpeed`，再检查嵌套对象。
4. 启动后读取日志，进入世界运行 `/vsslssmod probe` 和 `/vsslssmod compat`。
5. 用 C 键确认玩家快照与环境变化，最后再继续修改下一组。

字典字段（服装、呼吸防护、水污染来源等）有条目数量、代码长度和数值范围限制；不要把原版饱和度直接当作克数或 kJ。
