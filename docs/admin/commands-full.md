# 管理员指令完整参考

> 以下命令从三个模组的命令注册代码提取。权限以源码 `.RequiresPrivilege` 和 handler 二次检查为准。

## Living Survival Simulation（`/vsslssmod`）

| 命令 | 权限/执行者 | 实际行为 |
| --- | --- | --- |
| `/vsslssmod` | `chat` | 输出模式、在线会话数、边界状态和版本 |
| `/vsslssmod check` | `chat`、玩家 | 读取自身状态诊断 |
| `/vsslssmod drink` | `chat`、玩家 | 触发一次服务器验证饮水 |
| `/vsslssmod pressure` | `chat`、玩家 | 开始医疗压力动作 |
| `/vsslssmod clean` | `chat`、玩家 | 开始清洁护理动作 |
| `/vsslssmod cancel` | `chat`、玩家 | 取消护理动作 |
| `/vsslssmod mode <mode>` | `controlserver` | 运行时设置 `survival`/`shadow`/`observe`，经配置校验和版本递增 |
| `/vsslssmod compat` | `controlserver` | 列出 capability owner 与 provider |
| `/vsslssmod probe` | `controlserver`、玩家 | 强制快照并输出时钟、环境、质量行 |
| `/vsslssmod speed <倍率>` | `controlserver` | 当前 handler 返回 speed 配置提示；实际设置走设置协议，不把聊天参数直接写入 |

客户端调试命令：`.vsslssmodhud` 切换 HUD，`.slssdebug` 打开调试窗口，`.slsspollution` 切换污染高亮，`.slssperf start|stop|status` 管理性能采样。

## Civilization Simulation（`/vsscsmod` / `/vscncs`）

| 命令族 | 权限 | 子命令/用途 |
| --- | --- | --- |
| `statuscopy` | 玩家可用 | 只导出自己的状态 |
| `name` | `controlserver` | 名称校验/重置 |
| `territory debug` | `controlserver`、游戏内管理员 | 领地调试 |
| `tribe` | `controlserver` | `list`、`delete <部落名>`、`solo on\|off\|toggle\|status` |
| `sleep` | `controlserver` | `on\|off\|toggle\|status` |
| `cluster` | `chat` 的 `info`；管理操作需 `controlserver` | `infoall`、`list`、`who`、`tp`、`assign`、`reset`、`resetall`、`reroll` |
| `content` | `controlserver` | 公告/教程 `list\|add\|edit\|delete\|clear` |
| `reset` | `controlserver` | `<玩家>`、`start <正整数>`、`stop` |
| `resetall` | `controlserver` | 重置所有玩家死亡计数 |
| `reload` | `controlserver` | `config` 或 `content [all\|announcements\|tutorials]` 热重载 |

## Civilization Patches（`/vsscpmod`）

| 命令 | 权限 | 行为 |
| --- | --- | --- |
| `/vsscpmod` | `chat` | `info status\|on\|off\|reload`、`fixstack`、`trunkrelease` |
| `.vsscpmod inventory start\|stop` | 客户端 | 切换 CarryOn 兼容库存诊断 |

命令行为可能被兼容模组是否加载、服务端/客户端侧和当前版本 API 改变；排障时保留服务器日志中的 capability/compatibility 输出。
