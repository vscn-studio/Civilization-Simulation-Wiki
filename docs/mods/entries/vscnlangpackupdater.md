# 汉化更新

VSCN 汉化包自动更新器 · 模组代码：vscnlangpackupdater

> 来源：整合包安装包 `VSCN 汉化包自动更新器-26.8.7.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `vscnlangpackupdater` |
| 版本 | 26.8.7 |
| 类型 | 含程序代码 |
| 运行端 | client |
| 客户端必需 | 否 |
| 服务端必需 | 否 |
| 依赖及最低版本 | game 1.22.0 |
| 作者 | VSCN-Studio |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

自动通过加速通道检查并下载最新版 VSCN Vintage Story 汉化包。

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

````text
# VSCN 汉化包自动更新器

`vscnlangpackupdater` 是一个客户端代码模组，用于在游戏启动后自动检查并下载最新版 VSCN Vintage Story 汉化包。

启动后它会请求最新 Release 信息：

```text
https://api.github.com/repos/vscn-studio/VintageStory-Chinese-Language-Package/releases/latest
```

默认会先通过 GitHub 加速通道访问 Release API 和下载地址，所有加速通道失败后再回退到原始 GitHub 地址。如果最新 Release 版本高于当前已加载的 `vscnlangpack` 版本，它会把匹配的 `VintageStory-Chinese-Language-Package-<version>.zip` 下载到玩家的 `Mods` 目录，并提示玩家重启游戏生效。

## 构建

将 `VINTAGE_STORY` 设置为包含 `VintagestoryAPI.dll` 的 Vintage Story 安装目录，然后运行。面向 Vintage Story 1.22.x 的代码模组目前需要 .NET 10 SDK。

```powershell
dotnet build src/Updater/Updater.csproj -c Release
```

模组文件会复制到：

```text
src/Updater/bin/Release/mod/
```

发布自动更新器时，将该 `mod` 目录中的内容打包为 zip。

## 配置

模组首次启动时会写入 `ModConfig/vscnlangpackupdater.json`。

```json
{
  "enabled": true,
  "checkDelayMilliseconds": 3000,
  "httpTimeoutSeconds": 30,
  "notifyWhenUpToDate": false,
  "notifyOnFailure": true,
  "deleteOldPackages": true,
  "releasesApiUrl": "https://api.github.com/repos/vscn-studio/VintageStory-Chinese-Language-Package/releases/latest",
  "releasesLatestUrl": "https://github.com/vscn-studio/VintageStory-Chinese-Language-Package/releases/latest",
  "releaseAssetDownloadUrlTemplate": "https://github.com/vscn-studio/VintageStory-Chinese-Language-Package/releases/download/{tag}/{asset}",
  "githubUrlTemplates": [
    "https://ghproxy.net/{url}",
    "https://gh-proxy.org/{url}",
    "https://v4.gh-proxy.org/{url}",
    "https://v6.gh-proxy.org/{url}",
    "https://axisnow.gh-proxy.org/{url}",
    "https://v6.gh-proxy.com/{url}",
    "https://hk.gh-proxy.com/{url}",
    "https://cdn.gh-proxy.com/{url}",
    "https://edgeone.gh-proxy.com/{url}",
    "{url}"
  ],
  "assetFilePrefix": "VintageStory-Chinese-Language-Package-",
  "assetFileSuffix": ".zip"
}
```

`githubUrlTemplates` 同时用于 Release API、最新版跳转页和语言包 zip 下载。`{url}` 会替换为原始 GitHub 地址，`{escapedUrl}` 会替换为 URL 编码后的原始地址；如果某个模板不包含占位符，会直接把原始地址拼到模板末尾。候选地址和重定向仅允许 HTTPS 及受信任的 GitHub/CDN/代理主机。建议保留 `{url}` 作为最后兜底通道；未知主机会被安全检查拒绝。如果 GitHub API 超时或返回错误，更新器会依次请求 `https://github.com/vscn-studio/VintageStory-Chinese-Language-Package/releases/latest` 和 `https://vscn.studio/VintageStory-Chinese-Language-Package/releases/latest`；两者都支持 Release JSON 或页面跳转解析，随后用 `releaseAssetDownloadUrlTemplate` 拼出语言包下载地址。下载会限制响应大小；API 提供 digest 时会校验 SHA-256，并在安装前检查 ZIP 路径、条目数量、解压大小、modid 和版本。
````

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `vscnlangpackupdater.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 0 | — |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**vscnlangpackupdater.dll**（`07c75913147f03e2`）：32 个类型。

```text
Class <Module>
Class <>f__AnonymousType0
Class <>z__ReadOnlySingleElementList
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F52F7B1D7E75CB60DE18F41EEA9F4D7FA36940874F11E3444FD9B09D5B5D57950__VersionRegex_0
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F52F7B1D7E75CB60DE18F41EEA9F4D7FA36940874F11E3444FD9B09D5B5D57950__Utilities
Class VscnLanguagePackUpdater.GitHubReleaseClient
Class VscnLanguagePackUpdater.GitHubRelease
Class VscnLanguagePackUpdater.GitHubReleaseAsset
Class VscnLanguagePackUpdater.SafeResponse
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem
Class VscnLanguagePackUpdater.PackageInstaller
Class VscnLanguagePackUpdater.PackageVersion
Class VscnLanguagePackUpdater.UpdaterConfig
Class VscnLanguagePackUpdater.UpdaterConstants
Class <PrivateImplementationDetails>
Class <>z__ReadOnlySingleElementList.Enumerator
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F52F7B1D7E75CB60DE18F41EEA9F4D7FA36940874F11E3444FD9B09D5B5D57950__VersionRegex_0.RunnerFactory
Class VscnLanguagePackUpdater.GitHubReleaseClient.<>O
Class VscnLanguagePackUpdater.GitHubReleaseClient.<>c
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem.<>c
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem.<>c__DisplayClass10_0
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem.<>c__DisplayClass13_0
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem.<>c__DisplayClass4_0
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem.<>c__DisplayClass7_0
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem.<>c__DisplayClass8_0
Class VscnLanguagePackUpdater.LanguagePackUpdaterModSystem.<>c__DisplayClass9_0
Class VscnLanguagePackUpdater.PackageInstaller.<>c
Class VscnLanguagePackUpdater.UpdaterConfig.<>O
Class VscnLanguagePackUpdater.UpdaterConfig.<>c
Class VscnLanguagePackUpdater.UpdaterConfig.<>c__DisplayClass49_0
Class VscnLanguagePackUpdater.UpdaterConfig.<>c__DisplayClass54_0
Class System.Text.RegularExpressions.Generated.<RegexGenerator_g>F52F7B1D7E75CB60DE18F41EEA9F4D7FA36940874F11E3444FD9B09D5B5D57950__VersionRegex_0.RunnerFactory.Runner
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
