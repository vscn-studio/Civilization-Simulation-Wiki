<!-- generated:start -->
# 舒适床铺：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · comfybed</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/bdtree/recipes/grid/comfybed.json`

```json
[
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "game:cloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · comfybed</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:checkeredcloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}_checkered-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/tailorsdelight/recipes/grid/comfybed.json`

```json
[
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-*",
        "name": "color",
        "allowedVariants": [
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:checkeredcloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "black",
          "blue",
          "brown",
          "gray",
          "green",
          "orange",
          "pink",
          "purple",
          "red",
          "white",
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}_checkered-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · comfybed_tailorsdelight_bdtree</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:checkeredcloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}_checkered-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/tailorsdelight/recipes/grid/comfybed_tailorsdelight_bdtree.json`

```json
[
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-*",
        "name": "color",
        "allowedVariants": [
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:checkeredcloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "black",
          "blue",
          "brown",
          "gray",
          "green",
          "orange",
          "pink",
          "purple",
          "red",
          "white",
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}_checkered-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · bed</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:bed-wood-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L__	HHH	WWW
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:bed-village-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C__	HHH	PWP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:bed-village-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C__	HHH	PWP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:bed-village-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C__	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/wool/recipes/grid/bed.json`

```json
[
  {
    "ingredientPattern": "L__\tHHH\tWWW",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "W": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:bed-wood-head-north"
    }
  },
  {
    "ingredientPattern": "C__\tHHH\tPWP",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-*"
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 3
      },
      "W": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:bed-village-head-north"
    }
  },
  {
    "ingredientPattern": "C__\tHHH\tPWP",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:cloth-*"
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 3
      },
      "W": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:bed-village-head-north"
    }
  },
  {
    "ingredientPattern": "C__\tHHH\tPWP",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-*"
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 3
      },
      "W": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:bed-village-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · comfybed</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/wool/recipes/grid/comfybed.json`

```json
[
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "game:cloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、名称未汉化（见物品代码） · comfybed_wool_bdtree</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:bed-wood-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L__	HHH	WWW
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/wool/recipes/grid/comfybed_wool_bdtree.json`

```json
[
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "L__\tHHH\tWWW",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "W": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:bed-wood-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "game:cloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · comfybed_wool_tailorsdelight</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:checkeredcloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}_checkered-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/wool/recipes/grid/comfybed_wool_tailorsdelight.json`

```json
[
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-*",
        "name": "color",
        "allowedVariants": [
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:checkeredcloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "black",
          "blue",
          "brown",
          "gray",
          "green",
          "orange",
          "pink",
          "purple",
          "red",
          "white",
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}_checkered-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · comfybed_wool_tailorsdelight_bdtree</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>tailorsdelight:checkeredcloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'black', 'blue', 'brown', 'gray', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>wool:fleece-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>bdtree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}_checkered-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/compatibility/wool/recipes/grid/comfybed_wool_tailorsdelight_bdtree.json`

```json
[
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-*",
        "name": "color",
        "allowedVariants": [
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:checkeredcloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "black",
          "blue",
          "brown",
          "gray",
          "green",
          "orange",
          "pink",
          "purple",
          "red",
          "white",
          "yellow",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "item",
        "code": "wool:fleece-*"
      },
      "P": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "bdtree:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}_checkered-head-north"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码）、变体材料（按代码匹配） · comfybed</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>*:cloth-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>*:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:bed-village-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C__	HHH	PWP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'mordant', 'blue', 'brown', 'gray', 'black', 'green', 'orange', 'pink', 'purple', 'red', 'white', 'yellow'] |
| 投入 F | 羽毛<br><code>game:feather</code> | 32 | 未声明附加限制 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>bed-comfy-{wood}-{color}-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LCF	HHH	PWP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/comfybeds/recipes/grid/comfybed.json`

```json
[
  {
    "ingredientPattern": "C__\tHHH\tPWP",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "*:cloth-*"
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 3
      },
      "W": {
        "type": "item",
        "code": "*:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:bed-village-head-north"
    }
  },
  {
    "ingredientPattern": "LCF\tHHH\tPWP",
    "recipeGroup": 1,
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-*"
      },
      "C": {
        "type": "item",
        "code": "game:cloth-*",
        "name": "color",
        "allowedVariants": [
          "plain",
          "mordant",
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
      },
      "F": {
        "type": "item",
        "code": "game:feather",
        "quantity": 32
      },
      "H": {
        "type": "block",
        "code": "game:hay-normal-ud"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3,
        "name": "wood"
      },
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2,
        "name": "wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "bed-comfy-{wood}-{color}-head-north"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
