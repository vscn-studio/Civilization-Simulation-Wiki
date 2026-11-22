<!-- generated:start -->
# 司南与罗盘：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：中国罗盘


指南

放入任意手即可显示屏幕顶部居中的方向刻度 HUD。无背景框和图标，“南、北、东、西”文字显示在刻度上方，正三角紧贴刻度下方表示当前朝向。室外风会扰动刻度；室内和石英盖内不受影响。 安装 VSCN Civilization Simulation 时手持指南针并按住 Ctrl 滚动鼠标滚轮，可切换部落导航。启用后刻度上方显示“部落”文字，同向文字会错开放置；目标超出视野时文字停留在对应边缘。再次操作关闭部落标记。放置后右键可拨动指针。

制作磁针

右手持磁铁矿粒，潜行并对空按住右键10秒。双手摩擦时发出轻柔摩擦声，完成后消耗1粒获得1枚磁针。松手、换物品或指向目标会中断。

航海罗盘

4块同种木板＋1块铜板＋1枚磁针。支持原版12种树木及两种老化木板。2块透明石英合成石英盖，与罗盘合成后防风。

司南

磁铁矿粒＋凿子粗凿成司南勺（凿子消耗20耐久）。蓝黏土、红黏土、耐火黏土捏制对应陶模，烧制后浇注200单位铜，冷却得无字盘片。薄铜片＋凿子刻出凸起的铜质文字和线纹，制成司南盘，耗10耐久。司南盘＋司南勺组装司南。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · sinan-mold</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>chinesecompass:sinan-mold-{color}-raw-plate</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "game:clay-*",
    "name": "color",
    "allowedVariants": [
      "blue",
      "fire",
      "red"
    ]
  },
  "pattern": [
    [
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################"
    ],
    [
      "################",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "#______________#",
      "################"
    ]
  ],
  "name": "chinesecompass:sinan-mold",
  "output": {
    "type": "block",
    "code": "chinesecompass:sinan-mold-{color}-raw-plate"
  }
}
```

</details>

</details>

<details><summary>中国航海罗盘（桦木） · 石英盖、中国航海罗盘（橡木） · 石英盖、中国航海罗盘（枫木） · 石英盖、中国航海罗盘（松木） · 石英盖、中国航海罗盘（金合欢木） · 石英盖、中国航海罗盘（木棉木） · 石英盖、中国航海罗盘（落羽杉） · 石英盖、中国航海罗盘（落叶松） · 石英盖、中国航海罗盘（红杉） · 石英盖、中国航海罗盘（乌木） · 石英盖、中国航海罗盘（胡桃木） · 石英盖、中国航海罗盘（紫心木） · 石英盖、中国航海罗盘（老化木） · 石英盖、中国航海罗盘（重度老化木） · 石英盖 · compass-cover</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（桦木）<br><code>chinesecompass:marinerscompass-birch-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（桦木） · 石英盖<br><code>chinesecompass:marinerscompass-birch-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（桦木）<br><code>chinesecompass:marinerscompass-birch-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（桦木） · 石英盖<br><code>chinesecompass:marinerscompass-birch-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（橡木）<br><code>chinesecompass:marinerscompass-oak-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（橡木） · 石英盖<br><code>chinesecompass:marinerscompass-oak-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（橡木）<br><code>chinesecompass:marinerscompass-oak-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（橡木） · 石英盖<br><code>chinesecompass:marinerscompass-oak-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（枫木）<br><code>chinesecompass:marinerscompass-maple-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（枫木） · 石英盖<br><code>chinesecompass:marinerscompass-maple-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（枫木）<br><code>chinesecompass:marinerscompass-maple-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（枫木） · 石英盖<br><code>chinesecompass:marinerscompass-maple-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（松木）<br><code>chinesecompass:marinerscompass-pine-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（松木） · 石英盖<br><code>chinesecompass:marinerscompass-pine-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（松木）<br><code>chinesecompass:marinerscompass-pine-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（松木） · 石英盖<br><code>chinesecompass:marinerscompass-pine-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（金合欢木）<br><code>chinesecompass:marinerscompass-acacia-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（金合欢木） · 石英盖<br><code>chinesecompass:marinerscompass-acacia-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（金合欢木）<br><code>chinesecompass:marinerscompass-acacia-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（金合欢木） · 石英盖<br><code>chinesecompass:marinerscompass-acacia-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（木棉木）<br><code>chinesecompass:marinerscompass-kapok-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（木棉木） · 石英盖<br><code>chinesecompass:marinerscompass-kapok-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（木棉木）<br><code>chinesecompass:marinerscompass-kapok-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（木棉木） · 石英盖<br><code>chinesecompass:marinerscompass-kapok-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（落羽杉）<br><code>chinesecompass:marinerscompass-baldcypress-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（落羽杉） · 石英盖<br><code>chinesecompass:marinerscompass-baldcypress-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（落羽杉）<br><code>chinesecompass:marinerscompass-baldcypress-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（落羽杉） · 石英盖<br><code>chinesecompass:marinerscompass-baldcypress-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（落叶松）<br><code>chinesecompass:marinerscompass-larch-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（落叶松） · 石英盖<br><code>chinesecompass:marinerscompass-larch-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（落叶松）<br><code>chinesecompass:marinerscompass-larch-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（落叶松） · 石英盖<br><code>chinesecompass:marinerscompass-larch-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（红杉）<br><code>chinesecompass:marinerscompass-redwood-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（红杉） · 石英盖<br><code>chinesecompass:marinerscompass-redwood-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（红杉）<br><code>chinesecompass:marinerscompass-redwood-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（红杉） · 石英盖<br><code>chinesecompass:marinerscompass-redwood-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（乌木）<br><code>chinesecompass:marinerscompass-ebony-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（乌木） · 石英盖<br><code>chinesecompass:marinerscompass-ebony-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（乌木）<br><code>chinesecompass:marinerscompass-ebony-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（乌木） · 石英盖<br><code>chinesecompass:marinerscompass-ebony-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 21**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（胡桃木）<br><code>chinesecompass:marinerscompass-walnut-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（胡桃木） · 石英盖<br><code>chinesecompass:marinerscompass-walnut-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 22**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（胡桃木）<br><code>chinesecompass:marinerscompass-walnut-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（胡桃木） · 石英盖<br><code>chinesecompass:marinerscompass-walnut-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 23**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（紫心木）<br><code>chinesecompass:marinerscompass-purpleheart-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（紫心木） · 石英盖<br><code>chinesecompass:marinerscompass-purpleheart-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 24**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（紫心木）<br><code>chinesecompass:marinerscompass-purpleheart-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（紫心木） · 石英盖<br><code>chinesecompass:marinerscompass-purpleheart-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 25**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（老化木）<br><code>chinesecompass:marinerscompass-aged-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（老化木） · 石英盖<br><code>chinesecompass:marinerscompass-aged-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 26**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（老化木）<br><code>chinesecompass:marinerscompass-aged-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（老化木） · 石英盖<br><code>chinesecompass:marinerscompass-aged-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 27**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（重度老化木）<br><code>chinesecompass:marinerscompass-veryaged-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（重度老化木） · 石英盖<br><code>chinesecompass:marinerscompass-veryaged-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

**方案 28**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 中国航海罗盘（重度老化木）<br><code>chinesecompass:marinerscompass-veryaged-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（重度老化木） · 石英盖<br><code>chinesecompass:marinerscompass-veryaged-covered</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CQ
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-birch-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-birch-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-birch-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-birch-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-oak-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-oak-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-oak-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-oak-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-maple-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-maple-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-maple-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-maple-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-pine-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-pine-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-pine-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-pine-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-acacia-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-acacia-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-acacia-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-acacia-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-kapok-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-kapok-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-kapok-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-kapok-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-baldcypress-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-baldcypress-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-baldcypress-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-baldcypress-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-larch-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-larch-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-larch-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-larch-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-redwood-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-redwood-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-redwood-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-redwood-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-ebony-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-ebony-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-ebony-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-ebony-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-walnut-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-walnut-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-walnut-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-walnut-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-purpleheart-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-purpleheart-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-purpleheart-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-purpleheart-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-aged-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-aged-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-aged-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-aged-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-veryaged-open"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-veryaged-covered"
    }
  },
  {
    "ingredientPattern": "CQ",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "block",
        "code": "chinesecompass:marinerscompass-veryaged-closed"
      },
      "Q": {
        "type": "item",
        "code": "chinesecompass:quartz-cover"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-veryaged-covered"
    }
  }
]
```

