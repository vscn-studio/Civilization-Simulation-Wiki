# 炽天使文明模拟 Wiki

基于 VitePress 的中文 Wiki，面向 Vintage Story 整合包玩家、管理员和模组开发者，整理 Seraph 文明模拟、生存模拟与兼容补丁的玩法和实现资料。

网站分为玩家指南、核心模组、整合包玩法、资料查询、管理员、开发者六个栏目。内容依据源码、资源和配置整理；来源及核验边界见[维护说明](docs/develop/maintenance.md)。

## 本地预览

推荐 **Node.js 24 LTS**（见 `.nvmrc`），最低 Node.js 22。已提交 `package-lock.json`，使用 `npm ci` 安装锁定的依赖。

```sh
npm ci
npm run dev
```

构建和预览正式站点：

```sh
npm run build
npm run check:content
npm run preview
```

构建输出为 `docs/.vitepress/dist/`。仅运行网站无需安装游戏、Python 或三个模组源码项目，仓库中的 Markdown 和公开数据快照已包含构建所需内容。

## 发布到 GitHub Pages

1. 在 GitHub 创建仓库，默认分支使用 `main`（也支持 `master`），上传本项目文件。提交 `package-lock.json`、`docs/public/data/` 和 `scripts/` 中的清单；无需提交 `node_modules/` 或构建产物，忽略规则已配置。
2. 打开仓库 **Settings → Pages → Build and deployment → Source**，选择 **GitHub Actions**。
3. 打开 **Actions → Build and deploy Wiki → Run workflow**，选择默认分支执行首次发布。以后向默认分支推送提交会自动更新网站。
4. 查看 Action 的部署结果或 **Settings → Pages** 获取网站地址。

[部署工作流](.github/workflows/pages.yml) 会安装锁定依赖、构建站点、检查内部链接，并用浏览器验证导航、营养与模组数据、搜索结果跳转；全部成功才上传并部署。Pull Request 执行检查，不部署。

工作流通过 GitHub Pages 设置自动获取网站路径：普通项目仓库使用 `/仓库名/`，`用户名.github.io` 仓库使用 `/`。不需要将仓库名写死在 VitePress 配置中。自定义域名在 **Settings → Pages** 设置，随后重新运行工作流，让构建使用更新后的路径。

部署使用 GitHub 自动提供的 `GITHUB_TOKEN`，不需要个人访问令牌。构建任务只读仓库与 Pages 设置；部署任务拥有 `pages: write` 和 `id-token: write` 权限。若修改默认分支为其他名称，请同步修改工作流的 `push` / `pull_request` 分支过滤。

## 其他静态托管与子路径验证

将 `docs/.vitepress/dist/` 的内容上传到静态托管服务即可。部署到子路径时，构建、链接检查和预览必须使用相同的 `WIKI_BASE`，路径需以 `/` 开头和结尾。

PowerShell：

```powershell
$env:WIKI_BASE = '/wiki/'
npm run build
npm run check:content
npm run test:deployment
npm run preview
# 完成后恢复根路径设置：Remove-Item Env:WIKI_BASE
```

Bash：

```sh
export WIKI_BASE=/wiki/
npm run build
npm run check:content
npm run test:deployment
npm run preview
# 完成后恢复根路径设置：unset WIKI_BASE
```

## 维护与贡献

| 命令 | 用途 |
| --- | --- |
| `npm run dev` | 本地开发预览 |
| `npm run build` | 生成静态网站 |
| `npm run check:content` | 检查分类、数据覆盖与构建后的内部链接 |
| `npm run test:deployment` | 验证当前发布路径下的页面、数据与搜索 |
| `npm run test:browser` | 根路径下的完整布局与交互检查，先以默认路径构建 |
| `npm run check:generation` | 本地生成器的重复生成与正文保护检查，需要原始资料目录 |

浏览器检查在本地使用已安装的 Chrome，GitHub Actions 自动安装 Chromium。构建与检查应使用相同的 `WIKI_BASE`，更换路径后需重新构建。

内容更新流程见 [CONTRIBUTING.md](CONTRIBUTING.md) 和[维护说明](docs/develop/maintenance.md)。生成原始图鉴与配置表需要 Python 3 及相应源码、模组和配置目录；这些提取步骤不在云端发布流程中运行。

内容来源与权利范围见 [NOTICE.md](NOTICE.md)。仓库尚未为原创内容指定统一许可证；第三方资料保留原有权利与许可。
