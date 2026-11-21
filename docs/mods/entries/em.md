# 扩展材料

Expanded Matter · 模组代码：em

> 来源：整合包安装包 `Expanded Matter-3.8.3.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `em` |
| 版本 | 3.8.3 |
| 类型 | 资源内容 |
| 运行端 | 未声明 |
| 客户端必需 | 未声明 |
| 服务端必需 | 未声明 |
| 依赖及最低版本 | game 1.22.0, survival 1.22.0 |
| 作者 | Tels, Phiwa |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“建筑、工业与工艺”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

A library that extends the base game with new materials and variants.

</details>

作者提供的链接：https://gitlab.com/codesmiths/vs_expanded_matter

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

```text
# Expanded Matter

"Matter expands on its own free will."

This Vintage Story mod library adds new variants and types to the base game materials.
To be used by other mods, contains no end-user functionality in itself.

## More Information

You can find more information and pretty pictures at our [Wiki](https://gitlab.com/codesmiths/vs_expanded_matter/-/wikis/home).

We hope you enjoy our work.

~Phiwa & Tels

# Download

* The mod From [Official Vintage Story ModDB](https://mods.vintagestory.at/em)
* The source code can be found on [Gitlab](https://gitlab.com/codesmiths/vs_expanded_matter/-/releases)

# Installation

This mod should work in existing worlds. If in doubt, please create a new world.

  <u>**Make a backup of your savegame and world before trying this mod!**</u>

# Languages

* English (100%)
* German (100%)
* Japanese (100%)
* Portuguese (50%)
* Spanish (100%)
* Ukrainian (100%)

All other languages are more or less missing completely.
If you would like to translate this mod into other languages, please [contact us](https://gitlab.com/codesmiths/vs_expanded_matter/-/wikis/Contact).

# Changes and Roadmap

Please see the [Changelog](Changelog) for the changes in the latest release.

If you have any ideas, or know about features that already done in another mod, then we
love [to hear from you](https://gitlab.com/codesmiths/vs_bricklayers/-/wikis/Contact).

# Signature key

All our releases are signed using PGP (GnuPG) and their integrity can be verified by using the public key as published
[on the wiki](https://gitlab.com/codesmiths/vs_bricklayers/-/wikis/Signing-Key).
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
| 物品定义 | 14 | `assets/em/itemtypes/liquid/causticpotash.json`<br>`assets/em/itemtypes/liquid/causticsoda.json`<br>`assets/em/itemtypes/liquid/cobaltsulfate.json`<br>`assets/em/itemtypes/liquid/diluted_kernite.json`<br>`assets/em/itemtypes/liquid/diluted_saltpeter.json`<br>`assets/em/itemtypes/liquid/mercury.json`<br>`assets/em/itemtypes/liquid/washingsoda.json`<br>`assets/em/itemtypes/resource/ash.json`<br>`assets/em/itemtypes/resource/crushed-metal.json`<br>`assets/em/itemtypes/resource/crushed-ore.json`<br>`assets/em/itemtypes/resource/crushed-stone.json`<br>`assets/em/itemtypes/resource/powdered-metal.json`<br>另有 2 个文件 |
| 实体定义 | 0 | — |
| 配方定义 | 72 | `assets/em/compatibility/ancienttools/recipes/grid/pitch_pot.json`<br>`assets/em/compatibility/tailorsdelight/recipes/cooking/picricacid_down.json`<br>`assets/em/compatibility/wool/recipes/barrel/mordant_wool.json`<br>`assets/em/compatibility/wool/recipes/cooking/picricacid_fleece.json`<br>`assets/em/recipes/barrel/alum.json`<br>`assets/em/recipes/barrel/ash_sludge.json`<br>`assets/em/recipes/barrel/causticpotash.json`<br>`assets/em/recipes/barrel/causticsoda.json`<br>`assets/em/recipes/barrel/cleaning_pots.json`<br>`assets/em/recipes/barrel/cobaltsulfate.json`<br>`assets/em/recipes/barrel/colored_leather.json`<br>`assets/em/recipes/barrel/curing/curing_meat.json`<br>另有 60 个文件 |
| 资产补丁 | 54 | `assets/em/compatibility/aldiclasses/patches/washerygradecoke.json`<br>`assets/em/compatibility/ancienttools/patches/em_powdered_coal.json`<br>`assets/em/compatibility/brickmold/patches/em-recipes-grid-rawrefractorybrick.json`<br>`assets/em/compatibility/brickmold/patches/em-survival-itemtypes-resource-refractorybrick.json`<br>`assets/em/compatibility/foodshelves/patches/glassjars.json`<br>`assets/em/compatibility/purposefulstorage/patches/ps_storagebin.json`<br>`assets/em/compatibility/wildcraftfruit/patches/dye/survival-recipes-barrel-wildcraft-dyes.json`<br>`assets/em/compatibility/wildcraftfruit/patches/em-verdigris.json`<br>`assets/em/compatibility/wildcrafttree/patches/dye/survival-recipes-barrel-wildcraft-dyes.json`<br>`assets/em/patches/dye/grass/survival-recipes-barrel-dye-green.json`<br>`assets/em/patches/dye/sealing/survival-recipes-barrel-dye-blue.json`<br>`assets/em/patches/dye/sealing/survival-recipes-barrel-dye-green.json`<br>另有 42 个文件 |
| 语言资源 | 14 | `assets/em/lang/cs.json`<br>`assets/em/lang/de.json`<br>`assets/em/lang/en.json`<br>`assets/em/lang/es-419.json`<br>`assets/em/lang/es-es.json`<br>`assets/em/lang/fr.json`<br>`assets/em/lang/it.json`<br>`assets/em/lang/ja.json`<br>`assets/em/lang/pl.json`<br>`assets/em/lang/pt-br.json`<br>`assets/em/lang/ru.json`<br>`assets/em/lang/sv-se.json`<br>另有 2 个文件 |
| 手册资源 | 0 | — |
| 包内配置数据 | 1 | `assets/em/config/configlib-patches.json` |
类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 72 个配方文件与 0 个手册章节](/reference/recipes/em)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
