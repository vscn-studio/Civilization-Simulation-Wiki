<!-- generated:start -->
# 扩展材料：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>名称未汉化（见物品代码） · pitch_pot</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 粉末状煤<br><code>em:powdered-ore-coal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 名称未汉化（见物品代码）<br><code>game:claypot-burned</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>ancienttools:pitchpot-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "comment": "Compatibility with Ancient Tools",
    "ingredientPattern": "C,P",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "em:powdered-ore-coal"
      },
      "P": {
        "type": "block",
        "code": "game:claypot-burned"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "ancienttools:pitchpot-empty",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · picricacid_down</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>nitricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>indigo</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "picricacid",
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
        "code": "em:powdered-ore-picricacid"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "nitricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.5,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-nitric",
            "shapeElement": "bowl/water"
          }
        ]
      },
      {
        "code": "indigo",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "tailorsdelight:down-*"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-picricacid",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>媒染羊毛布、媒染羊毛线 · mordant_wool</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸铜<br><code>game:sulfate-full-copper</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 素色羊毛布<br><code>wool:cloth-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸亚铁<br><code>game:sulfate-full-iron</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 素色羊毛布<br><code>wool:cloth-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 素色羊毛布<br><code>wool:cloth-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 素色羊毛布<br><code>wool:cloth-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸铜<br><code>game:sulfate-full-copper</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 羊毛线<br><code>wool:twine-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸亚铁<br><code>game:sulfate-full-iron</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 羊毛线<br><code>wool:twine-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 羊毛线<br><code>wool:twine-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 羊毛线<br><code>wool:twine-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "mordantedwoolsulfatecopper",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-copper",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant"
    }
  },
  {
    "code": "mordantedwoolsulfateiron",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-iron",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant"
    }
  },
  {
    "code": "mordantedwoolsulfatezinc",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant"
    }
  },
  {
    "code": "mordantclothsoda",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant"
    }
  },
  {
    "code": "mordantedwooltwinecopper",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-copper",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:twine-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  },
  {
    "code": "mordantedwooltwineiron",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-iron",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:twine-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  },
  {
    "code": "mordantedwooltwinezinc",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:twine-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  },
  {
    "code": "mordantedwooltwinesoda",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:twine-wool-plain"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · picricacid_fleece</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>nitricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>indigo</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "picricacid",
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
        "code": "em:powdered-ore-picricacid"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "nitricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.5,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-nitric",
            "shapeElement": "bowl/water"
          }
        ]
      },
      {
        "code": "indigo",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "wool:fleece-*"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-picricacid",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>明矾粉 · alum</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸<br><code>game:acid-full-sulfuric</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉状铝土矿<br><code>em:powdered-stone-bauxite</code> | 2 | 未声明附加限制 |
| 产物 | 明矾粉<br><code>game:powder-alum</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：120。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:acid-full-sulfuric",
        "litres": 1
      },
      {
        "type": "item",
        "code": "em:powdered-stone-bauxite",
        "quantity": 2
      }
    ],
    "sealHours": 120,
    "output": {
      "type": "item",
      "code": "game:powder-alum",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>植物灰泥、木灰泥、海藻灰泥 · ash_sludge</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 植物灰<br><code>em:ash-organic-plant-dry</code> | 10 | 未声明附加限制 |
| 产物 | 植物灰泥<br><code>em:ash-organic-plant-sludge</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：False；密封时间（游戏小时）：288。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 木灰<br><code>em:ash-organic-wood-dry</code> | 10 | 未声明附加限制 |
| 产物 | 木灰泥<br><code>em:ash-organic-wood-sludge</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：False；密封时间（游戏小时）：288。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 腐烂物<br><code>game:rot</code> | 10 升 | 未声明附加限制 |
| 产物 | 植物灰泥<br><code>em:ash-organic-plant-sludge</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 海藻灰<br><code>em:ash-organic-tang-dry</code> | 10 | 未声明附加限制 |
| 产物 | 海藻灰泥<br><code>em:ash-organic-tang-sludge</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：False；密封时间（游戏小时）：288。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "ash_plant_sludge",
    "enabled": false,
    "sealHours": 288,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "em:ash-organic-plant-dry",
        "quantity": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "em:ash-organic-plant-sludge",
      "quantity": 3
    }
  },
  {
    "code": "ash_wood_sludge",
    "enabled": false,
    "sealHours": 288,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "em:ash-organic-wood-dry",
        "quantity": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "em:ash-organic-wood-sludge",
      "quantity": 3
    }
  },
  {
    "code": "ash_rot_sludge",
    "enabled": false,
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "game:rot",
        "litres": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "em:ash-organic-plant-sludge",
      "quantity": 2
    }
  },
  {
    "code": "ash_tang_sludge",
    "enabled": false,
    "sealHours": 288,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "em:ash-organic-tang-dry",
        "quantity": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "em:ash-organic-tang-sludge",
      "quantity": 3
    }
  }
]
```

</details>

</details>

<details><summary>氢氧化钾溶液 · causticpotash</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 熟石灰<br><code>game:slakedlimeportion</code> | 3 升 | 未声明附加限制 |
| 投入 2 | 钾肥<br><code>game:potash</code> | 1 | 未声明附加限制 |
| 产物 | 氢氧化钾溶液<br><code>em:causticpotashportion</code> | 3 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "causticpotash",
    "ingredients": [
      {
        "type": "item",
        "code": "game:slakedlimeportion",
        "litres": 3
      },
      {
        "type": "item",
        "code": "game:potash",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:causticpotashportion",
      "litres": 3
    }
  }
]
```

</details>

</details>

