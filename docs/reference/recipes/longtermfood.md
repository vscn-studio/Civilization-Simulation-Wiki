<!-- generated:start -->
# 长期储存食品：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>特殊配方 · salt</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "salt",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 36
      },
      "transitionHours": {
        "avg": 36
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "saltwaterportion"
      }
    },
    "shape": {
      "base": "block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "saltwaterportion",
            "shapeElement": "bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "salt",
      "quantity": 1
    }
  },
  {
    "code": "salt",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 36
      },
      "transitionHours": {
        "avg": 36
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "saltwaterportion"
      }
    },
    "shape": {
      "base": "block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "saltwaterportion",
            "shapeElement": "bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "salt",
      "quantity": 2
    }
  },
  {
    "code": "salt",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 36
      },
      "transitionHours": {
        "avg": 36
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "saltwaterportion"
      }
    },
    "shape": {
      "base": "block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "saltwaterportion",
            "shapeElement": "bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "salt",
      "quantity": 3
    }
  },
  {
    "code": "salt",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 36
      },
      "transitionHours": {
        "avg": 36
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "saltwaterportion"
      }
    },
    "shape": {
      "base": "block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "water",
        "validStacks": [
          {
            "type": "item",
            "code": "saltwaterportion",
            "shapeElement": "bowl/water"
          }
        ],
        "minQuantity": 4,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "Item",
      "code": "salt",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码）、黄海草、红海草、橙海草、绿海草 · algae-barrel</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:seaweed-section</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:seaweed-section</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：96。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 海草<br><code>game:seaweed-top</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:seaweed-section</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：96。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 黄海草<br><code>game:aquatic-seagrass-yellow-section</code> | 1 | 未声明附加限制 |
| 产物 | 黄海草<br><code>game:aquatic-seagrass-yellow-section</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：96。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 红海草<br><code>game:aquatic-seagrass-red-section</code> | 1 | 未声明附加限制 |
| 产物 | 红海草<br><code>game:aquatic-seagrass-red-section</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：96。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 橙海草<br><code>game:aquatic-seagrass-orange-section</code> | 1 | 未声明附加限制 |
| 产物 | 橙海草<br><code>game:aquatic-seagrass-orange-section</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：96。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 绿海草<br><code>game:aquatic-seagrass-green-section</code> | 1 | 未声明附加限制 |
| 产物 | 绿海草<br><code>game:aquatic-seagrass-green-section</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：96。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "seaweed-section",
    "enabled": true,
    "sealHours": 96,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "block",
        "code": "game:seaweed-section",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:seaweed-section",
      "stackSize": 2
    }
  },
  {
    "code": "seaweed-top",
    "enabled": true,
    "sealHours": 96,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "block",
        "code": "game:seaweed-top",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:seaweed-section",
      "stackSize": 2
    }
  },
  {
    "code": "seaweed-yellow",
    "enabled": true,
    "sealHours": 96,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "block",
        "code": "game:aquatic-seagrass-yellow-section",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:aquatic-seagrass-yellow-section",
      "stackSize": 2
    }
  },
  {
    "code": "seaweed-red",
    "enabled": true,
    "sealHours": 96,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "block",
        "code": "game:aquatic-seagrass-red-section",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:aquatic-seagrass-red-section",
      "stackSize": 2
    }
  },
  {
    "code": "seaweed-orange",
    "enabled": true,
    "sealHours": 96,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "block",
        "code": "game:aquatic-seagrass-orange-section",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:aquatic-seagrass-orange-section",
      "stackSize": 2
    }
  },
  {
    "code": "seaweed-green",
    "enabled": true,
    "sealHours": 96,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5
      },
      {
        "type": "block",
        "code": "game:aquatic-seagrass-green-section",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:aquatic-seagrass-green-section",
      "stackSize": 2
    }
  }
]
```

</details>

</details>

<details><summary>腌藻、绿色染料、红色染料 · algae-green</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 盐水<br><code>game:brineportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 研磨绿藻<br><code>pemmican:algae-grind-green</code> | 1 | 未声明附加限制 |
| 产物 | 腌藻<br><code>pemmican:algae-grind-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：168。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 研磨绿藻<br><code>pemmican:algae-grind-green</code> | 1 | 未声明附加限制 |
| 产物 | 绿色染料<br><code>game:dye-green</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释明矾<br><code>game:dilutedalumportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 研磨红藻<br><code>pemmican:algae-grind-red</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释铬铁矿<br><code>game:dilutedchromiteportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 研磨红藻<br><code>pemmican:algae-grind-red</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 研磨红藻<br><code>pemmican:algae-grind-red</code> | 1 | 未声明附加限制 |
| 产物 | 红色染料<br><code>game:dye-red</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "algae-salt",
    "sealHours": 168,
    "ingredients": [
      {
        "type": "item",
        "code": "game:brineportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "pemmican:algae-grind-green",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:algae-grind-salt",
      "stackSize": 1
    }
  },
  {
    "code": "algae-green-dye",
    "sealHours": 4,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "pemmican:algae-grind-green",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-green",
      "litres": 1
    }
  },
  {
    "code": "algae-red-dye1",
    "sealHours": 4,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedalumportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "pemmican:algae-grind-red",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 1
    }
  },
  {
    "code": "algae-red-dye2",
    "sealHours": 4,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedchromiteportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "pemmican:algae-grind-red",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 1
    }
  },
  {
    "code": "algae-red-dye3",
    "sealHours": 4,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dilutedcassiteriteportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "pemmican:algae-grind-red",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:dye-red",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>蘑菇啤酒、森林艾尔 · beer-brewing</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 蘑菇醪液<br><code>pemmican:yeast-ale</code> | 1 | 未声明附加限制 |
| 产物 | 蘑菇啤酒<br><code>pemmican:beer-ale</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 森林蘑菇醪液<br><code>pemmican:yeast-forest</code> | 1 | 未声明附加限制 |
| 产物 | 森林艾尔<br><code>pemmican:beer-forest</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "beer-mushroomale",
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
        "code": "pemmican:yeast-ale",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:beer-ale",
      "litres": 1
    }
  },
  {
    "code": "beer-forest",
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
        "code": "pemmican:yeast-forest",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:beer-forest",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>凝乳 · cheesemaking</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 奶<br><code>game:milkportion</code> | 25 升 | 未声明附加限制 |
| 投入 2 | 切碎的腌土豆<br><code>pemmican:choppedvegetable-pickledpotato</code> | 1 | 未声明附加限制 |
| 产物 | 凝乳<br><code>game:curdledmilkportion</code> | 25 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 奶<br><code>game:milkportion</code> | 20 升 | 未声明附加限制 |
| 投入 2 | 切碎的腌土豆<br><code>pemmican:choppedvegetable-pickledpotato</code> | 1 | 未声明附加限制 |
| 产物 | 凝乳<br><code>game:curdledmilkportion</code> | 20 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 奶<br><code>game:milkportion</code> | 25 升 | 未声明附加限制 |
| 投入 2 | 腌蘑菇<br><code>pemmican:mushroomclean-pickled</code> | 1 | 未声明附加限制 |
| 产物 | 凝乳<br><code>game:curdledmilkportion</code> | 25 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 奶<br><code>game:milkportion</code> | 20 升 | 未声明附加限制 |
| 投入 2 | 腌蘑菇<br><code>pemmican:mushroomclean-pickled</code> | 1 | 未声明附加限制 |
| 产物 | 凝乳<br><code>game:curdledmilkportion</code> | 20 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 奶<br><code>game:milkportion</code> | 25 升 | 未声明附加限制 |
| 投入 2 | 腌土豆<br><code>pemmican:pickledvegetable-pickledpotato</code> | 1 | 未声明附加限制 |
| 产物 | 凝乳<br><code>game:curdledmilkportion</code> | 25 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 奶<br><code>game:milkportion</code> | 20 升 | 未声明附加限制 |
| 投入 2 | 腌土豆<br><code>pemmican:pickledvegetable-pickledpotato</code> | 1 | 未声明附加限制 |
| 产物 | 凝乳<br><code>game:curdledmilkportion</code> | 20 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "curdledmilkportion-new",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:milkportion",
        "litres": 25
      },
      {
        "type": "item",
        "code": "pemmican:choppedvegetable-pickledpotato",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:curdledmilkportion",
      "litres": 25
    }
  },
  {
    "code": "curdledmilkportion-new",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:milkportion",
        "litres": 20
      },
      {
        "type": "item",
        "code": "pemmican:choppedvegetable-pickledpotato",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:curdledmilkportion",
      "litres": 20
    }
  },
  {
    "code": "curdledmilkportion-new",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:milkportion",
        "litres": 25
      },
      {
        "type": "item",
        "code": "pemmican:mushroomclean-pickled",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:curdledmilkportion",
      "litres": 25
    }
  },
  {
    "code": "curdledmilkportion-new",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:milkportion",
        "litres": 20
      },
      {
        "type": "item",
        "code": "pemmican:mushroomclean-pickled",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:curdledmilkportion",
      "litres": 20
    }
  },
  {
    "code": "curdledmilkportion-new",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:milkportion",
        "litres": 25
      },
      {
        "type": "item",
        "code": "pemmican:pickledvegetable-pickledpotato",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:curdledmilkportion",
      "litres": 25
    }
  },
  {
    "code": "curdledmilkportion-new",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:milkportion",
        "litres": 20
      },
      {
        "type": "item",
        "code": "pemmican:pickledvegetable-pickledpotato",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:curdledmilkportion",
      "litres": 20
    }
  }
]
```

</details>

</details>

