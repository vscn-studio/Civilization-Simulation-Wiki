<!-- generated:start -->
# 食物架：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：食品架指南


食品架：玩家指南

介绍

此模组添加了多种存储选项，例如用于展示的架子、用于装饰的篮子以及其他专用容器。某些方块还提供机械效果，例如对保鲜度、熟化或干燥速度的增益。

注意

此模组在设计时考虑了 [https://mods.vintagestory.at/expandedfoods] 扩展食品。只有安装了扩展食品模组，某些方块（例如桶架）才能熟化液体。如果没有安装，它们仍会提供与保鲜度相关的增益，但不会发生熟化过程。

方块增益

某些方块会提供对腐烂速度、熟化速度或干燥速度的增益。如果方块具有此类增益，将直接显示在鼠标悬停时的方块提示信息中。这些提示信息也可能显示有用的生活便利功能——例如， [handbook://block-foodshelves:seedbins-normal-east] 种子箱会显示其所含种子所需的养分类型。

冰块冷却机制

诸如 [handbook://block-foodshelves:coolingcabinet-normal-east] 冷藏柜和 [handbook://block-foodshelves:meatfreezer-normal-east] 肉类冷冻柜等方块，在其门关闭时提供微小的基础保鲜增益。让门敞开则会抵消此效果，因此请始终保持门关闭！

这些方块可以通过 [handbook://item-foodshelves:cutice] 冰砖进一步增强。冰块被放置在专用的抽屉中，会随时间融化，并且必须定期更换。此增益仅在主隔层和冰块抽屉都关闭时才生效，所以请务必检查好这些门！

用于装饰和保存的篮子

篮子主要用于装饰，并非为批量存储而设计。但是，当放置在 [handbook://block-foodshelves:coolingcabinet-normal-east] 冷藏柜内时，它们会继承冷藏柜的保鲜增益（无论是否使用了冰块），这使其成为一种既能保鲜又能增添时尚感的食品储存方式。

更多信息

并非所有容器都能接受所有物品。每个方块都有专门的手册条目，列出了有效的物品类型，并在相关时注明这些物品来自哪个模组。

交互操作

大多数交互操作都会通过世界交互提示（游戏内浮动的提示）显示。例如：向篮子添加物品、关闭柜门或用冰块填充抽屉。

某些交互操作不会显示，特别是当篮子位于柜子内部时。你仍然可以直接将物品放入篮子（右键单击正确的物品，或按住 CTRL 键以插入多个物品）。空手时，按住 CTRL 键可以一次取出一个物品。

尽情享受你装饰精美且功能齐全的厨房吧！

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>名称未汉化（见物品代码） · barrelrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>barrelrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
S_S
PSP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>barrelrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
S_S
PSP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>foodshelves:barrelrack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>barrelrack-top-east</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PSP,S_S,PSP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "barrelrack-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PSP,S_S,PSP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "barrelrack-normal-east"
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "foodshelves:barrelrack-normal-east"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 2,
    "shapeless": true,
    "copyAttributesFrom": "B",
    "output": {
      "type": "block",
      "code": "barrelrack-top-east",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · tun</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tun-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
NP_
SPS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tun-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPS
NP_
SPS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SPS,NP_,SPS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tun-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "SPS,NP_,SPS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tun-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · tunrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 8 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tunrack-normal-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
SNS
PSP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 8 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 8 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tunrack-normal-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
SNS
PSP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>foodshelves:tunrack-normal-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tunrack-top-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PSP,SNS,PSP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tunrack-normal-north",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PSP,SNS,PSP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 8
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "tunrack-normal-north"
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "foodshelves:tunrack-normal-north"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 2,
    "shapeless": true,
    "copyAttributesFrom": "B",
    "output": {
      "type": "block",
      "code": "tunrack-top-north",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · eggbasket</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>eggbasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__
_S
_P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>eggbasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>eggbasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "__,_S,_P",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "eggbasket-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "eggbasket-normal",
        "attributes": {
          "FSAttributes": {
            "wood": "oak"
          }
        }
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "eggbasket-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · fruitbasket</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitbasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
___
S_S
_P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>fruitbasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitbasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "___,S_S,_P_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fruitbasket-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "fruitbasket-normal",
        "attributes": {
          "FSAttributes": {
            "wood": "oak"
          }
        }
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "fruitbasket-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · mushroombasket</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>foodshelves:eggbasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>mushroombasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PBP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PBP",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "foodshelves:eggbasket-normal"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "copyAttributesFrom": "B",
    "output": {
      "type": "block",
      "code": "mushroombasket-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · vegetablebasket</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 O | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vegetablebasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_O_
S_S
P_P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 O | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vegetablebasket-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_O_
S_S
P_P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_O_,S_S,P_P",
    "ingredients": {
      "O": {
        "type": "item",
        "code": "game:stick"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      },
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "vegetablebasket-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_O_,S_S,P_P",
    "ingredients": {
      "O": {
        "type": "item",
        "code": "game:stick"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      },
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "vegetablebasket-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · coolingcabinet</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 4 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:shelf-*</code> | 3 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>coolingcabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PNP
GSG
PCP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:shelf-*</code> | 3 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>coolingcabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PNP
GSG
PCP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:shelf-*</code> | 3 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:rockpolished-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>coolingcabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PNP
GSG
PCP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PNP,GSG,PCP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 4
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 2
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "S": {
        "type": "block",
        "code": "game:shelf-*",
        "quantity": 3
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "coolingcabinet-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PNP,GSG,PCP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 2
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "S": {
        "type": "block",
        "code": "game:shelf-*",
        "quantity": 3
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "coolingcabinet-normal-east",
      "attributes": {
        "FSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PNP,GSG,PCP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 2
      },
      "G": {
        "type": "block",
        "code": "*:glass-*"
      },
      "S": {
        "type": "block",
        "code": "game:shelf-*",
        "quantity": 3
      },
      "C": {
        "type": "block",
        "code": "*:rockpolished-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "coolingcabinet-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · fruitcooler</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitcooler-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GPH
RCR
PZP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitcooler-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GPH
RCR
PZP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:rockpolished-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitcooler-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GPH
RCR
PZP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitcooler-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GPH
RCR
PZP
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitcooler-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GPH
RCR
PZP
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:rockpolished-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fruitcooler-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GPH
RCR
PZP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "GPH,RCR,PZP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fruitcooler-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "GPH,RCR,PZP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fruitcooler-normal-east",
      "attributes": {
        "FSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "GPH,RCR,PZP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "*:rockpolished-*"
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fruitcooler-normal-east"
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "GPH,RCR,PZP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fruitcooler-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "GPH,RCR,PZP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fruitcooler-normal-east",
      "attributes": {
        "FSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "GPH,RCR,PZP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "*:rockpolished-*"
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fruitcooler-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · icekeeper</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>icekeeper-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RGR
PCP
PHP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>icekeeper-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RGR
PCP
PHP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:rockpolished-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>icekeeper-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RGR
PCP
PHP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>icekeeper-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RGR
PCP
PHP
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>icekeeper-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RGR
PCP
PHP
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 4 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:rockpolished-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>icekeeper-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RGR
PCP
PHP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "RGR,PCP,PHP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "icekeeper-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "RGR,PCP,PHP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "icekeeper-normal-east",
      "attributes": {
        "FSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "RGR,PCP,PHP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "*:rockpolished-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "icekeeper-normal-east"
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "RGR,PCP,PHP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "icekeeper-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "RGR,PCP,PHP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "icekeeper-normal-east",
      "attributes": {
        "FSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "RGR,PCP,PHP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:resin",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 10
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      },
      "C": {
        "type": "block",
        "code": "*:rockpolished-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "icekeeper-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · meatfreezer</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 5 | 未声明附加限制 |
| 投入 N | 树脂<br><code>game:resin</code> | 8 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>meatfreezer-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PCP
HZN
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 5 | 未声明附加限制 |
| 投入 N | 树脂<br><code>game:resin</code> | 8 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>meatfreezer-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PCP
HZN
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 5 | 未声明附加限制 |
| 投入 N | 树脂<br><code>game:resin</code> | 8 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:rockpolished-*</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>meatfreezer-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PCP
HZN
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 5 | 未声明附加限制 |
| 投入 N | 树脂<br><code>game:resin</code> | 8 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>meatfreezer-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PCP
HZN
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 5 | 未声明附加限制 |
| 投入 N | 树脂<br><code>game:resin</code> | 8 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:rockpolished-{rock}</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>meatfreezer-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PCP
HZN
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 5 | 未声明附加限制 |
| 投入 N | 树脂<br><code>game:resin</code> | 8 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>chiseltools:truechisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 Z | 变体材料（按代码匹配）<br><code>game:ingot-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:rockpolished-*</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>meatfreezer-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PCP
HZN
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PGP,PCP,HZN",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 5
      },
      "N": {
        "type": "item",
        "code": "game:resin",
        "quantity": 8
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 20
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}",
        "quantity": 4
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "meatfreezer-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PGP,PCP,HZN",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 5
      },
      "N": {
        "type": "item",
        "code": "game:resin",
        "quantity": 8
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 20
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}",
        "quantity": 4
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "meatfreezer-normal-east",
      "attributes": {
        "FSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PGP,PCP,HZN",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 5
      },
      "N": {
        "type": "item",
        "code": "game:resin",
        "quantity": 8
      },
      "H": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 20
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "*:glass-*"
      },
      "C": {
        "type": "block",
        "code": "*:rockpolished-*",
        "quantity": 4
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "meatfreezer-normal-east"
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "PGP,PCP,HZN",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 5
      },
      "N": {
        "type": "item",
        "code": "game:resin",
        "quantity": 8
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 20
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}",
        "quantity": 4
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "meatfreezer-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "PGP,PCP,HZN",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 5
      },
      "N": {
        "type": "item",
        "code": "game:resin",
        "quantity": 8
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 20
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      },
      "C": {
        "type": "block",
        "code": "game:rockpolished-{rock}",
        "quantity": 4
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "meatfreezer-normal-east",
      "attributes": {
        "FSAttributes": {
          "rock": "{rock}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "PGP,PCP,HZN",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 5
      },
      "N": {
        "type": "item",
        "code": "game:resin",
        "quantity": 8
      },
      "H": {
        "type": "item",
        "code": "chiseltools:truechisel-*",
        "isTool": true,
        "toolDurabilityCost": 20
      },
      "Z": {
        "type": "item",
        "code": "game:ingot-{metal}"
      },
      "G": {
        "type": "block",
        "code": "*:glass-*"
      },
      "C": {
        "type": "block",
        "code": "*:rockpolished-*",
        "quantity": 4
      }
    },
    "allowedVariants": {
      "metal": [
        "zinc",
        "tin"
      ]
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "meatfreezer-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>冰砖 · cutice</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 蓝冰<br><code>game:glacierice</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 冰砖<br><code>cutice</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
IS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 蓝冰<br><code>game:ice-glacier</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 冰砖<br><code>cutice</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
IS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 致密蓝冰<br><code>game:packedglacierice</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 冰砖<br><code>cutice</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
IS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 致密蓝冰<br><code>game:ice-packedglacier</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 冰砖<br><code>cutice</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
IS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 湖冰<br><code>game:lakeice</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 冰砖<br><code>cutice</code> | 8 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
IS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "IS",
    "ingredients": {
      "I": {
        "type": "block",
        "code": "game:glacierice"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "cutice",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "IS",
    "ingredients": {
      "I": {
        "type": "block",
        "code": "game:ice-glacier"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "cutice",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "IS",
    "ingredients": {
      "I": {
        "type": "block",
        "code": "game:packedglacierice"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "cutice",
      "quantity": 8
    }
  },
  {
    "ingredientPattern": "IS",
    "ingredients": {
      "I": {
        "type": "block",
        "code": "game:ice-packedglacier"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "cutice",
      "quantity": 8
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "IS",
    "ingredients": {
      "I": {
        "type": "block",
        "code": "game:lakeice"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "cutice",
      "quantity": 8
    }
  }
]
```

</details>

</details>

<details><summary>食物展示盒、顶级食品展示盒 · fooddisplayblock</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 食物展示盒<br><code>fooddisplayblock-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
SGS
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 食物展示盒<br><code>fooddisplayblock-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
SGS
PPP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 顶级食品展示盒<br><code>fooddisplayblock-top</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
SGS
P_P
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 顶级食品展示盒<br><code>fooddisplayblock-top</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
SGS
P_P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PPP,SGS,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fooddisplayblock-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PPP,SGS,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "*:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fooddisplayblock-normal"
    }
  },
  {
    "ingredientPattern": "_P_,SGS,P_P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 2,
    "output": {
      "type": "block",
      "code": "fooddisplayblock-top",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_P_,SGS,P_P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "*:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 2,
    "output": {
      "type": "block",
      "code": "fooddisplayblock-top"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · fooddisplaycase</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fooddisplaycase-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_PP
SGP
PPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>fooddisplaycase-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_PP
SGP
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_PP,SGP,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fooddisplaycase-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_PP,SGP,PPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "fooddisplaycase-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · jar</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>jar-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SGS
SPS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>jar-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SGS
SPS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SGS,SPS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jar-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "SGS,SPS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jar-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · jarlarge</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>jarlarge-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
SGS
SSS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>jarlarge-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
SGS
SSS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_P_,SGS,SSS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jarlarge-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_P_,SGS,SSS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "*:glass-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jarlarge-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · seedbins</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 3 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>seedbins-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PSP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 3 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>*:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>seedbins-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PGP
PSP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PGP,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 3
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "seedbins-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PGP,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 3
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      },
      "G": {
        "type": "block",
        "code": "*:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "seedbins-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · wallcabinet</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>wallcabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
SGS
PSP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>wallcabinet-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
SGS
PSP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PSP,SGS,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "wallcabinet-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PSP,SGS,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "wallcabinet-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · buckethook</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>buckethook-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PS
P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>buckethook-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PS
P_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PS,P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "buckethook-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PS,P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "buckethook-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · ceilingrack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>ceilingrack-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
SRS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>ceilingrack-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
SRS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PPP,SRS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood"
      },
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "ceilingrack-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PPP,SRS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "ceilingrack-normal"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · floursack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-{cloth}</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>floursack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PCP
PSP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-{cloth}</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>floursack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PCP
PSP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>*:cloth-*</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>floursack-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PCP
PSP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PCP,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      },
      "C": {
        "type": "item",
        "code": "game:cloth-{cloth}",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "skipVariants": {
      "cloth": [
        "mordant"
      ]
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "floursack-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}",
          "cloth": "{cloth}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PCP,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "C": {
        "type": "item",
        "code": "game:cloth-{cloth}",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick",
        "quantity": 4
      }
    },
    "skipVariants": {
      "cloth": [
        "mordant"
      ]
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "floursack-normal-east",
      "attributes": {
        "FSAttributes": {
          "cloth": "{cloth}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PCP,PSP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "C": {
        "type": "item",
        "code": "*:cloth-*",
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
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "floursack-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · jarstand</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>jarstand-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_SS
SPP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>jarstand-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_SS
SPP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_SS,SPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jarstand-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_SS,SPP",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "jarstand-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · pumpkincase</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>pumpkincase-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
P_P
_P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>pumpkincase-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
P_P
_P_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_P_,P_P,_P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "pumpkincase-normal",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "_P_,P_P,_P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "pumpkincase-normal"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、名称未汉化（见物品代码） · tablewshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>game:table-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>tablewshelf-{type}-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 名称未汉化（见物品代码）<br><code>tablewshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 名称未汉化（见物品代码）<br><code>game:polishedrockslab-whitemarble-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>tablewshelf-whitemarble-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
M
S
T
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 名称未汉化（见物品代码）<br><code>tablewshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 名称未汉化（见物品代码）<br><code>game:polishedrockslab-redmarble-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>tablewshelf-redmarble-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
M
S
T
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 名称未汉化（见物品代码）<br><code>tablewshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 名称未汉化（见物品代码）<br><code>game:polishedrockslab-greenmarble-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>tablewshelf-greenmarble-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
M
S
T
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>vanvar:table-{wood}-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tablewshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TP
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>vanvar:table-{wood}-whitemarble</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tablewshelf-whitemarble-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TP
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>vanvar:table-{wood}-redmarble</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tablewshelf-redmarble-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TP
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>vanvar:table-{wood}-greenmarble</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tablewshelf-greenmarble-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "TP",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "game:table-{type}"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "skipVariants": {
      "type": [
        "aged"
      ]
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tablewshelf-{type}-east"
    }
  },
  {
    "ingredientPattern": "M,S,T",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "tablewshelf-normal-east"
      },
      "M": {
        "type": "block",
        "code": "game:polishedrockslab-whitemarble-down-free"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 2,
    "copyAttributesFrom": "T",
    "output": {
      "type": "block",
      "code": "tablewshelf-whitemarble-east"
    }
  },
  {
    "ingredientPattern": "M,S,T",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "tablewshelf-normal-east"
      },
      "M": {
        "type": "block",
        "code": "game:polishedrockslab-redmarble-down-free"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 2,
    "copyAttributesFrom": "T",
    "output": {
      "type": "block",
      "code": "tablewshelf-redmarble-east"
    }
  },
  {
    "ingredientPattern": "M,S,T",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "tablewshelf-normal-east"
      },
      "M": {
        "type": "block",
        "code": "game:polishedrockslab-greenmarble-down-free"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 2,
    "copyAttributesFrom": "T",
    "output": {
      "type": "block",
      "code": "tablewshelf-greenmarble-east"
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "TP",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "vanvar:table-{wood}-normal"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "skipVariants": {
      "wood": [
        "aged"
      ]
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tablewshelf-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "TP",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "vanvar:table-{wood}-whitemarble"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "skipVariants": {
      "wood": [
        "aged"
      ]
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tablewshelf-whitemarble-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "TP",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "vanvar:table-{wood}-redmarble"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "skipVariants": {
      "wood": [
        "aged"
      ]
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tablewshelf-redmarble-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "TP",
    "ingredients": {
      "T": {
        "type": "block",
        "code": "vanvar:table-{wood}-greenmarble"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "skipVariants": {
      "wood": [
        "aged"
      ]
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tablewshelf-greenmarble-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · barshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:breadshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>barshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
_S_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:barshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>barshelf-short-east</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": false,
    "ingredientPattern": "PPP,_S_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      },
      "S": {
        "type": "block",
        "code": "foodshelves:breadshelf-normal-east"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "barshelf-normal-east"
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "foodshelves:barshelf-normal-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "barshelf-short-east",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · breadshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>breadshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP
P_
P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>breadshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP
P_
P_
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:breadshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>breadshelf-short-east</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PP,P_,P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "breadshelf-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "PP,P_,P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "breadshelf-normal-east"
    }
  },
  {
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "foodshelves:breadshelf-normal-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "breadshelf-short-east",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · doubleshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>doubleshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
___
PPP
SSS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>doubleshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
___
PPP
SSS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "___,PPP,SSS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "doubleshelf-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "___,PPP,SSS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "doubleshelf-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · eggshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:breadshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>eggshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_P_
PSP
_P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:eggshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>eggshelf-short-east</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_P_,PSP,_P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "block",
        "code": "foodshelves:breadshelf-normal-east"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "eggshelf-normal-east"
    }
  },
  {
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "foodshelves:eggshelf-normal-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "eggshelf-short-east",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · pieshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-{wood}</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>pieshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
P
P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>pieshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
P
P
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P,P,P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:plank-{wood}",
        "quantity": 2
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "pieshelf-normal-east",
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  },
  {
    "ingredientPattern": "P,P,P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 1,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "pieshelf-normal-east"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · seedshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:pieshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>seedshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_P
_S_
P_P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:seedshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>seedshelf-short-east</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:seedshelf-short-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>seedshelf-veryshort-east</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P_P,_S_,P_P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*"
      },
      "S": {
        "type": "block",
        "code": "foodshelves:pieshelf-normal-east"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "seedshelf-normal-east"
    }
  },
  {
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "foodshelves:seedshelf-normal-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "seedshelf-short-east",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "foodshelves:seedshelf-short-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 2,
    "shapeless": true,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "seedshelf-veryshort-east",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shortshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:shelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>shortshelf-normal-east</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>vanvar:shelf-{wood}-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>shortshelf-normal-east</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:shelf-normal-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "shortshelf-normal-east",
      "quantity": 2
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "vanvar:shelf-{wood}-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "skipVariants": {
      "wood": [
        "aged"
      ]
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "shortshelf-normal-east",
      "quantity": 2,
      "attributes": {
        "FSAttributes": {
          "wood": "{wood}"
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · sushishelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:breadshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>sushishelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_P
_S_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>foodshelves:sushishelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>sushishelf-short-east</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ST
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "enabled": false,
    "ingredientPattern": "P_P,_S_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      },
      "S": {
        "type": "block",
        "code": "foodshelves:breadshelf-normal-east"
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "sushishelf-normal-east"
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "ST",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "foodshelves:sushishelf-normal-east"
      },
      "T": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "copyAttributesFrom": "S",
    "output": {
      "type": "block",
      "code": "sushishelf-short-east",
      "quantity": 2
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