<details><summary>烧碱液 · causticsoda</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 熟石灰<br><code>game:slakedlimeportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 纯碱<br><code>em:powdered-ore-soda</code> | 1 | 未声明附加限制 |
| 产物 | 烧碱液<br><code>em:causticsodaportion</code> | 1 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "causticsoda",
    "ingredients": [
      {
        "type": "item",
        "code": "game:slakedlimeportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "em:powdered-ore-soda",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:causticsodaportion",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · cleaning_pots</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 氢氧化钾溶液<br><code>em:causticpotashportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:dirtyclaypot-*-empty</code> | 1 | 允许变体：['blue', 'fire', 'black', 'brown', 'cream', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:claypot-{color}-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:dirtyclaypot-*-empty</code> | 1 | 允许变体：['blue', 'fire', 'black', 'brown', 'cream', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:claypot-{color}-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "cleaningpots",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticpotashportion",
        "name": "lye",
        "litres": 6,
        "consumeLitres": 2
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-*-empty",
        "name": "color",
        "allowedVariants": [
          "blue",
          "fire",
          "black",
          "brown",
          "cream",
          "gray",
          "orange",
          "red",
          "tan"
        ],
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-{color}-fired",
      "quantity": 1
    }
  },
  {
    "code": "cleaningpots",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "name": "lye",
        "litres": 6,
        "consumeLitres": 2
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-*-empty",
        "name": "color",
        "allowedVariants": [
          "blue",
          "fire",
          "black",
          "brown",
          "cream",
          "gray",
          "orange",
          "red",
          "tan"
        ],
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-{color}-fired",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>硫酸钴 · cobaltsulfate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸<br><code>game:acid-full-sulfuric</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉末状镍黄铁矿<br><code>em:powdered-ore-pentlandite</code> | 1 | 未声明附加限制 |
| 产物 | 硫酸钴<br><code>em:cobaltsulfateportion</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "cobaltsulfate",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "game:acid-full-sulfuric",
        "litres": 1
      },
      {
        "type": "item",
        "code": "em:powdered-ore-pentlandite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:cobaltsulfateportion",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>黑色皮革 · colored_leather</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸亚铁<br><code>game:sulfate-full-iron</code> | 3 升 | 未声明附加限制 |
| 投入 2 | 皮革<br><code>game:leather-normal-plain</code> | 1 | 未声明附加限制 |
| 产物 | 黑色皮革<br><code>game:leather-normal-black</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dyedleather",
    "enabled": true,
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-iron",
        "litres": 3,
        "consumeLitres": 3
      },
      {
        "type": "item",
        "code": "game:leather-normal-plain",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:leather-normal-black",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · curing_meat</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硝石盐水<br><code>em:dilutedsaltpeterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:*-raw</code> | 1 | 允许变体：['redmeat', 'poultry', 'bushmeat', 'fish'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:{meat}-cured</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；密封时间（游戏小时）：504。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "curedmeat",
    "enabled": false,
    "sealHours": 504,
    "ingredients": [
      {
        "type": "item",
        "code": "em:dilutedsaltpeterportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:*-raw",
        "quantity": 1,
        "name": "meat",
        "allowedVariants": [
          "redmeat",
          "poultry",
          "bushmeat",
          "fish"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:{meat}-cured",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · curing_vegetables</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硝石盐水<br><code>em:dilutedsaltpeterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 1 | 允许变体：['carrot', 'onion', 'parsnip', 'pumpkin', 'turnip', 'cabbage', 'olive'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:pickledvegetable-{vegetable}</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；密封时间（游戏小时）：384。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "pickledvegetable",
    "enabled": false,
    "sealHours": 384,
    "ingredients": [
      {
        "type": "item",
        "code": "em:dilutedsaltpeterportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:vegetable-*",
        "quantity": 1,
        "name": "vegetable",
        "allowedVariants": [
          "carrot",
          "onion",
          "parsnip",
          "pumpkin",
          "turnip",
          "cabbage",
          "olive"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:pickledvegetable-{vegetable}",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>硝石盐水 · diluted_saltpeter</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 硝石<br><code>game:saltpeter</code> | 1 | 未声明附加限制 |
| 产物 | 硝石盐水<br><code>em:dilutedsaltpeterportion</code> | 1 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dilutedsaltpeter",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:saltpeter",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:dilutedsaltpeterportion",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>稀释明矾 · dilutedalum</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 明矾粉<br><code>game:powder-alum</code> | 2 | 未声明附加限制 |
| 产物 | 稀释明矾<br><code>game:dilutedalumportion</code> | 5 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dilutedalum_powdered",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "item",
        "code": "game:powder-alum",
        "quantity": 2
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dilutedalumportion",
      "litres": 5
    }
  }
]
```

</details>

</details>

<details><summary>稀释锡石 · dilutedcassiterite</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锡<br><code>em:powdered-ore-cassiterite</code> | 2 | 未声明附加限制 |
| 产物 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 5 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dilutedcassiterite_powdered",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cassiterite",
        "quantity": 2
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dilutedcassiteriteportion",
      "litres": 5
    }
  }
]
```

</details>

</details>

<details><summary>稀释铬铁矿 · dilutedchromite</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 粉末状铬铁矿<br><code>em:powdered-ore-chromite</code> | 2 | 未声明附加限制 |
| 产物 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 5 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dilutedchromite_powdered",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "item",
        "code": "em:powdered-ore-chromite",
        "quantity": 2
      }
    ],
    "recipeGroup": 2,
    "output": {
      "type": "item",
      "code": "game:dilutedchromiteportion",
      "litres": 5
    }
  }
]
```

</details>

</details>

<details><summary>黑色染料 · black</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状磁铁矿<br><code>em:powdered-ore-magnetite</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状磁铁矿<br><code>em:powdered-ore-magnetite</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状磁铁矿<br><code>em:powdered-ore-magnetite</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状黑镁<br><code>em:powdered-ore-manganesedioxide</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状黑镁<br><code>em:powdered-ore-manganesedioxide</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状黑镁<br><code>em:powdered-ore-manganesedioxide</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 烧铜<br><code>em:powdered-ore-copperoxide</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 烧铜<br><code>em:powdered-ore-copperoxide</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 烧铜<br><code>em:powdered-ore-copperoxide</code> | 1 | 未声明附加限制 |
| 产物 | 黑色染料<br><code>game:dye-black</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-black-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-magnetite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-magnetite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-magnetite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganesedioxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganesedioxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganesedioxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-copperoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-copperoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  },
  {
    "code": "dye-black-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-copperoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-black",
      "litres": 2
    }
  }
]
```

</details>

</details>

<details><summary>蓝色染料、靛蓝染料 · blue</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 普鲁士蓝<br><code>em:powdered-ore-prussianblue</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 特纳蓝<br><code>em:powdered-ore-cobaltblue</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 特纳蓝<br><code>em:powdered-ore-cobaltblue</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 特纳蓝<br><code>em:powdered-ore-cobaltblue</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状镍<br><code>em:powdered-metal-nickel</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状镍<br><code>em:powdered-metal-nickel</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状镍<br><code>em:powdered-metal-nickel</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 古蓝<br><code>em:powdered-ore-cuprorivaite</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 古蓝<br><code>em:powdered-ore-cuprorivaite</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 古蓝<br><code>em:powdered-ore-cuprorivaite</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 青金石粉<br><code>game:powder-lapislazuli</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 青金石粉<br><code>game:powder-lapislazuli</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 青金石粉<br><code>game:powder-lapislazuli</code> | 1 | 未声明附加限制 |
| 产物 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 靛蓝粉<br><code>em:powdered-ore-indigo</code> | 1 | 未声明附加限制 |
| 产物 | 靛蓝染料<br><code>game:dye-woad</code> | 2 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-prussianblue",
    "comment": "keep this index 0 to easily patch it. Very strong, deep blue.",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-prussianblue",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cobaltblue",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cobaltblue",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cobaltblue",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-metal-nickel",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-metal-nickel",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-metal-nickel",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cuprorivaite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cuprorivaite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cuprorivaite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-alum",
    "name": "dye-blue-lapis-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-lapislazuli",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-cassiterite",
    "name": "dye-blue-lapis-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-lapislazuli",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-chromite",
    "name": "dye-blue-lapis-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-lapislazuli",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-blue",
      "litres": 2
    }
  },
  {
    "code": "dye-blue-indigo",
    "sealHours": 4,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-indigo",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-woad",
      "litres": 2
    }
  }
]
```

</details>

</details>

<details><summary>灰色染料 · gray</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 8 升 | 未声明附加限制 |
| 投入 2 | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 1 | 未声明附加限制 |
| 产物 | 灰色染料<br><code>game:dye-gray</code> | 8 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 8 升 | 未声明附加限制 |
| 投入 2 | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 1 | 未声明附加限制 |
| 产物 | 灰色染料<br><code>game:dye-gray</code> | 8 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 8 升 | 未声明附加限制 |
| 投入 2 | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 1 | 未声明附加限制 |
| 产物 | 灰色染料<br><code>game:dye-gray</code> | 8 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-gray-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 8
      },
      {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-gray",
      "litres": 8
    }
  },
  {
    "code": "dye-gray-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 8
      },
      {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-gray",
      "litres": 8
    }
  },
  {
    "code": "dye-gray-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 8
      },
      {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-gray",
      "litres": 8
    }
  }
]
```

</details>

</details>

