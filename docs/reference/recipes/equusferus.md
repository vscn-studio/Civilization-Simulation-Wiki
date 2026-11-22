<!-- generated:start -->
# 野马：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配）、费鲁斯马鞍（棕色）、费鲁斯马鞍（蓝色） · wearables</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 6 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 费鲁斯马鞍（素色）<br><code>saddle-plain</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>saddle-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 费鲁斯马鞍（素色）<br><code>saddle-plain</code> | 1 | 未声明附加限制 |
| 产物 | 费鲁斯马鞍（棕色）<br><code>saddle-brown</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 费鲁斯马鞍（素色）<br><code>saddle-plain</code> | 1 | 未声明附加限制 |
| 产物 | 费鲁斯马鞍（蓝色）<br><code>saddle-blue</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "wearabledye1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "saddle-plain",
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "saddle-{color}",
      "stackSize": 1
    }
  },
  {
    "code": "saddletannin",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "saddle-plain",
        "quantity": 1
      }
    ],
    "recipeGroup": 2,
    "output": {
      "type": "item",
      "code": "saddle-brown",
      "stackSize": 1
    }
  },
  {
    "code": "wearablewoad1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "saddle-plain",
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "saddle-blue",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、费鲁斯马辔（轻衔铁）、费鲁斯马辔（勒衔） · bridleandsaddle</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:leather-normal-*</code> | 5 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 4 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>saddle-{leather}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L_L
LKL
LNL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:leather-normal-*</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 1 | 未声明附加限制 |
| 产物 | 费鲁斯马辔（轻衔铁）<br><code>bridle-hold</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LNL
L_L
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:leather-normal-*</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 1 | 未声明附加限制 |
| 产物 | 费鲁斯马辔（勒衔）<br><code>bridle-press</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L_L
LNL
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 费鲁斯马辔（轻衔铁）<br><code>bridle-hold</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 费鲁斯马辔（勒衔）<br><code>bridle-press</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 费鲁斯马辔（勒衔）<br><code>bridle-press</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 费鲁斯马辔（轻衔铁）<br><code>bridle-hold</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "L_L,LKL,LNL",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:leather-normal-*",
        "name": "leather",
        "quantity": 5
      },
      "K": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 1
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "saddle-{leather}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LNL,L_L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:leather-normal-*",
        "name": "leather",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "bridle-hold",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "L_L,LNL",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:leather-normal-*",
        "name": "leather",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "item",
      "code": "bridle-press",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "bridle-hold",
        "name": "style"
      }
    },
    "name": "bridlecontrolconv1",
    "width": 1,
    "height": 1,
    "RecipeGroup": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "bridle-press",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "bridle-press",
        "name": "style"
      }
    },
    "name": "bridlecontrolconv2",
    "width": 1,
    "height": 1,
    "RecipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "bridle-hold",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>费鲁斯马鞍（素色） · scrapedye</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>saddle-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-generic*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 费鲁斯马鞍（素色）<br><code>saddle-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TK
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "code": "mainbaguncolor3",
    "ingredientPattern": "TK",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "saddle-*",
        "name": "color"
      },
      "K": {
        "type": "item",
        "code": "game:knife-generic*",
        "IsTool": true
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "saddle-plain"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
