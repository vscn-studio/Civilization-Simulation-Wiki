<!-- generated:start -->
# 乐器扩展：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>手风琴 · accordion</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:leather-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 手风琴<br><code>vsinstrumentsredux:instrument-accordion</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
_E_
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,_E_",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:stick",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:leather-*"
    },
    "E": {
      "type": "block",
      "code": "game:linen-*"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-accordion"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableAccordion"
    }
  ]
}
```

</details>

</details>

<details><summary>风笛 · bagpipes</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:leather-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 风笛<br><code>vsinstrumentsredux:instrument-bagpipes</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
EDE
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,EDE",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:leather-*"
    },
    "E": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-bagpipes"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableBagpipes"
    }
  ]
}
```

</details>

</details>

<details><summary>巴拉莱卡琴 · balalaika</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 亚麻纤维<br><code>game:flaxfibers</code> | 2 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 巴拉莱卡琴<br><code>vsinstrumentsredux:instrument-balalaika</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
DDD
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,DDD",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-balalaika"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableBalalaika"
    }
  ]
}
```

</details>

</details>

<details><summary>班卓琴 · banjo</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 亚麻纤维<br><code>game:flaxfibers</code> | 4 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:leather-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 班卓琴<br><code>vsinstrumentsredux:instrument-banjo</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
CEC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,CEC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 4
    },
    "E": {
      "type": "item",
      "code": "game:leather-*"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-banjo"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableBanjo"
    }
  ]
}
```

</details>

</details>

<details><summary>猫咪玩具钢琴 · cattoypiano</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 投入 D | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 E | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 猫咪玩具钢琴<br><code>vsinstrumentsredux:instrument-cattoypiano</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
ECC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,ECC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 1
    },
    "D": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "E": {
      "type": "item",
      "code": "game:gear-temporal"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-cattoypiano"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableCatToyPiano"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · clarinet</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 银金属粒<br><code>game:metalbit-silver</code> | 8 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument-Clarinet</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB
CD
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB,CD",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:metalbit-silver",
      "quantity": 8
    }
  },
  "width": 2,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-Clarinet"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableClarinet"
    }
  ]
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · conch</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:seashell-conch-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>vsinstrumentsredux:instrument-conch-{color}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A,B",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "block",
      "code": "game:seashell-conch-*",
      "name": "color"
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-conch-{color}"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableConch"
    }
  ]
}
```

</details>

</details>

<details><summary>克鲁姆弯管 · crumhorn</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 木棍<br><code>game:stick</code> | 2 | 未声明附加限制 |
| 产物 | 克鲁姆弯管<br><code>vsinstrumentsredux:instrument-crumhorn</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A,B",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:stick",
      "quantity": 2
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-crumhorn"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableCrumhorn"
    }
  ]
}
```

</details>

</details>

<details><summary>迪吉里杜管 · didgeridoo</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 迪吉里杜管<br><code>vsinstrumentsredux:instrument-didgeridoo</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A__
BCC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A__,BCC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:stick"
    },
    "C": {
      "type": "block",
      "code": "game:log-placed-*-ud"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-didgeridoo"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableDidgeridoo"
    }
  ]
}
```

</details>

</details>

<details><summary>扬琴 · dulcimer</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 亚麻纤维<br><code>game:flaxfibers</code> | 2 | 未声明附加限制 |
| 投入 D | 骨头<br><code>game:bone</code> | 3 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 扬琴<br><code>vsinstrumentsredux:instrument-dulcimer</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CCD
EEE
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CCD,EEE",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:bone",
      "quantity": 3
    },
    "E": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-dulcimer"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableDulcimer"
    }
  ]
}
```

</details>

</details>

