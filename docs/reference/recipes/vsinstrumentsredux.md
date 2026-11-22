<!-- generated:start -->
# 乐器：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>鼓机 · drum-machine</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 烙铁<br><code>game:solderingiron</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 D | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 E | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 铅焊条<br><code>game:solderbar-tin</code> | 2 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 H | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 鼓机<br><code>vsinstrumentsredux:instrument-drum-machine</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DEF
G_H
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DEF,G_H",
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
      "code": "game:solderingiron",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "D": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "E": {
      "type": "item",
      "code": "game:gear-temporal"
    },
    "F": {
      "type": "item",
      "code": "game:solderbar-tin",
      "quantity": 2
    },
    "G": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "H": {
      "type": "item",
      "code": "game:metalplate-copper"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-drum-machine"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableDrumMachine"
    }
  ]
}
```

</details>

</details>

<details><summary>二胡 · erhu</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 亚麻纤维<br><code>game:flaxfibers</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:leather-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 产物 | 二胡<br><code>vsinstrumentsredux:instrument-erhu</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC_
SFS
PLF
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "HC_,SFS,PLF",
  "width": 3,
  "height": 3,
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:plank-*"
    },
    "F": {
      "type": "item",
      "code": "game:flaxfibers"
    },
    "S": {
      "type": "item",
      "code": "game:stick"
    },
    "L": {
      "type": "item",
      "code": "game:leather-*"
    },
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "C": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true,
      "toolDurabilityCost": 10
    }
  },
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-erhu"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableErhu"
    }
  ]
}
```

</details>

</details>

<details><summary>长笛 · flute</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 银锭<br><code>game:ingot-silver</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 长笛<br><code>vsinstrumentsredux:instrument-flute</code> | 未声明；按配方类型判定 | 未声明附加限制 |

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
      "code": "game:ingot-silver"
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-flute"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableFlute"
    }
  ]
}
```

</details>

</details>

<details><summary>头戴留声机 · headphonograph</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 烙铁<br><code>game:solderingiron</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 投入 E | 黄铜锭<br><code>game:ingot-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 铅焊条<br><code>game:solderbar-tin</code> | 1 | 未声明附加限制 |
| 产物 | 头戴留声机<br><code>vsinstrumentsredux:headphonograph</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DEF
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DEF",
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
      "code": "game:solderingiron",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 1
    },
    "E": {
      "type": "item",
      "code": "game:ingot-brass"
    },
    "F": {
      "type": "item",
      "code": "game:solderbar-tin",
      "quantity": 1
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:headphonograph"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableHeadphonograph"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · musicbox</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:phonographcylinder</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:musicbox-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

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
      "code": "vsinstrumentsredux:phonographcylinder"
    },
    "E": {
      "type": "item",
      "code": "game:ingot-*"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:musicbox-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableMusicBox"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · musiclectern</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 墨水和羽毛笔<br><code>game:inkandquill</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:musiclectern-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A__
BCB
DDD
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A__,BCB,DDD",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:plank-*"
    },
    "C": {
      "type": "item",
      "code": "game:inkandquill"
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
    "code": "vsinstrumentsredux:musiclectern-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableMusicLectern"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · phonograph</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 黄铜锭<br><code>game:ingot-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 4 | 未声明附加限制 |
| 投入 D | 铁锭<br><code>game:ingot-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:phonograph-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_A_
_B_
CDC
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_A_,_B_,CDC",
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
    },
    "C": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 4
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
    "code": "vsinstrumentsredux:phonograph-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enablePhonograph"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · phonographcylinder</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 桦木木材<br><code>game:plank-birch</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:phonographcylinder</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
B
A
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A,B,A",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:plank-birch"
    },
    "B": {
      "type": "item",
      "code": "game:beeswax"
    }
  },
  "width": 1,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:phonographcylinder"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enablePhonographCylinder"
    }
  ]
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · pianobench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:pianobench-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_A_
BBB
B_B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_A_,BBB,B_B",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "B": {
      "type": "item",
      "code": "game:plank-*"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsinstrumentsredux:pianobench-north"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enablePianoBench"
    }
  ]
}
```

</details>

</details>

