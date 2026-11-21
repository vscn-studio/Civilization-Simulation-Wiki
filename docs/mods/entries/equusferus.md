# 野马

Equus: Wild Horses 2.0 · 模组代码：equusferus

> 来源：整合包安装包 `Equus_ Wild Horses 2.0-1.0.6.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `equusferus` |
| 版本 | 1.0.6 |
| 类型 | 含程序代码 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0, genelib 3.1.2, jaunt 3.1.0 |
| 作者 | Shintharo12, Freakyuser396 |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“交通、地图与搬运”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds tameable wild horses to the game with coat genetics, successor to the original Equus mod

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
| 程序集 | 1 | `equusferus.dll` |
| 方块定义 | 0 | — |
| 物品定义 | 3 | `assets/equusferus/itemtypes/animals.json`<br>`assets/equusferus/itemtypes/ferusbridle.json`<br>`assets/equusferus/itemtypes/ferussaddle.json` |
| 实体定义 | 3 | `assets/equusferus/entities/ferus/ferus-unhandled.json`<br>`assets/equusferus/entities/ferus/ferus-wild.json`<br>`assets/equusferus/entities/ferus/ferus.json` |
| 配方定义 | 3 | `assets/equusferus/recipes/barrel/wearables.json`<br>`assets/equusferus/recipes/grid/bridleandsaddle.json`<br>`assets/equusferus/recipes/grid/scrapedye.json` |
| 资产补丁 | 10 | `assets/equusferus/patches/biomes.json`<br>`assets/equusferus/patches/configpatches.json`<br>`assets/equusferus/patches/elkphysics.json`<br>`assets/equusferus/patches/footprints.json`<br>`assets/equusferus/patches/naturalfertilizer.json`<br>`assets/equusferus/patches/vanilla-bedroll.json`<br>`assets/equusferus/patches/vanilla-blanket.json`<br>`assets/equusferus/patches/vanilla-lantern.json`<br>`assets/equusferus/patches/vanilla-medallion.json`<br>`assets/equusferus/patches/vanilla-saddlebags.json` |
| 语言资源 | 2 | `assets/equusferus/lang/en.json`<br>`assets/equusferus/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 1 | `assets/equusferus/config/configlib-patches.json` |

### 程序集类型索引

通过 ILSpy 读取程序集中的类型名，名称不是原始源码，也不能单独证明运行条件。哈希为 DLL SHA-256 前 16 位。

**equusferus.dll**（`02de10164cc7864a`）：3 个类型。

```text
Class <Module>
Class EquusFerus.EquusFerusInterpreter
Class EquusFerus.EquusFerusModSystem
```

类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 3 个配方文件与 0 个手册章节](/reference/recipes/equusferus)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