<details><summary>绿色染料 · green</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铬绿<br><code>em:powdered-ore-chromiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铬绿<br><code>em:powdered-ore-chromiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 石灰水<br><code>game:limewaterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铬绿<br><code>em:powdered-ore-chromiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释硼砂<br><code>game:dilutedboraxportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铬绿<br><code>em:powdered-ore-chromiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锰<br><code>em:powdered-ore-manganeseoxide</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锰<br><code>em:powdered-ore-manganeseoxide</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锰<br><code>em:powdered-ore-manganeseoxide</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉绿<br><code>em:powdered-ore-cadmiumgreen</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉绿<br><code>em:powdered-ore-cadmiumgreen</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉绿<br><code>em:powdered-ore-cadmiumgreen</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 钴绿<br><code>em:powdered-ore-cobaltgreen</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 钴绿<br><code>em:powdered-ore-cobaltgreen</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 石灰水<br><code>game:limewaterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 钴绿<br><code>em:powdered-ore-cobaltgreen</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-green-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-chromiumoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-chromiumoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-limewater",
    "ingredients": [
      {
        "type": "item",
        "code": "game:limewaterportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-chromiumoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-dilutedborax",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedboraxportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-chromiumoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-manganese-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganeseoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-manganese-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganeseoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-manganese-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganeseoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumgreen",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumgreen",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumgreen",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cobaltgreen",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cobaltgreen",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  },
  {
    "code": "dye-green-limewater",
    "ingredients": [
      {
        "type": "item",
        "code": "game:limewaterportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cobaltgreen",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 2
    }
  }
]
```

</details>

</details>

<details><summary>橙色染料 · orange</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状铝土矿<br><code>em:powdered-stone-bauxite</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状铝土矿<br><code>em:powdered-stone-bauxite</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状铝土矿<br><code>em:powdered-stone-bauxite</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 黄色染料<br><code>game:dye-yellow</code> | 8 升 | 未声明附加限制 |
| 投入 2 | 粉状铝土矿<br><code>em:powdered-stone-bauxite</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 8 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 黄色染料<br><code>game:dye-yellow</code> | 8 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 1 | 允许变体：['hematite', 'litharge', 'cadmiumselenide'] |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 8 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 黄色染料<br><code>game:dye-yellow</code> | 8 升 | 未声明附加限制 |
| 投入 2 | 朱砂粉<br><code>game:powder-cinnabar</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 8 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 氧化铁粉<br><code>game:powder-iron-oxide</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 氧化铁粉<br><code>game:powder-iron-oxide</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 氧化铁粉<br><code>game:powder-iron-oxide</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 黄色染料<br><code>game:dye-yellow</code> | 8 升 | 未声明附加限制 |
| 投入 2 | 氧化铁粉<br><code>game:powder-iron-oxide</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 8 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉橙<br><code>em:powdered-ore-cadmiumsulfoselenide</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉橙<br><code>em:powdered-ore-cadmiumsulfoselenide</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉橙<br><code>em:powdered-ore-cadmiumsulfoselenide</code> | 1 | 未声明附加限制 |
| 产物 | 橙色染料<br><code>game:dye-orange</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-orange-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-stone-bauxite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-stone-bauxite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-stone-bauxite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-yellow",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-yellow",
        "litres": 8
      },
      {
        "type": "item",
        "code": "em:powdered-stone-bauxite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 8
    }
  },
  {
    "code": "dye-orange-yellow",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-yellow",
        "litres": 8
      },
      {
        "type": "item",
        "code": "em:powdered-ore-*",
        "name": "ore",
        "quantity": 1,
        "allowedVariants": [
          "hematite",
          "litharge",
          "cadmiumselenide"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 8
    }
  },
  {
    "code": "dye-orange-yellow",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-yellow",
        "litres": 8
      },
      {
        "type": "item",
        "code": "game:powder-cinnabar",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 8
    }
  },
  {
    "code": "dye-orange-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-iron-oxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-iron-oxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-iron-oxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-yellow",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-yellow",
        "litres": 8
      },
      {
        "type": "item",
        "code": "game:powder-iron-oxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 8
    }
  },
  {
    "code": "dye-orange-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfoselenide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfoselenide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  },
  {
    "code": "dye-orange-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfoselenide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-orange",
      "litres": 2
    }
  }
]
```

</details>

</details>

<details><summary>粉色染料 · pink</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状菱锰矿<br><code>em:powdered-ore-rhodochrosite</code> | 1 | 未声明附加限制 |
| 产物 | 粉色染料<br><code>game:dye-pink</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状菱锰矿<br><code>em:powdered-ore-rhodochrosite</code> | 1 | 未声明附加限制 |
| 产物 | 粉色染料<br><code>game:dye-pink</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状菱锰矿<br><code>em:powdered-ore-rhodochrosite</code> | 1 | 未声明附加限制 |
| 产物 | 粉色染料<br><code>game:dye-pink</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-pink-alum",
    "name": "dye-pink-rhodochrosite-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-rhodochrosite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-pink",
      "litres": 2
    }
  },
  {
    "code": "dye-pink-cassiterite",
    "name": "dye-pink-rhodochrosite-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-rhodochrosite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-pink",
      "litres": 2
    }
  },
  {
    "code": "dye-pink-chromite",
    "name": "dye-pink-rhodochrosite-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-rhodochrosite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-pink",
      "litres": 2
    }
  }
]
```

</details>

</details>

<details><summary>紫色染料 · purple</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状镍<br><code>em:powdered-metal-nickel</code> | 1 | 未声明附加限制 |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 青金石粉<br><code>game:powder-lapislazuli</code> | 1 | 未声明附加限制 |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 1 | 允许变体：['cobaltblue', 'cuprorivaite', 'indigo', 'prussianblue'] |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 1 | 允许变体：['hematite', 'litharge', 'cadmiumselenide'] |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蓝色染料<br><code>game:dye-blue</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 朱砂粉<br><code>game:powder-cinnabar</code> | 1 | 未声明附加限制 |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 1 | 允许变体：['hematite', 'litharge', 'cadmiumselenide'] |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 朱砂粉<br><code>game:powder-cinnabar</code> | 1 | 未声明附加限制 |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 锰紫<br><code>em:powdered-ore-manganeseviolet</code> | 1 | 未声明附加限制 |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 4 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 锰紫<br><code>em:powdered-ore-manganeseviolet</code> | 1 | 未声明附加限制 |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 4 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 锰紫<br><code>em:powdered-ore-manganeseviolet</code> | 1 | 未声明附加限制 |
| 产物 | 紫色染料<br><code>game:dye-purple</code> | 4 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-purple-red",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-red",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-metal-nickel",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 2
    }
  },
  {
    "code": "dye-purple-red",
    "name": "dye-purple-red-lapis",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-red",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-lapislazuli",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 2
    }
  },
  {
    "code": "dye-purple-red",
    "name": "dye-purple-red-blue-pigments",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-red",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-*",
        "name": "blue",
        "quantity": 1,
        "allowedVariants": [
          "cobaltblue",
          "cuprorivaite",
          "indigo",
          "prussianblue"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 2
    }
  },
  {
    "code": "dye-purple-blue",
    "name": "dye-purple-blue-litharge",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-blue",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-*",
        "name": "red",
        "quantity": 1,
        "allowedVariants": [
          "hematite",
          "litharge",
          "cadmiumselenide"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 2
    }
  },
  {
    "code": "dye-purple-blue",
    "name": "dye-purple-blue-cinnabar",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-blue",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-cinnabar",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 2
    }
  },
  {
    "code": "dye-purple-woad-blue",
    "name": "dye-purple-woad-blue-litharge",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-*",
        "name": "red",
        "quantity": 1,
        "allowedVariants": [
          "hematite",
          "litharge",
          "cadmiumselenide"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 2
    }
  },
  {
    "code": "dye-purple-woad-blue",
    "name": "dye-purple-woad-blue-cinnabar",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:powder-cinnabar",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 2
    }
  },
  {
    "code": "dye-purple-alum",
    "comment": "very strong purple pigment",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 4
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganeseviolet",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 4
    }
  },
  {
    "code": "dye-purple-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 4
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganeseviolet",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 4
    }
  },
  {
    "code": "dye-purple-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 4
      },
      {
        "type": "item",
        "code": "em:powdered-ore-manganeseviolet",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-purple",
      "litres": 4
    }
  }
]
```

</details>

</details>

<details><summary>红色染料 · red</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 一氧化铅<br><code>em:powdered-ore-litharge</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状赤铁矿<br><code>em:powdered-ore-hematite</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 一氧化铅<br><code>em:powdered-ore-litharge</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状赤铁矿<br><code>em:powdered-ore-hematite</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 一氧化铅<br><code>em:powdered-ore-litharge</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状赤铁矿<br><code>em:powdered-ore-hematite</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉红<br><code>em:powdered-ore-cadmiumselenide</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉红<br><code>em:powdered-ore-cadmiumselenide</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉红<br><code>em:powdered-ore-cadmiumselenide</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 3 升 | 未声明附加限制 |
| 投入 2 | 硫酸钴<br><code>em:powdered-ore-cobaltsulfate</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 3 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-red-alum",
    "name": "dye-red-litharge-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-litharge",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-alum",
    "name": "dye-red-hematite-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-hematite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-cassiterite",
    "name": "dye-red-litharge-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-litharge",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-cassiterite",
    "name": "dye-red-hematite-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-hematite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-chromite",
    "name": "dye-red-litharge-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-litharge",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-chromite",
    "name": "dye-red-hematite-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-hematite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumselenide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumselenide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumselenide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 2
    }
  },
  {
    "code": "dye-red",
    "name": "dye-red-cobaltsulfate",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 3
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cobaltsulfate",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 3
    }
  }
]
```

</details>

</details>

<details><summary>白色染料 · white</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释硼砂<br><code>game:dilutedboraxportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 硼砂粉<br><code>game:powder-borax</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 10 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锡<br><code>em:powdered-ore-cassiterite</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释硼砂<br><code>game:dilutedboraxportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锡<br><code>em:powdered-ore-cassiterite</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锡<br><code>em:powdered-ore-cassiterite</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 白铅<br><code>em:powdered-ore-whitelead</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释硼砂<br><code>game:dilutedboraxportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 白铅<br><code>em:powdered-ore-whitelead</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 白铅<br><code>em:powdered-ore-whitelead</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锌<br><code>em:powdered-ore-zincoxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释硼砂<br><code>game:dilutedboraxportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锌<br><code>em:powdered-ore-zincoxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状氧化锌<br><code>em:powdered-ore-zincoxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 白镁氧<br><code>em:powdered-ore-magnesiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释硼砂<br><code>game:dilutedboraxportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 白镁氧<br><code>em:powdered-ore-magnesiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 白镁氧<br><code>em:powdered-ore-magnesiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状二氧化钛<br><code>em:powdered-ore-titaniumdioxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释硼砂<br><code>game:dilutedboraxportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状二氧化钛<br><code>em:powdered-ore-titaniumdioxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状二氧化钛<br><code>em:powdered-ore-titaniumdioxide</code> | 1 | 未声明附加限制 |
| 产物 | 白色染料<br><code>game:dye-white</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-white-borax",
    "comment": "original white dye was 2:1 water:borax, dilutedborax is 5:2 (or 10:4) water:borax, so add 1 for 10L, making it 10:5 water:borax for the dye again",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedboraxportion",
        "litres": 10
      },
      {
        "type": "item",
        "code": "game:powder-borax",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 10
    }
  },
  {
    "code": "dye-white-tin",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cassiterite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-tin",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedboraxportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cassiterite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-tin",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cassiterite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-lead",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-whitelead",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-lead",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedboraxportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-whitelead",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-lead",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-whitelead",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-zinc",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-zincoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-zinc",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedboraxportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-zincoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-zinc",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-zincoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-magnesium",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-magnesiumoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-magnesium",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedboraxportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-magnesiumoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-magnesium",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-magnesiumoxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-titaniumdioxide",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-titaniumdioxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-titaniumdioxide",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedboraxportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-titaniumdioxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  },
  {
    "code": "dye-white-titaniumdioxide",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-titaniumdioxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-white",
      "litres": 2
    }
  }
]
```