<details><summary>短笛 · fife</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:metalbit-*</code> | 1 | 未声明附加限制 |
| 投入 D | 木棍<br><code>game:stick</code> | 1 | 未声明附加限制 |
| 产物 | 短笛<br><code>vsinstrumentsredux:instrument-fife</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:metalbit-*",
      "quantity": 1
    },
    "D": {
      "type": "item",
      "code": "game:stick",
      "quantity": 1
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-fife"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableFife"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · glockenspiel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 钢锭<br><code>game:ingot-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_glockenspiel-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
_C_
D_D
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,_C_,D_D",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:ingot-steel"
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 3
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_glockenspiel-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableGlockenspiel"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · guzheng</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 亚麻纤维<br><code>game:flaxfibers</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_guzheng-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
CDC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,CDC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_guzheng-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableGuzheng"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · hammereddulcimer</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 亚麻纤维<br><code>game:flaxfibers</code> | 4 | 未声明附加限制 |
| 投入 E | 铁锭<br><code>game:ingot-iron</code> | 3 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_hammereddulcimer-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DDE
FFF
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DDE,FFF",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:stick"
    },
    "D": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 4
    },
    "E": {
      "type": "item",
      "code": "game:ingot-iron",
      "quantity": 3
    },
    "F": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 4
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_hammereddulcimer-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableHammeredDulcimer"
    }
  ]
}
```

</details>

</details>

<details><summary>手碟 · handpan</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 钢锭<br><code>game:ingot-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 手碟<br><code>vsinstrumentsredux:instrument-handpan</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_A_
_B_
_B_
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_A_,_B_,_B_",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:ingot-steel"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-handpan"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableHandpan"
    }
  ]
}
```

</details>

</details>

<details><summary>轮擦提琴 · hurdygurdy</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 亚麻纤维<br><code>game:flaxfibers</code> | 4 | 未声明附加限制 |
| 投入 E | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 产物 | 轮擦提琴<br><code>vsinstrumentsredux:instrument-hurdygurdy</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
CEC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,CEC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 4
    },
    "E": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-hurdygurdy"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableHurdyGurdy"
    }
  ]
}
```

</details>

</details>

<details><summary>卡林巴拇指琴 · kalimba</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 D | 钢锭<br><code>game:ingot-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 卡林巴拇指琴<br><code>vsinstrumentsredux:instrument-kalimba</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
_D_
EEE
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,_D_,EEE",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "D": {
      "type": "item",
      "code": "game:ingot-steel"
    },
    "E": {
      "type": "item",
      "code": "game:plank-*"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-kalimba"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableKalimba"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · koto</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 亚麻纤维<br><code>game:flaxfibers</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_koto-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CCC
CDC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CCC,CDC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 4
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_koto-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableKoto"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · logdrum</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_logdrum-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A__
BCB
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A__,BCB",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:stick"
    },
    "C": {
      "type": "block",
      "code": "game:log-placed-*-ud"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_logdrum-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableLogDrum"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · marimba</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_marimba-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CCC
DED
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CCC,DED",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 1
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 3
    },
    "E": {
      "type": "block",
      "code": "game:log-placed-*-ud"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_marimba-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableMarimba"
    }
  ]
}
```

</details>

</details>

<details><summary>猫叫合成器 · meowsynth</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 投入 D | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 E | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 猫叫合成器<br><code>vsinstrumentsredux:instrument-meowsynth</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
CCE
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,CCE",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 1
    },
    "D": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "E": {
      "type": "item",
      "code": "game:gear-temporal"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-meowsynth"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableMeowSynth"
    }
  ]
}
```

</details>

</details>

<details><summary>陶笛 · ocarina</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 陶笛<br><code>vsinstrumentsredux:instrument-ocarina</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A_
BB
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A_,BB",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "block",
      "code": "game:log-placed-*-ud"
    }
  },
  "width": 2,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-ocarina"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableOcarina"
    }
  ]
}
```

</details>

</details>

<details><summary>乌德琴 · oud</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 亚麻纤维<br><code>game:flaxfibers</code> | 4 | 未声明附加限制 |
| 产物 | 乌德琴<br><code>vsinstrumentsredux:instrument-oud</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
CEC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,CEC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*"
    },
    "D": {
      "type": "item",
      "code": "game:resin"
    },
    "E": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 4
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-oud"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableOud"
    }
  ]
}
```

</details>

</details>

<details><summary>排箫 · panflute</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 亚麻纤维<br><code>game:flaxfibers</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 排箫<br><code>vsinstrumentsredux:instrument-panflute</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A__
BBB
BCB
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A__,BBB,BCB",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:stick"
    },
    "C": {
      "type": "item",
      "code": "game:flaxfibers"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-panflute"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enablePanFlute"
    }
  ]
}
```

</details>

</details>

