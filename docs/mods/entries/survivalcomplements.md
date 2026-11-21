# 生存补充

Survival Complements · 模组代码：survivalcomplements

> 来源：整合包安装包 `Survival Complements-1.0.0.zip` 内的模组元数据。此页面描述该快照，模组的实际行为及服务器设置可能不同。

## 身份与安装

| 项目 | 包内声明 |
| --- | --- |
| 模组 ID | `survivalcomplements` |
| 版本 | 1.0.0 |
| 类型 | 资源内容 |
| 运行端 | 客户端与服务端 |
| 客户端必需 | 是 |
| 服务端必需 | 是 |
| 依赖及最低版本 | game 1.22.0, survival 1.22.0 |
| 作者 | HansJack |

未声明的安装要求不能视为不需要；安装前应以模组发布说明及服务器要求为准。

## 功能与使用

本模组归入“身体、战斗与成长”。操作与材料可从[玩法路线](/pack/overview)和[配方手册目录](/reference/recipes/)查阅。

<details><summary>作者功能说明原文</summary>

Adds survival crafting recipes for vanilla roofing beams and iron support chains.

</details>

## 随包说明

以下是安装包根目录中的原文摘录；命令和操作请结合当前游戏版本核实。

````text
# Survival Complements

为 Vintage Story 原版创造物品补充生存制作配方。作者：**HansJack**；模组 ID：`survivalcomplements`；许可证：**MIT**；版本：**1.0.0**。

这是纯内容模组，无 DLL、无外部模组依赖。目标版本为 Vintage Story 1.22.x。

## 安装

将 `dist/survivalcomplements-1.0.0.zip` 原样放入游戏数据目录的 `Mods` 文件夹，重启游戏。更新时移除旧版 ZIP，服务器与客户端均安装同一版本。不要解压后再套一层目录，也不要同时安装 ZIP 和源码目录。

## 配方

屋脊梁每次制作产出 **1 个**；支撑链条产量见下方。每个材料格消耗 **1 个**材料；工具每次消耗 **1 点耐久**，不会作为材料消耗（耐久归零时按原版规则损坏）。以下 `·` 表示空格，**工具可放在任意一个空格**，其他空格保持为空。材料位置固定，无需把工具放在示例指定位置。

细屋脊梁：

```text
材 材 材
·  ·  ·
·  ·  ·
```

粗屋脊梁：

```text
材 材 材
材 材 材
·  ·  ·
```

| 屋脊梁系列 | 对应材料 | 工具 | 细梁 / 粗梁成本 |
| --- | --- | --- | --- |
| 黑、棕、奶白、耐火、灰、橙、红、沙色陶瓦 | 同色已烧制瓦片 | 凿子 | 3 / 6 个 |
| 板岩（石制） | 板岩石子 | 凿子 | 3 / 6 个 |
| 铜板 | 铜板 | 锤子 | 3 / 6 个 |
| 竹子 | 竹桩 | 刀 | 3 / 6 个 |
| 各木种、古木 | 同种木板 | 锯子 | 3 / 6 个 |

木材包括金合欢、古木、落羽杉、桦木、黑檀、木棉、落叶松、枫木、橡木、松木、紫心木、红杉、核桃木。不同颜色或木种不能混用。原版未提供对应梁的茅草、草皮、陈旧古木不添加虚构产物。铜板加工使用锤子，竹材使用刀，木材使用锯子，陶瓦和板岩使用凿子。

细支撑链条：**4 个铁链 + 锤子 → 16 个**。铁链摆成菱形：

```text
·  链 ·
链 ·  链
·  链 ·
```

粗支撑链条：**4 个铁链 + 锤子 → 4 个**。铁链放在四角：

```text
链 ·  链
·  ·  ·
链 ·  链
```

输入铁链是原版物品 `game:metalchain-iron`；不再使用铁金属粒。两种配方用不同图案区分，避免相同输入产生歧义。产物使用非锈蚀的 `game:supportchain-twonew` 与 `game:supportchain-fournew`。细、粗屋脊梁分别对应 `game:beam-ridge-材料-free` 与 `game:beam-plane-材料-free`，已按原版模型尺寸确认。

## 生存实用性

