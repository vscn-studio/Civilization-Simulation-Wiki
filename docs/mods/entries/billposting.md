# 告示张贴

Billposting · 模组代码：billposting

> 来源：整合包安装包 `Billposting-2.0.3.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `billposting` |
| 版本 | 2.0.3 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game (未指定版本) |
| 作者 | Moby_ |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交易、社交与创作”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Makes it possible to pin parchment to walls, as billposts

</details>

安装包根目录没有可读取的说明文件；详细操作和配置请查阅游戏内手册或作者资料。

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 1 | `billposting.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 0 | — |
| 实体定义 | 1 | `assets/billposting/entities/billpost.json` |
| 配方定义 | 0 | — |
| 资产补丁 | 1 | `assets/billposting/patches/survival-itemtypes-lore-paper.json` |
| 语言资源 | 2 | `assets/billposting/lang/en.json`<br>`assets/billposting/lang/fr.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**billposting.dll**（`70a41167043fd142`）：10 个类型。

```text
Class <Module>
Class billposting.billpostingModSystem
Class billposting.BillpostingConfig
Class billposting.EntityBillpost
Class billposting.BehaviorBillpostable
Class billposting.BillpostDrawUtil
Class billposting.BillpostTextureUtil
Class billposting.EntityBillpostRenderer
Class billposting.src.util.BillpostElementTextBase
Class <PrivateImplementationDetails>
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->
