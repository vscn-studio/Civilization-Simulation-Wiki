# 中文换行

中文换行修复 · 模组代码：chineselinebreak

> 来源：整合包安装包 `中文换行修复-1.0.4.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `chineselinebreak` |
| 版本 | 1.0.4 |
| 类型 | 含程序代码 |
| 运行端 | 客户端 |
| 客户端必需 | 未声明 |
| 服务端必需 | 否 |
| 依赖及最低版本 | game 1.21.1 |
| 作者 | Aimli_ |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

将标准中文用户界面的换行逻辑替换为针对纯文本、富文本和链接的“字符安全”换行处理。

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `ChineseLineBreak.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 0 | — |
| 资产补丁 | 0 | — |
| 语言资源 | 2 | `assets/chineselinebreak/lang/en.json`<br>`assets/chineselinebreak/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**ChineseLineBreak.dll**（`2171db83bd1a5ebc`）：7 个类型。

```text
Class <Module>
Class ChineseLineBreak.ChineseLineBreakConfig
Class ChineseLineBreak.ChineseLineBreakerPatch
Class ChineseLineBreak.ChineseLineBreakModSystem
Class ChineseLineBreak.ChineseLineBreakerPatch.EligibleComponentMarker
Class ChineseLineBreak.ChineseLineBreakerPatch.<>c
Class ChineseLineBreak.ChineseLineBreakerPatch.<LineizeTranspiler>d__29
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
