# 灰烬材料

Valley of Ashes · 模组代码：ashes

> 来源：整合包安装包 `Valley of Ashes-1.5.1.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `ashes` |
| 版本 | 1.5.1 |
| 类型 | 资源内容 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.3, survival 1.22.3, em 3.8.0 |
| 作者 | Tels, Phiwa |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Craft plant and wood ash, ash fertilizer and potash.

</details>

作者提供的链接：https://gitlab.com/codesmiths/vs_valley_of_ashes

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

```text
# Valley of Ashes

This Vintage Story mod adds wood & plant ash and related crafting recipes.

We hope you enjoy our work.

~Phiwa & Tels

# Download

* The mod from [Official Vintage Story ModDB](https://mods.vintagestory.at/valley_of_ashes)
* You also need to install [Expanded Matter](https://mods.vintagestory.at/em)
* The source code can be found on [Gitlab](https://gitlab.com/codesmiths/vs_valley_of_ashes/-/releases)

Valley of Ashes has config lib support, to use it, you need install these two mods:

* [Config lib](https://mods.vintagestory.at/configlib) (You need at least 1.3.13)
* [ImGui lib](https://mods.vintagestory.at/imgui)

If these two mods are not installed, potash crafting will be disabled by default.

# Installation

This mod should work in existing worlds and should also be removable without
any problems. If in doubt, please create a new world.

  <u>**Make a backup of your savegame and world before trying this mod!**</u>

If you would like to translate this mod into other languages, please [contact us](https://gitlab.com/codesmiths/vs_bricklayers/-/wikis/Contact).

# Configuration

If you change any of the settings in the config file or via the in-game GUI, you
need to restart the server or reload the world for the settings to become effective.

# Signature key

All our releases are signed using PGP (GnuPG) and their integrity can be verified by using the public key as published
[on the wiki](https://gitlab.com/codesmiths/vs_bricklayers/-/wikis/Signing-key).
```

[返回整合包图鉴](/mods/)

<!-- package-evidence:start -->
<details><summary>安装包技术资料与实现证据</summary>

## 安装包实现证据

以下清单来自此版本安装包内的实际文件；资源可能由其他模组或配置条件控制，存在文件不等于功能必然启用。

| 类型 | 数量 | 包内路径示例 |
| --- | ---: | --- |
| 源码文件 | 0 | — |
| 程序集 | 0 | — |
| 方块定义 | 0 | — |
| 物品定义 | 1 | `assets/ashes/itemtypes/resource/plantdebris.json` |
| 实体定义 | 0 | — |
| 配方定义 | 7 | `assets/ashes/compatibility/ancienttools/recipes/barrel/bark_ash_sludge.json`<br>`assets/ashes/compatibility/meteoricexpansion/recipes/grid/ash.json`<br>`assets/ashes/compatibility/soapandlyecontinued/recipes/barrel/lye.json`<br>`assets/ashes/compatibility/soapandlyecontinued/recipes/barrel/soapbar_washingsoda.json`<br>`assets/ashes/recipes/barrel/causticpotash.json`<br>`assets/ashes/recipes/barrel/washingsoda.json`<br>`assets/ashes/recipes/cooking/ash_potash.json` |
| 资产补丁 | 21 | `assets/ashes/compatibility/ancienttools/patches/ancienttools-bark-ash-solution.json`<br>`assets/ashes/compatibility/ancienttools/patches/ancienttools-bark-ash.json`<br>`assets/ashes/compatibility/em/patches/em-ash.json`<br>`assets/ashes/compatibility/em/patches/survival-plant-ash-making.json`<br>`assets/ashes/compatibility/em/patches/survival-tang-ash-making.json`<br>`assets/ashes/compatibility/em/patches/survival-wood-ash-making.json`<br>`assets/ashes/compatibility/indappledgroves/patches/groves-bark-ash.json`<br>`assets/ashes/compatibility/meteoricexpansion/patches/me-survival-blocktypes-rockashpile.json`<br>`assets/ashes/compatibility/soapandlyecontinued/patches/blocktypes-wood-woodtyped-log.json`<br>`assets/ashes/compatibility/soapandlyecontinued/patches/entities-trader-clothes.json`<br>`assets/ashes/compatibility/soapandlyecontinued/patches/entities-trader-commodities.json`<br>`assets/ashes/compatibility/soapandlyecontinued/patches/sal-patches-traders.json`<br>另有 9 个文件 |
| 语言资源 | 4 | `assets/ashes/lang/de.json`<br>`assets/ashes/lang/en.json`<br>`assets/ashes/lang/fr.json`<br>`assets/ashes/lang/uk.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 1 | `assets/ashes/config/configlib-patches.json` |
类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 7 个配方文件与 0 个手册章节](/reference/recipes/ashes)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
