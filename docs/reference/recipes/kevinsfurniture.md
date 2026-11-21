<!-- generated:start -->
# 家具：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · angledwindows</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:glasspane-leaded-*-ew</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>angledwindowl-closed-{type}-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WS
_W
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:glasspane-leaded-*-ew</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>angledwindowr-closed-{type}-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SW
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/angledwindows.json`

```json
[
  {
    "ingredientPattern": "WS,_W",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:glasspane-leaded-*-ew",
        "name": "type"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "block",
      "code": "angledwindowl-closed-{type}-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SW,W_",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:glasspane-leaded-*-ew",
        "name": "type"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "block",
      "code": "angledwindowr-closed-{type}-east",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · cabinets</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['aged', 'veryaged'] |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 架子<br><code>game:shelf-normal-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>cabinet-east-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WSW
WNW
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['aged', 'veryaged'] |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 架子<br><code>game:shelf-normal-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>DoorlessCabinet-east-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/cabinets.json`

```json
[
  {
    "ingredientPattern": "WWW,WSW,WNW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "type",
        "skipVariants": [
          "aged",
          "veryaged"
        ]
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "block",
        "code": "game:shelf-normal-*"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "cabinet-east-{type}"
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "type",
        "skipVariants": [
          "aged",
          "veryaged"
        ]
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "block",
        "code": "game:shelf-normal-*"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "DoorlessCabinet-east-{type}"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · canopy</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:supportbeam*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 3 | 排除变体：['mordant'] |
| 投入 M | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>canopy-closed-{type}-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LLL
LCL
MCM
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/canopy.json`

```json
{
  "ingredientPattern": "LLL,LCL,MCM",
  "ingredients": {
    "L": {
      "type": "block",
      "code": "game:supportbeam*"
    },
    "C": {
      "type": "item",
      "code": "game:cloth-*",
      "name": "type",
      "quantity": 3,
      "skipVariants": [
        "mordant"
      ]
    },
    "M": {
      "type": "item",
      "code": "game:metalnailsandstrips-*",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "canopy-closed-{type}-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · celticbed</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 名称未汉化（见物品代码）<br><code>game:bed-wood-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>celticbed-head-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BB
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/celticbed.json`

```json
{
  "ingredientPattern": "BB",
  "ingredients": {
    "B": {
      "type": "block",
      "code": "game:bed-wood-head-north"
    }
  },
  "width": 2,
  "height": 1,
  "shapeless": true,
  "output": {
    "type": "block",
    "code": "celticbed-head-north",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · coffeetable</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['aged', 'veryaged'] |
| 投入 Q | 白水晶<br><code>game:clearquartz</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>coffeetable-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PQP
PPP
P_P
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/coffeetable.json`

```json
{
  "ingredientPattern": "PQP,PPP,P_P",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:plank-*",
      "name": "type",
      "skipVariants": [
        "aged",
        "veryaged"
      ]
    },
    "Q": {
      "type": "item",
      "code": "game:clearquartz"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "coffeetable-{type}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · cushion</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 1 | 允许变体：['plain', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'] |
| 产物 | 变体材料（按代码匹配）<br><code>floor_cushion-{color}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_L_
T_T
_L_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/cushion.json`

```json
[
  {
    "ingredientPattern": "_L_,T_T,_L_",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "game:flaxtwine"
      },
      "L": {
        "type": "item",
        "code": "game:cloth-*",
        "quantity": 1,
        "name": "color",
        "allowedVariants": [
          "plain",
          "blue",
          "brown",
          "gray",
          "black",
          "green",
          "orange",
          "pink",
          "purple",
          "red",
          "white",
          "yellow"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "floor_cushion-{color}"
    }
  }
]
```

</details>

</details>

<details><summary>毛皮铺盖 · furroll</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:hide-pelt-*</code> | 1 | 允许变体：['medium', 'large', 'huge'] |
| 投入 S | 针线包<br><code>game:sewingkit</code> | 2 | 未声明附加限制 |
| 产物 | 毛皮铺盖<br><code>furroll-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
P_P
_P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 小型毛皮<br><code>game:hide-pelt-small</code> | 2 | 未声明附加限制 |
| 投入 S | 针线包<br><code>game:sewingkit</code> | 2 | 未声明附加限制 |
| 产物 | 毛皮铺盖<br><code>furroll-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
P_P
_P_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/furroll.json`

```json
[
  {
    "ingredientPattern": "PSP,P_P,_P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:hide-pelt-*",
        "allowedVariants": [
          "medium",
          "large",
          "huge"
        ],
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:sewingkit",
        "quantity": 2
      }
    },
    "name": "furroll",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "furroll-head-north"
    }
  },
  {
    "ingredientPattern": "PSP,P_P,_P_",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:hide-pelt-small",
        "quantity": 2
      },
      "S": {
        "type": "item",
        "code": "game:sewingkit",
        "quantity": 2
      }
    },
    "name": "furroll",
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "output": {
      "type": "block",
      "code": "furroll-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>伽利略温度计 · galileo</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:debarkedlog-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 玻璃<br><code>game:glass-plain</code> | 1 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 伽利略温度计<br><code>galileothermometer</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
G_
G_
LS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/galileo.json`

```json
[
  {
    "ingredientPattern": "G_,G_,LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:debarkedlog-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-plain",
        "quantity": 1
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "galileothermometer"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · knifeblock</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:debarkedlog-*-ud</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>knifeblock-east-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_K
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/knifeblock.json`

```json
{
  "ingredientPattern": "_K,W_",
  "ingredients": {
    "W": {
      "type": "block",
      "code": "game:debarkedlog-*-ud",
      "name": "type",
      "allowedVariants": [
        "acacia",
        "baldcypress",
        "birch",
        "ebony",
        "kapok",
        "larch",
        "maple",
        "oak",
        "pine",
        "purpleheart",
        "redwood",
        "walnut"
      ]
    },
    "K": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true
    }
  },
  "width": 2,
  "height": 2,
  "output": {
    "type": "block",
    "code": "knifeblock-east-{type}"
  }
}
```

</details>

</details>

<details><summary>皮革门帘 · leatherflap</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 小型毛皮<br><code>game:hide-pelt-small</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革门帘<br><code>leatherflap-closed-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
_L
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/leatherflap.json`

```json
{
  "ingredientPattern": "KL,_L",
  "ingredients": {
    "K": {
      "type": "item",
      "code": "game:knife-*",
      "istool": true
    },
    "L": {
      "type": "item",
      "code": "game:hide-pelt-small"
    }
  },
  "width": 2,
  "height": 2,
  "output": {
    "type": "block",
    "code": "leatherflap-closed-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · nightstand</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstand-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
W_W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/nightstand.json`

```json
{
  "ingredientPattern": "WWW,WNW,W_W",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*"
    },
    "N": {
      "type": "item",
      "code": "game:metalnailsandstrips-*"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "nightstand-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · nightstandfancy</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 橡木木材<br><code>game:plank-oak</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 金合欢木木材<br><code>game:plank-acacia</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 落羽杉木木材<br><code>game:plank-baldcypress</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 桦木木材<br><code>game:plank-birch</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 黑檀木木材<br><code>game:plank-ebony</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木棉木木材<br><code>game:plank-kapok</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 落叶松木木材<br><code>game:plank-larch</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 枫木木材<br><code>game:plank-maple</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 松木木材<br><code>game:plank-pine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 紫心木木材<br><code>game:plank-purpleheart</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 红杉木木材<br><code>game:plank-redwood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 胡桃木木材<br><code>game:plank-walnut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 古木木材<br><code>game:plank-aged</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 名称未汉化（见物品代码）<br><code>nightstandfancy-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WNW
WSW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/nightstandfancy.json`

```json
[
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-oak"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "oak"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-acacia"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "acacia"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-baldcypress"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "baldcypress"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-birch"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "birch"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-ebony"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "ebony"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-kapok"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "kapok"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-larch"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "larch"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-maple"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "maple"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-pine"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "pine"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-purpleheart"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "purpleheart"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-redwood"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "redwood"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-walnut"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "walnut"
      }
    }
  },
  {
    "ingredientPattern": "WWW,WNW,WSW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-aged"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "nightstandfancy-east",
      "attributes": {
        "type": "aged"
      }
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · primitivestool</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:debarkedlog-*-ud</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>primitivestool-east-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_W_
SKS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/primitivestool.json`

```json
{
  "ingredientPattern": "_W_,SKS",
  "ingredients": {
    "W": {
      "type": "block",
      "code": "game:debarkedlog-*-ud",
      "name": "type",
      "allowedVariants": [
        "acacia",
        "baldcypress",
        "birch",
        "ebony",
        "kapok",
        "larch",
        "maple",
        "oak",
        "pine",
        "purpleheart",
        "redwood",
        "walnut"
      ]
    },
    "S": {
      "type": "item",
      "code": "game:stick",
      "quantity": 2
    },
    "K": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "primitivestool-east-{type}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · shoerack</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['aged', 'veryaged'] |
| 投入 S | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>shoerack-east-{type}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
S_S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/shoerack.json`

```json
{
  "ingredientPattern": "WWW,S_S",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "type",
      "skipVariants": [
        "aged",
        "veryaged"
      ]
    },
    "S": {
      "type": "item",
      "code": "game:stick",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "shoerack-east-{type}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · slidewindow</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:glasspane-leaded-*-ew</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>slidewindow-closed-{type}-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/slidewindow.json`

```json
{
  "ingredientPattern": "W,W",
  "ingredients": {
    "W": {
      "type": "block",
      "code": "game:glasspane-leaded-*-ew",
      "name": "type"
    }
  },
  "width": 1,
  "height": 2,
  "shapeless": false,
  "output": {
    "type": "block",
    "code": "slidewindow-closed-{type}-east",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · smallwindows</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:glasspane-leaded-*-ew</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>smallwindows-closed-{type}-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/smallwindows.json`

```json
{
  "ingredientPattern": "S,W",
  "ingredients": {
    "W": {
      "type": "block",
      "code": "game:glasspane-leaded-*-ew",
      "name": "type"
    },
    "S": {
      "type": "item",
      "code": "game:saw-*",
      "isTool": true
    }
  },
  "width": 1,
  "height": 2,
  "shapeless": false,
  "output": {
    "type": "block",
    "code": "smallwindows-closed-{type}-east",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · stove</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 起火器<br><code>game:firestarter</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>stove-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CCC
CFC
CCC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/stove.json`

```json
{
  "ingredientPattern": "CCC,CFC,CCC",
  "ingredients": {
    "C": {
      "type": "item",
      "code": "game:metalplate-copper"
    },
    "F": {
      "type": "item",
      "code": "game:firestarter"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "stove-east"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · swingwindow</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:glasspane-leaded-*-ew</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>swingwindow-closed-{type}-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/swingwindow.json`

```json
{
  "ingredientPattern": "W",
  "ingredients": {
    "W": {
      "type": "block",
      "code": "game:glasspane-leaded-*-ew",
      "name": "type"
    }
  },
  "width": 1,
  "height": 1,
  "shapeless": false,
  "output": {
    "type": "block",
    "code": "swingwindow-closed-{type}-east",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>高架子 · tallshelf</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:shelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 高架子<br><code>tallshelf-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WSW
W_W
W_W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/tallshelf.json`

```json
{
  "ingredientPattern": "WSW,W_W,W_W",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:stick"
    },
    "S": {
      "type": "block",
      "code": "game:shelf-normal-east"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "tallshelf-north"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、名称未汉化（见物品代码） · tallwindows</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:glasspane-leaded-*-ew</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>tallwindowl-closed-{type}-east</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W_W
W_W
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-aged-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-aged-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-acacia-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-acacia-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-baldcypress-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-baldcypress-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-birch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-birch-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-ebony-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-ebony-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-kapok-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-kapok-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-larch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-larch-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-maple-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-maple-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-oak-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-oak-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-pine-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-pine-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-purpleheart-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-purpleheart-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-redwood-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-redwood-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-walnut-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-walnut-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-aged-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-aged-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-acacia-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-acacia-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-baldcypress-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-baldcypress-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-birch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-birch-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-ebony-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-ebony-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-kapok-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-kapok-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 21**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-larch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-larch-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 22**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-maple-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-maple-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 23**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-oak-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-oak-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 24**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-pine-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-pine-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 25**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-purpleheart-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-purpleheart-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 26**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-redwood-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-redwood-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

**方案 27**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>tallwindowl-closed-walnut-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>tallwindowr-closed-walnut-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/tallwindows.json`

```json
[
  {
    "ingredientPattern": "W_W,W_W",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:glasspane-leaded-*-ew",
        "name": "type"
      }
    },
    "width": 3,
    "height": 2,
    "shapeless": false,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-{type}-east",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-aged-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-aged-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-acacia-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-acacia-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-baldcypress-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-baldcypress-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-birch-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-birch-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-ebony-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-ebony-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-kapok-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-kapok-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-larch-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-larch-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-maple-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-maple-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-oak-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-oak-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-pine-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-pine-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-purpleheart-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-purpleheart-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-redwood-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-redwood-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowr-closed-walnut-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowl-closed-walnut-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-aged-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-aged-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-acacia-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-acacia-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-baldcypress-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-baldcypress-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-birch-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-birch-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-ebony-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-ebony-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-kapok-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-kapok-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-larch-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-larch-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-maple-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-maple-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-oak-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-oak-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-pine-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-pine-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-purpleheart-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-purpleheart-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-redwood-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-redwood-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "R",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "tallwindowl-closed-walnut-east"
      }
    },
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "tallwindowr-closed-walnut-east",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · wardrobe</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 s | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>wardrobe-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
sss
K__
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/kevinsfurniture/recipes/grid/wardrobe.json`

```json
{
  "ingredientPattern": "sss,K__",
  "ingredients": {
    "s": {
      "type": "item",
      "code": "game:stick"
    },
    "K": {
      "type": "item",
      "code": "game:knife-*",
      "istool": true
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "wardrobe-east"
  }
}
```

</details>

</details>
<!-- generated:end -->