</details>

</details>

<details><summary>中国航海罗盘（桦木）、中国航海罗盘（橡木）、中国航海罗盘（枫木）、中国航海罗盘（松木）、中国航海罗盘（金合欢木）、中国航海罗盘（木棉木）、中国航海罗盘（落羽杉）、中国航海罗盘（落叶松）、中国航海罗盘（红杉）、中国航海罗盘（乌木）、中国航海罗盘（胡桃木）、中国航海罗盘（紫心木）、中国航海罗盘（老化木）、中国航海罗盘（重度老化木） · marinerscompass</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 桦木木材<br><code>game:plank-birch</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（桦木）<br><code>chinesecompass:marinerscompass-birch-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 橡木木材<br><code>game:plank-oak</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（橡木）<br><code>chinesecompass:marinerscompass-oak-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 枫木木材<br><code>game:plank-maple</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（枫木）<br><code>chinesecompass:marinerscompass-maple-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 松木木材<br><code>game:plank-pine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（松木）<br><code>chinesecompass:marinerscompass-pine-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 金合欢木木材<br><code>game:plank-acacia</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（金合欢木）<br><code>chinesecompass:marinerscompass-acacia-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木棉木木材<br><code>game:plank-kapok</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（木棉木）<br><code>chinesecompass:marinerscompass-kapok-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 落羽杉木木材<br><code>game:plank-baldcypress</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（落羽杉）<br><code>chinesecompass:marinerscompass-baldcypress-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 落叶松木木材<br><code>game:plank-larch</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（落叶松）<br><code>chinesecompass:marinerscompass-larch-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 红杉木木材<br><code>game:plank-redwood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（红杉）<br><code>chinesecompass:marinerscompass-redwood-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 黑檀木木材<br><code>game:plank-ebony</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（乌木）<br><code>chinesecompass:marinerscompass-ebony-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 胡桃木木材<br><code>game:plank-walnut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（胡桃木）<br><code>chinesecompass:marinerscompass-walnut-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 紫心木木材<br><code>game:plank-purpleheart</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（紫心木）<br><code>chinesecompass:marinerscompass-purpleheart-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 古木木材<br><code>game:plank-aged</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（老化木）<br><code>chinesecompass:marinerscompass-aged-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 陈旧古木木材<br><code>game:plank-veryaged</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 罗盘磁针<br><code>chinesecompass:magnetic-needle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中国航海罗盘（重度老化木）<br><code>chinesecompass:marinerscompass-veryaged-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WCW
_N_
W_W
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-birch"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-birch-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-oak"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-oak-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-maple"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-maple-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-pine"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-pine-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-acacia"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-acacia-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-kapok"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-kapok-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-baldcypress"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-baldcypress-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-larch"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-larch-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-redwood"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-redwood-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-ebony"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-ebony-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-walnut"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-walnut-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-purpleheart"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-purpleheart-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-aged"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-aged-open"
    }
  },
  {
    "ingredientPattern": "WCW,_N_,W_W",
    "width": 3,
    "height": 3,
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-veryaged"
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "N": {
        "type": "item",
        "code": "chinesecompass:magnetic-needle"
      }
    },
    "output": {
      "type": "block",
      "code": "chinesecompass:marinerscompass-veryaged-open"
    }
  }
]
```

</details>

</details>

<details><summary>石英防风盖 · quartz-cover</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 Q | 白水晶<br><code>game:clearquartz</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 石英防风盖<br><code>chinesecompass:quartz-cover</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
QQ
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "QQ",
  "width": 2,
  "height": 1,
  "shapeless": true,
  "ingredients": {
    "Q": {
      "type": "item",
      "code": "game:clearquartz"
    }
  },
  "output": {
    "type": "item",
    "code": "chinesecompass:quartz-cover"
  }
}
```

