<!-- generated:start -->
# 农业改造：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：农耕全指南

来源：`assets/farmingoverhaul/config/handbook/FarmingRevampedGuide.json`。

欢迎阅读农耕指南！

这里介绍农耕系统的全部改动。

所有作物的生长周期都已延长，产量也经过调整，以更贴近现实。

简单来说，谷物产量减少，蔬菜产量增加。

想收获蔬菜种子，需要让蔬菜开花！一株开花的作物足以提供种植 10～20 株新作物的种子。

谷物和豆类（以及菠萝和南瓜）可在合成栏中取得种子。

作物生长速度不再取决于养分或湿度：

无论土壤如何，作物的生长速度都相同。

不同作物有不同的需水量：

谷物基本不需要浇水，让雨水代劳即可（亚麻也是如此）。蔬菜则不同，通常应将土壤湿度保持在 60%～80%。偶尔一两天超出范围没有关系，但不要长期如此。

降雨会将湿度提高到 75%，紧邻水源的耕地则会达到 100%，因此不宜紧贴水边种植（水稻例外，水稻强烈建议这样种）。

养分影响产量：

各类作物受到的影响不同。谷物基本不受贫瘠土壤影响，生长迅速的叶菜受影响很大，其他作物介于两者之间。

几点建议：

动物不会吃你的谷物，因此无需用围栏保护。

用好堆肥！黑土固然不错，但先给芜菁施肥更重要。泥土可不能让你填饱肚子过冬！

“农耕是一份寄托希望的职业。”

——布赖恩·布雷特

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>千穗谷种子、亚麻种子、水稻种子、黑麦种子、斯佩耳特小麦种子、向日葵种子、大豆种子、花生种子、菠萝种子 · seed</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 千穗谷籽<br><code>game:grain-amaranth</code> | 1 | 未声明附加限制 |
| 产物 | 千穗谷种子<br><code>game:seeds-amaranth</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 亚麻籽<br><code>game:grain-flax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 亚麻种子<br><code>game:seeds-flax</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 稻米粒<br><code>game:grain-rice</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 水稻种子<br><code>game:seeds-rice</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 黑麦粒<br><code>game:grain-rye</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 黑麦种子<br><code>game:seeds-rye</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 斯佩耳特小麦粒<br><code>game:grain-spelt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 斯佩耳特小麦种子<br><code>game:seeds-spelt</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 向日葵种子<br><code>game:grain-sunflower</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 向日葵种子<br><code>game:seeds-sunflower</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 大豆<br><code>game:legume-soybean</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 大豆种子<br><code>game:seeds-soybean</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 花生<br><code>game:legume-peanut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 花生种子<br><code>game:seeds-peanut</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 V | 菠萝<br><code>game:pineapple</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 菠萝种子<br><code>game:seeds-pineapple</code> | 12 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/farmingoverhaul/recipes/grid/seed.json`

```json
[
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:grain-amaranth",
        "quantity": 1
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-amaranth",
      "quantity": 32
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:grain-flax"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-flax",
      "quantity": 32
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:grain-rice"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-rice",
      "quantity": 32
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:grain-rye"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-rye",
      "quantity": 32
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:grain-spelt"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-spelt",
      "quantity": 32
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:grain-sunflower"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-sunflower",
      "quantity": 32
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:legume-soybean"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-soybean",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "item",
        "code": "game:legume-peanut"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-peanut",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "V",
    "ingredients": {
      "V": {
        "type": "block",
        "code": "game:pineapple"
      }
    },
    "height": 1,
    "width": 1,
    "output": {
      "type": "item",
      "code": "game:seeds-pineapple",
      "quantity": 12
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
