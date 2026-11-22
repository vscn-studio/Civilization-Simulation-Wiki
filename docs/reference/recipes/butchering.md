<!-- generated:start -->
# 屠宰与肉类加工：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：屠宰：指南


屠宰指南

简介

本模组旨在提供更具沉浸感的屠宰机制，但同时也会提高游戏难度。你需要通过多个步骤才能从动物身上获取资源。

如何开始屠宰动物？

分步指南

步骤 0:

你需要准备以下物品开始屠宰：

- 任意刀具

-  [handbooksearch://剥皮钩] 剥皮钩

-  [handbooksearch://屠宰桌] 屠宰桌（屠宰桌会放入你的背包槽位，可以像放置装满的蜂箱一样使用ctrl + 数字1-4或滚轮放置。屠宰桌宽度为3格，并会向你放置位置的右侧延伸2格。）

- 可选： [handbooksearch://屠宰袋] 屠宰袋

- 可选：任意劈刀（在屠宰桌上处理动物时，劈刀比刀具消耗更少的耐久度）

步骤 1:

当你杀死一个生物时，你有两个选择。要么你把它切开，只得到其中一小部分物品（当你真的绝望时），要么你右键点击它，它会被放置到一个空的袋子槽位（快捷栏右侧的四个）。如果你有屠宰袋，它会被放置到你的物品栏中。

步骤 2:

把那只动物带到你建造了剥皮钩的地方。右键点击这个钩子会将动物从你的物品栏或袋子槽位中放到钩子上。

步骤 3:

瞄准钩子，用任意刀具按住右键直到生物被剥皮。

步骤 4:

等待生物放血完毕（这需要一小段时间）。你会注意到尸体的颜色会变成不那么红的色调。

步骤 5:

再次右键点击钩子取下尸体，它会再次被放回你的物品栏（如果你有屠宰袋）或袋子槽位。

步骤 6:

将放血后的尸体放在屠宰桌上，然后用任意刀具或劈刀按住右键。这将把尸体分解成生肉块，并留下一个可以打碎获取骨头的骨架。

## 手册 2：屠宰：信息


屠宰信息

掉落物与用途：

- 肌腱（来自野味生物，需晾干后使用）

用途：

[handbooksearch://弓] 弓

缝纫工具包

肌腱胶

- 上等肉（来自红肉生物，提供高饱食度和生命恢复）

用途：

餐食

预处理疗愈上等肉

脂肪提炼

- 内脏（屠宰生物的内脏器官，在木桶中清洗后可用于食物配方）

用途：

血肠 &amp; 黑布丁

- 血液（可用于多种食物配方，通过在剥皮钩上进入放血阶段的生物下方2-4格处放置木桶来收集）

用途：

[handbooksearch://血面团] 血面团（用于制作面包和馅饼）

血汤（在汤的烹饪配方中替代水）

- 生皮

用途：

皮胶

- 骨头

用途：

骨制敲击（可制作箭头和骨针）

模组机制：

- 熏制（通过在熏制架下方放置火坑来熏制食物，以延长食物的保质期）

- 血液收集（通过在放血动物下方2-4格处放置木桶，并等待生物变为放血完毕状态来获取血液）

- 动物重量（动物尸体现在会减慢你的移动速度）

注意事项：

- 小型生物如鸡、野兔和狐狸可以放入任何物品栏槽位，不需要放在袋子槽位中。

- 在屠宰桌上屠宰动物时，劈刀比刀具消耗更少的耐久度。

- 如果生物在剥皮钩和屠宰桌上放置时间过长，它们会腐烂。要从中获取腐肉，只需将其放入你的合成栏中。

- 屠宰和熏制最好在地窖环境中进行。

- 可以制作屠宰袋来提供额外的空间来运回死去的动物。

- 屠宰桌会放入你的背包槽位，可以像放置蜂箱一样放置。其次，它们有3格宽，并将向你放置位置的右侧延伸2格。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>干净内脏 · cleanoffal</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 血淋内脏<br><code>offal-bloody</code> | 1 | 未声明附加限制 |
| 产物 | 干净内脏<br><code>offal-clean</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "code": "cleanoffal",
  "sealHours": 24,
  "ingredients": [
    {
      "type": "item",
      "code": "game:waterportion",
      "litres": 1,
      "consumeLitres": 1
    },
    {
      "type": "item",
      "code": "offal-bloody",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "offal-clean",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>腌制疗愈上等肉 · curedhealingprimemeat</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 盐<br><code>game:salt</code> | 2 | 未声明附加限制 |
| 投入 2 | 预处理疗愈上等肉<br><code>primemeat-healing</code> | 1 | 未声明附加限制 |
| 产物 | 腌制疗愈上等肉<br><code>primemeat-curedhealing</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：480。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "code": "curedprimemeat",
  "sealHours": 480,
  "ingredients": [
    {
      "type": "item",
      "code": "game:salt",
      "quantity": 2
    },
    {
      "type": "item",
      "code": "primemeat-healing",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "primemeat-curedhealing",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>特殊配方 · fatrender</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>meat</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**加工条件：** 配方开关：True。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": true,
    "code": "fatrender",
    "isFood": true,
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 48
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "game:waterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      },
      {
        "code": "meat",
        "validStacks": [
          {
            "type": "item",
            "code": "butchering:primemeat-raw"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "game:fat-rendered",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · glue</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sinew</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**加工条件：** 配方开关：True。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>hide</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**加工条件：** 配方开关：True。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>hide</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**加工条件：** 配方开关：True。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>hardenedglue</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**加工条件：** 配方开关：True。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": true,
    "code": "glue-sinew",
    "perishableProps": {
      "type": "Harden",
      "freshHours": {
        "avg": 4
      },
      "transitionHours": {
        "avg": 0.01
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "butchering:glueportion-sinew-cold"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "game:waterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "sinew",
        "validStacks": [
          {
            "type": "item",
            "code": "butchering:sinew-ground"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "butchering:glueportion-sinew-cold",
      "quantity": 100
    }
  },
  {
    "enabled": true,
    "code": "glue-hide-smallhide",
    "perishableProps": {
      "type": "Harden",
      "freshHours": {
        "avg": 6
      },
      "transitionHours": {
        "avg": 0.01
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "butchering:glueportion-hide-cold"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "game:waterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "hide",
        "validStacks": [
          {
            "type": "item",
            "code": "game:hide-scraped-small"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "butchering:glueportion-hide-hot",
      "quantity": 400
    }
  },
  {
    "enabled": true,
    "code": "glue-hide-mediumhide",
    "perishableProps": {
      "type": "Harden",
      "freshHours": {
        "avg": 6
      },
      "transitionHours": {
        "avg": 0.01
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "butchering:glueportion-hide-cold"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "game:waterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "hide",
        "validStacks": [
          {
            "type": "item",
            "code": "game:hide-scraped-medium"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "butchering:glueportion-hide-hot",
      "quantity": 600
    }
  },
  {
    "enabled": true,
    "code": "glue-hide-reheat",
    "perishableProps": {
      "type": "Harden",
      "freshHours": {
        "avg": 6
      },
      "transitionHours": {
        "avg": 0.01
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "butchering:glueportion-hide-cold"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "hardenedglue",
        "validStacks": [
          {
            "type": "item",
            "code": "butchering:glueportion-hide-cold"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "butchering:glueportion-hide-hot",
      "quantity": 100
    }
  }
]
```

</details>

</details>

<details><summary>生黑布丁 · blackpudding</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 干净内脏<br><code>offal-clean</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生黑布丁<br><code>sausage-blackpudding-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
H
F
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "C,H,F",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "offal-clean"
      },
      "H": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 1,
    "height": 3,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 0.8
      }
    },
    "output": {
      "type": "item",
      "code": "sausage-blackpudding-raw",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>血饵、变体材料（按代码匹配） · bloodbait</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:flour-*</code> | 未声明；按配方类型判定 | 允许变体：['flax', 'millet', 'rice', 'rye', 'spelt', 'cassava', 'amaranth', 'sunflower'] |
| 产物 | 血饵<br><code>fishingbait-blood</code> | 6 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FWF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:flour-*</code> | 未声明；按配方类型判定 | 允许变体：['flax', 'millet', 'rice', 'rye', 'spelt', 'cassava', 'amaranth', 'sunflower'] |
| 产物 | 血饵<br><code>fishingbait-blood</code> | 6 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FWF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:flour-*</code> | 未声明；按配方类型判定 | 允许变体：['flax', 'millet', 'rice', 'rye', 'spelt', 'cassava', 'amaranth', 'sunflower'] |
| 产物 | 血饵<br><code>fishingbait-blood</code> | 6 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FWF
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 变体材料（按代码匹配）<br><code>game:fishingpole-simple-{type}</code> | 1 | 允许变体：['wood', 'bamboo'] |
| 投入 B | 血饵<br><code>fishingbait-blood</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:fishingpole-simple-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "FWF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "item",
        "code": "game:flour-*",
        "allowedVariants": [
          "flax",
          "millet",
          "rice",
          "rye",
          "spelt",
          "cassava",
          "amaranth",
          "sunflower"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 1
      }
    },
    "name": "bloodbait",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "fishingbait-blood",
      "quantity": 6
    }
  },
  {
    "ingredientPattern": "FWF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "F": {
        "type": "item",
        "code": "game:flour-*",
        "allowedVariants": [
          "flax",
          "millet",
          "rice",
          "rye",
          "spelt",
          "cassava",
          "amaranth",
          "sunflower"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 1
      }
    },
    "name": "bloodbait",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "fishingbait-blood",
      "quantity": 6
    }
  },
  {
    "ingredientPattern": "FWF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "F": {
        "type": "item",
        "code": "game:flour-*",
        "allowedVariants": [
          "flax",
          "millet",
          "rice",
          "rye",
          "spelt",
          "cassava",
          "amaranth",
          "sunflower"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 1
      }
    },
    "name": "bloodbait",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "fishingbait-blood",
      "quantity": 6
    }
  },
  {
    "name": "fishingpole-bait-blood",
    "recipeGroup": 3,
    "ingredientPattern": "R,B",
    "shapeless": true,
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:fishingpole-simple-{type}",
        "allowedVariants": [
          "wood",
          "bamboo"
        ],
        "quantity": 1
      },
      "B": {
        "type": "item",
        "code": "fishingbait-blood",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:fishingpole-simple-{type}",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · blooddough</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:flour-*</code> | 未声明；按配方类型判定 | 允许变体：['flax', 'millet', 'rice', 'rye', 'spelt', 'cassava', 'amaranth', 'sunflower'] |
| 产物 | 变体材料（按代码匹配）<br><code>blooddough-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:flour-*</code> | 未声明；按配方类型判定 | 允许变体：['flax', 'millet', 'rice', 'rye', 'spelt', 'cassava', 'amaranth', 'sunflower'] |
| 产物 | 变体材料（按代码匹配）<br><code>blooddough-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:flour-*</code> | 未声明；按配方类型判定 | 允许变体：['flax', 'millet', 'rice', 'rye', 'spelt', 'cassava', 'amaranth', 'sunflower'] |
| 产物 | 变体材料（按代码匹配）<br><code>blooddough-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WF
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "WF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "item",
        "code": "game:flour-*",
        "allowedVariants": [
          "flax",
          "millet",
          "rice",
          "rye",
          "spelt",
          "cassava",
          "amaranth",
          "sunflower"
        ],
        "name": "type"
      }
    },
    "width": 2,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 0.2
      }
    },
    "name": "blooddough",
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "blooddough-{type}"
    }
  },
  {
    "ingredientPattern": "WF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "F": {
        "type": "item",
        "code": "game:flour-*",
        "allowedVariants": [
          "flax",
          "millet",
          "rice",
          "rye",
          "spelt",
          "cassava",
          "amaranth",
          "sunflower"
        ],
        "name": "type"
      }
    },
    "width": 2,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 0.2
      }
    },
    "name": "blooddough",
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "blooddough-{type}"
    }
  },
  {
    "ingredientPattern": "WF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "F": {
        "type": "item",
        "code": "game:flour-*",
        "allowedVariants": [
          "flax",
          "millet",
          "rice",
          "rye",
          "spelt",
          "cassava",
          "amaranth",
          "sunflower"
        ],
        "name": "type"
      }
    },
    "width": 2,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 0.2
      }
    },
    "name": "blooddough",
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "blooddough-{type}"
    }
  }
]
```

</details>

</details>

<details><summary>生血肠 · bloodsausage</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 干净内脏<br><code>offal-clean</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:redmeat-*</code> | 2 | 允许变体：['raw', 'cured'] |
| 产物 | 生血肠<br><code>sausage-bloodsausage-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
H
M
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 干净内脏<br><code>offal-clean</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:bushmeat-*</code> | 4 | 允许变体：['raw', 'cured'] |
| 产物 | 生血肠<br><code>sausage-bloodsausage-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
H
M
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 干净内脏<br><code>offal-clean</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:poultry-*</code> | 3 | 允许变体：['raw'] |
| 产物 | 生血肠<br><code>sausage-bloodsausage-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
H
M
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "C,H,M",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "offal-clean"
      },
      "H": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-*",
        "allowedVariants": [
          "raw",
          "cured"
        ],
        "quantity": 2
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 0.2
      }
    },
    "output": {
      "type": "item",
      "code": "sausage-bloodsausage-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "C,H,M",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "offal-clean"
      },
      "H": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-*",
        "allowedVariants": [
          "raw",
          "cured"
        ],
        "quantity": 4
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 0.2
      }
    },
    "output": {
      "type": "item",
      "code": "sausage-bloodsausage-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "C,H,M",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "offal-clean"
      },
      "H": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-*",
        "allowedVariants": [
          "raw"
        ],
        "quantity": 3
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:bloodportion"
        },
        "requiresLitres": 0.2
      }
    },
    "output": {
      "type": "item",
      "code": "sausage-bloodsausage-raw",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>骨头 · bone</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 坚骨<br><code>strongbone</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 1 | 未声明附加限制 |
| 产物 | 骨头<br><code>game:bone</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BK
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "BK",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "strongbone",
        "quantity": 1
      },
      "K": {
        "type": "item",
        "code": "game:axe-*",
        "quantity": 1,
        "istool": true
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:bone",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>骨针 · boneneedle</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 小骨头<br><code>game:bone-tiny</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 1 | 未声明附加限制 |
| 产物 | 骨针<br><code>needle-bone</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BK
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 鱼骨<br><code>game:bone-fish</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 1 | 未声明附加限制 |
| 产物 | 骨针<br><code>needle-bone</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BK
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "BK",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bone-tiny",
        "quantity": 1
      },
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "quantity": 1,
        "istool": true
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "needle-bone",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "BK",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bone-fish",
        "quantity": 1
      },
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "quantity": 1,
        "istool": true
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "needle-bone",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>骨镐、骨箭、粗制箭 · bonetools</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 骨质镐头<br><code>toolhead-pick-bone</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 1 | 未声明附加限制 |
| 产物 | 骨镐<br><code>bonepickaxe</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
H
S
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 骨质箭头<br><code>toolhead-arrow-bone</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 1 | 未声明附加限制 |
| 投入 F | 羽毛<br><code>game:feather</code> | 1 | 未声明附加限制 |
| 产物 | 骨箭<br><code>arrow-bone</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
H
S
F
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 骨质箭头<br><code>toolhead-arrow-bone</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 1 | 未声明附加限制 |
| 产物 | 粗制箭<br><code>game:arrow-crude</code> | 1 | 未声明附加限制 |

**加工条件：** 所需特性：bowyer；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
H
S
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "H,S",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "toolhead-pick-bone",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "bonepickaxe",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "H,S,F",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "toolhead-arrow-bone",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "arrow-bone",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "H,S",
    "requiresTrait": "bowyer",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "toolhead-arrow-bone",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:arrow-crude",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码）、变体材料（按代码匹配） · butcherhook</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*</code> | 2 | 未声明附加限制 |
| 投入 H | 燧石钩<br><code>hook-flint</code> | 2 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 1 | 未声明附加限制 |
| 投入 F | 燧石<br><code>game:flint</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butcherhook-flint-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
RHF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*</code> | 2 | 未声明附加限制 |
| 投入 H | 燧石钩<br><code>hook-flint</code> | 2 | 未声明附加限制 |
| 投入 R | 脂肪块<br><code>game:fat</code> | 1 | 未声明附加限制 |
| 投入 F | 燧石<br><code>game:flint</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butcherhook-flint-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
RHF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*</code> | 2 | 未声明附加限制 |
| 投入 H | 燧石钩<br><code>hook-flint</code> | 2 | 未声明附加限制 |
| 投入 R | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 F | 燧石<br><code>game:flint</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butcherhook-flint-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
RHF
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 4 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>hook-*</code> | 2 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze'] |
| 投入 R | 树脂<br><code>game:resin</code> | 1 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 2 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze'] |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>butcherhook-{material}-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
RHF
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 4 | 未声明附加限制 |
| 投入 H | 铁制钩<br><code>hook-iron</code> | 2 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 1 | 未声明附加限制 |
| 投入 F | 铁钉子和垫片<br><code>game:metalnailsandstrips-iron</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butcherhook-iron-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
RHF
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>butcherhook-*-north</code> | 1 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'iron'] |
| 投入 W | 变体材料（按代码匹配）<br><code>game:wrench-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>butcherhookceiling-{material}-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HW
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>butcherhookceiling-*-north</code> | 1 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'iron'] |
| 投入 W | 变体材料（按代码匹配）<br><code>game:wrench-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>butcherhook-{material}-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HW
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>butcherhook-*-north</code> | 1 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'iron'] |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>hook-{material}</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
H
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>butcherhookceiling-*-north</code> | 1 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'iron'] |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>hook-{material}</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
H
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>hook-*</code> | 1 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'iron'] |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:metalbit-{material}</code> | 5 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
H
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SLS,RHF",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:log-*",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "hook-flint",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:flint",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butcherhook-flint-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SLS,RHF",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:log-*",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "hook-flint",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:fat",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:flint",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butcherhook-flint-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SLS,RHF",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:log-*",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "hook-flint",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:fat-rendered",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:flint",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butcherhook-flint-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SLS,RHF",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 4
      },
      "H": {
        "type": "item",
        "code": "hook-*",
        "quantity": 2,
        "name": "material",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 2,
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze"
        ]
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butcherhook-{material}-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SLS,RHF",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 4
      },
      "H": {
        "type": "item",
        "code": "hook-iron",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:metalnailsandstrips-iron",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butcherhook-iron-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HW",
    "ingredients": {
      "H": {
        "type": "block",
        "code": "butcherhook-*-north",
        "quantity": 1,
        "name": "material",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "iron"
        ]
      },
      "W": {
        "type": "item",
        "code": "game:wrench-*",
        "istool": true
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "block",
      "code": "butcherhookceiling-{material}-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HW",
    "ingredients": {
      "H": {
        "type": "block",
        "code": "butcherhookceiling-*-north",
        "quantity": 1,
        "name": "material",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "iron"
        ]
      },
      "W": {
        "type": "item",
        "code": "game:wrench-*",
        "istool": true
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "block",
      "code": "butcherhook-{material}-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "C,H",
    "ingredients": {
      "H": {
        "type": "block",
        "code": "butcherhook-*-north",
        "quantity": 1,
        "name": "material",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "iron"
        ]
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "istool": true
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "hook-{material}",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "C,H",
    "ingredients": {
      "H": {
        "type": "block",
        "code": "butcherhookceiling-*-north",
        "quantity": 1,
        "name": "material",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "iron"
        ]
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "istool": true
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "hook-{material}",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "C,H",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "hook-*",
        "quantity": 1,
        "name": "material",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "iron"
        ]
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "istool": true
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:metalbit-{material}",
      "quantity": 5
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · butchertables</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 允许变体：['chert', 'granite', 'andesite', 'basalt', 'obsidian', 'peridotite', 'flint', 'bonechert', 'bonegranite', 'boneandesite', 'bonebasalt', 'boneobsidian', 'boneperidotite', 'boneflint'] |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 允许变体：['chert', 'granite', 'andesite', 'basalt', 'obsidian', 'peridotite', 'flint', 'bone-chert', 'bone-granite', 'bone-andesite', 'bone-basalt', 'bone-obsidian', 'bone-peridotite', 'bone-flint'] |
| 投入 F | 燧石<br><code>game:flint</code> | 6 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 12 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butchertable-primitive-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KAF
LSL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 16 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze'] |
| 投入 S | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze'] |
| 投入 L | 变体材料（按代码匹配）<br><code>game:cleaver-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze'] |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butchertable-simple-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KSL
PCP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 16 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 允许变体：['iron'] |
| 投入 S | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 允许变体：['iron'] |
| 投入 L | 变体材料（按代码匹配）<br><code>game:cleaver-*</code> | 未声明；按配方类型判定 | 允许变体：['iron'] |
| 投入 I | 铁板<br><code>game:metalplate-iron</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>butchertable-advanced-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KSL
PIP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "KAF,LSL",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:log-*",
        "quantity": 2
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "allowedVariants": [
          "chert",
          "granite",
          "andesite",
          "basalt",
          "obsidian",
          "peridotite",
          "flint",
          "bonechert",
          "bonegranite",
          "boneandesite",
          "bonebasalt",
          "boneobsidian",
          "boneperidotite",
          "boneflint"
        ]
      },
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "allowedVariants": [
          "chert",
          "granite",
          "andesite",
          "basalt",
          "obsidian",
          "peridotite",
          "flint",
          "bone-chert",
          "bone-granite",
          "bone-andesite",
          "bone-basalt",
          "bone-obsidian",
          "bone-peridotite",
          "bone-flint"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:flint",
        "quantity": 6
      },
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 12
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butchertable-primitive-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KSL,PCP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 16
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze"
        ]
      },
      "S": {
        "type": "item",
        "code": "game:shears-*",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze"
        ]
      },
      "L": {
        "type": "item",
        "code": "game:cleaver-*",
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze"
        ]
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-copper",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butchertable-simple-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KSL,PIP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 16
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "allowedVariants": [
          "iron"
        ]
      },
      "S": {
        "type": "item",
        "code": "game:shears-*",
        "allowedVariants": [
          "iron"
        ]
      },
      "L": {
        "type": "item",
        "code": "game:cleaver-*",
        "allowedVariants": [
          "iron"
        ]
      },
      "I": {
        "type": "item",
        "code": "game:metalplate-iron",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "butchertable-advanced-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>屠宰袋 · butcherybaghide</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 巨型毛皮<br><code>game:hide-pelt-huge</code> | 1 | 未声明附加限制 |
| 投入 F | 亚麻线<br><code>game:flaxtwine</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 8 | 未声明附加限制 |
| 产物 | 屠宰袋<br><code>butcherybag-standard</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FTF
KTP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 大型毛皮<br><code>game:hide-pelt-large</code> | 2 | 未声明附加限制 |
| 投入 F | 亚麻线<br><code>game:flaxtwine</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 8 | 未声明附加限制 |
| 产物 | 屠宰袋<br><code>butcherybag-standard</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FTF
KTP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 中型毛皮<br><code>game:hide-pelt-medium</code> | 3 | 未声明附加限制 |
| 投入 F | 亚麻线<br><code>game:flaxtwine</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 8 | 未声明附加限制 |
| 产物 | 屠宰袋<br><code>butcherybag-standard</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FTF
KTP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 小型毛皮<br><code>game:hide-pelt-small</code> | 4 | 未声明附加限制 |
| 投入 F | 亚麻线<br><code>game:flaxtwine</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 8 | 未声明附加限制 |
| 产物 | 屠宰袋<br><code>butcherybag-standard</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FTF
KTP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "FTF,KTP",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:hide-pelt-huge",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:flaxtwine",
        "quantity": 2
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-standard",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "FTF,KTP",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:hide-pelt-large",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:flaxtwine",
        "quantity": 2
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-standard",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "FTF,KTP",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:hide-pelt-medium",
        "quantity": 3
      },
      "F": {
        "type": "item",
        "code": "game:flaxtwine",
        "quantity": 2
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-standard",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "FTF,KTP",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:hide-pelt-small",
        "quantity": 4
      },
      "F": {
        "type": "item",
        "code": "game:flaxtwine",
        "quantity": 2
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-standard",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>皮革屠宰袋 · butcherybagleather</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 皮革<br><code>game:leather-normal-plain</code> | 8 | 未声明附加限制 |
| 投入 F | 铜棒<br><code>game:rod-copper</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 铜钉子和垫片<br><code>game:metalnailsandstrips-copper</code> | 2 | 未声明附加限制 |
| 产物 | 皮革屠宰袋<br><code>butcherybag-leather</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FTF
KTP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "FTF,KTP",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:leather-normal-plain",
        "quantity": 8
      },
      "F": {
        "type": "item",
        "code": "game:rod-copper",
        "quantity": 1
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "P": {
        "type": "item",
        "code": "game:metalnailsandstrips-copper",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-leather",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>原始屠宰袋 · butcherybagreed</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 香蒲<br><code>game:cattailtops</code> | 24 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 6 | 未声明附加限制 |
| 产物 | 原始屠宰袋<br><code>butcherybag-primitive</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RTR
KTS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 纸莎草<br><code>game:papyrustops</code> | 24 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 6 | 未声明附加限制 |
| 产物 | 原始屠宰袋<br><code>butcherybag-primitive</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RTR
KTS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "RTR,KTS",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 24
      },
      "R": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 6
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-primitive",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "RTR,KTS",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 24
      },
      "R": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 6
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-primitive",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>结实皮革屠宰袋 · butcherybagsturdyleather</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 坚固皮革<br><code>game:leather-sturdy-plain</code> | 8 | 未声明附加限制 |
| 投入 F | 铁棒<br><code>game:rod-iron</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 铁钉子和垫片<br><code>game:metalnailsandstrips-iron</code> | 2 | 未声明附加限制 |
| 产物 | 结实皮革屠宰袋<br><code>butcherybag-sturdyleather</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FTF
KTP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "FTF,KTP",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:leather-sturdy-plain",
        "quantity": 8
      },
      "F": {
        "type": "item",
        "code": "game:rod-iron",
        "quantity": 1
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "Istool": true
      },
      "P": {
        "type": "item",
        "code": "game:metalnailsandstrips-iron",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "butcherybag-sturdyleather",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>预处理疗愈上等肉 · healingprimemeat</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 名称未汉化（见物品代码）<br><code>game:flower-horsetail-free</code> | 2 | 未声明附加限制 |
| 投入 H | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生上等肉<br><code>primemeat-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 预处理疗愈上等肉<br><code>primemeat-healing</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
T
H
M
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "T,H,M",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "game:flower-horsetail-free",
        "quantity": 2
      },
      "H": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "M": {
        "type": "item",
        "code": "primemeat-raw"
      }
    },
    "width": 1,
    "height": 3,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.2
      }
    },
    "output": {
      "type": "item",
      "code": "primemeat-healing",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>象牙块 · ivory</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 象牙<br><code>ivory-raw</code> | 1 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 未声明附加限制 |
| 产物 | 象牙块<br><code>ivoryblock</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
III
ICI
III
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "III,ICI,III",
    "ingredients": {
      "I": {
        "type": "item",
        "code": "ivory-raw",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "quantity": 1,
        "istool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "ivoryblock",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>腐烂物 · rot</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*-rotten</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 腐烂物<br><code>game:rot</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "recipeGroup": 2,
  "ingredientPattern": "P",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "*-rotten"
    }
  },
  "width": 1,
  "height": 1,
  "output": {
    "type": "item",
    "code": "game:rot",
    "quantity": 8
  }
}
```

</details>

</details>

<details><summary>针线包 · sewingkitbone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 骨针<br><code>needle-bone</code> | 1 | 未声明附加限制 |
| 投入 M | 皮革<br><code>game:leather-normal-plain</code> | 1 | 未声明附加限制 |
| 投入 F | 亚麻纤维<br><code>game:flaxfibers</code> | 2 | 未声明附加限制 |
| 产物 | 针线包<br><code>game:sewingkit</code> | 2 | 未声明附加限制 |

**加工条件：** 所需特性：clothier；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMK
MMF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 骨针<br><code>needle-bone</code> | 1 | 未声明附加限制 |
| 投入 M | 干燥肌腱<br><code>sinew-dry</code> | 1 | 未声明附加限制 |
| 投入 F | 亚麻纤维<br><code>game:flaxfibers</code> | 2 | 未声明附加限制 |
| 产物 | 针线包<br><code>game:sewingkit</code> | 1 | 未声明附加限制 |

**加工条件：** 所需特性：clothier；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMK
MMF
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "MMK,MMF",
    "requiresTrait": "clothier",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "needle-bone",
        "quantity": 1
      },
      "M": {
        "type": "item",
        "code": "game:leather-normal-plain",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:flaxfibers",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 2,
    "output": {
      "type": "item",
      "code": "game:sewingkit",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "MMK,MMF",
    "requiresTrait": "clothier",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "needle-bone",
        "quantity": 1
      },
      "M": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:flaxfibers",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "game:sewingkit",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>简易弓、长弓、反曲弓 · sinewbows</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 4 | 未声明附加限制 |
| 产物 | 简易弓<br><code>game:bow-simple</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_ST
S_T
_ST
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-*</code> | 未声明；按配方类型判定 | 允许变体：['small', 'medium'] |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-*</code> | 未声明；按配方类型判定 | 允许变体：['small', 'medium'] |
| 投入 F | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-*</code> | 未声明；按配方类型判定 | 允许变体：['small', 'medium'] |
| 投入 F | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-fox-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-fox-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-fox-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-raccoon-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-raccoon-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的长弓弓材<br><code>game:bowstave-long-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 6 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-raccoon-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长弓<br><code>game:bow-long</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_FT
BLT
_FT
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 晾干的反曲弓弓材<br><code>game:bowstave-recurve-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 干燥肌腱<br><code>sinew-dry</code> | 8 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 骨头<br><code>game:bone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生野味<br><code>game:bushmeat-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 反曲弓<br><code>game:bow-recurve</code> | 1 | 未声明附加限制 |

**加工条件：** 所需特性：bowyer；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MFT
BLT
MFT
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_ST,S_T,_ST",
    "recipeGroup": 2,
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-simple",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 3,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 3,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "F": {
        "type": "item",
        "code": "game:resin"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 3,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "F": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-*",
        "allowedVariants": [
          "small",
          "medium"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-*",
        "allowedVariants": [
          "small",
          "medium"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:resin"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-*",
        "allowedVariants": [
          "small",
          "medium"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-fox-*"
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-fox-*"
      },
      "F": {
        "type": "item",
        "code": "game:resin"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-fox-*"
      },
      "F": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-raccoon-*"
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-raccoon-*"
      },
      "F": {
        "type": "item",
        "code": "game:resin"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_FT,BLT,_FT",
    "recipeGroup": 4,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-long-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 6
      },
      "L": {
        "type": "item",
        "code": "game:hide-pelt-raccoon-*"
      },
      "F": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-long",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MFT,BLT,MFT",
    "requiresTrait": "bowyer",
    "recipeGroup": 2,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:bowstave-recurve-dry"
      },
      "T": {
        "type": "item",
        "code": "sinew-dry",
        "quantity": 8
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "F": {
        "type": "item",
        "code": "game:bone"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-raw"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:bow-recurve",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · smokingrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 4 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>hook-*</code> | 4 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze'] |
| 投入 R | 树脂<br><code>game:resin</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>smokingrack-copper-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPH
SRS
HPH
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 4 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>hook-*</code> | 4 | 允许变体：['iron'] |
| 投入 R | 树脂<br><code>game:resin</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>smokingrack-iron-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPH
SRS
HPH
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "HPH,SRS,HPH",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 4
      },
      "H": {
        "type": "item",
        "code": "hook-*",
        "quantity": 4,
        "allowedVariants": [
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "smokingrack-copper-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HPH,SRS,HPH",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 4
      },
      "H": {
        "type": "item",
        "code": "hook-*",
        "quantity": 4,
        "allowedVariants": [
          "iron"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "smokingrack-iron-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · temporalbutcherbox</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:wrench-*</code> | 1 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 1 | 未声明附加限制 |
| 投入 T | 白铜锭<br><code>game:ingot-cupronickel</code> | 2 | 未声明附加限制 |
| 投入 P | 金属零件<br><code>game:metal-parts</code> | 1 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:solderbar-*</code> | 5 | 未声明附加限制 |
| 投入 R | 生锈齿轮<br><code>game:gear-rusty</code> | 8 | 未声明附加限制 |
| 投入 M | 金属废料<br><code>game:metal-scraps</code> | 8 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>temporalbutcherbox-off-north</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WSH
PTP
RMR
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": false,
    "ingredientPattern": "WSH,PTP,RMR",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:wrench-*",
        "quantity": 1,
        "istool": true
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "quantity": 1,
        "istool": true
      },
      "T": {
        "type": "item",
        "code": "game:ingot-cupronickel",
        "quantity": 2
      },
      "P": {
        "type": "block",
        "code": "game:metal-parts",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:solderbar-*",
        "quantity": 5
      },
      "R": {
        "type": "item",
        "code": "game:gear-rusty",
        "quantity": 8
      },
      "M": {
        "type": "block",
        "code": "game:metal-scraps",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "temporalbutcherbox-off-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>骨质箭头 · bone-arrowhead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 骨质箭头<br><code>toolhead-arrow-bone</code> | 10 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "butchering:strongbone"
  },
  "pattern": [
    [
      "__#_#__#_#",
      "_#__#_#__#",
      "_#_#__#_#_",
      "__________",
      "__#_#__#_#",
      "_#__#_#__#",
      "_#_#__#_#_",
      "__________",
      "_##____##_",
      "___#__#___"
    ]
  ],
  "name": "Bone Arrowhead",
  "output": {
    "type": "item",
    "code": "toolhead-arrow-bone",
    "stacksize": 10
  }
}
```

</details>

</details>

<details><summary>骨质镐头 · bone-pick</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 骨质镐头<br><code>toolhead-pick-bone</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "butchering:strongbone"
  },
  "pattern": [
    [
      "___###____",
      "___###____",
      "___###____",
      "___##_____",
      "___##_____",
      "___##_____",
      "___###____",
      "____###___",
      "_____##___",
      "______#___"
    ]
  ],
  "name": "Bone Pick",
  "output": {
    "type": "item",
    "code": "toolhead-pick-bone",
    "stacksize": 1
  }
}
```

</details>

</details>

<details><summary>燧石钩 · flint-hook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 燧石钩<br><code>hook-flint</code> | 2 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "game:flint"
  },
  "pattern": [
    [
      "______###_",
      "________##",
      "_________#",
      "_____#__##",
      "_____####_",
      "_####_____",
      "##__#_____",
      "#_________",
      "##________",
      "_###______"
    ]
  ],
  "name": "Flint hook",
  "output": {
    "type": "item",
    "code": "hook-flint",
    "stacksize": 2
  }
}
```

