# 参与维护

使用 Node.js 24 LTS（版本记录在 `.nvmrc`）和 npm。首次运行 `npm ci`，然后运行 `npm run dev`。

## 修改内容

- 玩家正文先解释操作、效果和应对方式，英文代码与公式放在技术说明中。
- 数值、API、命令和实现说明应依据对应版本的源码、资源或配置，在维护记录中核实版本；网页只展示玩法、参数与接口，不展示本机路径、源码索引或安装包证据。
- 不能从名字推断功能；尚未确认的行为明确标注“未核实”。
- `generated:start` 与 `generated:end` 内是生成内容，修改时同步更新对应脚本。标记外可写人工说明。
- 导航维护于 `docs/.vitepress/navigation.mjs`；生成规则与本地源目录见[维护说明](MAINTENANCE.md)。
- 提交网站使用的 `docs/public/data/` 和 `scripts/*manifest.json` 等快照。GitHub 构建依赖这些文件，不会访问维护者的本地模组目录。

## 提交前验证

```sh
npm run build
npm run check:content
npm run test:deployment
```

修改布局或交互时再运行 `npm run test:browser`。本地默认使用已安装的 Chrome；CI 使用 Playwright Chromium。浏览器检查自动启动并关闭独立的预览服务，端口为 4173。

修改生成器时，还需在具备原始模组与源码目录的机器上运行 `npm run check:generation`。该检查不在 GitHub Actions 中运行。

不要提交模组安装包、程序集、游戏存档或原始服务器配置。已整理的公开配置表继续保留脱敏规则。引用第三方内容时保留其作者、来源与许可信息。

## 提交方式

通过 Pull Request 说明问题、修改结果和验证情况。内容纠错与网站问题可使用仓库的 Issue 模板。