</details>

</details>

<details><summary>黄色染料 · yellow</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铅黄<br><code>em:powdered-ore-massicot</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状褐铁矿<br><code>em:powdered-ore-limonite</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铅黄<br><code>em:powdered-ore-massicot</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状褐铁矿<br><code>em:powdered-ore-limonite</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铅黄<br><code>em:powdered-ore-massicot</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉末状褐铁矿<br><code>em:powdered-ore-limonite</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 苦味酸<br><code>em:powdered-ore-picricacid</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉黄<br><code>em:powdered-ore-cadmiumsulfide</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉黄<br><code>em:powdered-ore-cadmiumsulfide</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 镉黄<br><code>em:powdered-ore-cadmiumsulfide</code> | 1 | 未声明附加限制 |
| 产物 | 黄色染料<br><code>game:dye-yellow</code> | 2 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dye-yellow-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-massicot",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-limonite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-massicot",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-limonite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-massicot",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-limonite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-picric",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-picricacid",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-alum",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-cassiterite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  },
  {
    "code": "dye-yellow-chromite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 2
      },
      {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-yellow",
      "litres": 2
    }
  }
]
```

</details>

</details>

<details><summary>硫酸钙、白色石膏块 · gypsum</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 石灰<br><code>game:lime</code> | 1 | 未声明附加限制 |
| 产物 | 硫酸钙<br><code>game:sulfate-full-calcium</code> | 2 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 石膏粉<br><code>em:powdered-ore-gypsum</code> | 4 | 未声明附加限制 |
| 产物 | 白色石膏块<br><code>game:plaster-plain</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：1。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "aqueous-gypsum",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:lime",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:sulfate-full-calcium",
      "litres": 2
    }
  },
  {
    "code": "plaster",
    "comment": "Plaster in VS is lime plaster, this should be a different block.",
    "sealHours": 1,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "em:powdered-ore-gypsum",
        "quantity": 4
      }
    ],
    "output": {
      "type": "block",
      "code": "game:plaster-plain",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>粉末状赤铁矿 · hematite</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 盐酸<br><code>game:acid-full-hydrochloric</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 氧化铁粉<br><code>game:powder-iron-oxide</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状赤铁矿<br><code>em:powdered-ore-hematite</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "sealHours": 12,
    "code": "hematite",
    "comment": "iron pickling => iron(II) chloride + spent acid + oxygen => hematite + acid. So Fe3O4 + Fe + 8 HCl → 4 FeCl2 + 4 H2O => 4 FeCl2 + 4 H2O + O2 → 8 HCl + 2 Fe2O3. We 'consume' 25% of the acid as to avoid an endless loop.",
    "ingredients": [
      {
        "type": "item",
        "code": "game:acid-full-hydrochloric",
        "litres": 1,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "game:powder-iron-oxide",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-hematite",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>四水硼砂溶液、硼砂 · kernite_to_borax</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉末状四水硼砂<br><code>em:powdered-ore-kernite</code> | 2 | 未声明附加限制 |
| 产物 | 四水硼砂溶液<br><code>em:dilutedkerniteportion</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 四水硼砂溶液<br><code>em:dilutedkerniteportion</code> | 1 升 | 未声明附加限制 |
| 产物 | 硼砂<br><code>game:ore-borax</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：288。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "dilutedkernite",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "em:powdered-ore-kernite",
        "quantity": 2
      }
    ],
    "sealHours": 8,
    "output": {
      "type": "item",
      "code": "em:dilutedkerniteportion",
      "litres": 1
    }
  },
  {
    "code": "kernite-to-borax",
    "ingredients": [
      {
        "type": "item",
        "code": "em:dilutedkerniteportion",
        "litres": 1
      }
    ],
    "sealHours": 288,
    "output": {
      "type": "item",
      "code": "game:ore-borax",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>粉末状黑镁 · magnesia_nigra</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硝酸<br><code>game:acid-full-nitric</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉末状菱锰矿<br><code>em:powdered-ore-rhodochrosite</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状黑镁<br><code>em:powdered-ore-manganesedioxide</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "sealHours": 72,
    "code": "dilutedsaltpeter",
    "comment": "Should be a cooking recipe, but powdered rhodochrosite has a conv. temp and therefore cannot be used due to a VS bug in upto 1.21",
    "ingredients": [
      {
        "type": "item",
        "code": "game:acid-full-nitric",
        "litres": 1
      },
      {
        "type": "item",
        "code": "em:powdered-ore-rhodochrosite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-manganesedioxide",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>粉末状氢氧化镁 · magnesiumhydroxide</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 海水<br><code>game:saltwaterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 生石灰<br><code>game:quicklime</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状氢氧化镁<br><code>em:powdered-ore-magnesiumhydroxide</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "sealHours": 8,
    "code": "magnesiumhydroxide",
    "comment": "Should be slaked lime + salt water, but mixing two liquids in a barrel is not possible.",
    "ingredients": [
      {
        "type": "item",
        "code": "game:saltwaterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-magnesiumhydroxide",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>媒染布料 · mordantcloth</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸铜<br><code>game:sulfate-full-copper</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 布料<br><code>game:cloth-plain</code> | 1 | 未声明附加限制 |
| 产物 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸亚铁<br><code>game:sulfate-full-iron</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 布料<br><code>game:cloth-plain</code> | 1 | 未声明附加限制 |
| 产物 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 布料<br><code>game:cloth-plain</code> | 1 | 未声明附加限制 |
| 产物 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 布料<br><code>game:cloth-plain</code> | 1 | 未声明附加限制 |
| 产物 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "mordantclothcopper",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-copper",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:cloth-plain",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-mordant",
      "stackSize": 1
    }
  },
  {
    "code": "mordantclothiron",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-iron",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:cloth-plain",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-mordant",
      "stackSize": 1
    }
  },
  {
    "code": "mordantclothzinc",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:cloth-plain",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-mordant",
      "stackSize": 1
    }
  },
  {
    "code": "mordantclothsoda",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:cloth-plain",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-mordant",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>氧化铁粉 · rust</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 铁粉<br><code>game:powder-iron-raw</code> | 1 | 未声明附加限制 |
| 产物 | 氧化铁粉<br><code>game:powder-iron-oxide</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "rust",
    "sealHours": 48,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "game:powder-iron-raw",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:powder-iron-oxide",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>小型浸渍兽皮、中型浸渍兽皮、大型浸渍兽皮、巨型浸渍兽皮 · soaking_hides</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-*-small</code> | 1 | 允许变体：['raw', 'salted'] |
| 产物 | 小型浸渍兽皮<br><code>game:hide-soaked-small</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-*-medium</code> | 1 | 允许变体：['raw', 'salted'] |
| 产物 | 中型浸渍兽皮<br><code>game:hide-soaked-medium</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-*-large</code> | 1 | 允许变体：['raw', 'salted'] |
| 产物 | 大型浸渍兽皮<br><code>game:hide-soaked-large</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-*-huge</code> | 1 | 允许变体：['raw', 'salted'] |
| 产物 | 巨型浸渍兽皮<br><code>game:hide-soaked-huge</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-*-small",
        "name": "type",
        "quantity": 1,
        "allowedVariants": [
          "raw",
          "salted"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-small",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-*-medium",
        "name": "type",
        "quantity": 1,
        "allowedVariants": [
          "raw",
          "salted"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-medium",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-*-large",
        "name": "type",
        "quantity": 1,
        "allowedVariants": [
          "raw",
          "salted"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-large",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-*-huge",
        "name": "type",
        "quantity": 1,
        "allowedVariants": [
          "raw",
          "salted"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-huge",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · soaking_hides_lye</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 烧碱液<br><code>em:causticsodaportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelye",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticsodaportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · soaking_hides_soda_lye</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "soakedhidewashingsoda",
    "comment": "longer seal time than caustic soda lye, since weaker",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidewashingsoda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidewashingsoda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidewashingsoda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidewashingsoda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidewashingsoda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidewashingsoda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidewashingsoda",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · soaking_hides_sulfate</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸锌<br><code>game:sulfate-full-zinc</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：16。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidezincsulfate",
    "sealHours": 16,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-zinc",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>粉末状孔雀石 · verdigris</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 碎铜<br><code>em:crushed-metal-copper</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状孔雀石<br><code>em:powdered-ore-malachite</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：168。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 铜箭头<br><code>game:arrowhead-copper</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状孔雀石<br><code>em:powdered-ore-malachite</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 铜矛头<br><code>game:spearhead-copper</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状孔雀石<br><code>em:powdered-ore-malachite</code> | 4 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 洗涤碱<br><code>em:washingsodaportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 铜鳞片<br><code>game:metalscale-copper</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状孔雀石<br><code>em:powdered-ore-malachite</code> | 6 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 硫酸铜<br><code>game:sulfate-full-copper</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 石灰<br><code>game:lime</code> | 1 | 未声明附加限制 |
| 产物 | 粉末状孔雀石<br><code>em:powdered-ore-malachite</code> | 2 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "verdigris",
    "enabled": true,
    "sealHours": 168,
    "comment": "From: https://en.wikipedia.org/wiki/Verdigris The industry there was long dominated by women, with verdigris manufactured in household cellars using copper plates stacked in clay pots that were filled with distilled wine.[15] The acid in the grapes caused the copper to develop crystals. The crystals ripened into verdigris and were scraped off when matured.",
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "em:crushed-metal-copper",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-malachite",
      "quantity": 2
    }
  },
  {
    "code": "verdigris-arrow",
    "enabled": true,
    "sealHours": 336,
    "comment": "game:ciderportion-* does not work, wildcards in barrel recipes are broken. vinegar does work but cannot be crafted in survival",
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "game:arrowhead-copper",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-malachite",
      "quantity": 2
    }
  },
  {
    "code": "verdigris-spear",
    "enabled": true,
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 2,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:spearhead-copper",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-malachite",
      "quantity": 4
    }
  },
  {
    "code": "verdigris-scale",
    "enabled": true,
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "em:washingsodaportion",
        "litres": 4,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:metalscale-copper",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-malachite",
      "quantity": 6
    }
  },
  {
    "code": "malachite-powder",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "game:sulfate-full-copper",
        "litres": 2
      },
      {
        "type": "item",
        "code": "game:lime",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-malachite",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>洗涤碱 · washingsoda</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 纯碱<br><code>em:powdered-ore-soda</code> | 1 | 未声明附加限制 |
| 产物 | 洗涤碱<br><code>em:washingsodaportion</code> | 10 升 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "washingsoda",
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "item",
        "code": "em:powdered-ore-soda",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:washingsodaportion",
      "litres": 10
    }
  }
]
```