</details>

</details>

<details><summary>生血肠、生黑布丁 · bloodmeatnuggetsausages</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 投入 2 inputs 1 | 血液<br><code>butchering:bloodportion</code> | 20 | 未声明附加限制 |
| 投入 3 inputs 1 | 生野味肉块<br><code>expandedfoods:meatnugget-bushmeat-raw</code> | 4 | 未声明附加限制 |
| 产物 | 生血肠<br><code>butchering:sausage-bloodsausage-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 投入 2 inputs 1 | 血液<br><code>butchering:bloodportion</code> | 20 | 未声明附加限制 |
| 投入 3 inputs 1 | 生红肉块<br><code>expandedfoods:meatnugget-redmeat-raw</code> | 2 | 未声明附加限制 |
| 产物 | 生血肠<br><code>butchering:sausage-bloodsausage-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 投入 2 inputs 1 | 血液<br><code>butchering:bloodportion</code> | 80 | 未声明附加限制 |
| 投入 3 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 产物 | 生黑布丁<br><code>butchering:sausage-blackpudding-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:bloodportion",
            "quantity": 20
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:meatnugget-bushmeat-raw",
            "quantity": 4
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "butchering:sausage-bloodsausage-raw",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:bloodportion",
            "quantity": 20
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:meatnugget-redmeat-raw",
            "quantity": 2
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "butchering:sausage-bloodsausage-raw",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:bloodportion",
            "quantity": 80
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "butchering:sausage-blackpudding-raw",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>干净内脏 · cleaningoffal</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 血淋内脏<br><code>butchering:offal-bloody</code> | 1 | 未声明附加限制 |
| 投入 2 inputs 1 | 水<br><code>game:waterportion</code> | 20 | 未声明附加限制 |
| 产物 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-bloody",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:waterportion",
            "quantity": 20
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "butchering:offal-clean",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>生鱼肉香肠、腌制中的鱼肉香肠、生奶酪鱼肉香肠、腌制中的奶酪鱼肉香肠 · fishnuggetsausages</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 生鱼肉块<br><code>expandedfoods:fishnugget-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 生鱼肉香肠<br><code>expandedfoods:sausagefish-normal-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 生鱼肉块<br><code>expandedfoods:fishnugget-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 盐<br><code>game:salt</code> | 1 | 未声明附加限制 |
| 投入 4 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 腌制中的鱼肉香肠<br><code>expandedfoods:sausagefish-normal-curing</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 生鱼肉块<br><code>expandedfoods:fishnugget-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 一份切达奶酪<br><code>game:cheese-cheddar-1slice</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 2 | 一份蓝纹奶酪<br><code>game:cheese-blue-1slice</code> | 1 | 未声明附加限制 |
| 投入 4 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 生奶酪鱼肉香肠<br><code>expandedfoods:sausagefish-cheese-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 生鱼肉块<br><code>expandedfoods:fishnugget-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 一份切达奶酪<br><code>game:cheese-cheddar-1slice</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 2 | 一份蓝纹奶酪<br><code>game:cheese-blue-1slice</code> | 1 | 未声明附加限制 |
| 投入 4 inputs 1 | 盐<br><code>game:salt</code> | 1 | 未声明附加限制 |
| 投入 5 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 腌制中的奶酪鱼肉香肠<br><code>expandedfoods:sausagefish-cheese-curing</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:fishnugget-raw",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausagefish-normal-raw",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:fishnugget-raw",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:salt",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausagefish-normal-curing",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:fishnugget-raw",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:cheese-cheddar-1slice",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "game:cheese-blue-1slice",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausagefish-cheese-raw",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:fishnugget-raw",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:cheese-cheddar-1slice",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "game:cheese-blue-1slice",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:salt",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausagefish-cheese-curing",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · meatnuggetsausages</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 变体材料（按代码匹配）<br><code>expandedfoods:meatnugget-*-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>expandedfoods:sausage-{meat}-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 变体材料（按代码匹配）<br><code>expandedfoods:meatnugget-*-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 盐<br><code>game:salt</code> | 1 | 未声明附加限制 |
| 投入 4 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>expandedfoods:sausage-{meat}-curing</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 变体材料（按代码匹配）<br><code>expandedfoods:meatnugget-*-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 一份切达奶酪<br><code>game:cheese-cheddar-1slice</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 2 | 一份蓝纹奶酪<br><code>game:cheese-blue-1slice</code> | 1 | 未声明附加限制 |
| 投入 4 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>expandedfoods:sausage-{meat}cheese-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 inputs 1 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 投入 1 inputs 2 | 猪油<br><code>expandedfoods:lard</code> | 10 | 未声明附加限制 |
| 投入 2 inputs 1 | 变体材料（按代码匹配）<br><code>expandedfoods:meatnugget-*-raw</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 1 | 一份切达奶酪<br><code>game:cheese-cheddar-1slice</code> | 1 | 未声明附加限制 |
| 投入 3 inputs 2 | 一份蓝纹奶酪<br><code>game:cheese-blue-1slice</code> | 1 | 未声明附加限制 |
| 投入 4 inputs 1 | 盐<br><code>game:salt</code> | 1 | 未声明附加限制 |
| 投入 5 inputs 1 | 干净内脏<br><code>butchering:offal-clean</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>expandedfoods:sausage-{meat}cheese-curing</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:meatnugget-*-raw",
            "quantity": 1,
            "name": "meat"
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausage-{meat}-raw",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:meatnugget-*-raw",
            "quantity": 1,
            "name": "meat"
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:salt",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausage-{meat}-curing",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:meatnugget-*-raw",
            "quantity": 1,
            "name": "meat"
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:cheese-cheddar-1slice",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "game:cheese-blue-1slice",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausage-{meat}cheese-raw",
      "stackSize": 1
    }
  },
  {
    "enabled": false,
    "ingredients": [
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "expandedfoods:lard",
            "quantity": 10
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "expandedfoods:meatnugget-*-raw",
            "quantity": 1,
            "name": "meat"
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:cheese-cheddar-1slice",
            "quantity": 1
          },
          {
            "type": "item",
            "code": "game:cheese-blue-1slice",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "game:salt",
            "quantity": 1
          }
        ]
      },
      {
        "inputs": [
          {
            "type": "item",
            "code": "butchering:offal-clean",
            "quantity": 1
          }
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "expandedfoods:sausage-{meat}cheese-curing",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · fourbutcheringhook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>hook-{metal}</code> | 4 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "copper",
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "iron"
    ]
  },
  "name": "4 Butchering Hook",
  "code": "fourbutcheringhook-{metal}",
  "pattern": [
    [
      "_##___##_",
      "_#_____#_",
      "_#_#_#_#_",
      "_###_###_",
      "_________",
      "_###_###_",
      "_#_#_#_#_",
      "_#_____#_",
      "_##___##_"
    ]
  ],
  "output": {
    "type": "item",
    "code": "hook-{metal}",
    "stacksize": 4
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · onebutcheringhook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>hook-{metal}</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "enabled": false,
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "recipeAttributes": {
      "nuggetRecipe": true
    },
    "name": "metal",
    "allowedVariants": [
      "copper",
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "iron"
    ]
  },
  "name": "1 Butchering Hook",
  "code": "onebutcheringhook-{metal}",
  "pattern": [
    [
      "##_",
      "#__",
      "#_#",
      "###"
    ]
  ],
  "output": {
    "type": "item",
    "code": "hook-{metal}",
    "stacksize": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
