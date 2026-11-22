<!-- generated:start -->
# 砖厂：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配）、湿棕粘土砖坯 · bricks</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>brickyard:wetclaybrick-{type}</code> | 6 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 湿棕粘土砖坯<br><code>brickyard:wetclaybrick-brown</code> | 6 | 未声明附加限制 |

**加工条件：** 配方开关：False。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:clay-*",
      "name": "type",
      "allowedVariants": [
        "blue",
        "fire",
        "red"
      ]
    },
    "pattern": [
      [
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "______________",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####"
      ],
      [
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "______________",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####"
      ],
      [
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "______________",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####"
      ]
    ],
    "name": "WetClayBrick",
    "output": {
      "type": "item",
      "code": "brickyard:wetclaybrick-{type}",
      "stacksize": 6
    }
  },
  {
    "enabled": false,
    "ingredient": {
      "type": "item",
      "code": "amphorae:clay-brown"
    },
    "pattern": [
      [
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "______________",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####"
      ],
      [
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "______________",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####"
      ],
      [
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "______________",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####",
        "####_####_####"
      ]
    ],
    "name": "WetClayBrick",
    "output": {
      "type": "item",
      "code": "brickyard:wetclaybrick-brown",
      "stacksize": 6
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · adobe</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 深色土坯砖<br><code>brickyard:adoberawbrick-dark</code> | 1 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:clay-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:mudbrickslab-dark-down-free</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_C_
GGG
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 浅色土坯砖<br><code>brickyard:adoberawbrick-light</code> | 1 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:clay-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:mudbrickslab-light-down-free</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_C_
GGG
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "_C_,GGG",
    "enabled": true,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-dark",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "game:clay-*",
        "quantity": 1
      }
    },
    "name": "mudbrickslab",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "game:mudbrickslab-dark-down-free",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "_C_,GGG",
    "enabled": true,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-light",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "game:clay-*",
        "quantity": 1
      }
    },
    "name": "mudbrickslab",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "game:mudbrickslab-light-down-free",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>浅色泥砖、深色泥砖、名称未汉化（见物品代码） · adobeamphorae</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 浅色土坯砖<br><code>brickyard:adoberawbrick-light</code> | 1 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>amphorae:clay-*</code> | 1 | 未声明附加限制 |
| 产物 | 浅色泥砖<br><code>game:mudbrick-light</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GGG
GCG
GGG
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 深色土坯砖<br><code>brickyard:adoberawbrick-dark</code> | 1 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>amphorae:clay-*</code> | 1 | 未声明附加限制 |
| 产物 | 深色泥砖<br><code>game:mudbrick-dark</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GGG
GCG
GGG
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 深色土坯砖<br><code>brickyard:adoberawbrick-dark</code> | 1 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>amphorae:clay-brown</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:mudbrickslab-dark-down-free</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_C_
GGG
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 浅色土坯砖<br><code>brickyard:adoberawbrick-light</code> | 1 | 未声明附加限制 |
| 投入 C | 名称未汉化（见物品代码）<br><code>amphorae:clay-brown</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:mudbrickslab-light-down-free</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_C_
GGG
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "dependsOn": [
      {
        "modid": "amphorae"
      }
    ],
    "ingredientPattern": "GGG,GCG,GGG",
    "enabled": false,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-light",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "amphorae:clay-*",
        "quantity": 1
      }
    },
    "name": "themudbrick",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:mudbrick-light",
      "quantity": 2
    }
  },
  {
    "dependsOn": [
      {
        "modid": "amphorae"
      }
    ],
    "ingredientPattern": "GGG,GCG,GGG",
    "enabled": false,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-dark",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "amphorae:clay-*",
        "quantity": 1
      }
    },
    "name": "themudbrick",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:mudbrick-dark",
      "quantity": 2
    }
  },
  {
    "dependsOn": [
      {
        "modid": "amphorae"
      }
    ],
    "ingredientPattern": "_C_,GGG",
    "enabled": false,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-dark",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "amphorae:clay-brown",
        "quantity": 1
      }
    },
    "name": "mudbrickslab",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "game:mudbrickslab-dark-down-free",
      "quantity": 2
    }
  },
  {
    "dependsOn": [
      {
        "modid": "amphorae"
      }
    ],
    "ingredientPattern": "_C_,GGG",
    "enabled": false,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-light",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "amphorae:clay-brown",
        "quantity": 1
      }
    },
    "name": "mudbrickslab",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "game:mudbrickslab-light-down-free",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>浅色泥砖、深色泥砖 · adobebrick</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 浅色土坯砖<br><code>brickyard:adoberawbrick-light</code> | 1 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:clay-*</code> | 1 | 未声明附加限制 |
