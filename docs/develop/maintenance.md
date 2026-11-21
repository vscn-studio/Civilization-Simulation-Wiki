# 内容来源与维护

## 版本与证据

核心页面优先来自三个本地源码项目的 C#、资源、配置类型、测试和生存模拟游戏内手册；README 只作为版本、许可和发布说明的交叉证据。整合包图鉴来自本地 `Mods` 文件夹中的 ZIP、目录内 `modinfo.json`、程序集类型索引和资源。图鉴记录安装包快照，并不证明模组实际已启用，也不推断未声明的依赖或安装端。

源码版本和整合包版本须分别核对；构建 Wiki 不会重新打包模组。服务器配置目录用于生成“当前实例实值”页和键路径清单；玩家历史、认证令牌、连接凭据、审计日志等敏感内容不写入文档。

## 本地运行与构建

推荐 Node.js 24 LTS（最低 22）和 npm。在网站根目录运行：

```sh
npm ci
npm run dev
npm run build
npm run preview
```

构建输出位于 `docs/.vitepress/dist`。部署到域名根路径时直接托管该目录；部署到子路径时构建前将环境变量 `WIKI_BASE` 设置为带前后斜杠的路径，例如 `/wiki/`。部署目标应将生成的静态文件原样发布。

仓库包含 GitHub Pages 工作流 `.github/workflows/pages.yml`。在仓库 Settings → Pages 中选择 GitHub Actions 后，默认分支的推送会自动构建、检查链接、验证浏览器数据加载与搜索，再部署网站。工作流自动读取 Pages 的根路径或仓库子路径，不依赖本机源码目录，也不运行本地资料提取脚本。首次启用可在 Actions 中手动运行；完整设置步骤见仓库根目录 `README.md`。

本地子路径检查应让构建、`npm run check:content` 和 `npm run test:deployment` 使用相同的 `WIKI_BASE`。完整的 `npm run test:browser` 使用默认根路径构建。

## 更新清单

1. 备份现有文档并确认三个源码版本与整合包版本；按需设置 `SERAPH_MODS_DIR` 与 `SERAPH_SURVIVAL_SOURCE` 指向本机目录。
2. 运行 `npm run inventory` 更新模组图鉴和生存游戏内手册；运行 `npm run asset-catalogue` 更新原版/整合包资源与食物检索。
3. 先运行 `npm run config-tables` 和 `npm run config-inventory` 更新配置快照，再运行 `npm run source-feature-pages` 更新开发者栏目中的三个源码索引和配置声明来源。运行 `npm run source-details` 更新疾病、属性和身体异常，`npm run site-catalogue` 更新中文模组分类。
4. 对照源码、配置定义、手册和测试人工更新核心指南。生成脚本只生成可机械提取的证据，不能替代控制流审阅；脚本不会自动验证玩法，更不会修改核心模组项目。
5. 运行 `npm run check:generation` 检查重复生成与正文保护，再运行 `npm run build`、`npm run check:content`、`npm run test:browser`。浏览器检查使用本机 Chrome，覆盖三种宽度和深浅色。

## 中文正文与生成内容的边界

`wiki_content.py` 只替换 `generated:start` 与 `generated:end` 之间的内容。标记外可写人工说明；没有标记的既有文章不会被覆盖，生成结果写入 `scripts/generated/` 供审阅。旧 `generate_core_docs.py` 仅输出草稿，不再修改玩家正文。

疾病解释在 `disease_editorial.py` 维护，属性展示规则在 `player_presentation.py` 维护；中文模组名称与分类在 `site_catalogue.py`，页面导航在 `docs/.vitepress/navigation.mjs`。物品名称从实际语言资源解析，技术代码与下载数据保留原样。无法确认的中文名称显示“名称未汉化”，不猜测含义。

`reorganize_wiki.py` 与 `polish_player_pages.py` 是一次性迁移工具，不属于日常更新流程；迁移前正文保存在本地 `scripts/editorial-backup/`，不发布到站点。

自动盘点生成的条目以模组 ID 命名，ID 冲突时附加安装包名称哈希；包删除后需人工清理不再使用的旧条目。现有图鉴条目不会被盘点脚本覆盖；新增包会创建页面，版本变化需人工核对并更新已有条目。运行 `python scripts/package_evidence.py` 可更新页面中标记的安装包证据段落，需要本机已安装 ILSpy 命令行工具。此工具读取程序集类型和资源路径，不等同于逐项分析控制流；遇到无法解析的原生库会标记。

## 核验进度

[源码盘点](/develop/source-inventory)列出当前三个项目源码文件与哈希，文件被列出不表示对应行为已完成审阅。核心概览、公式页和带“源码核验”标题的专题均标注了实际读取的源文件；仍未逐项审阅的行为会明确写成“未核实”，不会根据名称推断功能。整合包页面的文件与类型索引为客观盘点，具体玩法和配置仍需逐项审阅程序集与资源。

## 核心发布包校验

本次盘点时，整合包内三个核心主包的 SHA-256 与各项目 `artifacts` 中的同版本 ZIP 一致：

| 模组 | 发布包 SHA-256 |
| --- | --- |
| 文明模拟 1.0.0 | `c2f12f0174048104d9efb414676adebbef2dde8a8122378532eda1b5547bb70a` |
| 文明补丁 1.0.1 | `ca17ba8f8413c1da5477952ca88dbedff0e6ea360d641c9675ed2da551ec1c58` |
| 生存模拟 1.0.1 | `53b1c3ac61b8ba3b4dd7654085cc0327d69745f07c0a1ce3c610b97f26f83bfb` |

此结果只证明这两份 ZIP 相同，不能证明当前源码就是构建该 ZIP 时的源码。更新发布包或源码后应重新比较。

