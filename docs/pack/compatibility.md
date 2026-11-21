# 兼容性与排障

## 先看能力所有权

运行 `/vsslssmod compat`，确认每项 capability 只有一个 owner。重复 owner 会造成双重饮水、重复伤口或环境计量。

## 常见排查

| 现象 | 检查 |
| --- | --- |
| C 键全是未知 | 服务端快照未刷新、协议版本不匹配或模组未加载 |
| 食物不增加营养 | 代码未出现在校准表，查看 `UnmappedPortions` |
| 水被判定污染 | 查看水源种类、过滤阶段和 `WaterBatch` 病原/危害字段 |
| 伤口没有护理效果 | 检查治疗路由、`RequiresWound`、伤口类型和 receipt |
| 配置无法加载 | 检查 `Format=seraph.release.config`、`ConfigVersion=1` 及嵌套 Validate |

保留服务器日志中的错误文本和 capability 输出，第三方 DLL 的类型存在本身不能证明运行时一定启用。
