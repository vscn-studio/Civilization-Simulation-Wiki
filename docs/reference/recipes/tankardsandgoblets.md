<!-- generated:start -->
# 酒杯与高脚杯：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>简易木啤酒杯、铂啤酒杯 · basictankardrecipe</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 简易木啤酒杯<br><code>tankard-wood</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP
_P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 铂锭<br><code>game:ingot-platinum</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 铂啤酒杯<br><code>tankardsandgoblets:tankard-metal-platinum</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
NP
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SP,_P",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "block",
      "code": "tankard-wood"
    }
  },
  {
    "ingredientPattern": "HC,NP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "P": {
        "type": "item",
        "code": "game:ingot-platinum"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "block",
      "code": "tankardsandgoblets:tankard-metal-platinum",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · jeweledgoblet</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:ore-*</code> | 未声明；按配方类型判定 | 允许变体：['cinnabar', 'lapislazuli', 'olivine', 'quartz'] |
| 投入 P | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['iron', 'copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'brass', 'silver', 'steel', 'meteoriciron', 'gold', 'platinum'] |
| 产物 | 变体材料（按代码匹配）<br><code>goblet-jeweled-{metal}-{gem}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
_N
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:gem-*-rough</code> | 未声明；按配方类型判定 | 允许变体：['diamond', 'emerald'] |
| 投入 P | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['iron', 'copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'brass', 'silver', 'steel', 'meteoriciron', 'gold', 'platinum'] |
| 产物 | 变体材料（按代码匹配）<br><code>goblet-jeweled-{metal}-{gem}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
_N
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:nugget-*</code> | 4 | 允许变体：['malachite'] |
| 投入 P | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['iron', 'copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'brass', 'silver', 'steel', 'meteoriciron', 'gold', 'platinum'] |
| 产物 | 变体材料（按代码匹配）<br><code>goblet-jeweled-{metal}-{gem}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
_N
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 粉水晶<br><code>game:rosequartz</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['iron', 'copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'brass', 'silver', 'steel', 'meteoriciron', 'gold', 'platinum'] |
| 产物 | 变体材料（按代码匹配）<br><code>goblet-jeweled-{metal}-rosequartz</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
_N
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 紫水晶<br><code>game:amethyst</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['iron', 'copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'brass', 'silver', 'steel', 'meteoriciron', 'gold', 'platinum'] |
| 产物 | 变体材料（按代码匹配）<br><code>goblet-jeweled-{metal}-amethyst</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
_N
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "HC,GP,_N",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "item",
        "code": "game:ore-*",
        "name": "gem",
        "allowedVariants": [
          "cinnabar",
          "lapislazuli",
          "olivine",
          "quartz"
        ]
      },
      "P": {
        "type": "item",
        "code": "game:ingot-*",
        "name": "metal",
        "allowedVariants": [
          "iron",
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "silver",
          "steel",
          "meteoriciron",
          "gold",
          "platinum"
        ]
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "goblet-jeweled-{metal}-{gem}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP,_N",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "item",
        "code": "game:gem-*-rough",
        "name": "gem",
        "allowedVariants": [
          "diamond",
          "emerald"
        ]
      },
      "P": {
        "type": "item",
        "code": "game:ingot-*",
        "name": "metal",
        "allowedVariants": [
          "iron",
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "silver",
          "steel",
          "meteoriciron",
          "gold",
          "platinum"
        ]
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "goblet-jeweled-{metal}-{gem}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP,_N",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "item",
        "code": "game:nugget-*",
        "name": "gem",
        "allowedVariants": [
          "malachite"
        ],
        "quantity": 4
      },
      "P": {
        "type": "item",
        "code": "game:ingot-*",
        "name": "metal",
        "allowedVariants": [
          "iron",
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "silver",
          "steel",
          "meteoriciron",
          "gold",
          "platinum"
        ]
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "goblet-jeweled-{metal}-{gem}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP,_N",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "item",
        "code": "game:rosequartz"
      },
      "P": {
        "type": "item",
        "code": "game:ingot-*",
        "name": "metal",
        "allowedVariants": [
          "iron",
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "silver",
          "steel",
          "meteoriciron",
          "gold",
          "platinum"
        ]
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "goblet-jeweled-{metal}-rosequartz",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP,_N",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "G": {
        "type": "item",
        "code": "game:amethyst"
      },
      "P": {
        "type": "item",
        "code": "game:ingot-*",
        "name": "metal",
        "allowedVariants": [
          "iron",
          "copper",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "brass",
          "silver",
          "steel",
          "meteoriciron",
          "gold",
          "platinum"
        ]
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "goblet-jeweled-{metal}-amethyst",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、白水晶、橄榄石 · large demijohn</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-largedemijohn-null-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP_
G_G
_G_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 香蒲<br><code>game:cattailtops</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-largedemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP_
G_G
RGR
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 纸莎草<br><code>game:papyrustops</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-largedemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP_
G_G
RGR
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 名称未汉化（见物品代码）<br><code>game:wildvine-section-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-largedemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP_
G_G
RGR
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-largedemijohn-null-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'red', 'brown', 'blue'] |
| 产物 | 白水晶<br><code>game:clearquartz</code> | 6 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-largedemijohn-wicker-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'red', 'brown', 'blue'] |
| 产物 | 白水晶<br><code>game:clearquartz</code> | 6 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-largedemijohn-{type}-green</code> | 未声明；按配方类型判定 | 允许变体：['null', 'wicker'] |
| 产物 | 橄榄石<br><code>game:ore-olivine</code> | 12 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SP_,G_G,_G_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-largedemijohn-null-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SP_,G_G,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-largedemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SP_,G_G,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-largedemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SP_,G_G,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:wildvine-section-north"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-largedemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-largedemijohn-null-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "red",
          "brown",
          "blue"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:clearquartz",
      "quantity": 6
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-largedemijohn-wicker-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "red",
          "brown",
          "blue"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:clearquartz",
      "quantity": 6
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-largedemijohn-{type}-green",
        "name": "type",
        "allowedVariants": [
          "null",
          "wicker"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:ore-olivine",
      "quantity": 12
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · metalgoblet</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['iron', 'copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'brass', 'silver', 'steel', 'meteoriciron', 'gold', 'platinum', 'lead'] |
| 产物 | 变体材料（按代码匹配）<br><code>goblet-{metal}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
_P
_N
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "HC,_P,_N",
  "ingredients": {
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 5
    },
    "C": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 5
    },
    "N": {
      "type": "item",
      "code": "game:metalnailsandstrips-*"
    },
    "P": {
      "type": "item",
      "code": "game:ingot-*",
      "name": "metal",
      "allowedVariants": [
        "iron",
        "copper",
        "tinbronze",
        "bismuthbronze",
        "blackbronze",
        "brass",
        "silver",
        "steel",
        "meteoriciron",
        "gold",
        "platinum",
        "lead"
      ]
    }
  },
  "width": 2,
  "height": 3,
  "output": {
    "type": "block",
    "code": "goblet-{metal}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、白水晶、橄榄石 · small demijohn</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-null-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP
GG
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 2 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-null-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SP
GG
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 2 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 香蒲<br><code>game:cattailtops</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
_P_
RGR
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 2 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 纸莎草<br><code>game:papyrustops</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
_P_
RGR
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 2 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 名称未汉化（见物品代码）<br><code>game:wildvine-section-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
_P_
RGR
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 4 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 纸莎草<br><code>game:papyrustops</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
_P_
RGR
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 4 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 香蒲<br><code>game:cattailtops</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
_P_
RGR
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 4 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 投入 R | 名称未汉化（见物品代码）<br><code>game:wildvine-section-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
_P_
RGR
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-null-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BK
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 名称未汉化（见物品代码）<br><code>game:wildvine-section-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-null-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RBR
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 香蒲<br><code>game:cattailtops</code> | 2 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-null-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RBR
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 纸莎草<br><code>game:papyrustops</code> | 2 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-null-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RBR
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-null-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'red', 'brown', 'blue'] |
| 产物 | 白水晶<br><code>game:clearquartz</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-wicker-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'red', 'brown', 'blue'] |
| 产物 | 白水晶<br><code>game:clearquartz</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-smalldemijohn-{type}-green</code> | 未声明；按配方类型判定 | 允许变体：['null', 'wicker'] |
| 产物 | 橄榄石<br><code>game:ore-olivine</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "SP,GG",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-null-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SP,GG",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free",
        "name": "type",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 2
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-null-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,_P_,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,_P_,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 2
      },
      "R": {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,_P_,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 2
      },
      "R": {
        "type": "block",
        "code": "game:wildvine-section-north"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,_P_,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,_P_,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 4
      },
      "R": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,_P_,RGR",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 4
      },
      "R": {
        "type": "block",
        "code": "game:wildvine-section-north"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "BK",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-smalldemijohn-wicker-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-null-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "RBR",
    "ingredients": {
      "R": {
        "type": "block",
        "code": "game:wildvine-section-north"
      },
      "B": {
        "type": "block",
        "code": "t&g-smalldemijohn-null-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "RBR",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 2
      },
      "B": {
        "type": "block",
        "code": "t&g-smalldemijohn-null-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "RBR",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 2
      },
      "B": {
        "type": "block",
        "code": "t&g-smalldemijohn-null-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "block",
      "code": "t&g-smalldemijohn-wicker-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-smalldemijohn-null-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "red",
          "brown",
          "blue"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:clearquartz",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-smalldemijohn-wicker-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "red",
          "brown",
          "blue"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:clearquartz",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-smalldemijohn-{type}-green",
        "name": "type",
        "allowedVariants": [
          "null",
          "wicker"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:ore-olivine",
      "quantity": 8
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、橄榄石、白水晶 · winebottle</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-winebottle-{glassblock}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S
P
G
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glassslab-*-down-free</code> | 2 | 允许变体：['plain', 'green', 'red', 'brown', 'smoky', 'blue'] |
| 产物 | 变体材料（按代码匹配）<br><code>t&amp;g-winebottle-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S
P
G
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 名称未汉化（见物品代码）<br><code>t&amp;g-winebottle-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 橄榄石<br><code>game:ore-olivine</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 B | 变体材料（按代码匹配）<br><code>t&amp;g-winebottle-{type}</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'red', 'brown', 'blue'] |
| 产物 | 白水晶<br><code>game:clearquartz</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HB
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "S,P,G",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glass-*",
        "name": "glassblock",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ]
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-winebottle-{glassblock}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "S,P,G",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "G": {
        "type": "block",
        "code": "game:glassslab-*-down-free",
        "name": "type",
        "allowedVariants": [
          "plain",
          "green",
          "red",
          "brown",
          "smoky",
          "blue"
        ],
        "quantity": 2
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "block",
      "code": "t&g-winebottle-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-winebottle-green",
        "name": "type"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:ore-olivine",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "HB",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "B": {
        "type": "block",
        "code": "t&g-winebottle-{type}",
        "name": "type",
        "allowedVariants": [
          "plain",
          "red",
          "brown",
          "blue"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:clearquartz",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · woodentankard</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:leather-normal-*</code> | 未声明；按配方类型判定 | 允许变体：['plain', 'red', 'gray', 'black', 'white', 'pink', 'purple', 'yellow', 'blue', 'green', 'orange'] |
| 投入 W | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 允许变体：['oak', 'birch', 'pine', 'acacia', 'aged', 'larch', 'baldcypress', 'ebony', 'kapok', 'maple', 'purpleheart', 'redwood', 'walnut'] |
| 产物 | 变体材料（按代码匹配）<br><code>tankard-woodtype-{wood}.-leather-{binding}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
LW
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 允许变体：['iron', 'copper', 'bismuthbronze', 'blackbronze', 'cupronickel', 'gold', 'meteoriciron', 'silver', 'steel', 'tinbronze'] |
| 投入 W | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 允许变体：['oak', 'birch', 'pine', 'acacia', 'aged', 'larch', 'baldcypress', 'ebony', 'kapok', 'maple', 'purpleheart', 'redwood', 'walnut'] |
| 产物 | 变体材料（按代码匹配）<br><code>tankard-woodtype-{wood}.-{binding}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
NW
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:nugget-*</code> | 2 | 允许变体：['malachite'] |
| 投入 W | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 允许变体：['oak', 'birch', 'pine', 'acacia', 'aged', 'larch', 'baldcypress', 'ebony', 'kapok', 'maple', 'purpleheart', 'redwood', 'walnut'] |
| 产物 | 变体材料（按代码匹配）<br><code>tankard-woodtype-{wood}.-{binding}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC_
NWN
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalbit-*</code> | 2 | 允许变体：['iron', 'copper', 'bismuthbronze', 'blackbronze', 'cupronickel', 'gold', 'meteoriciron', 'silver', 'steel', 'tinbronze', 'bismuth', 'brass', 'platinum', 'nickel'] |
| 投入 W | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 允许变体：['oak', 'birch', 'pine', 'acacia', 'aged', 'larch', 'baldcypress', 'ebony', 'kapok', 'maple', 'purpleheart', 'redwood', 'walnut'] |
| 产物 | 变体材料（按代码匹配）<br><code>tankard-woodtype-{wood}.-{binding}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC_
NWN
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "HC,LW",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-*",
        "name": "binding",
        "allowedVariants": [
          "plain",
          "red",
          "gray",
          "black",
          "white",
          "pink",
          "purple",
          "yellow",
          "blue",
          "green",
          "orange"
        ]
      },
      "W": {
        "type": "block",
        "code": "game:log-placed-*-ud",
        "name": "wood",
        "allowedVariants": [
          "oak",
          "birch",
          "pine",
          "acacia",
          "aged",
          "larch",
          "baldcypress",
          "ebony",
          "kapok",
          "maple",
          "purpleheart",
          "redwood",
          "walnut"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "block",
      "code": "tankard-woodtype-{wood}.-leather-{binding}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,NW",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "name": "binding",
        "allowedVariants": [
          "iron",
          "copper",
          "bismuthbronze",
          "blackbronze",
          "cupronickel",
          "gold",
          "meteoriciron",
          "silver",
          "steel",
          "tinbronze"
        ]
      },
      "W": {
        "type": "block",
        "code": "game:log-placed-*-ud",
        "name": "wood",
        "allowedVariants": [
          "oak",
          "birch",
          "pine",
          "acacia",
          "aged",
          "larch",
          "baldcypress",
          "ebony",
          "kapok",
          "maple",
          "purpleheart",
          "redwood",
          "walnut"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "block",
      "code": "tankard-woodtype-{wood}.-{binding}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC_,NWN",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:nugget-*",
        "name": "binding",
        "allowedVariants": [
          "malachite"
        ],
        "quantity": 2
      },
      "W": {
        "type": "block",
        "code": "game:log-placed-*-ud",
        "name": "wood",
        "allowedVariants": [
          "oak",
          "birch",
          "pine",
          "acacia",
          "aged",
          "larch",
          "baldcypress",
          "ebony",
          "kapok",
          "maple",
          "purpleheart",
          "redwood",
          "walnut"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "tankard-woodtype-{wood}.-{binding}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC_,NWN",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "N": {
        "type": "item",
        "code": "game:metalbit-*",
        "name": "binding",
        "allowedVariants": [
          "iron",
          "copper",
          "bismuthbronze",
          "blackbronze",
          "cupronickel",
          "gold",
          "meteoriciron",
          "silver",
          "steel",
          "tinbronze",
          "bismuth",
          "brass",
          "platinum",
          "nickel"
        ],
        "quantity": 2
      },
      "W": {
        "type": "block",
        "code": "game:log-placed-*-ud",
        "name": "wood",
        "allowedVariants": [
          "oak",
          "birch",
          "pine",
          "acacia",
          "aged",
          "larch",
          "baldcypress",
          "ebony",
          "kapok",
          "maple",
          "purpleheart",
          "redwood",
          "walnut"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "tankard-woodtype-{wood}.-{binding}",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · metaltankard</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>tankard-metal-{metal}</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "iron",
      "copper",
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "brass",
      "silver",
      "steel",
      "meteoriciron",
      "gold",
      "lead",
      "platinum"
    ]
  },
  "pattern": [
    [
      "###_",
      "####",
      "###_"
    ],
    [
      "###_",
      "#_##",
      "###_"
    ],
    [
      "###_",
      "#_##",
      "###_"
    ]
  ],
  "code": "tankard-metal-{metal}",
  "output": {
    "type": "block",
    "code": "tankard-metal-{metal}",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