</details>

</details>

<details><summary>司南盘（铜） · sinan-engrave</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 司南盘片（铜）<br><code>chinesecompass:sinan-blank-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 司南盘（铜）<br><code>chinesecompass:sinan-plate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "PC",
  "width": 2,
  "height": 1,
  "shapeless": true,
  "ingredients": {
    "P": {
      "type": "item",
      "code": "chinesecompass:sinan-blank-copper"
    },
    "C": {
      "type": "item",
      "tags": [
        "tool-chisel"
      ],
      "isTool": true,
      "toolDurabilityCost": 10
    }
  },
  "output": {
    "type": "item",
    "code": "chinesecompass:sinan-plate-copper"
  }
}
```

</details>

</details>

<details><summary>司南勺（磁铁矿） · sinan-spoon</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 O | 磁铁矿金属粒<br><code>game:nugget-magnetite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 司南勺（磁铁矿）<br><code>chinesecompass:sinan-spoon-magnetite</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
OC
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "OC",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "O": {
        "type": "item",
        "code": "game:nugget-magnetite"
      },
      "C": {
        "type": "item",
        "tags": [
          "tool-chisel"
        ],
        "isTool": true,
        "toolDurabilityCost": 20
      }
    },
    "output": {
      "type": "item",
      "code": "chinesecompass:sinan-spoon-magnetite",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>司南 · sinan</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 司南勺（磁铁矿）<br><code>chinesecompass:sinan-spoon-magnetite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 司南盘（铜）<br><code>chinesecompass:sinan-plate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 司南<br><code>chinesecompass:sinan</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "SP",
  "width": 2,
  "height": 1,
  "shapeless": true,
  "ingredients": {
    "S": {
      "type": "item",
      "code": "chinesecompass:sinan-spoon-magnetite"
    },
    "P": {
      "type": "item",
      "code": "chinesecompass:sinan-plate-copper"
    }
  },
  "output": {
    "type": "block",
    "code": "chinesecompass:sinan",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