</details>

</details>

<details><summary>黄饼 · yellowcake</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 氢氧化钾溶液<br><code>em:causticpotashportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 粉状铀<br><code>em:powdered-metal-uranium</code> | 1 | 未声明附加限制 |
| 产物 | 黄饼<br><code>em:powdered-ore-yellowcake</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：54。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "causticpotash",
    "sealHours": 54,
    "comment": "Technically, this should produce wet yellowcake, which needs to be dried with heat to produce the final result.",
    "ingredients": [
      {
        "type": "item",
        "code": "em:causticpotashportion",
        "litres": 2,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "em:powdered-metal-uranium",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "em:powdered-ore-yellowcake",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · alum</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>alunite</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>potassium</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>sulphuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "alum",
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
        "code": "game:crushed-alum"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "alunite",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:crushed-bauxite"
          }
        ]
      },
      {
        "code": "potassium",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:potash"
          }
        ]
      },
      {
        "code": "sulphuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:crushed-alum",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · antiseptics</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sulfuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>potash</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>iodine</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**加工条件：** 配方开关：True。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "iodine",
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
        "code": "em:powdered-ore-iodine"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "sulfuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "bowl/water"
          }
        ]
      },
      {
        "code": "potash",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:potash"
          }
        ]
      },
      {
        "code": "iodine",
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:rot",
            "shapeElement": "bowl/water"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-iodine",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · blue_pigments</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>woaddye</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>lime</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>copper</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>quartz</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 4 | 名称未汉化（见物品代码）<br><code>alkali</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>cyanide</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>potassium</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>iron</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sulfate</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>aluminum</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>flux</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "indigo",
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
        "code": "em:powdered-ore-indigo"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "woaddye",
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:dye-woad",
            "shapeElement": "bowl/water"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-indigo",
      "quantity": 1
    }
  },
  {
    "code": "egyptianblue",
    "comment": "it should be much more quartz then the others, but that would restrict the output too much due to cooking pot size. Should also use copperoxide, but this cant be used in cooking due to the melting temp.",
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
        "code": "em:powdered-ore-cuprorivaite"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "lime",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:limewaterportion",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "copper",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-metal-copper"
          }
        ]
      },
      {
        "code": "quartz",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-ore-quartz",
            "quantity": 2
          }
        ]
      },
      {
        "code": "alkali",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-ore-soda"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-cuprorivaite",
      "quantity": 2
    }
  },
  {
    "code": "prussianblue",
    "comment": "Should use ferros ferrocyanide salts. We use iron-sulfate as a standin. Yeah, I know...",
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
        "code": "em:powdered-ore-prussianblue"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "cyanide",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.5,
        "validStacks": [
          {
            "type": "item",
            "code": "game:sulfate-full-iron",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "potassium",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.5,
        "validStacks": [
          {
            "type": "item",
            "code": "em:causticpotashportion",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "iron",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-iron-raw"
          },
          {
            "type": "item",
            "code": "game:powder-iron-oxide"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-prussianblue",
      "quantity": 1
    }
  },
  {
    "code": "cobaltblue",
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
        "code": "em:powdered-ore-cobaltblue"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "sulfate",
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:cobaltsulfateportion",
            "shapeElement": "bowl/water"
          }
        ]
      },
      {
        "code": "aluminum",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:crushed-bauxite"
          }
        ]
      },
      {
        "code": "flux",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-sylvite"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-cobaltblue",
      "quantity": 3
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · cadmiumsulfide</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>iron</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sulphuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "cadmiumsulfide",
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
        "code": "em:powdered-ore-cadmiumsulfide"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "iron",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:crushed-sphalerite"
          }
        ]
      },
      {
        "code": "sulphuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:sulfate-full-iron",
            "shapeElement": "bowl/water"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-cadmiumsulfide",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · cobaltsulfate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sulphuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "cobaltsulfate",
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
        "code": "em:powdered-ore-cobaltsulfate"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "sulphuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:cobaltsulfateportion",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-cobaltsulfate",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · coppersulfate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>copper</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sulphuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "coppersulfate",
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
        "code": "game:sulfate-full-copper"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "copper",
        "minQuantity": 3,
        "maxQuantity": 3,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-metal-copper"
          }
        ]
      },
      {
        "code": "sulphuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:sulfate-full-copper",
      "quantity": 100
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · green_pigments</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sulfate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>chromium</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>aluminum</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 4 | 名称未汉化（见物品代码）<br><code>flux</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "cobaltgreen",
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
        "code": "em:powdered-ore-cobaltblue"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "sulfate",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:cobaltsulfateportion",
            "shapeElement": "bowl/water"
          }
        ]
      },
      {
        "code": "chromium",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:crushed-chromite"
          }
        ]
      },
      {
        "code": "aluminum",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:crushed-bauxite"
          }
        ]
      },
      {
        "code": "flux",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-sylvite"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-cobaltgreen",
      "quantity": 3
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · gypsum</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>liqud</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "gypsum",
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
        "code": "game:sulfate-full-calcium"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "liqud",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:sulfate-full-calcium",
            "shapeElement": "game:bowl/water"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-gypsum",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · hydrochloricacid</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>saltpeter</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>alum</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>salt</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 4 | 名称未汉化（见物品代码）<br><code>sulfate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "hydrochloricacid",
    "comment": "Take equal parts of sweet salt, Bitter salt, Ṭabarzad salt, Andarānī salt, Indian salt, salt of Al-Qilī, and salt of Urine. After adding an equal weight of good crystallised Sal-ammoniac, dissolve by moisture, and distil (the mixture). There will distil over a strong water, which will cleave stone (sakhr) instantly.",
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
        "code": "game:acid-full-hydrochloric"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "saltpeter",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:saltpeter",
            "quantity": 1
          }
        ]
      },
      {
        "code": "alum",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-alum"
          }
        ]
      },
      {
        "code": "salt",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:salt"
          }
        ]
      },
      {
        "code": "sulfate",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:sulfate-full-copper",
            "shapeElement": "bowl/water"
          },
          {
            "type": "item",
            "code": "game:sulfate-full-iron",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:acid-full-hydrochloric",
      "quantity": 100
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · ironsulfate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>iron</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sulphuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "ironsulfate",
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
        "code": "game:sulfate-full-iron"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "iron",
        "minQuantity": 3,
        "maxQuantity": 3,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-iron-raw"
          }
        ]
      },
      {
        "code": "sulphuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:sulfate-full-iron",
      "quantity": 100
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · lead_oxide</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sulfur</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>lead</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "lead_oxide",
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
        "code": "em:powdered-ore-galena"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "sulfur",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "lead",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-metal-lead"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-galena",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · magnesiumhydroxide</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>seawater</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>limewater</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "magnesiumhydroxide",
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
        "code": "em:powdered-ore-magnesiumhydroxide"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "seawater",
        "validStacks": [
          {
            "type": "item",
            "code": "game:saltwaterportion",
            "shapeElement": "bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "limewater",
        "validStacks": [
          {
            "type": "item",
            "code": "game:slakedlimeportion",
            "shapeElement": "bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-magnesiumhydroxide",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · manganeseviolet</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sulfur</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>manganese</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>phosphor</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 4 | 名称未汉化（见物品代码）<br><code>nitrogen_carbon</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "manganeseviolet",
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
        "code": "em:powdered-ore-manganeseviolet"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "sulfur",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "manganese",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:crushed-ore-rhodochrosite"
          }
        ]
      },
      {
        "code": "phosphor",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:crushed-ore-phosphorite"
          }
        ]
      },
      {
        "code": "nitrogen_carbon",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:rot"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-manganeseviolet",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · mercury</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 4 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>cinnabar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "mercury1",
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
        "code": "em:mercuryportion"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:mercuryportion",
      "quantity": 10
    }
  },
  {
    "code": "mercury1",
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
        "code": "em:mercuryportion"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      },
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:mercuryportion",
      "quantity": 20
    }
  },
  {
    "code": "mercury1",
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
        "code": "em:mercuryportion"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      },
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      },
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:mercuryportion",
      "quantity": 30
    }
  },
  {
    "code": "mercury1",
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
        "code": "em:mercuryportion"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      },
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      },
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      },
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-cinnabar"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:mercuryportion",
      "quantity": 40
    }
  },
  {
    "code": "mercury2",
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
        "code": "em:mercuryportion"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "cinnabar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:crushed-cinnabar"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:mercuryportion",
      "quantity": 20
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · nitricacid</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>saltpeter</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>alum</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>coppersulfate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>saltpeter</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>alum</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>coppersulfate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "nitricacid",
    "comment": "Take five parts of pure flowers of nitre, three parts of Cyprus vitriol and two parts of Yemen alum. Powder them well, separately, until they are like dust and then place them in a flask. Plug the latter with a palm fibre and attach a glass receiver to it. Then invert the apparatus and heat the upper portion (i.e. the flask containing the mixture) with a gentle fire. There will flow down by reason of the heat an oil like cow's butter.",
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
        "code": "game:acid-full-nitric"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "saltpeter",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:saltpeter",
            "quantity": 5
          }
        ]
      },
      {
        "code": "alum",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:crushed-alum"
          }
        ]
      },
      {
        "code": "coppersulfate",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:sulfate-full-copper",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 3
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:acid-full-nitric",
      "quantity": 250
    }
  },
  {
    "code": "nitricacid",
    "comment": "slightly more efficient, because you need to grind the alum.",
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
        "code": "game:acid-full-nitric"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "saltpeter",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:saltpeter",
            "quantity": 5
          }
        ]
      },
      {
        "code": "alum",
        "minQuantity": 2,
        "maxQuantity": 2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:powder-alum"
          }
        ]
      },
      {
        "code": "coppersulfate",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:sulfate-full-copper",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 3
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:acid-full-nitric",
      "quantity": 300
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · picricacid</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>nitricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>indigo</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>nitricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>resin</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "picricacid",
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
        "code": "em:powdered-ore-picricacid"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "nitricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.5,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-nitric",
            "shapeElement": "bowl/water"
          }
        ]
      },
      {
        "code": "indigo",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-ore-indigo"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-picricacid",
      "quantity": 1
    }
  },
  {
    "code": "picricacid",
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
        "code": "em:powdered-ore-picricacid"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "nitricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.5,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-nitric",
            "shapeElement": "bowl/water"
          }
        ]
      },
      {
        "code": "resin",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:resin"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-picricacid",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · pitch_glue</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 粉末状煤<br><code>em:powdered-ore-coal</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "glueportion-pitch-hot",
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
        "code": "game:glueportion-pitch-cold"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "game:resin",
        "validStacks": [
          {
            "type": "item",
            "code": "game:resin"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      },
      {
        "code": "em:powdered-ore-coal",
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-ore-coal",
            "quantity": 2
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:glueportion-pitch-hot",
      "quantity": 100
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · saltpeter</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>nitricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>potassiumhydroxide</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "saltpeter",
    "enabled": false,
    "comment": "Potassium nitrate can also be produced by neutralizing nitric acid with potassium hydroxide. This reaction is highly exothermic. Which basically means you should cool, not cook it, but VS does not allow mixing of two liquids in a barrel...",
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
        "code": "game:saltpeter"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "nitricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-nitric",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      },
      {
        "code": "potassiumhydroxide",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:causticpotashportion",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:saltpeter",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · soda</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>saltbrine</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>lime</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>saltpeter</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>seawater</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>lime</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>saltpeter</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>saltpeter</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>salt</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>lime</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "soda",
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
        "code": "em:powdered-ore-soda"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "saltbrine",
        "minQuantity": 2,
        "maxQuantity": 2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:brineportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "portionSizeLitres": 1
      },
      {
        "code": "lime",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:limewaterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "portionSizeLitres": 1
      },
      {
        "code": "saltpeter",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:saltpeter"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-soda",
      "quantity": 1
    }
  },
  {
    "code": "soda_sea",
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
        "code": "em:powdered-ore-soda"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "seawater",
        "minQuantity": 2,
        "maxQuantity": 2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:saltwaterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "portionSizeLitres": 1
      },
      {
        "code": "lime",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:limewaterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "portionSizeLitres": 1
      },
      {
        "code": "saltpeter",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:saltpeter"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-soda",
      "quantity": 1
    }
  },
  {
    "code": "soda_saltpeterbrine",
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
        "code": "em:powdered-ore-soda"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "saltpeter",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:dilutedsaltpeterportion",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      },
      {
        "code": "salt",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:salt"
          }
        ]
      },
      {
        "code": "lime",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:limewaterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "portionSizeLitres": 1
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

<details><summary>特殊配方 · titaniumdioxide</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>titanium</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sulphuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "coppersulfate",
    "comment": "Should return sulfate-full-iron but that does not yet work in VS.",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 96
      },
      "transitionHours": {
        "avg": 96
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "em:powdered-ore-titaniumdioxide"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "titanium",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-ore-ilmenite"
          }
        ]
      },
      {
        "code": "sulphuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "bowl/water"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-titaniumdioxide",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · verdigris</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>coppersulfate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>causticsoda</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "copperhydroxide",
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
        "code": "em:powdered-ore-malachite"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "coppersulfate",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:sulfate-full-copper",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 0.5
      },
      {
        "code": "causticsoda",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:causticsodaportion",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 0.5
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-malachite",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · white_lead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>vinegar</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>tannin</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>compost</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 4 | 名称未汉化（见物品代码）<br><code>lead</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "white_lead",
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
        "code": "em:powdered-ore-whitelead"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "vinegar",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:slakedlimeportion",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "tannin",
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.2,
        "validStacks": [
          {
            "type": "item",
            "code": "game:weaktanninportion",
            "shapeElement": "game:bowl/water"
          }
        ]
      },
      {
        "code": "compost",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:compost"
          }
        ]
      },
      {
        "code": "lead",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-metal-lead"
          }
        ]
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "em:powdered-ore-whitelead",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · zincsulfate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>copper</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sulphuricacid</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "zincsulfate",
    "comment": "powdered zinc has a conversion temperature and thus cannot be used in cooking recipes...",
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
        "code": "game:sulfate-full-zinc"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "copper",
        "minQuantity": 3,
        "maxQuantity": 3,
        "validStacks": [
          {
            "type": "item",
            "code": "em:powdered-ore-zincoxide"
          }
        ]
      },
      {
        "code": "sulphuricacid",
        "minQuantity": 1,
        "maxQuantity": 1,
        "validStacks": [
          {
            "type": "item",
            "code": "game:acid-full-sulfuric",
            "shapeElement": "bowl/water"
          }
        ],
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:sulfate-full-zinc",
      "quantity": 100
    }
  }
]
```

</details>

</details>

<details><summary>炸药 · blastingpowder</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 苦味酸<br><code>em:powdered-ore-picricacid</code> | 4 | 未声明附加限制 |
| 投入 C | 木炭粉<br><code>game:powder-charcoal</code> | 2 | 未声明附加限制 |
| 产物 | 炸药<br><code>game:blastingpowder</code> | 6 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 苦味酸<br><code>em:powdered-ore-picricacid</code> | 4 | 未声明附加限制 |
| 投入 C | 粉末状煤<br><code>em:powdered-ore-coal</code> | 2 | 未声明附加限制 |
| 投入 R | 腐烂物<br><code>game:rot</code> | 1 | 未声明附加限制 |
| 产物 | 炸药<br><code>game:blastingpowder</code> | 6 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PCR
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 硝石<br><code>game:saltpeter</code> | 4 | 未声明附加限制 |
| 投入 S | 硫磺粉<br><code>game:powder-sulfur</code> | 2 | 未声明附加限制 |
| 投入 C | 粉末状煤<br><code>em:powdered-ore-coal</code> | 2 | 未声明附加限制 |
| 投入 R | 腐烂物<br><code>game:rot</code> | 1 | 未声明附加限制 |
| 产物 | 炸药<br><code>game:blastingpowder</code> | 6 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSC
_R_
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 苦味酸<br><code>em:powdered-ore-picricacid</code> | 4 | 未声明附加限制 |
| 投入 C | 粉末状煤<br><code>em:powdered-ore-coal</code> | 2 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:plantdebris-*</code> | 1 | 未声明附加限制 |
| 产物 | 炸药<br><code>game:blastingpowder</code> | 6 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PCR
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 硝石<br><code>game:saltpeter</code> | 4 | 未声明附加限制 |
| 投入 S | 硫磺粉<br><code>game:powder-sulfur</code> | 2 | 未声明附加限制 |
| 投入 C | 粉末状煤<br><code>em:powdered-ore-coal</code> | 2 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:plantdebris-*</code> | 1 | 未声明附加限制 |
| 产物 | 炸药<br><code>game:blastingpowder</code> | 6 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSC
_R_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "name": "blastingpowder2",
    "comment": "gunpowder actually needs cellulose fibers, so it needs charcoal, not just any coal.",
    "ingredientPattern": "PC",
    "enabled": true,
    "recipeGroup": 7,
    "ingredients": {
      "P": {
        "type": "item",
        "code": "em:powdered-ore-picricacid",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:powder-charcoal",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:blastingpowder",
      "quantity": 6
    }
  },
  {
    "name": "blastingpowder3",
    "comment": "gunpowder actually needs cellulose fibers, so for non-charcoal, add rot.",
    "ingredientPattern": "PCR",
    "enabled": true,
    "recipeGroup": 6,
    "ingredients": {
      "P": {
        "type": "item",
        "code": "em:powdered-ore-picricacid",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "em:powdered-ore-coal",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:rot",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:blastingpowder",
      "quantity": 6
    }
  },
  {
    "name": "blastingpowder3",
    "comment": "gunpowder actually needs cellulose fibers, so for non-charcoal, add rot.",
    "ingredientPattern": "PSC,_R_",
    "enabled": true,
    "recipeGroup": 8,
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:saltpeter",
        "quantity": 4
      },
      "S": {
        "type": "item",
        "code": "game:powder-sulfur",
        "quantity": 2
      },
      "C": {
        "type": "item",
        "code": "em:powdered-ore-coal",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:rot",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:blastingpowder",
      "quantity": 6
    }
  },
  {
    "name": "blastingpowder3",
    "comment": "gunpowder actually needs cellulose fibers, so for non-charcoal, add plant debris.",
    "ingredientPattern": "PCR",
    "enabled": true,
    "recipeGroup": 6,
    "ingredients": {
      "P": {
        "type": "item",
        "code": "em:powdered-ore-picricacid",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "em:powdered-ore-coal",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:plantdebris-*",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:blastingpowder",
      "quantity": 6
    }
  },
  {
    "name": "blastingpowder3",
    "comment": "gunpowder actually needs cellulose fibers, so for non-charcoal, add plant debris.",
    "ingredientPattern": "PSC,_R_",
    "enabled": true,
    "recipeGroup": 8,
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:saltpeter",
        "quantity": 4
      },
      "S": {
        "type": "item",
        "code": "game:powder-sulfur",
        "quantity": 2
      },
      "C": {
        "type": "item",
        "code": "em:powdered-ore-coal",
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:plantdebris-*",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:blastingpowder",
      "quantity": 6
    }
  }
]
```