<details><summary>便携留声机 · portablephonograph</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 烙铁<br><code>game:solderingiron</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:leather-*</code> | 1 | 未声明附加限制 |
| 投入 E | 名称未汉化（见物品代码）<br><code>vsinstrumentsredux:phonograph-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 铅焊条<br><code>game:solderbar-tin</code> | 1 | 未声明附加限制 |
| 产物 | 便携留声机<br><code>vsinstrumentsredux:portablephonograph</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DEF
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DEF",
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
      "code": "game:solderingiron",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "D": {
      "type": "item",
      "code": "game:leather-*",
      "quantity": 1
    },
    "E": {
      "type": "block",
      "code": "vsinstrumentsredux:phonograph-north"
    },
    "F": {
      "type": "item",
      "code": "game:solderbar-tin",
      "quantity": 1
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:portablephonograph"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enablePortablePhonograph"
    }
  ]
}
```

</details>

</details>

<details><summary>锯齿波合成器 · saw-synth</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 烙铁<br><code>game:solderingiron</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 E | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 F | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 铅焊条<br><code>game:solderbar-tin</code> | 2 | 未声明附加限制 |
| 投入 D | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 G | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 锯齿波合成器<br><code>vsinstrumentsredux:instrument-saw-synth</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DEF
G_H
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DEF,G_H",
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
      "code": "game:solderingiron",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "E": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "F": {
      "type": "item",
      "code": "game:gear-temporal"
    },
    "H": {
      "type": "item",
      "code": "game:solderbar-tin",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "G": {
      "type": "item",
      "code": "game:metalplate-copper"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-saw-synth"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableSawSynth"
    }
  ]
}
```

</details>

</details>

<details><summary>萨克斯管 · saxophone</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 黄铜锭<br><code>game:ingot-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 萨克斯管<br><code>vsinstrumentsredux:instrument-saxophone</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
A
B
B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "A,B,B",
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
  "width": 1,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-saxophone"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableSaxophone"
    }
  ]
}
```

</details>

</details>

<details><summary>方波合成器 · square-synth</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 烙铁<br><code>game:solderingiron</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 F | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 H | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 铅焊条<br><code>game:solderbar-tin</code> | 2 | 未声明附加限制 |
| 投入 E | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 D | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 方波合成器<br><code>vsinstrumentsredux:instrument-square-synth</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DEF
G_H
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DEF,G_H",
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
      "code": "game:solderingiron",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "F": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "H": {
      "type": "item",
      "code": "game:gear-temporal"
    },
    "G": {
      "type": "item",
      "code": "game:solderbar-tin",
      "quantity": 2
    },
    "E": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:metalplate-copper"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-square-synth"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableSquareSynth"
    }
  ]
}
```

</details>

</details>

<details><summary>贝斯合成器 · synth-bass</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 烙铁<br><code>game:solderingiron</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 H | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 G | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 D | 铅焊条<br><code>game:solderbar-tin</code> | 2 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 E | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 贝斯合成器<br><code>vsinstrumentsredux:instrument-synth-bass</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DEF
G_H
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DEF,G_H",
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
      "code": "game:solderingiron",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "H": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "G": {
      "type": "item",
      "code": "game:gear-temporal"
    },
    "D": {
      "type": "item",
      "code": "game:solderbar-tin",
      "quantity": 2
    },
    "F": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "E": {
      "type": "item",
      "code": "game:metalplate-copper"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-synth-bass"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableSynthBass"
    }
  ]
}
```

</details>

</details>

<details><summary>暖音铺底合成器 · warm-pad</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 C | 烙铁<br><code>game:solderingiron</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 G | 骨头<br><code>game:bone</code> | 2 | 未声明附加限制 |
| 投入 D | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 铅焊条<br><code>game:solderbar-tin</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 F | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 暖音铺底合成器<br><code>vsinstrumentsredux:instrument-warm-pad</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ABC
DEF
G_H
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "ABC,DEF,G_H",
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
      "code": "game:solderingiron",
      "isTool": true,
      "toolDurabilityCost": 10
    },
    "G": {
      "type": "item",
      "code": "game:bone",
      "quantity": 2
    },
    "D": {
      "type": "item",
      "code": "game:gear-temporal"
    },
    "E": {
      "type": "item",
      "code": "game:solderbar-tin",
      "quantity": 2
    },
    "H": {
      "type": "item",
      "code": "game:plank-*",
      "quantity": 2
    },
    "F": {
      "type": "item",
      "code": "game:metalplate-copper"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "vsinstrumentsredux:instrument-warm-pad"
  },
  "dependsOn": [
    {
      "prop": "vsinstruments:enableWarmPad"
    }
  ]
}
```

</details>

</details>
<!-- generated:end -->
