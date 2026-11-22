# Wiki 维护

网站构建只使用已提交的 Markdown 和公开 JSON；GitHub Actions 无需游戏或模组目录。日常编辑与发布见 README。

## 本地资料更新

提取脚本使用环境变量指定本地输入，不提交真实目录或原始安装包。

| 环境变量 | 输入 |
| --- | --- |
| SERAPH_GAME_DIR | 游戏安装目录 |
| SERAPH_MODS_DIR | 整合包 Mods 目录 |
| SERAPH_MODCONFIG_DIR | 服务器 ModConfig 目录 |
| SERAPH_SURVIVAL_SOURCE | 生存模拟项目目录 |

未设置生存模拟目录时，使用 Wiki 同级的 Seraph Living Survival Simulation 项目。其他输入按命令需要提供；缺失时脚本会明确退出。

| 命令 | 更新内容 |
| --- | --- |
| npm run inventory | 模组名称、ID、版本、分类与条目 |
| npm run asset-catalogue | 营养查询数据、配方与游戏内手册 |
| npm run source-details | 疾病、属性与身体异常说明 |
| npm run source-feature-pages | 生存配置含义、当前值与校验 |
| npm run config-inventory | 配置清单与核心模组配置快照 |
| npm run config-tables | 配置字段表 |

generated:start/end 标记内由生成器维护，标记外的正文由人工维护。没有标记的已有页面不会被覆盖，新提取结果写入忽略的 scripts/generated/，审核后再合并。已退役的源码索引与公开来源页不会重新生成。

模组清单中的版本反映实际安装包；教程和 API 应标明适用的当前版本。更新功能时直接修订相应页面，不累计旧版本说明或提交日志。模组源码仍用于核实机制，公开网页不展示源码文件定位、安装包哈希或维护者目录。

运行 npm run check:generation 验证重复生成稳定性及人工正文保护，再执行 README 中的构建、内容和浏览器检查。公开数据保留食品数值、适用条件和模组名称，不包含提取文件、校准引用或包证据字段。