</details>

</details>

<details><summary>岩石爆破炸弹、废料炸弹 · bombs</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 8 | 允许变体：['hematite', 'limonite', 'magnetite'] |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 岩石爆破炸弹<br><code>game:bomb-stone</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
CBF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 金属废料<br><code>game:metal-scraps</code> | 2 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 8 | 允许变体：['hematite', 'limonite', 'magnetite'] |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 废料炸弹<br><code>game:bomb-scrap</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
CBF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 4 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 8 | 允许变体：['hematite', 'limonite', 'magnetite'] |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 废料炸弹<br><code>game:bomb-scrap</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
CBF
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 4 | 未声明附加限制 |
| 投入 T | 金属废料<br><code>game:metal-scraps</code> | 2 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>em:powdered-ore-*</code> | 8 | 允许变体：['hematite', 'limonite', 'magnetite'] |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 废料炸弹<br><code>game:bomb-scrap</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPT
CBF
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 8 | 未声明附加限制 |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 岩石爆破炸弹<br><code>game:bomb-stone</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
CBF
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 金属废料<br><code>game:metal-scraps</code> | 2 | 未声明附加限制 |
| 投入 P | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 8 | 未声明附加限制 |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 废料炸弹<br><code>game:bomb-scrap</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
CBF
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 4 | 未声明附加限制 |
| 投入 P | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 8 | 未声明附加限制 |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 废料炸弹<br><code>game:bomb-scrap</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
CBF
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 4 | 未声明附加限制 |
| 投入 T | 金属废料<br><code>game:metal-scraps</code> | 2 | 未声明附加限制 |
| 投入 P | 粉状生锈金属<br><code>em:powdered-metal-rusty</code> | 8 | 未声明附加限制 |
| 投入 B | 炸药<br><code>game:blastingpowder</code> | 4 | 未声明附加限制 |
| 投入 C | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 废料炸弹<br><code>game:bomb-scrap</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPT
CBF
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_P_,CBF",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "em:powdered-ore-*",
        "quantity": 8,
        "name": "iron",
        "allowedVariants": [
          "hematite",
          "limonite",
          "magnetite"
        ]
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "bomb-stone",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-stone",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "SPS,CBF",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:metal-scraps",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "em:powdered-ore-*",
        "quantity": 8,
        "name": "iron",
        "allowedVariants": [
          "hematite",
          "limonite",
          "magnetite"
        ]
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "bomb-scrap",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-scrap",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "SPS,CBF",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 4
      },
      "P": {
        "type": "item",
        "code": "em:powdered-ore-*",
        "quantity": 8,
        "name": "iron",
        "allowedVariants": [
          "hematite",
          "limonite",
          "magnetite"
        ]
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "recipeGroup": 1,
    "name": "bomb-scrap",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-scrap",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "SPT,CBF",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 4
      },
      "T": {
        "type": "block",
        "code": "game:metal-scraps",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "em:powdered-ore-*",
        "quantity": 8,
        "name": "iron",
        "allowedVariants": [
          "hematite",
          "limonite",
          "magnetite"
        ]
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "recipeGroup": 2,
    "name": "bomb-scrap",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-scrap",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "_P_,CBF",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 8
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "bomb-stone",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-stone",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "SPS,CBF",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:metal-scraps",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 8
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "bomb-scrap",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-scrap",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "SPS,CBF",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 4
      },
      "P": {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 8
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "recipeGroup": 1,
    "name": "bomb-scrap",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-scrap",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "SPT,CBF",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 4
      },
      "T": {
        "type": "block",
        "code": "game:metal-scraps",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "em:powdered-metal-rusty",
        "quantity": 8
      },
      "B": {
        "type": "item",
        "code": "game:blastingpowder",
        "quantity": 4
      },
      "C": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "F": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "recipeGroup": 2,
    "name": "bomb-scrap",
    "width": 3,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:bomb-scrap",
      "quantity": 8
    }
  }
]
```

</details>

</details>

<details><summary>碎煤 · crushing</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 木炭<br><code>game:charcoal</code> | 1 | 未声明附加限制 |
| 产物 | 碎煤<br><code>em:crushed-ore-coal</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
H
C
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：4 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:ore-*</code> | 1 | 允许变体：['bituminouscoal', 'anthracite'] |
| 产物 | 碎煤<br><code>em:crushed-ore-coal</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
H
C
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：4 |
| 投入 C | 焦炭<br><code>game:coke</code> | 1 | 未声明附加限制 |
| 产物 | 碎煤<br><code>em:crushed-ore-coal</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
H
C
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "H,C",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:charcoal",
        "name": "ore",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "em:crushed-ore-coal",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "H,C",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 4
      },
      "C": {
        "type": "item",
        "code": "game:ore-*",
        "name": "ore",
        "quantity": 1,
        "allowedVariants": [
          "bituminouscoal",
          "anthracite"
        ]
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "em:crushed-ore-coal",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "H,C",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 4
      },
      "C": {
        "type": "item",
        "code": "game:coke",
        "name": "ore",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "em:crushed-ore-coal",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>白铜粒 · metalbit</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20；排除变体：['copper'] |
| 投入 P | 金属零件<br><code>game:metal-parts</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 白铜粒<br><code>game:metalbit-cupronickel</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "C,P",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "name": "metal",
        "isTool": true,
        "skipVariants": [
          "copper"
        ],
        "toolDurabilityCost": 20
      },
      "P": {
        "type": "block",
        "code": "game:metal-parts"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:metalbit-cupronickel",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>镉红、镉橙、镉绿 · pigments</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 镉黄<br><code>em:powdered-ore-cadmiumsulfide</code> | 1 | 未声明附加限制 |
| 投入 S | 粉末状闪锌矿<br><code>em:powdered-ore-sphalerite</code> | 1 | 未声明附加限制 |
| 产物 | 镉红<br><code>em:powdered-ore-cadmiumselenide</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CCS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 镉红<br><code>em:powdered-ore-cadmiumselenide</code> | 1 | 未声明附加限制 |
| 投入 S | 粉末状闪锌矿<br><code>em:powdered-ore-sphalerite</code> | 1 | 未声明附加限制 |
| 产物 | 镉橙<br><code>em:powdered-ore-cadmiumsulfoselenide</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CCS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 镉黄<br><code>em:powdered-ore-cadmiumsulfide</code> | 4 | 未声明附加限制 |
| 投入 S | 粉末状闪锌矿<br><code>em:powdered-ore-sphalerite</code> | 5 | 未声明附加限制 |
| 产物 | 镉橙<br><code>em:powdered-ore-cadmiumsulfoselenide</code> | 9 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 镉黄<br><code>em:powdered-ore-cadmiumsulfide</code> | 1 | 未声明附加限制 |
| 投入 S | 铬绿<br><code>em:powdered-ore-chromiumoxide</code> | 1 | 未声明附加限制 |
| 产物 | 镉绿<br><code>em:powdered-ore-cadmiumgreen</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "name": "cadmiumred",
    "ingredientPattern": "CCS",
    "enabled": true,
    "recipeGroup": 6,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfide",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "em:powdered-ore-sphalerite",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "em:powdered-ore-cadmiumselenide",
      "quantity": 3
    }
  },
  {
    "name": "cadmiumorange",
    "ingredientPattern": "CCS",
    "enabled": true,
    "recipeGroup": 8,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "em:powdered-ore-cadmiumselenide",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "em:powdered-ore-sphalerite",
        "quantity": 1
      }
    },
    "shapeless": true,
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "em:powdered-ore-cadmiumsulfoselenide",
      "quantity": 3
    }
  },
  {
    "name": "cadmiumorange",
    "ingredientPattern": "CS",
    "enabled": true,
    "recipeGroup": 6,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfide",
        "quantity": 4
      },
      "S": {
        "type": "item",
        "code": "em:powdered-ore-sphalerite",
        "quantity": 5
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "em:powdered-ore-cadmiumsulfoselenide",
      "quantity": 9
    }
  },
  {
    "name": "cadmiumgreen",
    "ingredientPattern": "CS",
    "enabled": true,
    "recipeGroup": 6,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "em:powdered-ore-cadmiumsulfide",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "em:powdered-ore-chromiumoxide",
        "quantity": 1
      }
    },
    "shapeless": true,
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "em:powdered-ore-cadmiumgreen",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>粉末状煤 · powdered_coal</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 木炭粉<br><code>game:powder-charcoal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 粉末状煤<br><code>em:powdered-ore-coal</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "comment": "Compatibility with 1.19.4",
    "ingredientPattern": "C",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:powder-charcoal"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "em:powdered-ore-coal",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>未烧制的三级耐火砖、未烧制的二级耐火砖 · rawrefractorybrick</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 粉碎的石英<br><code>game:crushed-quartz</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 粉碎的铝土矿<br><code>game:crushed-bauxite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 粉碎的橄榄石<br><code>game:crushed-olivine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 I | 粉碎的铬铁矿<br><code>game:crushed-chromite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 未烧制的三级耐火砖<br><code>game:refractorybrick-raw-tier3</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FF
QB
PI
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 粉碎的石英<br><code>game:crushed-quartz</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 粉碎的铝土矿<br><code>game:crushed-bauxite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 白镁氧<br><code>em:powdered-ore-magnesiumoxide</code> | 4 | 未声明附加限制 |
| 产物 | 未烧制的二级耐火砖<br><code>game:refractorybrick-raw-tier2</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FF
QB
P_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "chromiterefractorybricks",
    "ingredientPattern": "FF,QB,PI",
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:clay-fire"
      },
      "Q": {
        "type": "item",
        "code": "game:crushed-quartz"
      },
      "B": {
        "type": "item",
        "code": "game:crushed-bauxite"
      },
      "P": {
        "type": "item",
        "code": "game:crushed-olivine"
      },
      "I": {
        "type": "item",
        "code": "game:crushed-chromite"
      }
    },
    "recipeGroup": 2,
    "width": 2,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "game:refractorybrick-raw-tier3",
      "quantity": 1
    }
  },
  {
    "code": "magnesiumrefractorybricks",
    "ingredientPattern": "FF,QB,P_",
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:clay-fire"
      },
      "Q": {
        "type": "item",
        "code": "game:crushed-quartz"
      },
      "B": {
        "type": "item",
        "code": "game:crushed-bauxite"
      },
      "P": {
        "type": "item",
        "code": "em:powdered-ore-magnesiumoxide",
        "quantity": 4
      }
    },
    "recipeGroup": 2,
    "width": 2,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "game:refractorybrick-raw-tier2",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>黑土 · terra_preta</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 堆肥土<br><code>game:compost</code> | 4 | 未声明附加限制 |
| 投入 S | 碎煤<br><code>em:crushed-ore-coal</code> | 8 | 未声明附加限制 |
| 投入 B | 骨粉<br><code>game:bonemeal</code> | 2 | 未声明附加限制 |
| 产物 | 黑土<br><code>game:soil-high-none</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CBC
BSB
CBC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 堆肥土<br><code>game:compost</code> | 4 | 未声明附加限制 |
| 投入 S | 肥沃泥土<br><code>game:soil-compost-none</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 K | 碎煤<br><code>em:crushed-ore-coal</code> | 4 | 未声明附加限制 |
| 投入 B | 骨粉<br><code>game:bonemeal</code> | 4 | 未声明附加限制 |
| 产物 | 黑土<br><code>game:soil-high-none</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CBC
KSK
CBC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 堆肥土<br><code>game:compost</code> | 4 | 未声明附加限制 |
| 投入 S | 粉末状煤<br><code>em:powdered-ore-coal</code> | 16 | 未声明附加限制 |
| 投入 B | 骨粉<br><code>game:bonemeal</code> | 2 | 未声明附加限制 |
| 产物 | 黑土<br><code>game:soil-high-none</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CBC
BSB
CBC
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 堆肥土<br><code>game:compost</code> | 4 | 未声明附加限制 |
| 投入 S | 肥沃泥土<br><code>game:soil-compost-none</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 K | 粉末状煤<br><code>em:powdered-ore-coal</code> | 8 | 未声明附加限制 |
| 投入 B | 骨粉<br><code>game:bonemeal</code> | 4 | 未声明附加限制 |
| 产物 | 黑土<br><code>game:soil-high-none</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CBC
KSK
CBC
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "CBC,BSB,CBC",
    "comment": "Needs charcoal, not just any coal with residues like sulphur in it.",
    "enabled": false,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:compost",
        "quantity": 4
      },
      "S": {
        "type": "item",
        "code": "em:crushed-ore-coal",
        "quantity": 8
      },
      "B": {
        "type": "item",
        "code": "game:bonemeal",
        "quantity": 2
      }
    },
    "recipeGroup": 1,
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:soil-high-none",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CBC,KSK,CBC",
    "enabled": false,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:compost",
        "quantity": 4
      },
      "S": {
        "type": "block",
        "code": "game:soil-compost-none"
      },
      "K": {
        "type": "item",
        "code": "em:crushed-ore-coal",
        "quantity": 4
      },
      "B": {
        "type": "item",
        "code": "game:bonemeal",
        "quantity": 4
      }
    },
    "recipeGroup": 2,
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:soil-high-none",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "CBC,BSB,CBC",
    "enabled": false,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:compost",
        "quantity": 4
      },
      "S": {
        "type": "item",
        "code": "em:powdered-ore-coal",
        "quantity": 16
      },
      "B": {
        "type": "item",
        "code": "game:bonemeal",
        "quantity": 2
      }
    },
    "recipeGroup": 1,
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:soil-high-none",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CBC,KSK,CBC",
    "enabled": false,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:compost",
        "quantity": 4
      },
      "S": {
        "type": "block",
        "code": "game:soil-compost-none"
      },
      "K": {
        "type": "item",
        "code": "em:powdered-ore-coal",
        "quantity": 8
      },
      "B": {
        "type": "item",
        "code": "game:bonemeal",
        "quantity": 4
      }
    },
    "recipeGroup": 2,
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:soil-high-none",
      "quantity": 2
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
