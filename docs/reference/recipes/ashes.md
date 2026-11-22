<!-- generated:start -->
# 灰烬材料：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>木灰泥 · bark_ash_sludge</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>ancienttools:barkashsolution</code> | 10 升 | 未声明附加限制 |
| 产物 | 木灰泥<br><code>em:ash-organic-wood-sludge</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：216。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "barkashsludge",
    "enabled": true,
    "sealHours": 216,
    "ingredients": [
      {
        "type": "item",
        "code": "ancienttools:barkashsolution",
        "litres": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "em:ash-organic-wood-sludge",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · ash</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>meteoricexpansion:rockash</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>em:ash-inorganic-rock</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "A",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "meteoricexpansion:rockash"
      }
    },
    "width": 1,
    "height": 1,
    "output": {
      "type": "item",
      "code": "em:ash-inorganic-rock"
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · lye</summary>

<details><summary>技术说明：完整配方</summary>


```json
[]
```

</details>

</details>

<details><summary>碱液皂块、洗涤碱 · soapbar_washingsoda</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 产物 | 碱液皂块<br><code>soapandlyecontinued:soapbar-lye</code> | 2 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂块<br><code>soapandlyecontinued:soapbar-lye</code> | 1 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 产物 | 洗涤碱<br><code>em:washingsodaportion</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：1。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "soapbar_soda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:fat-rendered",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "soapandlyecontinued:soapbar-lye",
      "quantity": 2
    }
  },
  {
    "code": "soap",
    "sealHours": 1,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapbar-lye",
        "quantity": 1
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1,
        "consumeLitres": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:washingsodaportion",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>氢氧化钾溶液 · causticpotash</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 熟石灰<br><code>game:slakedlimeportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 木灰泥<br><code>em:ash-organic-wood-sludge</code> | 1 | 未声明附加限制 |
| 产物 | 氢氧化钾溶液<br><code>em:causticpotashportion</code> | 6 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "causticpotashportion",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "game:slakedlimeportion",
        "litres": 5
      },
      {
        "type": "item",
        "code": "em:ash-organic-wood-sludge",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:causticpotashportion",
      "litres": 6
    }
  }
]
```

</details>

</details>

<details><summary>洗涤碱 · washingsoda</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 熟石灰<br><code>game:slakedlimeportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 植物灰泥<br><code>em:ash-organic-plant-sludge</code> | 1 | 未声明附加限制 |
| 产物 | 洗涤碱<br><code>em:washingsodaportion</code> | 6 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "washingsodaportion",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "game:slakedlimeportion",
        "litres": 5
      },
      {
        "type": "item",
        "code": "em:ash-organic-plant-sludge",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:washingsodaportion",
      "litres": 6
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · ash_potash</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sludge</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sludge</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**加工条件：** 配方开关：True。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "potash",
    "enabled": false,
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 72
      },
      "transitionHours": {
        "avg": 72
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:potash"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 0.2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:waterportion",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "sludge",
        "minQuantity": 2,
        "maxQuantity": 2,
        "validStacks": [
          {
            "type": "item",
            "code": "em:ash-organic-wood-sludge"
          },
          {
            "type": "item",
            "code": "em:ash-organic-tang-sludge"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:potash",
      "quantity": 1
    }
  },
  {
    "code": "soda",
    "enabled": true,
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 72
      },
      "transitionHours": {
        "avg": 72
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:potash"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 0.2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:waterportion",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "sludge",
        "minQuantity": 2,
        "maxQuantity": 2,
        "validStacks": [
          {
            "type": "item",
            "code": "em:ash-organic-plant-sludge"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-soda",
      "quantity": 1
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