<details><summary>深棕陶瓷烹饪锅、耐火陶瓷烹饪锅、黑色陶瓷烹饪锅、棕色陶瓷烹饪锅、奶白陶瓷烹饪锅、灰色陶瓷烹饪锅、橙色陶瓷烹饪锅、土橙色陶瓷烹饪锅、红色陶瓷烹饪锅、沙色陶瓷烹饪锅 · cleanpot</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-blue-empty</code> | 1 | 未声明附加限制 |
| 产物 | 深棕陶瓷烹饪锅<br><code>game:claypot-blue-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-fire-empty</code> | 1 | 未声明附加限制 |
| 产物 | 耐火陶瓷烹饪锅<br><code>game:claypot-fire-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-black-empty</code> | 1 | 未声明附加限制 |
| 产物 | 黑色陶瓷烹饪锅<br><code>game:claypot-black-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-brown-empty</code> | 1 | 未声明附加限制 |
| 产物 | 棕色陶瓷烹饪锅<br><code>game:claypot-brown-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-cream-empty</code> | 1 | 未声明附加限制 |
| 产物 | 奶白陶瓷烹饪锅<br><code>game:claypot-cream-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-gray-empty</code> | 1 | 未声明附加限制 |
| 产物 | 灰色陶瓷烹饪锅<br><code>game:claypot-gray-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-orange-empty</code> | 1 | 未声明附加限制 |
| 产物 | 橙色陶瓷烹饪锅<br><code>game:claypot-orange-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-earthyorange-empty</code> | 1 | 未声明附加限制 |
| 产物 | 土橙色陶瓷烹饪锅<br><code>game:claypot-earthyorange-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-red-empty</code> | 1 | 未声明附加限制 |
| 产物 | 红色陶瓷烹饪锅<br><code>game:claypot-red-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:dirtyclaypot-tan-empty</code> | 1 | 未声明附加限制 |
| 产物 | 沙色陶瓷烹饪锅<br><code>game:claypot-tan-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-blue-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-blue-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-fire-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-fire-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-black-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-black-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-brown-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-brown-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-cream-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-cream-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-gray-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-gray-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-orange-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-orange-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-earthyorange-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-earthyorange-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-red-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-red-fired",
      "stackSize": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 0.2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 10
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-tan-empty",
        "quantity": 1
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-tan-fired",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>治疗葡萄酒（新酿） · medbrew</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 活球灵液<br><code>pemmican:medrefined-healbulb</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:fruit-{fruit}</code> | 1 | 允许变体：['blueberry', 'cranberry', 'redcurrant', 'whitecurrant', 'blackcurrant', 'saguaro', 'pinaple', 'redapple', 'pinkapple', 'yellowapple', 'cherry', 'peach', 'pear', 'orange', 'mango', 'breadfruit', 'luchee', 'pomegranade', 'beautyberry', 'blackberry', 'cloudberry', 'cloudberry', 'raspberry', 'strawberry'] |
| 产物 | 治疗葡萄酒（新酿）<br><code>pemmican:medbrew-raw</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "medbrew",
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:medrefined-healbulb",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:fruit-{fruit}",
        "quantity": 1,
        "allowedVariants": [
          "blueberry",
          "cranberry",
          "redcurrant",
          "whitecurrant",
          "blackcurrant",
          "saguaro",
          "pinaple",
          "redapple",
          "pinkapple",
          "yellowapple",
          "cherry",
          "peach",
          "pear",
          "orange",
          "mango",
          "breadfruit",
          "luchee",
          "pomegranade",
          "beautyberry",
          "blackberry",
          "cloudberry",
          "cloudberry",
          "raspberry",
          "strawberry"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:medbrew-raw",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>纸莎草纤维 · papyrus-fiber</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 纸莎草<br><code>game:papyrustops</code> | 1 | 未声明附加限制 |
| 产物 | 纸莎草纤维<br><code>pemmican:papyrus-fiber</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "papyrus-fiber",
    "enabled": true,
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:papyrus-fiber",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>腌土豆、切碎的腌土豆 · pickled</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 盐水<br><code>game:brineportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>pemmican:vegetable-potato-raw</code> | 1 | 未声明附加限制 |
| 产物 | 腌土豆<br><code>pemmican:pickledvegetable-pickledpotato</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：144。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 盐水<br><code>game:brineportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 1 | 未声明附加限制 |
| 产物 | 切碎的腌土豆<br><code>pemmican:choppedvegetable-pickledpotato</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "pickled-potato",
    "enabled": true,
    "sealHours": 144,
    "ingredients": [
      {
        "type": "item",
        "code": "game:brineportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "pemmican:vegetable-potato-raw",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:pickledvegetable-pickledpotato",
      "stackSize": 1
    }
  },
  {
    "code": "pickled-potato2",
    "enabled": true,
    "sealHours": 48,
    "ingredients": [
      {
        "type": "item",
        "code": "game:brineportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "pemmican:choppedvegetable-potato",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:choppedvegetable-pickledpotato",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>腌蘑菇 · pickledmushroom</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 盐水<br><code>game:brineportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 清洗过的蘑菇<br><code>pemmican:mushroomclean-raw</code> | 1 | 未声明附加限制 |
| 产物 | 腌蘑菇<br><code>pemmican:mushroomclean-pickled</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "code": "pickledmushroom",
  "sealHours": 336,
  "ingredients": [
    {
      "type": "item",
      "code": "game:brineportion",
      "litres": 1
    },
    {
      "type": "item",
      "code": "pemmican:mushroomclean-raw",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "pemmican:mushroomclean-pickled",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>竹纤维片、香蒲纤维片、纸莎草纤维片 · pulp-to-hide</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 石灰水<br><code>game:limewaterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 竹浆<br><code>pemmican:pulp-bamboo</code> | 10 | 未声明附加限制 |
| 产物 | 竹纤维片<br><code>pemmican:planthide-bamboo</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 石灰水<br><code>game:limewaterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 香蒲浆<br><code>pemmican:pulp-cattail</code> | 10 | 未声明附加限制 |
| 产物 | 香蒲纤维片<br><code>pemmican:planthide-cattail</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 石灰水<br><code>game:limewaterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 纸莎草浆<br><code>pemmican:pulp-papyrus</code> | 10 | 未声明附加限制 |
| 产物 | 纸莎草纤维片<br><code>pemmican:planthide-papyrus</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "pulp-to-hide",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "game:limewaterportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "pemmican:pulp-bamboo",
        "quantity": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:planthide-bamboo",
      "stackSize": 1
    }
  },
  {
    "code": "pulp-to-hide",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "game:limewaterportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "pemmican:pulp-cattail",
        "quantity": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:planthide-cattail",
      "stackSize": 1
    }
  },
  {
    "code": "pulp-to-hide",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "game:limewaterportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "pemmican:pulp-papyrus",
        "quantity": 10
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:planthide-papyrus",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>咸牛奶、奶 · saltymilk</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 奶<br><code>game:milkportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 盐<br><code>game:salt</code> | 1 | 未声明附加限制 |
| 产物 | 咸牛奶<br><code>pemmican:saltmilkportion</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.1。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 咸牛奶<br><code>pemmican:saltmilkportion</code> | 1 升 | 未声明附加限制 |
| 产物 | 奶<br><code>game:milkportion</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0.1。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "saltymilk",
    "sealHours": 0.1,
    "ingredients": [
      {
        "type": "item",
        "code": "game:milkportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:salt",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:saltmilkportion",
      "litres": 1
    }
  },
  {
    "code": "normalmilk",
    "sealHours": 0.1,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:saltmilkportion",
        "litres": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:milkportion",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>淀粉（生）、淀粉糊、媒染布料 · starch</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 研磨土豆<br><code>pemmican:sugargrind-potato</code> | 1 | 未声明附加限制 |
| 产物 | 淀粉（生）<br><code>pemmican:starch-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 淀粉<br><code>pemmican:starch-dry</code> | 1 | 未声明附加限制 |
| 产物 | 淀粉糊<br><code>pemmican:starchwaterportion</code> | 5 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 淀粉糊<br><code>pemmican:starchwaterportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 布料<br><code>game:cloth-plain</code> | 1 | 未声明附加限制 |
| 产物 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：8。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "starch",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "pemmican:sugargrind-potato",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:starch-raw",
      "stackSize": 1
    }
  },
  {
    "code": "starch-cloth",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "pemmican:starch-dry",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:starchwaterportion",
      "litres": 5
    }
  },
  {
    "code": "starch-cloth-mordant",
    "sealHours": 8,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:starchwaterportion",
        "litres": 2,
        "consumeLitres": 2
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
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>甘蔗醪液、甜菜醪液、糖醪液、糖浆、土豆醪液、玉米醪液 · wort-brewing</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 甘蔗糖浆<br><code>pemmican:syrup-cane</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:fruit-{fruit}</code> | 1 | 允许变体：['blueberry', 'cranberry', 'redcurrant', 'whitecurrant', 'blackcurrant', 'saguaro', 'pinaple', 'redapple', 'pinkapple', 'yellowapple', 'cherry', 'peach', 'pear', 'orange', 'mango', 'breadfruit', 'luchee', 'pomegranade', 'beautyberry', 'blackberry', 'cloudberry', 'cloudberry', 'raspberry', 'strawberry'] |
| 产物 | 甘蔗醪液<br><code>pemmican:wort-cane</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 甜菜糖蜜<br><code>pemmican:syrup-beet</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:fruit-{fruit}</code> | 1 | 允许变体：['blueberry', 'cranberry', 'redcurrant', 'whitecurrant', 'blackcurrant', 'saguaro', 'pinaple', 'redapple', 'pinkapple', 'yellowapple', 'cherry', 'peach', 'pear', 'orange', 'mango', 'breadfruit', 'luchee', 'pomegranade', 'beautyberry', 'blackberry', 'cloudberry', 'cloudberry', 'raspberry', 'strawberry'] |
| 产物 | 甜菜醪液<br><code>pemmican:wort-beet</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 糖浆<br><code>pemmican:syrup-sugar</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:fruit-{fruit}</code> | 1 | 允许变体：['blueberry', 'cranberry', 'redcurrant', 'whitecurrant', 'blackcurrant', 'saguaro', 'pinaple', 'redapple', 'pinkapple', 'yellowapple', 'cherry', 'peach', 'pear', 'orange', 'mango', 'breadfruit', 'luchee', 'pomegranade', 'beautyberry', 'blackberry', 'cloudberry', 'cloudberry', 'raspberry', 'strawberry'] |
| 产物 | 糖醪液<br><code>pemmican:wort-sugar</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 糖<br><code>pemmican:sugar</code> | 1 | 未声明附加限制 |
| 产物 | 糖浆<br><code>pemmican:syrup-sugar</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 土豆汁<br><code>pemmican:sugarjuice-potato</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:fruit-{fruit}</code> | 1 | 允许变体：['blueberry', 'cranberry', 'redcurrant', 'whitecurrant', 'blackcurrant', 'saguaro', 'pinaple', 'redapple', 'pinkapple', 'yellowapple', 'cherry', 'peach', 'pear', 'orange', 'mango', 'breadfruit', 'luchee', 'pomegranade', 'beautyberry', 'blackberry', 'cloudberry', 'cloudberry', 'raspberry', 'strawberry'] |
| 产物 | 土豆醪液<br><code>pemmican:wort-potato</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 玉米面粉<br><code>pemmican:flour-corn</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 产物 | 玉米醪液<br><code>pemmican:wort-corn</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：336。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "wort-cane",
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:syrup-cane",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:fruit-{fruit}",
        "quantity": 1,
        "allowedVariants": [
          "blueberry",
          "cranberry",
          "redcurrant",
          "whitecurrant",
          "blackcurrant",
          "saguaro",
          "pinaple",
          "redapple",
          "pinkapple",
          "yellowapple",
          "cherry",
          "peach",
          "pear",
          "orange",
          "mango",
          "breadfruit",
          "luchee",
          "pomegranade",
          "beautyberry",
          "blackberry",
          "cloudberry",
          "cloudberry",
          "raspberry",
          "strawberry"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:wort-cane",
      "litres": 1
    }
  },
  {
    "code": "wort-beet",
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:syrup-beet",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:fruit-{fruit}",
        "quantity": 1,
        "allowedVariants": [
          "blueberry",
          "cranberry",
          "redcurrant",
          "whitecurrant",
          "blackcurrant",
          "saguaro",
          "pinaple",
          "redapple",
          "pinkapple",
          "yellowapple",
          "cherry",
          "peach",
          "pear",
          "orange",
          "mango",
          "breadfruit",
          "luchee",
          "pomegranade",
          "beautyberry",
          "blackberry",
          "cloudberry",
          "cloudberry",
          "raspberry",
          "strawberry"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:wort-beet",
      "litres": 1
    }
  },
  {
    "code": "wort-sugar",
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:syrup-sugar",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:fruit-{fruit}",
        "quantity": 1,
        "allowedVariants": [
          "blueberry",
          "cranberry",
          "redcurrant",
          "whitecurrant",
          "blackcurrant",
          "saguaro",
          "pinaple",
          "redapple",
          "pinkapple",
          "yellowapple",
          "cherry",
          "peach",
          "pear",
          "orange",
          "mango",
          "breadfruit",
          "luchee",
          "pomegranade",
          "beautyberry",
          "blackberry",
          "cloudberry",
          "cloudberry",
          "raspberry",
          "strawberry"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:wort-sugar",
      "litres": 1
    }
  },
  {
    "code": "syrup-sugar",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "pemmican:sugar",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:syrup-sugar",
      "litres": 1
    }
  },
  {
    "code": "wort-potato",
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:sugarjuice-potato",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:fruit-{fruit}",
        "quantity": 1,
        "allowedVariants": [
          "blueberry",
          "cranberry",
          "redcurrant",
          "whitecurrant",
          "blackcurrant",
          "saguaro",
          "pinaple",
          "redapple",
          "pinkapple",
          "yellowapple",
          "cherry",
          "peach",
          "pear",
          "orange",
          "mango",
          "breadfruit",
          "luchee",
          "pomegranade",
          "beautyberry",
          "blackberry",
          "cloudberry",
          "cloudberry",
          "raspberry",
          "strawberry"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "pemmican:wort-potato",
      "litres": 1
    }
  },
  {
    "code": "wort-corn",
    "sealHours": 336,
    "ingredients": [
      {
        "type": "item",
        "code": "pemmican:flour-corn",
        "litres": 1
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
      "code": "pemmican:wort-corn",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · algae</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>alginate</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>lime</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "chem-fiber",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 72
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "alginate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:algae-grind-brown",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      },
      {
        "code": "lime",
        "validStacks": [
          {
            "type": "item",
            "code": "game:limewaterportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:algae-fiber",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · chips</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>pickled-potato</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>oil</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>pickled-potato</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>oil</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>potato</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>oil</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>salt</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>pickled-potato</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>oil</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>pickled-potato</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>oil</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>potato</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>oil</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 3 | 名称未汉化（见物品代码）<br><code>salt</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "chips1",
    "perishableProps": {
      "type": "Perish",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "pickled-potato",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:choppedvegetable-pickledpotato",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      },
      {
        "code": "oil",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:foodoilportion-corn",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:chips-potato",
      "quantity": 1
    }
  },
  {
    "code": "chips2",
    "perishableProps": {
      "type": "Perish",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "pickled-potato",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:choppedvegetable-pickledpotato",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      },
      {
        "code": "oil",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:foodoilportion-corn",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 0.1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:chips-potato",
      "quantity": 2
    }
  },
  {
    "code": "chips3",
    "perishableProps": {
      "type": "Perish",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "potato",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:choppedvegetable-potato",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      },
      {
        "code": "oil",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:foodoilportion-corn",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.1
      },
      {
        "code": "salt",
        "validStacks": [
          {
            "type": "item",
            "code": "game:salt",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:chips-potato",
      "quantity": 1
    }
  },
  {
    "code": "chips1-fat",
    "perishableProps": {
      "type": "Perish",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "pickled-potato",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:choppedvegetable-pickledpotato",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      },
      {
        "code": "oil",
        "validStacks": [
          {
            "type": "item",
            "code": "game:fat-rendered"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:chips-potato",
      "quantity": 1
    }
  },
  {
    "code": "chips2-fat",
    "perishableProps": {
      "type": "Perish",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "pickled-potato",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:choppedvegetable-pickledpotato",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      },
      {
        "code": "oil",
        "validStacks": [
          {
            "type": "item",
            "code": "game:fat-rendered"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:chips-potato",
      "quantity": 2
    }
  },
  {
    "code": "chips3-fat",
    "perishableProps": {
      "type": "Perish",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "potato",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:choppedvegetable-potato",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      },
      {
        "code": "oil",
        "validStacks": [
          {
            "type": "item",
            "code": "game:fat-rendered"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      },
      {
        "code": "salt",
        "validStacks": [
          {
            "type": "item",
            "code": "game:salt",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:chips-potato",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · green-candle</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>wax</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>flax</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>wax</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>flax</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>wax</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>flax</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "green-candle",
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
        "code": "game:candle"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "wax",
        "validStacks": [
          {
            "type": "item",
            "code": "game:beeswax"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      },
      {
        "code": "flax",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:algae-fiber"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:candle",
      "quantity": 1
    }
  },
  {
    "code": "green-candle-f",
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
        "code": "game:candle"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "wax",
        "validStacks": [
          {
            "type": "item",
            "code": "game:fat"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      },
      {
        "code": "flax",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:algae-fiber"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:candle",
      "quantity": 1
    }
  },
  {
    "code": "green-candle-f",
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
        "code": "game:candle"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "wax",
        "validStacks": [
          {
            "type": "item",
            "code": "game:fat-rendered"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      },
      {
        "code": "flax",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:algae-fiber"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:candle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · leather</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>wax</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sulfur</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>wax</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>sulfur</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "leather-sturdy-plain1",
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
        "code": "game:leather-sturdy-plain"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "wax",
        "validStacks": [
          {
            "type": "item",
            "code": "game:resin"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      },
      {
        "code": "sulfur",
        "validStacks": [
          {
            "type": "item",
            "code": "game:hide-chromium-large"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:leather-sturdy-plain",
      "quantity": 3
    }
  },
  {
    "code": "leather-sturdy-plain2",
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
        "code": "game:leather-sturdy-plain"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "ingredients": [
      {
        "code": "wax",
        "validStacks": [
          {
            "type": "item",
            "code": "game:resin"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      },
      {
        "code": "sulfur",
        "validStacks": [
          {
            "type": "item",
            "code": "game:hide-chromium-huge"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:leather-sturdy-plain",
      "quantity": 6
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · med-aloe</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 芦荟叶<br><code>aloe</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 芦荟叶<br><code>aloe</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 芦荟叶<br><code>aloe</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "medrefined-aloe1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
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
        "code": "aloe",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:aloe",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medjuice-aloe",
      "quantity": 25
    }
  },
  {
    "code": "medrefined-aloe2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
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
        "code": "aloe",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:aloe",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medjuice-aloe",
      "quantity": 50
    }
  },
  {
    "code": "medrefined-aloe3",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
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
        "code": "aloe",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:aloe",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medjuice-aloe",
      "quantity": 75
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · med-healbulb</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>fat</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>fat</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>fat</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>fat</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 活球果<br><code>healbulb</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 活球果<br><code>healbulb</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 活球果<br><code>healbulb</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 活球果<br><code>healbulb</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 活球果<br><code>healbulb</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>concetrate</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 活球果<br><code>healbulb</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "salve1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medrefined-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "fat",
        "validStacks": [
          {
            "type": "item",
            "code": "game:fat",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:heal-salve",
      "quantity": 2
    }
  },
  {
    "code": "salve2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medrefined-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "fat",
        "validStacks": [
          {
            "type": "item",
            "code": "game:fat-rendered",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:heal-salve",
      "quantity": 2
    }
  },
  {
    "code": "salve3",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medrefined-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "fat",
        "validStacks": [
          {
            "type": "item",
            "code": "game:resin",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:heal-salve",
      "quantity": 2
    }
  },
  {
    "code": "salve4",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medrefined-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      },
      {
        "code": "fat",
        "validStacks": [
          {
            "type": "item",
            "code": "game:beeswax",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:heal-salve",
      "quantity": 2
    }
  },
  {
    "code": "medrefined-healbulb1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
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
        "code": "healbulb",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medjuice-healbulb",
      "quantity": 25
    }
  },
  {
    "code": "medrefined-healbulb2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
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
        "code": "healbulb",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medjuice-healbulb",
      "quantity": 50
    }
  },
  {
    "code": "medrefined-healbulb3",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
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
        "code": "healbulb",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medjuice-healbulb",
      "quantity": 75
    }
  },
  {
    "code": "medcookie1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medrefined-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.25
      },
      {
        "code": "healbulb",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:nutribar-general",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:nutribar-healing",
      "quantity": 1
    }
  },
  {
    "code": "medcookie2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medrefined-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.5
      },
      {
        "code": "healbulb",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:nutribar-general",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:nutribar-healing",
      "quantity": 2
    }
  },
  {
    "code": "medcookie",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "concetrate",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medrefined-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 0.75
      },
      {
        "code": "healbulb",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:nutribar-general",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:nutribar-healing",
      "quantity": 3
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · medrefine</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>medjuice</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>medjuice</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "medrefine-1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "medjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medjuice-healbulb",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medrefined-healbulb",
      "quantity": 50
    }
  },
  {
    "code": "medrefine-1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "medjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:medjuice-aloe",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:medrefined-healbulb",
      "quantity": 50
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · milk-dry</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>drymilk</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>drymilk</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>drymilk</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>drymilk</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "saltymilk-dry",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 9000
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "drymilk",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:saltmilkportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:longmilk-dry",
      "quantity": 1
    }
  },
  {
    "code": "saltymilk-dry",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 9000
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "drymilk",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:saltmilkportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:longmilk-dry",
      "quantity": 2
    }
  },
  {
    "code": "saltymilk-dry",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 9000
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "drymilk",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:saltmilkportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:longmilk-dry",
      "quantity": 3
    }
  },
  {
    "code": "saltymilk-dry",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 9000
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "drymilk",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:saltmilkportion",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 4,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:longmilk-dry",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · milk-normal</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>drymilk</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>drymilk</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "normalmilk",
    "perishableProps": {
      "freshHours": {
        "avg": 72
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "drymilk",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:longmilk-dry"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1
      },
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
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:milkportion",
      "quantity": 100
    }
  },
  {
    "code": "normalmilk",
    "perishableProps": {
      "freshHours": {
        "avg": 72
      },
      "transitionHours": {
        "avg": 48
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "drymilk",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:longmilk-dry"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2
      },
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
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "game:milkportion",
      "quantity": 200
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · syrup</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>sugarjuice</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：3；最多数量：3 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>syrup</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "syrup-beet-1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-beet",
      "quantity": 20
    }
  },
  {
    "code": "syrup-beet-2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-beet",
      "quantity": 40
    }
  },
  {
    "code": "syrup-beet-3",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-beet",
      "quantity": 60
    }
  },
  {
    "code": "syrup-beet-4",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 4,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-beet",
      "quantity": 80
    }
  },
  {
    "code": "syrup-cane-1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-cane",
      "quantity": 40
    }
  },
  {
    "code": "syrup-cane-2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-cane",
      "quantity": 80
    }
  },
  {
    "code": "syrup-cane-3",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-cane",
      "quantity": 160
    }
  },
  {
    "code": "syrup-cane-4",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "sugarjuice",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:sugarjuice-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 4,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:syrup-cane",
      "quantity": 320
    }
  },
  {
    "code": "sugar-beet-1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 1
    }
  },
  {
    "code": "sugar-beet-2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 2
    }
  },
  {
    "code": "sugar-beet-3",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 3
    }
  },
  {
    "code": "sugar-beet-4",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-beet",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 4,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 4
    }
  },
  {
    "code": "sugar-cane-1",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 1,
        "maxQuantity": 1,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 1
    }
  },
  {
    "code": "sugar-cane-2",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 2,
        "maxQuantity": 2,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 2
    }
  },
  {
    "code": "sugar-cane-3",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 3,
        "maxQuantity": 3,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 3
    }
  },
  {
    "code": "sugar-cane-4",
    "perishableProps": {
      "type": "None",
      "freshHours": {
        "avg": 2156
      },
      "transitionHours": {
        "avg": 200
      },
      "transitionRatio": 1,
      "transitionedStack": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "shape": {
      "base": "game:block/food/meal/liquid"
    },
    "isfood": true,
    "ingredients": [
      {
        "code": "syrup",
        "validStacks": [
          {
            "type": "item",
            "code": "pemmican:syrup-cane",
            "shapeElement": "game:bowl/water"
          }
        ],
        "minQuantity": 4,
        "maxQuantity": 4,
        "portionSizeLitres": 1
      }
    ],
    "cooksInto": {
      "type": "item",
      "code": "pemmican:sugar",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>研磨绿藻、研磨褐藻、研磨红藻、海藻肥料（生）、亚麻线、海苔片 · algae</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 海草<br><code>game:seaweed-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 研磨绿藻<br><code>pemmican:algae-grind-green</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 黄海草<br><code>game:aquatic-seagrass-yellow-section</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 研磨绿藻<br><code>pemmican:algae-grind-green</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 绿海草<br><code>game:aquatic-seagrass-green-section</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 研磨绿藻<br><code>pemmican:algae-grind-green</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 橙海草<br><code>game:aquatic-seagrass-orange-section</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 研磨褐藻<br><code>pemmican:algae-grind-brown</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 红海草<br><code>game:aquatic-seagrass-red-section</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 研磨红藻<br><code>pemmican:algae-grind-red</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KB
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 研磨褐藻<br><code>pemmican:algae-grind-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 腐烂物<br><code>game:rot</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 海藻肥料（生）<br><code>pemmican:algaefertilizer-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 研磨褐藻<br><code>pemmican:algae-grind-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 研磨绿藻<br><code>pemmican:algae-grind-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 海藻肥料（生）<br><code>pemmican:algaefertilizer-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 研磨褐藻<br><code>pemmican:algae-grind-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 研磨红藻<br><code>pemmican:algae-grind-red</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 海藻肥料（生）<br><code>pemmican:algaefertilizer-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 藻类纤维<br><code>pemmican:algae-fiber</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 亚麻线<br><code>game:flaxtwine</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KK
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 研磨绿藻<br><code>pemmican:algae-grind-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 海苔片<br><code>expandedfoods:driedseaweed-sheet</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "block",
        "code": "game:seaweed-*"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:algae-grind-green",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "block",
        "code": "game:aquatic-seagrass-yellow-section"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:algae-grind-green",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "block",
        "code": "game:aquatic-seagrass-green-section"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:algae-grind-green",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "block",
        "code": "game:aquatic-seagrass-orange-section"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:algae-grind-brown",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "block",
        "code": "game:aquatic-seagrass-red-section"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:algae-grind-red",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:algae-grind-brown"
      },
      "B": {
        "type": "item",
        "code": "game:rot"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:algaefertilizer-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:algae-grind-brown"
      },
      "B": {
        "type": "item",
        "code": "pemmican:algae-grind-green"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:algaefertilizer-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:algae-grind-brown"
      },
      "B": {
        "type": "item",
        "code": "pemmican:algae-grind-red"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:algaefertilizer-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KK",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:algae-fiber"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "game:flaxtwine",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "S",
    "enabled": false,
    "ingredients": {
      "S": {
        "type": "item",
        "code": "pemmican:algae-grind-green"
      }
    },
    "name": "seaweed",
    "width": 1,
    "height": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "expandedfoods:driedseaweed-sheet"
    }
  }
]
```

</details>

</details>

<details><summary>蜡封绷带 · bandage-wax</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 1 | 未声明附加限制 |
| 投入 B | 酒精浸透的绷带<br><code>game:bandage-alcoholed</code> | 1 | 未声明附加限制 |
| 产物 | 蜡封绷带<br><code>pemmican:heal-wax</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "W,B",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:beeswax",
        "quantity": 1
      },
      "B": {
        "type": "item",
        "code": "game:bandage-alcoholed",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:heal-wax",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>蘑菇醪液、森林蘑菇醪液 · beer-yeast</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 巴西菇<br><code>game:mushroom-almondmushroom-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 未声明；按配方类型判定 | 允许变体：['spelt', 'rye'] |
| 产物 | 蘑菇醪液<br><code>pemmican:yeast-ale</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMM
MGM
MMM
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 草菇<br><code>game:mushroom-paddystraw-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 未声明；按配方类型判定 | 允许变体：['spelt', 'rye'] |
| 产物 | 蘑菇醪液<br><code>pemmican:yeast-ale</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMM
MGM
MMM
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 野蘑菇<br><code>game:mushroom-fieldmushroom-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 未声明；按配方类型判定 | 允许变体：['spelt', 'rye'] |
| 产物 | 蘑菇醪液<br><code>pemmican:yeast-ale</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMM
MGM
MMM
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 名称未汉化（见物品代码）<br><code>game:mushroom-beardedtooth-normal-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 未声明；按配方类型判定 | 允许变体：['spelt', 'rye'] |
| 产物 | 森林蘑菇醪液<br><code>pemmican:yeast-forest</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMM
MGM
MMM
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 香菇<br><code>game:mushroom-shiitake-normal-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 未声明；按配方类型判定 | 允许变体：['spelt', 'rye'] |
| 产物 | 森林蘑菇醪液<br><code>pemmican:yeast-forest</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMM
MGM
MMM
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 名称未汉化（见物品代码）<br><code>game:mushroom-whiteoyster-normal-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 未声明；按配方类型判定 | 允许变体：['spelt', 'rye'] |
| 产物 | 森林蘑菇醪液<br><code>pemmican:yeast-forest</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MMM
MGM
MMM
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "MMM,MGM,MMM",
    "ingredients": {
      "M": {
        "type": "block",
        "code": "game:mushroom-almondmushroom-normal"
      },
      "G": {
        "type": "item",
        "code": "game:grain-*",
        "allowedVariants": [
          "spelt",
          "rye"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:yeast-ale",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MMM,MGM,MMM",
    "ingredients": {
      "M": {
        "type": "block",
        "code": "game:mushroom-paddystraw-normal"
      },
      "G": {
        "type": "item",
        "code": "game:grain-*",
        "allowedVariants": [
          "spelt",
          "rye"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:yeast-ale",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MMM,MGM,MMM",
    "ingredients": {
      "M": {
        "type": "block",
        "code": "game:mushroom-fieldmushroom-normal"
      },
      "G": {
        "type": "item",
        "code": "game:grain-*",
        "allowedVariants": [
          "spelt",
          "rye"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:yeast-ale",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MMM,MGM,MMM",
    "ingredients": {
      "M": {
        "type": "block",
        "code": "game:mushroom-beardedtooth-normal-north"
      },
      "G": {
        "type": "item",
        "code": "game:grain-*",
        "allowedVariants": [
          "spelt",
          "rye"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:yeast-forest",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MMM,MGM,MMM",
    "ingredients": {
      "M": {
        "type": "block",
        "code": "game:mushroom-shiitake-normal-north"
      },
      "G": {
        "type": "item",
        "code": "game:grain-*",
        "allowedVariants": [
          "spelt",
          "rye"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:yeast-forest",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MMM,MGM,MMM",
    "ingredients": {
      "M": {
        "type": "block",
        "code": "game:mushroom-whiteoyster-normal-north"
      },
      "G": {
        "type": "item",
        "code": "game:grain-*",
        "allowedVariants": [
          "spelt",
          "rye"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:yeast-forest",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>水果混合物 · caramel</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 水果混合物<br><code>pemmican:caramel-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_K_
BMB
BPB
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 水果混合物<br><code>pemmican:caramel-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_K_
BMB
BPB
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 水果混合物<br><code>pemmican:caramel-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_K_
BMB
BPB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_K_,BMB,BPB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:caramel-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_K_,BMB,BPB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:caramel-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_K_,BMB,BPB",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:caramel-raw",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>包装薯片、薯片 · chips-pack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 薯片<br><code>pemmican:chips-potato</code> | 5 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 包装薯片<br><code>pemmican:chips-pack</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包装薯片<br><code>pemmican:chips-pack</code> | 1 | 未声明附加限制 |
| 产物 | 薯片<br><code>pemmican:chips-potato</code> | 5 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "pemmican:chips-potato",
        "quantity": 5
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:chips-pack",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:chips-pack",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:chips-potato",
      "quantity": 5
    }
  }
]
```

</details>

</details>

<details><summary>玉米面团、土豆面团 · dough</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 玉米面粉<br><code>pemmican:flour-corn</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 玉米面团<br><code>pemmican:dough-corn</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
K
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 变体材料（按代码匹配）<br><code>pemmican:flour-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 土豆面团<br><code>pemmican:dough-potato</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
P
K
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 变体材料（按代码匹配）<br><code>game:flour-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 土豆面团<br><code>pemmican:dough-potato</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V
P
K
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "V,K",
    "ingredients": {
      "K": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "V": {
        "type": "item",
        "code": "pemmican:flour-corn"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:waterportion"
        },
        "requiresLitres": 1
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:dough-corn",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "V,P,K",
    "ingredients": {
      "K": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "pemmican:choppedvegetable-potato"
      },
      "V": {
        "type": "item",
        "code": "pemmican:flour-*"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:waterportion"
        },
        "requiresLitres": 1
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:dough-potato",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "V,P,K",
    "ingredients": {
      "K": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "pemmican:choppedvegetable-potato"
      },
      "V": {
        "type": "item",
        "code": "game:flour-*"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:waterportion"
        },
        "requiresLitres": 1
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:dough-potato",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>包装鱼、盐腌鱼 · fish-pack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐腌鱼<br><code>game:fish-cured</code> | 16 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 包装鱼<br><code>pemmican:fish-pack</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包装鱼<br><code>pemmican:fish-pack</code> | 1 | 未声明附加限制 |
| 产物 | 盐腌鱼<br><code>game:fish-cured</code> | 16 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "game:fish-cured",
        "quantity": 16
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:fish-pack",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:fish-pack",
        "quantity": 1,
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "game:fish-cured",
      "quantity": 16
    }
  }
]
```

</details>

</details>

<details><summary>活球果种子 · healingbulb-seeds</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 活球果<br><code>pemmican:healbulb</code> | 1 | 未声明附加限制 |
| 产物 | 活球果种子<br><code>pemmican:seeds-healbulb</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:healbulb",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:seeds-healbulb",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>草药敷剂、芦苇药膏敷剂、亚麻药膏敷剂 · healingherb</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 W | 干草<br><code>game:drygrass</code> | 2 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:flower-*-free</code> | 未声明；按配方类型判定 | 允许变体：['catmint', 'cornflower', 'heater', 'wilddaisy', 'goldenpoppy', 'lillyofthevalley', 'woad'] |
| 产物 | 草药敷剂<br><code>pemmican:healingherb-flower</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
F
W
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 治疗药膏<br><code>pemmican:heal-salve</code> | 1 | 未声明附加限制 |
| 投入 F | 香蒲<br><code>game:cattailtops</code> | 2 | 未声明附加限制 |
| 产物 | 芦苇药膏敷剂<br><code>pemmican:poultice-reed-salve</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
F
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 治疗药膏<br><code>pemmican:heal-salve</code> | 1 | 未声明附加限制 |
| 投入 F | 纸莎草<br><code>game:papyrustops</code> | 2 | 未声明附加限制 |
| 产物 | 芦苇药膏敷剂<br><code>pemmican:poultice-reed-salve</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
F
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 治疗药膏<br><code>pemmican:heal-salve</code> | 1 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:linen-{pattern}-down</code> | 1 | 未声明附加限制 |
| 产物 | 亚麻药膏敷剂<br><code>pemmican:poultice-linen-salve</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
F
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "K,F,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "W": {
        "type": "item",
        "code": "game:drygrass",
        "quantity": 2
      },
      "F": {
        "type": "block",
        "code": "game:flower-*-free",
        "name": "variant",
        "allowedVariants": [
          "catmint",
          "cornflower",
          "heater",
          "wilddaisy",
          "goldenpoppy",
          "lillyofthevalley",
          "woad"
        ]
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:healingherb-flower",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,F",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:heal-salve",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:poultice-reed-salve",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,F",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:heal-salve",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:poultice-reed-salve",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,F",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:heal-salve",
        "quantity": 1
      },
      "F": {
        "type": "block",
        "code": "game:linen-{pattern}-down",
        "quantity": 1,
        "allowedvariants": [
          "normal",
          "offset",
          "diamond",
          "square"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:poultice-linen-salve",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>肉串（生）、蘑菇串（生） · kebab</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:*-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 肉串（生）<br><code>pemmican:kebab-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__M
KV_
S__
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:*-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 肉串（生）<br><code>pemmican:kebab-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__M
KV_
S__
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蘑菇串（生）<br><code>pemmican:kebab-mushroom-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__M
KV_
S__
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:*-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 变体材料（按代码匹配）<br><code>pemmican:*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 肉串（生）<br><code>pemmican:kebab-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__M
KV_
S__
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": true,
    "ingredientPattern": "__M,KV_,S__",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "M": {
        "type": "item",
        "code": "game:*-raw",
        "name": "meat",
        "allowedvariants": [
          "redmeat",
          "bushmeat",
          "poultry",
          "fish"
        ]
      },
      "V": {
        "type": "block",
        "code": "game:*",
        "name": "ingredient",
        "allowedvariants": [
          "mushroom-fieldmushroom-normal",
          "mushroom-almondmushroom-normal",
          "mushroom-blacktrumpet-normal",
          "mushroom-chanterelle-normal",
          "mushroom-commonmorel-normal",
          "mushroom-golddropmilkcap-normal",
          "mushroom-greencrackedrussula-normal",
          "mushroom-indigomilkcap-normal",
          "mushroom-kingbolete-normal",
          "mushroom-lobster-normal",
          "mushroom-orangeoakbolete-normal",
          "mushroom-paddystraw-normal",
          "mushroom-puffball-normal",
          "mushroom-redwinecap-normal",
          "mushroom-saffronmilkcap-normal",
          "mushroom-violetwebcap-normal",
          "mushroom-beardedtooth-normal-north",
          "mushroom-chickenofthewoods-normal-north",
          "mushroom-dryadsaddle-normal-north",
          "mushroom-pinkoyster-normal-north",
          "mushroom-whiteoyster-normal-north",
          "mushroom-reishi-normal-north",
          "mushroom-tinderhoof-normal-north",
          "mushroom-deerear-normal-north",
          "mushroom-livermushroom-normal-north",
          "mushroom-shiitake-normal-north"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "pemmican:kebab-raw"
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "__M,KV_,S__",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "M": {
        "type": "item",
        "code": "game:*-raw",
        "name": "meat",
        "allowedvariants": [
          "redmeat",
          "bushmeat",
          "poultry",
          "fish"
        ]
      },
      "V": {
        "type": "item",
        "code": "game:*",
        "name": "ingredient",
        "allowedvariants": [
          "vegetable-carrot",
          "vegetable-onion",
          "vegetable-cabbage",
          "vegetable-turnip",
          "vegetable-parsnip",
          "vegetable-olive",
          "vegetable-pumpkin",
          "vegetable-cassava",
          "cattailroot",
          "papyrusroot",
          "pickledvegetable-carrot",
          "pickledvegetable-onion",
          "pickledvegetable-cabbage",
          "pickledvegetable-turnip",
          "pickledvegetable-parsnip",
          "pickledvegetable-olive"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "pemmican:kebab-raw"
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "__M,KV_,S__",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "M": {
        "type": "block",
        "code": "game:*",
        "name": "ingredient",
        "allowedvariants": [
          "mushroom-fieldmushroom-normal",
          "mushroom-almondmushroom-normal",
          "mushroom-blacktrumpet-normal",
          "mushroom-chanterelle-normal",
          "mushroom-commonmorel-normal",
          "mushroom-golddropmilkcap-normal",
          "mushroom-greencrackedrussula-normal",
          "mushroom-indigomilkcap-normal",
          "mushroom-kingbolete-normal",
          "mushroom-lobster-normal",
          "mushroom-orangeoakbolete-normal",
          "mushroom-paddystraw-normal",
          "mushroom-puffball-normal",
          "mushroom-redwinecap-normal",
          "mushroom-saffronmilkcap-normal",
          "mushroom-violetwebcap-normal",
          "mushroom-beardedtooth-normal-north",
          "mushroom-chickenofthewoods-normal-north",
          "mushroom-dryadsaddle-normal-north",
          "mushroom-pinkoyster-normal-north",
          "mushroom-whiteoyster-normal-north",
          "mushroom-reishi-normal-north",
          "mushroom-tinderhoof-normal-north",
          "mushroom-deerear-normal-north",
          "mushroom-livermushroom-normal-north",
          "mushroom-shiitake-normal-north"
        ]
      },
      "V": {
        "type": "block",
        "code": "game:*",
        "name": "ingredient1",
        "allowedvariants": [
          "mushroom-fieldmushroom-normal",
          "mushroom-almondmushroom-normal",
          "mushroom-blacktrumpet-normal",
          "mushroom-chanterelle-normal",
          "mushroom-commonmorel-normal",
          "mushroom-golddropmilkcap-normal",
          "mushroom-greencrackedrussula-normal",
          "mushroom-indigomilkcap-normal",
          "mushroom-kingbolete-normal",
          "mushroom-lobster-normal",
          "mushroom-orangeoakbolete-normal",
          "mushroom-paddystraw-normal",
          "mushroom-puffball-normal",
          "mushroom-redwinecap-normal",
          "mushroom-saffronmilkcap-normal",
          "mushroom-violetwebcap-normal",
          "mushroom-beardedtooth-normal-north",
          "mushroom-chickenofthewoods-normal-north",
          "mushroom-dryadsaddle-normal-north",
          "mushroom-pinkoyster-normal-north",
          "mushroom-whiteoyster-normal-north",
          "mushroom-reishi-normal-north",
          "mushroom-tinderhoof-normal-north",
          "mushroom-deerear-normal-north",
          "mushroom-livermushroom-normal-north",
          "mushroom-shiitake-normal-north"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "pemmican:kebab-mushroom-raw"
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "__M,KV_,S__",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "M": {
        "type": "item",
        "code": "game:*-raw",
        "name": "meat",
        "allowedvariants": [
          "redmeat",
          "bushmeat",
          "poultry",
          "fish"
        ]
      },
      "V": {
        "type": "item",
        "code": "pemmican:*",
        "name": "ingredient",
        "allowedvariants": [
          "vegetable-potato-raw",
          "vegetable-sugarbeet-raw",
          "vegetable-corn-raw"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "pemmican:kebab-raw"
    }
  }
]
```

</details>

</details>

<details><summary>包装红肉、盐腌红肉、包装野味肉、盐腌野味、包装白肉、盐腌禽肉 · meat-pack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐腌红肉<br><code>game:redmeat-cured</code> | 16 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 包装红肉<br><code>pemmican:curedmeatpack-red</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包装红肉<br><code>pemmican:curedmeatpack-red</code> | 1 | 未声明附加限制 |
| 产物 | 盐腌红肉<br><code>game:redmeat-cured</code> | 16 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐腌野味<br><code>game:bushmeat-cured</code> | 16 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 包装野味肉<br><code>pemmican:curedmeatpack-bushmeat</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包装野味肉<br><code>pemmican:curedmeatpack-bushmeat</code> | 1 | 未声明附加限制 |
| 产物 | 盐腌野味<br><code>game:bushmeat-cured</code> | 16 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐腌禽肉<br><code>game:poultry-cured</code> | 16 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 包装白肉<br><code>pemmican:curedmeatpack-poultry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包装白肉<br><code>pemmican:curedmeatpack-poultry</code> | 1 | 未声明附加限制 |
| 产物 | 盐腌禽肉<br><code>game:poultry-cured</code> | 16 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 16
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:curedmeatpack-red",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:curedmeatpack-red",
        "quantity": 1,
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "game:redmeat-cured",
      "quantity": 16
    }
  },
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "game:bushmeat-cured",
        "quantity": 16
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:curedmeatpack-bushmeat",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:curedmeatpack-bushmeat",
        "quantity": 1,
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "game:bushmeat-cured",
      "quantity": 16
    }
  },
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "game:poultry-cured",
        "quantity": 16
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:curedmeatpack-poultry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:curedmeatpack-poultry",
        "quantity": 1,
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "game:poultry-cured",
      "quantity": 16
    }
  }
]
```

</details>

</details>

<details><summary>蘑菇酱包装、蘑菇酱 · mushroom-pack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 5 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蘑菇酱包装<br><code>pemmican:mushroom-pack</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 蘑菇酱包装<br><code>pemmican:mushroom-pack</code> | 1 | 未声明附加限制 |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 5 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "pemmican:mushroompatebar",
        "quantity": 5
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:mushroom-pack",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:mushroom-pack",
        "quantity": 1,
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 5
    }
  }
]
```

</details>

</details>

<details><summary>清洗过的蘑菇 · mushroomclean</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:mushroom-*-normal</code> | 未声明；按配方类型判定 | 允许变体：['livermushroom', 'shiitake', 'fieldmushroom', 'almondmushroom', 'blacktrumpet', 'chanterelle', 'commonmorel', 'greencrackedrussula', 'indigomilkcap', 'kingbolete', 'lobster', 'orangeoakbolete', 'paddystraw', 'puffball', 'redwinecap', 'saffronmilkcap', 'violetwebcap', 'beardedtooth', 'whiteoyster', 'pinkoyster', 'witchhat', 'dryadsaddle', 'tinderhoof', 'chickenofthewoods', 'reishi', 'deerear', 'aniseedfunnel', 'aspenbolete', 'birchbolete', 'blewit', 'bluechanterelle', 'candycap', 'coccora', 'flattoppedclubcoral', 'friedchickenmushroom', 'hawkwing', 'hedgehogmushroom', 'honeymushroom', 'matsutake', 'parasol', 'purplefairyclub', 'queenbolete', 'redramaria', 'shaggymane', 'shrimpmushroom', 'slipperyjack', 'stinkhorn', 'winterchanterelle', 'beefsteakfungus'] |
| 产物 | 清洗过的蘑菇<br><code>pemmican:mushroomclean-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NW
G_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:mushroom-*-normal</code> | 未声明；按配方类型判定 | 允许变体：['livermushroom', 'shiitake', 'fieldmushroom', 'almondmushroom', 'blacktrumpet', 'chanterelle', 'commonmorrel', 'greencrackedrussula', 'indigomilkcap', 'kingbolete', 'lobster', 'orangeoatbolete', 'paddystraw', 'puffball', 'redwinecap', 'saffronmilkcap', 'violetwebcap', 'beardedtooth', 'whiteoyster', 'pinkoyster', 'witchhat', 'dryadsaddle', 'tinderhoof', 'chickenofthewoods', 'reishi', 'deerear', 'aniseedfunnel', 'aspenbolete', 'birchbolete', 'blewit', 'bluechanterelle', 'candycap', 'coccora', 'flattoppedclubcoral', 'friedchickenmushroom', 'hawkwing', 'hedgehogmushroom', 'honeymushroom', 'matsutake', 'parasol', 'purplefairyclub', 'queenbolete', 'redramaria', 'shaggymane', 'shrimpmushroom', 'slipperyjack', 'stinkhorn', 'winterchanterelle', 'beefsteakfungus'] |
| 产物 | 清洗过的蘑菇<br><code>pemmican:mushroomclean-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NW
G_
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:mushroom-*-normal</code> | 未声明；按配方类型判定 | 允许变体：['livermushroom', 'shiitake', 'fieldmushroom', 'almondmushroom', 'blacktrumpet', 'chanterelle', 'commonmorrel', 'greencrackedrussula', 'indigomilkcap', 'kingbolete', 'lobster', 'orangeoatbolete', 'paddystraw', 'puffball', 'redwinecap', 'saffronmilkcap', 'violetwebcap', 'beardedtooth', 'whiteoyster', 'pinkoyster', 'witchhat', 'dryadsaddle', 'tinderhoof', 'chickenofthewoods', 'reishi', 'deerear', 'aniseedfunnel', 'aspenbolete', 'birchbolete', 'blewit', 'bluechanterelle', 'candycap', 'coccora', 'flattoppedclubcoral', 'friedchickenmushroom', 'hawkwing', 'hedgehogmushroom', 'honeymushroom', 'matsutake', 'parasol', 'purplefairyclub', 'queenbolete', 'redramaria', 'shaggymane', 'shrimpmushroom', 'slipperyjack', 'stinkhorn', 'winterchanterelle', 'beefsteakfungus'] |
| 产物 | 清洗过的蘑菇<br><code>pemmican:mushroomclean-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NW
G_
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:mushroom-*-normal-north</code> | 未声明；按配方类型判定 | 允许变体：['beardedtooth', 'dryadsaddle', 'pinkoyster', 'tinderhoof', 'chickenofthewoods', 'reishi', 'deerear', 'whiteoyster', 'shiitake', 'livermushroom', 'beefsteakfungus'] |
| 产物 | 清洗过的蘑菇<br><code>pemmican:mushroomclean-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NW
G_
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:mushroom-*-normal-north</code> | 未声明；按配方类型判定 | 允许变体：['beardedtooth', 'dryadsaddle', 'pinkoyster', 'tinderhoof', 'chickenofthewoods', 'reishi', 'deerear', 'whiteoyster', 'shiitake', 'livermushroom', 'beefsteakfungus'] |
| 产物 | 清洗过的蘑菇<br><code>pemmican:mushroomclean-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NW
G_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:mushroom-*-normal-north</code> | 未声明；按配方类型判定 | 允许变体：['beardedtooth', 'dryadsaddle', 'pinkoyster', 'tinderhoof', 'chickenofthewoods', 'reishi', 'deerear', 'whiteoyster', 'shiitake', 'livermushroom', 'beefsteakfungus'] |
| 产物 | 清洗过的蘑菇<br><code>pemmican:mushroomclean-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NW
G_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "NW,G_",
    "ingredients": {
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "G": {
        "type": "block",
        "code": "game:mushroom-*-normal",
        "name": "variant",
        "allowedVariants": [
          "livermushroom",
          "shiitake",
          "fieldmushroom",
          "almondmushroom",
          "blacktrumpet",
          "chanterelle",
          "commonmorel",
          "greencrackedrussula",
          "indigomilkcap",
          "kingbolete",
          "lobster",
          "orangeoakbolete",
          "paddystraw",
          "puffball",
          "redwinecap",
          "saffronmilkcap",
          "violetwebcap",
          "beardedtooth",
          "whiteoyster",
          "pinkoyster",
          "witchhat",
          "dryadsaddle",
          "tinderhoof",
          "chickenofthewoods",
          "reishi",
          "deerear",
          "aniseedfunnel",
          "aspenbolete",
          "birchbolete",
          "blewit",
          "bluechanterelle",
          "candycap",
          "coccora",
          "flattoppedclubcoral",
          "friedchickenmushroom",
          "hawkwing",
          "hedgehogmushroom",
          "honeymushroom",
          "matsutake",
          "parasol",
          "purplefairyclub",
          "queenbolete",
          "redramaria",
          "shaggymane",
          "shrimpmushroom",
          "slipperyjack",
          "stinkhorn",
          "winterchanterelle",
          "beefsteakfungus"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "waterportion"
        },
        "requiresLitres": 0.5
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:mushroomclean-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NW,G_",
    "ingredients": {
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "G": {
        "type": "block",
        "code": "game:mushroom-*-normal",
        "name": "variant",
        "allowedVariants": [
          "livermushroom",
          "shiitake",
          "fieldmushroom",
          "almondmushroom",
          "blacktrumpet",
          "chanterelle",
          "commonmorrel",
          "greencrackedrussula",
          "indigomilkcap",
          "kingbolete",
          "lobster",
          "orangeoatbolete",
          "paddystraw",
          "puffball",
          "redwinecap",
          "saffronmilkcap",
          "violetwebcap",
          "beardedtooth",
          "whiteoyster",
          "pinkoyster",
          "witchhat",
          "dryadsaddle",
          "tinderhoof",
          "chickenofthewoods",
          "reishi",
          "deerear",
          "aniseedfunnel",
          "aspenbolete",
          "birchbolete",
          "blewit",
          "bluechanterelle",
          "candycap",
          "coccora",
          "flattoppedclubcoral",
          "friedchickenmushroom",
          "hawkwing",
          "hedgehogmushroom",
          "honeymushroom",
          "matsutake",
          "parasol",
          "purplefairyclub",
          "queenbolete",
          "redramaria",
          "shaggymane",
          "shrimpmushroom",
          "slipperyjack",
          "stinkhorn",
          "winterchanterelle",
          "beefsteakfungus"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "waterportion"
        },
        "requiresLitres": 0.5
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:mushroomclean-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NW,G_",
    "ingredients": {
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "G": {
        "type": "block",
        "code": "game:mushroom-*-normal",
        "name": "variant",
        "allowedVariants": [
          "livermushroom",
          "shiitake",
          "fieldmushroom",
          "almondmushroom",
          "blacktrumpet",
          "chanterelle",
          "commonmorrel",
          "greencrackedrussula",
          "indigomilkcap",
          "kingbolete",
          "lobster",
          "orangeoatbolete",
          "paddystraw",
          "puffball",
          "redwinecap",
          "saffronmilkcap",
          "violetwebcap",
          "beardedtooth",
          "whiteoyster",
          "pinkoyster",
          "witchhat",
          "dryadsaddle",
          "tinderhoof",
          "chickenofthewoods",
          "reishi",
          "deerear",
          "aniseedfunnel",
          "aspenbolete",
          "birchbolete",
          "blewit",
          "bluechanterelle",
          "candycap",
          "coccora",
          "flattoppedclubcoral",
          "friedchickenmushroom",
          "hawkwing",
          "hedgehogmushroom",
          "honeymushroom",
          "matsutake",
          "parasol",
          "purplefairyclub",
          "queenbolete",
          "redramaria",
          "shaggymane",
          "shrimpmushroom",
          "slipperyjack",
          "stinkhorn",
          "winterchanterelle",
          "beefsteakfungus"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "waterportion"
        },
        "requiresLitres": 0.5
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:mushroomclean-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NW,G_",
    "ingredients": {
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "G": {
        "type": "block",
        "code": "game:mushroom-*-normal-north",
        "name": "variant",
        "allowedVariants": [
          "beardedtooth",
          "dryadsaddle",
          "pinkoyster",
          "tinderhoof",
          "chickenofthewoods",
          "reishi",
          "deerear",
          "whiteoyster",
          "shiitake",
          "livermushroom",
          "beefsteakfungus"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "waterportion"
        },
        "requiresLitres": 0.5
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:mushroomclean-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NW,G_",
    "ingredients": {
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "G": {
        "type": "block",
        "code": "game:mushroom-*-normal-north",
        "name": "variant",
        "allowedVariants": [
          "beardedtooth",
          "dryadsaddle",
          "pinkoyster",
          "tinderhoof",
          "chickenofthewoods",
          "reishi",
          "deerear",
          "whiteoyster",
          "shiitake",
          "livermushroom",
          "beefsteakfungus"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "waterportion"
        },
        "requiresLitres": 0.5
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:mushroomclean-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NW,G_",
    "ingredients": {
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "G": {
        "type": "block",
        "code": "game:mushroom-*-normal-north",
        "name": "variant",
        "allowedVariants": [
          "beardedtooth",
          "dryadsaddle",
          "pinkoyster",
          "tinderhoof",
          "chickenofthewoods",
          "reishi",
          "deerear",
          "whiteoyster",
          "shiitake",
          "livermushroom",
          "beefsteakfungus"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "waterportion"
        },
        "requiresLitres": 0.5
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:mushroomclean-raw",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>蘑菇酱 · mushroompate</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 蘑菇泥（干燥）<br><code>pemmican:mushroompate-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 未声明；按配方类型判定 | 允许变体：['onion', 'carrot', 'parsnip'] |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 腌蘑菇<br><code>pemmican:mushroomclean-pickled</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 未声明；按配方类型判定 | 允许变体：['onion', 'carrot', 'parsnip'] |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 蘑菇泥（干燥）<br><code>pemmican:mushroompate-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 腌蘑菇<br><code>pemmican:mushroomclean-pickled</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 蘑菇泥（干燥）<br><code>pemmican:mushroompate-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 未声明；按配方类型判定 | 允许变体：['onion', 'carrot', 'parsnip'] |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 腌蘑菇<br><code>pemmican:mushroomclean-pickled</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 未声明；按配方类型判定 | 允许变体：['onion', 'carrot', 'parsnip'] |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 蘑菇泥（干燥）<br><code>pemmican:mushroompate-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 M | 腌蘑菇<br><code>pemmican:mushroomclean-pickled</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蘑菇酱<br><code>pemmican:mushroompatebar</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
NSP
MOM
MMM
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroompate-dry"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "game:vegetable-*",
        "name": "variant",
        "allowedVariants": [
          "onion",
          "carrot",
          "parsnip"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroomclean-pickled"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "game:vegetable-*",
        "name": "variant",
        "allowedVariants": [
          "onion",
          "carrot",
          "parsnip"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroompate-dry"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "pemmican:choppedvegetable-potato"
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroomclean-pickled"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "pemmican:choppedvegetable-potato"
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat-rendered"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroompate-dry"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "game:vegetable-*",
        "name": "variant",
        "allowedVariants": [
          "onion",
          "carrot",
          "parsnip"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat-rendered"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroomclean-pickled"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "game:vegetable-*",
        "name": "variant",
        "allowedVariants": [
          "onion",
          "carrot",
          "parsnip"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat-rendered"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroompate-dry"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "pemmican:choppedvegetable-potato"
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "NSP,MOM,MMM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:fat-rendered"
      },
      "N": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "M": {
        "type": "item",
        "code": "pemmican:mushroomclean-pickled"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "O": {
        "type": "item",
        "code": "pemmican:choppedvegetable-potato"
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:mushroompatebar",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>营养棒包装、营养棒 · nutri-pack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 营养棒<br><code>pemmican:nutribar-general</code> | 5 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒包装<br><code>pemmican:nutri-pack</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 营养棒包装<br><code>pemmican:nutri-pack</code> | 1 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 5 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "pemmican:nutribar-general",
        "quantity": 5
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:nutri-pack",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:nutri-pack",
        "quantity": 1,
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 5
    }
  }
]
```

</details>

</details>

<details><summary>营养棒 · nutribar</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 花生<br><code>game:legume-peanut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 花生<br><code>game:legume-peanut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 花生<br><code>game:legume-peanut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 向日葵种子<br><code>game:grain-sunflower</code> | 2 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 向日葵种子<br><code>game:grain-sunflower</code> | 2 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 向日葵种子<br><code>game:grain-sunflower</code> | 2 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 向日葵种子<br><code>game:grain-sunflower</code> | 2 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 果泥软糖<br><code>pemmican:caramel-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 花生<br><code>game:legume-peanut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 未声明附加限制 |
| 投入 M | 果泥软糖<br><code>pemmican:caramel-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐<br><code>game:salt</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 营养棒<br><code>pemmican:nutribar-general</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
MK
BP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:legume-peanut"
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.1
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:legume-peanut"
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.1
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:legume-peanut"
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.1
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:grain-sunflower",
        "quantity": 2
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.1
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:grain-sunflower",
        "quantity": 2
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.1
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:grain-sunflower",
        "quantity": 2
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.1
      }
    },
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:grain-sunflower",
        "quantity": 2
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "item",
        "code": "pemmican:caramel-dry"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "MK,BP",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:legume-peanut"
      },
      "B": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2
      },
      "M": {
        "type": "item",
        "code": "pemmican:caramel-dry"
      },
      "P": {
        "type": "item",
        "code": "game:salt"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:nutribar-general",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>亚麻线、羊皮纸 · papyrus-fiber</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 纸莎草纤维<br><code>pemmican:papyrus-fiber</code> | 1 | 未声明附加限制 |
| 产物 | 亚麻线<br><code>game:flaxtwine</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KK
KK
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 纸莎草纤维<br><code>pemmican:papyrus-fiber</code> | 1 | 未声明附加限制 |
| 产物 | 羊皮纸<br><code>game:paper-parchment</code> | 3 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KKK
KKK
KKK
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "KK,KK",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:papyrus-fiber",
        "quantity": 1
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "game:flaxtwine",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KKK,KKK,KKK",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "pemmican:papyrus-fiber",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "game:paper-parchment",
      "quantity": 3
    }
  }
]
```

</details>

</details>

<details><summary>生肉干饼、盐渍肉干饼、包装肉干饼、陈年牛肉（未烹饪） · pemmican</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生野味<br><code>game:bushmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生野味<br><code>game:bushmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生红肉<br><code>game:redmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 2 | 工具 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生红肉<br><code>game:redmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生红肉<br><code>game:redmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 盐<br><code>game:salt</code> | 2 | 未声明附加限制 |
| 投入 P | 肉干饼<br><code>pemmican:pemmican-bar</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_
P_
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 6 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 包装肉干饼<br><code>pemmican:pemmican-pack</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包装肉干饼<br><code>pemmican:pemmican-pack</code> | 1 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 6 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 盐腌红肉<br><code>game:redmeat-cured</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 陈年牛肉（未烹饪）<br><code>pemmican:redmeat-vintageraw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 盐腌红肉<br><code>game:redmeat-cured</code> | 1 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 陈年牛肉（未烹饪）<br><code>pemmican:redmeat-vintageraw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 盐腌红肉<br><code>game:redmeat-cured</code> | 1 | 未声明附加限制 |
| 投入 K | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 陈年牛肉（未烹饪）<br><code>pemmican:redmeat-vintageraw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 2 | 工具 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生野味<br><code>game:bushmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生野味<br><code>game:bushmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生野味<br><code>game:bushmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生红肉<br><code>game:redmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生红肉<br><code>game:redmeat-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生鱼<br><code>game:fish-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生鱼<br><code>game:fish-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生鱼<br><code>game:fish-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生鱼<br><code>game:fish-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 21**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌鱼<br><code>game:fish-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 22**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌鱼<br><code>game:fish-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 23**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌鱼<br><code>game:fish-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 24**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌鱼<br><code>game:fish-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 25**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌红肉<br><code>game:redmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 26**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌红肉<br><code>game:redmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 27**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌红肉<br><code>game:redmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 28**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌红肉<br><code>game:redmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 29**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌野味<br><code>game:bushmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 30**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌野味<br><code>game:bushmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 31**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌野味<br><code>game:bushmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 32**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌野味<br><code>game:bushmeat-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 33**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生禽肉<br><code>game:poultry-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 34**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生禽肉<br><code>game:poultry-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 35**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生禽肉<br><code>game:poultry-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 36**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 生禽肉<br><code>game:poultry-raw</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生肉干饼<br><code>pemmican:pemmican-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 37**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌禽肉<br><code>game:poultry-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 38**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 棒槌<br><code>game:club-generic-wood</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌禽肉<br><code>game:poultry-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 39**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌禽肉<br><code>game:poultry-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

**方案 40**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 盐腌禽肉<br><code>game:poultry-cured</code> | 2 | 未声明附加限制 |
| 投入 F | 脂肪块<br><code>game:fat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 盐渍肉干饼<br><code>pemmican:pemmican-salt</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
BBB
MFM
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 2,
        "isTool": true
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "S_,P_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:salt",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "pemmican:pemmican-bar"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "pemmican:pemmican-salt",
        "quantity": 6
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-pack",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:pemmican-pack",
        "quantity": 1,
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 6
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 1
      },
      "K": {
        "type": "block",
        "code": "game:bowl-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:redmeat-vintageraw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 1
      },
      "K": {
        "type": "block",
        "code": "game:jug-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:redmeat-vintageraw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 1
      },
      "K": {
        "type": "block",
        "code": "game:woodbucket"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "honeyportion"
        },
        "requiresLitres": 0.25
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:redmeat-vintageraw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 2,
        "isTool": true
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:fish-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 3,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:redmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 5,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 5,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 5,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:bushmeat-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 5,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-raw",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 4,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 6,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:club-generic-wood",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 6,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 6,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,BBB,MFM",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "item",
        "code": "game:fruit-*"
      },
      "M": {
        "type": "item",
        "code": "game:poultry-cured",
        "quantity": 2
      },
      "F": {
        "type": "item",
        "code": "game:fat"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 6,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:pemmican-salt",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · rusks-pack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>pemmican:rusks-{type}-dry</code> | 16 | 未声明附加限制 |
| 投入 C | 草席<br><code>game:rushmat</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>pemmican:ruskspack-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
P
C
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 变体材料（按代码匹配）<br><code>pemmican:ruskspack-{type}</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>pemmican:rusks-{type}-dry</code> | 16 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "R,P,C",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "P": {
        "type": "item",
        "code": "pemmican:rusks-{type}-dry",
        "quantity": 16,
        "alowwedvariants": [
          "spelt",
          "rye",
          "flax",
          "rice",
          "cassava",
          "amaranth",
          "sunflower",
          "corn",
          "potato"
        ]
      },
      "C": {
        "type": "block",
        "code": "game:rushmat"
      }
    },
    "width": 1,
    "height": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:ruskspack-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,P",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-generic-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "pemmican:ruskspack-{type}",
        "quantity": 1,
        "alowwedvariants": [
          "spelt",
          "rye",
          "flax",
          "rice",
          "cassava",
          "amaranth",
          "sunflower",
          "corn",
          "potato"
        ],
        "returnedStack": {
          "type": "block",
          "code": "game:rushmat",
          "quantity": 1
        }
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-{type}-dry",
      "quantity": 16
    }
  }
]
```

</details>

</details>

<details><summary>切片斯佩耳特面包、切片黑麦面包、切片亚麻面包、切片米面包、切片木薯面包、切片苋菜面包、切片葵花籽面包、生玉米面包干、生土豆面包干 · rusks</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 斯佩耳特小麦面包<br><code>game:bread-spelt-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切片斯佩耳特面包<br><code>pemmican:rusks-spelt-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 黑麦面包<br><code>game:bread-rye-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切片黑麦面包<br><code>pemmican:rusks-rye-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 亚麻面包<br><code>game:bread-flax-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切片亚麻面包<br><code>pemmican:rusks-flax-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 稻米面包<br><code>game:bread-rice-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切片米面包<br><code>pemmican:rusks-rice-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 木薯面包<br><code>game:bread-cassava-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切片木薯面包<br><code>pemmican:rusks-cassava-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 千穗谷籽面包<br><code>game:bread-amaranth-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切片苋菜面包<br><code>pemmican:rusks-amaranth-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 向日葵籽面包<br><code>game:bread-sunflower-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切片葵花籽面包<br><code>pemmican:rusks-sunflower-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 玉米面包<br><code>pemmican:bread-corn-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生玉米面包干<br><code>pemmican:rusks-corn-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 土豆面包<br><code>pemmican:bread-potato-perfect</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生土豆面包干<br><code>pemmican:rusks-potato-raw</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-spelt-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-spelt-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-rye-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-rye-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-flax-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-flax-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-rice-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-rice-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-cassava-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-cassava-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-amaranth-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-amaranth-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-sunflower-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-sunflower-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "pemmican:bread-corn-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-corn-raw",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "pemmican:bread-potato-perfect"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-potato-raw",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>斯佩耳特面包干、黑麦面包干、亚麻面包干、米面包干、木薯面包干、苋菜面包干、葵花籽面包干、玉米面包干、土豆面包干 · rusks2</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烤焦的斯佩耳特小麦面包<br><code>game:bread-spelt-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 斯佩耳特面包干<br><code>pemmican:rusks-spelt-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烤焦的黑麦面包<br><code>game:bread-rye-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 黑麦面包干<br><code>pemmican:rusks-rye-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烤焦的亚麻面包<br><code>game:bread-flax-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 亚麻面包干<br><code>pemmican:rusks-flax-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烤焦的稻米面包<br><code>game:bread-rice-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 米面包干<br><code>pemmican:rusks-rice-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烤焦的木薯面包<br><code>game:bread-cassava-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木薯面包干<br><code>pemmican:rusks-cassava-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烤焦的千穗谷籽面包<br><code>game:bread-amaranth-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 苋菜面包干<br><code>pemmican:rusks-amaranth-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 向日葵籽面包（烧焦）<br><code>game:bread-sunflower-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 葵花籽面包干<br><code>pemmican:rusks-sunflower-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烧焦的玉米面包<br><code>pemmican:bread-corn-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 玉米面包干<br><code>pemmican:rusks-corn-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 B | 烧焦的土豆面包<br><code>pemmican:bread-potato-charred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 土豆面包干<br><code>pemmican:rusks-potato-dry</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-spelt-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-spelt-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-rye-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-rye-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-flax-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-flax-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-rice-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-rice-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-cassava-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-cassava-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-amaranth-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-amaranth-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "game:bread-sunflower-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-sunflower-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "pemmican:bread-corn-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-corn-dry",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,B",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "B": {
        "type": "item",
        "code": "pemmican:bread-potato-charred"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pemmican:rusks-potato-dry",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>玉米种子、土豆种子、糖用甜菜种子、甘蔗种子 · seeds</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 V | 脱粒玉米<br><code>pemmican:choppedvegetable-corn</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 玉米种子<br><code>pemmican:seeds-corn</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
V
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 V | 名称未汉化（见物品代码）<br><code>pemmican:vegetable-potato-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 土豆种子<br><code>pemmican:seeds-potato</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
V
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 V | 名称未汉化（见物品代码）<br><code>pemmican:vegetable-sugarbeet-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 糖用甜菜种子<br><code>pemmican:seeds-sugarbeet</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
V
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 V | 甘蔗<br><code>pemmican:sugarcane</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 甘蔗种子<br><code>pemmican:seeds-sugarcane</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
V
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": true,
    "ingredientPattern": "A,V",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "V": {
        "type": "item",
        "code": "pemmican:choppedvegetable-corn"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:seeds-corn",
      "quantity": 1
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "A,V",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:shears-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "V": {
        "type": "item",
        "code": "pemmican:vegetable-potato-raw"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:seeds-potato",
      "quantity": 1
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "A,V",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:shears-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "V": {
        "type": "item",
        "code": "pemmican:vegetable-sugarbeet-raw"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:seeds-sugarbeet",
      "quantity": 1
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "A,V",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:shears-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "V": {
        "type": "block",
        "code": "pemmican:sugarcane"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:seeds-sugarcane",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>切碎的土豆、切碎的腌土豆 · vegetable</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 V | 名称未汉化（见物品代码）<br><code>pemmican:vegetable-potato-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切碎的土豆<br><code>pemmican:choppedvegetable-potato</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
V
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 V | 腌土豆<br><code>pemmican:pickledvegetable-pickledpotato</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 切碎的腌土豆<br><code>pemmican:choppedvegetable-pickledpotato</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
V
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "K,V",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "V": {
        "type": "item",
        "code": "pemmican:vegetable-potato-raw"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:choppedvegetable-potato",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,V",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "V": {
        "type": "item",
        "code": "pemmican:pickledvegetable-pickledpotato"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "pemmican:choppedvegetable-pickledpotato",
      "quantity": 1
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