| 产物 | 浅色泥砖<br><code>game:mudbrick-light</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GGG
GCG
GGG
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 深色土坯砖<br><code>brickyard:adoberawbrick-dark</code> | 1 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:clay-*</code> | 1 | 未声明附加限制 |
| 产物 | 深色泥砖<br><code>game:mudbrick-dark</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GGG
GCG
GGG
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "GGG,GCG,GGG",
    "enabled": true,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-light",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "game:clay-*",
        "quantity": 1
      }
    },
    "name": "themudbrick",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:mudbrick-light",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "GGG,GCG,GGG",
    "enabled": true,
    "ingredients": {
      "G": {
        "type": "item",
        "code": "brickyard:adoberawbrick-dark",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "game:clay-*",
        "quantity": 1
      }
    },
    "name": "themudbrick",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "game:mudbrick-dark",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、薄层棕粘土坯料、砖模、瓦模 · claylayer</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:clay-*</code> | 2 | 允许变体：['red', 'blue', 'fire'] |
| 产物 | 变体材料（按代码匹配）<br><code>brickyard:claylayer-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 名称未汉化（见物品代码）<br><code>amphorae:clay-brown</code> | 2 | 未声明附加限制 |
| 产物 | 薄层棕粘土坯料<br><code>brickyard:claylayer-brown</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>brickyard:claylayer-*</code> | 2 | 允许变体：['red', 'blue', 'fire'] |
| 产物 | 变体材料（按代码匹配）<br><code>brickyard:claylayerdouble-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
C
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>brickyard:claylayer-*</code> | 1 | 允许变体：['red', 'blue', 'fire'] |
| 产物 | 变体材料（按代码匹配）<br><code>brickyard:wetclaytile-{type}</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
C
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 木柴<br><code>game:firewood</code> | 2 | 未声明附加限制 |
| 投入 H | 燧石<br><code>game:flint</code> | 1 | 未声明附加限制 |
| 产物 | 砖模<br><code>brickyard:brickmold</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
V_V
_H_
WWW
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 V | 木柴<br><code>game:firewood</code> | 2 | 未声明附加限制 |
| 投入 H | 燧石<br><code>game:flint</code> | 1 | 未声明附加限制 |
| 产物 | 瓦模<br><code>brickyard:shinglemold</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
VWV
_H_
WVW
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "CC",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:clay-*",
        "name": "type",
        "allowedVariants": [
          "red",
          "blue",
          "fire"
        ],
        "quantity": 2
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "brickyard:claylayer-{type}",
      "quantity": 1
    }
  },
  {
    "enabled": false,
    "dependsOn": [
      {
        "modid": "amphorae"
      }
    ],
    "ingredientPattern": "CC",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "amphorae:clay-brown",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "brickyard:claylayer-brown",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "C,C",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "brickyard:claylayer-*",
        "name": "type",
        "allowedVariants": [
          "red",
          "blue",
          "fire"
        ],
        "quantity": 2
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "brickyard:claylayerdouble-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "A,C",
    "ingredients": {
      "A": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "brickyard:claylayer-*",
        "name": "type",
        "allowedVariants": [
          "red",
          "blue",
          "fire"
        ],
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "brickyard:wetclaytile-{type}",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "V_V,_H_,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood"
      },
      "V": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:flint",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "brickyard:brickmold"
    }
  },
  {
    "ingredientPattern": "VWV,_H_,WVW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood"
      },
      "V": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 2
      },
      "H": {
        "type": "item",
        "code": "game:flint",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "brickyard:shinglemold"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