<details><summary>钢琴 · piano</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 钢琴<br><code>vsinstrumentsredux:instrument-piano</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CCC
DDD
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CCC,DDD",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-piano"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enablePiano"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · pipeorgan</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 黄铜锭<br><code>game:ingot-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 钢琴<br><code>vsinstrumentsredux:instrument-piano</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:planks-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_pipeorgan-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABA
CCC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABA,CCC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:ingot-brass"
    },
    "B": {
      "type": "item",
      "code": "vsinstrumentsredux:instrument-piano"
    },
    "C": {
      "type": "block",
      "code": "game:planks-*-ud"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_pipeorgan-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enablePipeOrgan"
    }
  ]
}
```

</details>

</details>

<details><summary>三味线 · shamisen</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 E | 亚麻纤维<br><code>game:flaxfibers</code> | 4 | 未声明附加限制 |
| 产物 | 三味线<br><code>vsinstrumentsredux:instrument-shamisen</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
CEC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,CEC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "E": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 4
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-shamisen"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableShamisen"
    }
  ]
}
```

</details>

</details>

<details><summary>西塔琴 · sitar</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 亚麻纤维<br><code>game:flaxfibers</code> | 4 | 未声明附加限制 |
| 产物 | 西塔琴<br><code>vsinstrumentsredux:instrument-sitar</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
CDC
CDC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,CDC,CDC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*"
    },
    "D": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 4
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-sitar"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableSitar"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · standingpiano</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 钢琴<br><code>vsinstrumentsredux:instrument-piano</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:planks-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_standingpiano-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_A_
BBB
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_A_,BBB",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "vsinstrumentsredux:instrument-piano"
    },
    "B": {
      "type": "block",
      "code": "game:planks-*-ud"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_standingpiano-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableStandingPiano"
    }
  ]
}
```

</details>

</details>

<details><summary>钢鼓 · steeldrum</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 钢锭<br><code>game:ingot-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 钢鼓<br><code>vsinstrumentsredux:instrument-steeldrum</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_A_
_B_
CCC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_A_,_B_,CCC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:ingot-steel"
    },
    "C": {
      "type": "item",
      "code": "game:plank-*"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-steeldrum"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableSteelDrum"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · taikodrum</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:leather-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_taikodrum-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
DDD
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,DDD",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:leather-*"
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_taikodrum-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableTaikoDrum"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · theremin</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 钢锭<br><code>game:ingot-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_theremin-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CDC
CEC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CDC,CEC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:ingot-steel"
    },
    "E": {
      "type": "item",
      "code": "game:gear-temporal"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_theremin-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableTheremin"
    }
  ]
}
```

</details>

</details>

<details><summary>锡笛 · tinwhistle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 锡锭<br><code>game:ingot-tin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 锡笛<br><code>vsinstrumentsredux:instrument-tinwhistle</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A,B",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:ingot-tin"
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-tinwhistle"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableTinWhistle"
    }
  ]
}
```

</details>

</details>

<details><summary>小号 · trumpet</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 黄铜锭<br><code>game:ingot-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 小号<br><code>vsinstrumentsredux:instrument-trumpet</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A_
BB
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A_,BB",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:ingot-brass"
    }
  },
  "width": 2,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-trumpet"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableTrumpet"
    }
  ]
}
```

</details>

</details>

<details><summary>大号 · tuba</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 黄铜锭<br><code>game:ingot-brass</code> | 2 | 未声明附加限制 |
| 产物 | 大号<br><code>vsinstrumentsredux:instrument-tuba</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A,B",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:ingot-brass",
      "quantity": 2
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-tuba"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableTuba"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · tubularbells</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 黄铜锭<br><code>game:ingot-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 铁锭<br><code>game:ingot-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_tubularbells-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
_C_
DCD
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,_C_,DCD",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:ingot-brass"
    },
    "D": {
      "type": "item",
      "code": "game:ingot-iron"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_tubularbells-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableTubularBells"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · vibraphone</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 钢锭<br><code>game:ingot-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_vibraphone-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
_C_
DCD
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,_C_,DCD",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:ingot-steel"
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 3
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_vibraphone-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableVibraphone"
    }
  ]
}
```

</details>

</details>

<details><summary>木鱼 · woodblock</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木鱼<br><code>vsinstrumentsredux:instrument-woodblock</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A_
BC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A_,BC",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:stick"
    },
    "C": {
      "type": "block",
      "code": "game:log-placed-*-ud"
    }
  },
  "width": 2,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-woodblock"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableWoodBlock"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · xylophone</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:instrument_xylophone-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AB_
CCC
D_D
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "AB_,CCC,D_D",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 3
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:instrument_xylophone-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableXylophone"
    }
  ]
}
```

</details>

</details>
<!-- generated:end -->