- 共补充 24 种材质、48 种粗细屋脊梁，以及 2 种铁链的制作途径。
- 原版方块直接作为产物，保留原版自由放置与外观；不添加重复方块。
- 将上述可制作物品加入生存手册，提供中英文粗细名称。积雪版本与锈蚀链条继续隐藏。
- 开启非锈蚀铁链的原版拆除返还行为；屋脊梁沿用原版返还逻辑。锈蚀链条保持原版不返还设置。
- 未修改矿洞支撑强度或承重规则；支撑链条的名称不代表新增矿洞防塌功能。
- 3 / 6 份材料区分粗细梁；4 个铁链可制成 16 个细支撑链条或 4 个粗支撑链条，使粗链单位材料成本为细链的 4 倍；不提供反向拆解材料配方。

## 开发与打包

运行 `python tools/build.py`，生成 JSON 配方、补丁、语言文件及 ZIP。脚本仅依赖 Python 标准库。模组归档仅包含 `modinfo.json`、`LICENSE`、本文档和 `assets`。

原版网格不支持“材料有序、单独工具无序”的混合字段，因此枚举工具的所有合法空位，共生成 226 条有序配方。这样保留材料图案、支持任意空格放工具，也避免粗细链条的相同材料产生配方冲突。

## 验证

测试辅助模组在 Vintage Story **1.22.3** 的独立测试服务端调用原版网格匹配方法，覆盖 226 条配方、50 个产物、材料成本、产量、工具耐久成本配置、缺工具/错工具/缺材料/额外材料/混色拒绝、链条配方无歧义、旧铁粒输入拒绝，以及实际加载后的手册可见性和链条返还配置。最新结果见测试报告。

测试源码位于 `tools/SmokeTest`，测试报告位于 `validation/smoke-1.22.3.json`；辅助 DLL 不包含在发布 ZIP 中。可使用 `dotnet build tools/SmokeTest/SmokeTest.csproj -c Release -p:GamePath=游戏安装目录` 编译。测试辅助模组在服务端 GameReady 阶段执行，须仅在独立测试数据目录加载，并添加依赖 `survivalcomplements` 的测试 modinfo.json。

尚未进行客户端交互操作与放置/拆除实测，也未对其他 1.22.x 版本逐一运行测试。工具损耗与拆除返还使用原版逻辑，已验证对应配置；实际游玩表现仍以游戏内为准。
````

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
| 物品定义 | 0 | — |
| 实体定义 | 0 | — |
| 配方定义 | 25 | `assets/survivalcomplements/recipes/grid/roofing-acacia.json`<br>`assets/survivalcomplements/recipes/grid/roofing-aged.json`<br>`assets/survivalcomplements/recipes/grid/roofing-baldcypress.json`<br>`assets/survivalcomplements/recipes/grid/roofing-bamboo.json`<br>`assets/survivalcomplements/recipes/grid/roofing-birch.json`<br>`assets/survivalcomplements/recipes/grid/roofing-blackclay.json`<br>`assets/survivalcomplements/recipes/grid/roofing-brownclay.json`<br>`assets/survivalcomplements/recipes/grid/roofing-copper.json`<br>`assets/survivalcomplements/recipes/grid/roofing-creamclay.json`<br>`assets/survivalcomplements/recipes/grid/roofing-ebony.json`<br>`assets/survivalcomplements/recipes/grid/roofing-fireclay.json`<br>`assets/survivalcomplements/recipes/grid/roofing-grayclay.json`<br>另有 13 个文件 |
| 资产补丁 | 1 | `assets/survivalcomplements/patches/survival-access.json` |
| 语言资源 | 2 | `assets/game/lang/en.json`<br>`assets/game/lang/zh-cn.json` |
| 手册资源 | 0 | — |
| 包内配置数据 | 0 | — |
类型索引和资源清单不包含运行时控制流分析；具体操作、默认配置和交互规则仍需逐项核实。

</details>
<!-- package-evidence:end -->

<!-- reference-link:start -->
## 材料、加工与手册正文

[查阅本版本 25 个配方文件与 0 个手册章节](/reference/recipes/survivalcomplements)。配方中可查投入数量、产物、工具、网格和加工条件。
<!-- reference-link:end -->
