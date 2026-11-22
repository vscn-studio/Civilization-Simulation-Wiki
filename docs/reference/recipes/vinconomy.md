<!-- generated:start -->
# 经济系统：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>名称未汉化（见物品代码） · reimbursement-shop</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店收银机<br><code>shopregister-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>shopcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shopregister-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "shopregister-*"
      },
      "C": {
        "type": "item",
        "code": "shopcoupon"
      }
    },
    "mergeAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "shopregister-north",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · reimbursement-stall</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 商店武器架<br><code>weaponplaque-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>stallcoupon</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SC
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "SC",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "weaponplaque-*"
      },
      "C": {
        "type": "item",
        "code": "stallcoupon"
      }
    },
    "copyAttributesFrom": "S",
    "width": 2,
    "height": 1,
    "_shapeless": true,
    "output": {
      "type": "block",
      "code": "weaponplaque-north",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · tenretni</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:book-normal-*</code> | 未声明；按配方类型判定 | 允许变体：['brickred', 'cherryred', 'darkbeige', 'darkgray', 'darkgreen', 'darkolive', 'gray', 'olive', 'orange', 'orangebrown', 'purple', 'purpleorange', 'teal'] |
| 投入 Q | 墨水和羽毛笔<br><code>game:inkandquill</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>book-tenretni-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BQ
G_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>book-tenretni-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>book-tenretni-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
T
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "BQ,G_",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:book-normal-*",
        "allowedVariants": [
          "brickred",
          "cherryred",
          "darkbeige",
          "darkgray",
          "darkgreen",
          "darkolive",
          "gray",
          "olive",
          "orange",
          "orangebrown",
          "purple",
          "purpleorange",
          "teal"
        ],
        "name": "color"
      },
      "Q": {
        "type": "item",
        "code": "game:inkandquill"
      },
      "G": {
        "type": "item",
        "code": "game:gear-temporal"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "book-tenretni-{color}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "T",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "book-tenretni-*",
        "name": "color"
      }
    },
    "recipeGroup": 1,
    "width": 1,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "book-tenretni-{color}",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>商店目录 · catalog</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 商店账本<br><code>ledger</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 商店目录<br><code>catalog</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BQ
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "BQ",
  "ingredients": {
    "B": {
      "type": "item",
      "code": "ledger"
    },
    "Q": {
      "type": "item",
      "code": "game:gear-temporal"
    }
  },
  "recipeGroup": 1,
  "width": 2,
  "height": 1,
  "output": {
    "type": "item",
    "code": "catalog",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · clothingstall</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:hay-normal-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 I | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuth', 'bismuthbronze', 'blackbronze', 'brass', 'copper', 'gold', 'silver', 'iron', 'lead', 'meteoriciron', 'tinbronze', 'steel', 'tin', 'uranium', 'zinc'] |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>clothingstall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WHW
WHW
ICI
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "WHW,WHW,ICI",
  "ingredients": {
    "H": {
      "type": "block",
      "code": "game:hay-normal-ud"
    },
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "secondary",
      "allowedVariants": [
        "birch",
        "oak",
        "maple",
        "pine",
        "acacia",
        "kapok",
        "baldcypress",
        "larch",
        "redwood",
        "ebony",
        "walnut",
        "purpleheart"
      ]
    },
    "I": {
      "type": "item",
      "code": "game:ingot-*",
      "name": "primary",
      "allowedVariants": [
        "bismuth",
        "bismuthbronze",
        "blackbronze",
        "brass",
        "copper",
        "gold",
        "silver",
        "iron",
        "lead",
        "meteoriciron",
        "tinbronze",
        "steel",
        "tin",
        "uranium",
        "zinc"
      ]
    },
    "C": {
      "type": "block",
      "code": "game:chest-east",
      "attributes": {
        "type": "normal-generic"
      }
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "clothingstall-north",
    "attributes": {
      "PrimaryMaterial": "{primary}",
      "SecondaryMaterial": "{secondary}"
    }
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · couponcutter</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cleaver-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>couponslicer-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
__C
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "__C,PPP",
  "ingredients": {
    "C": {
      "type": "item",
      "code": "game:cleaver-*"
    },
    "P": {
      "type": "item",
      "code": "game:plank-*"
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "couponslicer-north"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · gachastall</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:metalplate-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuth', 'bismuthbronze', 'blackbronze', 'brass', 'copper', 'gold', 'silver', 'iron', 'lead', 'meteoriciron', 'tinbronze', 'steel', 'tin', 'uranium', 'zinc'] |
| 投入 S | 变体材料（按代码匹配）<br><code>game:metalplate-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuth', 'bismuthbronze', 'blackbronze', 'brass', 'copper', 'gold', 'silver', 'iron', 'lead', 'meteoriciron', 'tinbronze', 'steel', 'tin', 'uranium', 'zinc'] |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>gachastall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PP
GC
SS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "PP,GC,SS",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:metalplate-*",
        "name": "primary",
        "allowedVariants": [
          "bismuth",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "copper",
          "gold",
          "silver",
          "iron",
          "lead",
          "meteoriciron",
          "tinbronze",
          "steel",
          "tin",
          "uranium",
          "zinc"
        ]
      },
      "S": {
        "type": "item",
        "code": "game:metalplate-*",
        "name": "secondary",
        "allowedVariants": [
          "bismuth",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "copper",
          "gold",
          "silver",
          "iron",
          "lead",
          "meteoriciron",
          "tinbronze",
          "steel",
          "tin",
          "uranium",
          "zinc"
        ]
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "deco"
      },
      "C": {
        "type": "block",
        "code": "game:chest-east",
        "attributes": {
          "type": "normal-generic"
        }
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "gachastall-north",
      "attributes": {
        "PrimaryMaterial": "{primary}",
        "SecondaryMaterial": "{secondary}",
        "DecoMaterial": "{deco}"
      }
    }
  }
]
```

</details>

</details>

<details><summary>商店账本 · ledger</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:book-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 墨水和羽毛笔<br><code>game:inkandquill</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 商店账本<br><code>ledger</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BQ
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "BQ",
  "ingredients": {
    "B": {
      "type": "item",
      "code": "game:book-*"
    },
    "Q": {
      "type": "item",
      "code": "game:inkandquill"
    }
  },
  "recipeGroup": 1,
  "width": 2,
  "height": 1,
  "output": {
    "type": "item",
    "code": "ledger",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · mealtable</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 变体材料（按代码匹配）<br><code>game:claypot-*-fired</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>buffettable-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WCW
W_W
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "WWW,WCW,W_W",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "wood",
      "allowedVariants": [
        "birch",
        "oak",
        "maple",
        "pine",
        "acacia",
        "kapok",
        "baldcypress",
        "larch",
        "redwood",
        "ebony",
        "walnut",
        "purpleheart"
      ]
    },
    "C": {
      "type": "block",
      "code": "game:claypot-*-fired",
      "quantity": 4
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "buffettable-north",
    "attributes": {
      "PrimaryMaterial": "{wood}"
    }
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · producecrate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>crate-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WOW
WWW
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "WOW,WWW",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "wood",
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
    "O": {
      "type": "block",
      "code": "game:chest-east",
      "attributes": {
        "type": "normal-generic"
      }
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "crate-north",
    "attributes": {
      "PrimaryMaterial": "{wood}"
    }
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · purchasecrate</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['acacia', 'baldcypress', 'birch', 'ebony', 'kapok', 'larch', 'maple', 'oak', 'pine', 'purpleheart', 'redwood', 'walnut'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:crate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>purchasestall-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_WW
WOW
WWW
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-acacia"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "acacia",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-baldcypress"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "baldcypress",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-birch"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "birch",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-ebony"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "ebony",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-kapok"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "kapok",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-larch"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "larch",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-maple"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "maple",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-oak"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "oak",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-pine"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "pine",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-purpleheart"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "purpleheart",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-redwood"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "redwood",
        "SecondaryMaterial": "{wood}"
      }
    }
  },
  {
    "ingredientPattern": "_WW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
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
      "O": {
        "type": "block",
        "code": "game:crate",
        "attributes": {
          "type": "wood-walnut"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "purchasestall-north",
      "attributes": {
        "PrimaryMaterial": "walnut",
        "SecondaryMaterial": "{wood}"
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · sculpturestand</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>sculpturestand-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_C_
WWW
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_C_,WWW",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "wood",
      "allowedVariants": [
        "birch",
        "oak",
        "maple",
        "pine",
        "acacia",
        "kapok",
        "baldcypress",
        "larch",
        "redwood",
        "ebony",
        "walnut",
        "purpleheart"
      ]
    },
    "C": {
      "type": "block",
      "code": "game:chest-east",
      "attributes": {
        "type": "normal-generic"
      }
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "sculpturestand-east",
    "attributes": {
      "PrimaryMaterial": "{wood}"
    }
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shopbarrel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 I | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuth', 'bismuthbronze', 'blackbronze', 'brass', 'copper', 'gold', 'silver', 'iron', 'lead', 'meteoriciron', 'tinbronze', 'steel', 'tin', 'uranium', 'zinc'] |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shopbarrel-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SWS
IWI
SWS
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SWS,IWI,SWS",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "primary",
        "allowedVariants": [
          "birch",
          "oak",
          "maple",
          "pine",
          "acacia",
          "kapok",
          "baldcypress",
          "larch",
          "redwood",
          "ebony",
          "walnut",
          "purpleheart"
        ]
      },
      "I": {
        "type": "item",
        "code": "game:ingot-*",
        "name": "secondary",
        "allowedVariants": [
          "bismuth",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "copper",
          "gold",
          "silver",
          "iron",
          "lead",
          "meteoriciron",
          "tinbronze",
          "steel",
          "tin",
          "uranium",
          "zinc"
        ]
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "shopbarrel-north",
      "attributes": {
        "PrimaryMaterial": "{primary}",
        "SecondaryMaterial": "{secondary}"
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shopdispenser</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 I | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuth', 'bismuthbronze', 'blackbronze', 'brass', 'copper', 'gold', 'silver', 'iron', 'lead', 'meteoriciron', 'tinbronze', 'steel', 'tin', 'uranium', 'zinc'] |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shopdispenser-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
G_G
WWW
WIW
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "G_G,WWW,WIW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "primary",
        "allowedVariants": [
          "birch",
          "oak",
          "maple",
          "pine",
          "acacia",
          "kapok",
          "baldcypress",
          "larch",
          "redwood",
          "ebony",
          "walnut",
          "purpleheart"
        ]
      },
      "I": {
        "type": "item",
        "code": "game:ingot-*",
        "name": "secondary",
        "allowedVariants": [
          "bismuth",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "copper",
          "gold",
          "silver",
          "iron",
          "lead",
          "meteoriciron",
          "tinbronze",
          "steel",
          "tin",
          "uranium",
          "zinc"
        ]
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free",
        "name": "deco"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "shopdispenser-north",
      "attributes": {
        "PrimaryMaterial": "{primary}",
        "SecondaryMaterial": "{secondary}",
        "DecoMaterial": "{deco}"
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shopmat</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['black', 'blue', 'brown', 'gray', 'green', 'mordant', 'orange', 'pink', 'plain', 'purple', 'red', 'white', 'yellow'] |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shopmat-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
CCC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_S_,CCC",
  "ingredients": {
    "C": {
      "type": "item",
      "code": "game:cloth-*",
      "name": "cloth",
      "allowedVariants": [
        "black",
        "blue",
        "brown",
        "gray",
        "green",
        "mordant",
        "orange",
        "pink",
        "plain",
        "purple",
        "red",
        "white",
        "yellow"
      ]
    },
    "S": {
      "type": "block",
      "code": "game:chest-east",
      "attributes": {
        "type": "normal-generic"
      }
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "shopmat-north",
    "attributes": {
      "PrimaryMaterial": "{cloth}"
    }
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shopmatdouble</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['black', 'blue', 'brown', 'gray', 'green', 'mordant', 'orange', 'pink', 'plain', 'purple', 'red', 'white', 'yellow'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shopmatdouble-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_OC
CCW
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_OC,CCW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "secondary",
        "allowedVariants": [
          "birch",
          "oak",
          "maple",
          "pine",
          "acacia",
          "kapok",
          "baldcypress",
          "larch",
          "redwood",
          "ebony",
          "walnut",
          "purpleheart"
        ]
      },
      "C": {
        "type": "item",
        "code": "game:cloth-*",
        "name": "primary",
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "gray",
          "green",
          "mordant",
          "orange",
          "pink",
          "plain",
          "purple",
          "red",
          "white",
          "yellow"
        ]
      },
      "O": {
        "type": "block",
        "code": "game:chest-east",
        "attributes": {
          "type": "normal-generic"
        }
      }
    },
    "recipeGroup": 1,
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "shopmatdouble-north",
      "attributes": {
        "PrimaryMaterial": "{primary}",
        "SecondaryMaterial": "{secondary}"
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shopregister</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 变体材料（按代码匹配）<br><code>game:metalplate-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuth', 'bismuthbronze', 'blackbronze', 'brass', 'copper', 'gold', 'silver', 'iron', 'lead', 'meteoriciron', 'tinbronze', 'steel', 'tin', 'uranium', 'zinc'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shopregister-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
COC
WWW
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "WWW,COC,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "secondary",
        "allowedVariants": [
          "birch",
          "oak",
          "maple",
          "pine",
          "acacia",
          "kapok",
          "baldcypress",
          "larch",
          "redwood",
          "ebony",
          "walnut",
          "purpleheart"
        ]
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-*",
        "name": "primary",
        "allowedVariants": [
          "bismuth",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "copper",
          "gold",
          "silver",
          "iron",
          "lead",
          "meteoriciron",
          "tinbronze",
          "steel",
          "tin",
          "uranium",
          "zinc"
        ]
      },
      "O": {
        "type": "block",
        "code": "game:chest-east",
        "attributes": {
          "type": "normal-generic"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "shopregister-north",
      "attributes": {
        "PrimaryMaterial": "{primary}",
        "SecondaryMaterial": "{secondary}"
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shopshelf</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shopshelf-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
__C
WWW
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "WWW,__C,WWW",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "wood",
      "allowedVariants": [
        "birch",
        "oak",
        "maple",
        "pine",
        "acacia",
        "kapok",
        "baldcypress",
        "larch",
        "redwood",
        "ebony",
        "walnut",
        "purpleheart"
      ]
    },
    "C": {
      "type": "block",
      "code": "game:chest-east",
      "attributes": {
        "type": "normal-generic"
      }
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "shopshelf-north",
    "attributes": {
      "PrimaryMaterial": "{wood}"
    }
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · shoptoolrack</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shoptoolrack-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
_C_
WWW
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "WWW,_C_,WWW",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "wood",
      "allowedVariants": [
        "birch",
        "oak",
        "maple",
        "pine",
        "acacia",
        "kapok",
        "baldcypress",
        "larch",
        "redwood",
        "ebony",
        "walnut",
        "purpleheart"
      ]
    },
    "C": {
      "type": "block",
      "code": "game:chest-east",
      "attributes": {
        "type": "normal-generic"
      }
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "shoptoolrack-north",
    "attributes": {
      "PrimaryMaterial": "{wood}"
    }
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · tellermachine</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 变体材料（按代码匹配）<br><code>game:metalplate-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuth', 'bismuthbronze', 'blackbronze', 'brass', 'copper', 'gold', 'silver', 'iron', 'lead', 'meteoriciron', 'tinbronze', 'steel', 'tin', 'uranium', 'zinc'] |
| 投入 O | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>autoteller-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W__
COC
WWW
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "W__,COC,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "secondary",
        "allowedVariants": [
          "birch",
          "oak",
          "maple",
          "pine",
          "acacia",
          "kapok",
          "baldcypress",
          "larch",
          "redwood",
          "ebony",
          "walnut",
          "purpleheart"
        ]
      },
      "C": {
        "type": "item",
        "code": "game:metalplate-*",
        "name": "primary",
        "allowedVariants": [
          "bismuth",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "copper",
          "gold",
          "silver",
          "iron",
          "lead",
          "meteoriciron",
          "tinbronze",
          "steel",
          "tin",
          "uranium",
          "zinc"
        ]
      },
      "O": {
        "type": "block",
        "code": "game:chest-east",
        "attributes": {
          "type": "normal-generic"
        }
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "autoteller-north",
      "attributes": {
        "PrimaryMaterial": "{primary}",
        "SecondaryMaterial": "{secondary}"
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · weaponplaque</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 允许变体：['birch', 'oak', 'maple', 'pine', 'acacia', 'kapok', 'baldcypress', 'larch', 'redwood', 'ebony', 'walnut', 'purpleheart'] |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:chest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>weaponplaque-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_W_
WCW
_W_
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_W_,WCW,_W_",
  "ingredients": {
    "W": {
      "type": "item",
      "code": "game:plank-*",
      "name": "wood",
      "allowedVariants": [
        "birch",
        "oak",
        "maple",
        "pine",
        "acacia",
        "kapok",
        "baldcypress",
        "larch",
        "redwood",
        "ebony",
        "walnut",
        "purpleheart"
      ]
    },
    "C": {
      "type": "block",
      "code": "game:chest-east",
      "attributes": {
        "type": "normal-generic"
      }
    }
  },
  "recipeGroup": 1,
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "weaponplaque-north",
    "attributes": {
      "PrimaryMaterial": "{wood}"
    }
  }
}
```

</details>

</details>
<!-- generated:end -->
