<!-- generated:start -->
# 信封与邮件：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：信封与包裹


信封用于给其他玩家寄信；寄送物品则需要包裹。

要寄信，先在一张 [handbook://item-paper-parchment] 羊皮纸上写好信，再制作一个 [handbook://item-envelopes:envelope-empty] 空信封，然后将两者放入合成栏组合。要寄送包裹，先制作一个 [handbook://item-envelopes:parcel-empty] 空包裹。在合成栏中将其与写好的羊皮纸组合，即可放入信件。要装入其他物品，先将包裹放在平面上，手持物品潜行并右键点击包裹，再手持羊皮纸，同时按住潜行键和疾跑键并右键点击，将包裹包好。

火漆封缄

封缄信封或包裹需要 [handbooksearch://a stick of] 火漆棒和刻好图案的 [handbook://item-envelopes:sealstamp-blank] 火漆印章。将一碗染料（绿色、蓝色、黑色或红色）与一块蜂蜡组合，即可制作火漆棒。右键点击空白印章可雕刻图案并为其命名。将火漆棒、印章和信封或包裹放入合成栏，即可封缄。也可以主手持印章、副手持火漆棒，右键点击平面上尚未封缄的信封或包裹进行封缄。

填写收寄信息

副手持墨水与羽毛笔，主手持信封或包裹，按住疾跑键并右键点击，即可填写寄件人和收件人。

拆封

右键点击已封缄的信封，可破开封蜡并取出信件。右键点击包裹只会破开封蜡，还需手动取出物品。

刮除封蜡

用小刀刮掉封蜡后，信封或包裹即可重复使用。封蜡会损毁，但信封或包裹会保持完好。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>信封、火漆封缄信封（已拆封） · add-letter</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 空信封<br><code>envelope-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 信封<br><code>envelope-unsealed</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
E
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 火漆封缄信封（已拆封）<br><code>envelope-opened</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆封缄信封（已拆封）<br><code>envelope-opened</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
E
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:book-normal-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 火漆封缄信封（已拆封）<br><code>envelope-opened</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆封缄信封（已拆封）<br><code>envelope-opened</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
E
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:book-normal-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 空信封<br><code>envelope-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 信封<br><code>envelope-unsealed</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
E
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P,E",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "E": {
        "type": "item",
        "code": "envelope-empty"
      }
    },
    "width": 1,
    "height": 2,
    "copyAttributesFrom": "E",
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "envelope-unsealed",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "P,E",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "E": {
        "type": "item",
        "code": "envelope-opened"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "copyAttributesFrom": "E",
    "output": {
      "type": "item",
      "code": "envelope-opened",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "P,E",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:book-normal-*"
      },
      "E": {
        "type": "item",
        "code": "envelope-opened"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "copyAttributesFrom": "E",
    "output": {
      "type": "item",
      "code": "envelope-opened",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "P,E",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:book-normal-*"
      },
      "E": {
        "type": "item",
        "code": "envelope-empty"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "copyAttributesFrom": "E",
    "output": {
      "type": "item",
      "code": "envelope-unsealed",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>包裹 · add-parchment-to-parcel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 E | 空包裹<br><code>parcel-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 包裹<br><code>parcel-unsealed</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
E
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "P,E",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "E": {
        "type": "item",
        "code": "parcel-empty"
      }
    },
    "width": 1,
    "height": 2,
    "shapeless": true,
    "copyAttributesFrom": "E",
    "output": {
      "type": "item",
      "code": "parcel-unsealed",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>空信封 · envelope</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 空信封<br><code>envelope-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
R
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "P,R",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:paper-parchment"
    },
    "R": {
      "type": "item",
      "code": "game:resin"
    }
  },
  "width": 1,
  "height": 2,
  "shapeless": true,
  "output": {
    "type": "item",
    "code": "envelope-empty",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>空包裹 · parcel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:hide-pelt-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 亚麻纤维<br><code>game:flaxfibers</code> | 3 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 2 | 未声明附加限制 |
| 产物 | 空包裹<br><code>parcel-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
F
P
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "L,F,P",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:hide-pelt-*"
    },
    "F": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 3
    },
    "P": {
      "type": "item",
      "code": "game:paper-parchment",
      "quantity": 2
    }
  },
  "width": 1,
  "height": 3,
  "shapeless": true,
  "output": {
    "type": "item",
    "code": "parcel-empty",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>空信封 · remove-wax</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 E | 火漆封缄信封（已拆封）<br><code>envelope-opened</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 空信封<br><code>envelope-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K_
E_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "K_,E_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "E": {
        "type": "item",
        "code": "envelope-opened"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "envelope-empty",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>火漆印章 · repair-stamp</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 E | 火漆印章<br><code>envelopes:sealstamp-engraved</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 空白火漆印章<br><code>envelopes:sealstamp-blank</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆印章<br><code>envelopes:sealstamp-engraved</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
EB
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "EB",
  "ingredients": {
    "E": {
      "type": "item",
      "code": "envelopes:sealstamp-engraved"
    },
    "B": {
      "type": "item",
      "code": "envelopes:sealstamp-blank"
    }
  },
  "width": 2,
  "height": 1,
  "recipeGroup": 1,
  "copyAttributesFrom": "E",
  "output": {
    "type": "item",
    "code": "envelopes:sealstamp-engraved",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>火漆封缄包裹 · seal-parcel</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 火漆印章<br><code>sealstamp-engraved</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 变体材料（按代码匹配）<br><code>waxstick-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包裹<br><code>parcel-unsealed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆封缄包裹<br><code>parcel-sealed</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_
W_
P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 印章戒指<br><code>envelopes:signetring-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>waxstick-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 P | 包裹<br><code>parcel-unsealed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆封缄包裹<br><code>parcel-sealed</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_
W_
P_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "S_,W_,P_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "sealstamp-engraved",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "item",
        "code": "waxstick-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "parcel-unsealed"
      }
    },
    "width": 2,
    "height": 3,
    "shapeless": true,
    "copyAttributesFrom": "P",
    "output": {
      "type": "item",
      "code": "parcel-sealed",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "S_,W_,P_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "envelopes:signetring-*",
        "isTool": true
      },
      "W": {
        "type": "item",
        "code": "waxstick-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "P": {
        "type": "item",
        "code": "parcel-unsealed"
      }
    },
    "width": 2,
    "height": 3,
    "shapeless": true,
    "copyAttributesFrom": "P",
    "output": {
      "type": "item",
      "code": "parcel-sealed",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>火漆印章 · signetring-disassemble</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 R | 印章戒指<br><code>envelopes:signetring-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆印章<br><code>envelopes:sealstamp-engraved</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
_C_
_RS
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_H_,_C_,_RS",
  "ingredients": {
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true
    },
    "C": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true
    },
    "R": {
      "type": "item",
      "name": "metal",
      "code": "envelopes:signetring-*"
    },
    "S": {
      "type": "item",
      "code": "game:stick"
    }
  },
  "width": 3,
  "height": 3,
  "shapeless": true,
  "recipeGroup": 2,
  "copyAttributesFrom": "R",
  "output": {
    "type": "item",
    "code": "envelopes:sealstamp-engraved",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · signetring-engrave</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'gold', 'silver', 'electrum', 'iron', 'steel', 'meteoriciron'] |
| 投入 G | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 火漆印章<br><code>envelopes:sealstamp-engraved</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>envelopes:signetring-{metal}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSG
_H_
_C_
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "BSG,_H_,_C_",
  "ingredients": {
    "B": {
      "type": "item",
      "name": "metal",
      "code": "game:ingot-*",
      "allowedVariants": [
        "copper",
        "tinbronze",
        "bismuthbronze",
        "blackbronze",
        "gold",
        "silver",
        "electrum",
        "iron",
        "steel",
        "meteoriciron"
      ]
    },
    "G": {
      "type": "item",
      "name": "engraving",
      "code": "game:ingot-*"
    },
    "S": {
      "type": "item",
      "code": "envelopes:sealstamp-engraved"
    },
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true
    },
    "C": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "envelopes:signetring-{metal}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>空白火漆印章 · stamp-reengrave</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 火漆印章<br><code>envelopes:sealstamp-engraved</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 空白火漆印章<br><code>envelopes:sealstamp-blank</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
_C_
_S_
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "_H_,_C_,_S_",
  "ingredients": {
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true
    },
    "C": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true
    },
    "S": {
      "type": "item",
      "code": "envelopes:sealstamp-engraved"
    }
  },
  "width": 3,
  "height": 3,
  "shapeless": true,
  "recipeGroup": 2,
  "output": {
    "type": "item",
    "code": "envelopes:sealstamp-blank",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>空白火漆印章 · wax-seal-stamp</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:ingot-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 空白火漆印章<br><code>envelopes:sealstamp-blank</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_G
_H_
_C_
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "S_G,_H_,_C_",
  "ingredients": {
    "S": {
      "type": "item",
      "code": "game:stick"
    },
    "G": {
      "type": "item",
      "code": "game:ingot-*"
    },
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true
    },
    "C": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true
    }
  },
  "width": 3,
  "height": 3,
  "shapeless": true,
  "recipeGroup": 1,
  "output": {
    "type": "item",
    "code": "envelopes:sealstamp-blank",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>火漆封缄信封 · wax-seal</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 火漆印章<br><code>sealstamp-engraved</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 W | 变体材料（按代码匹配）<br><code>waxstick-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 E | 信封<br><code>envelope-unsealed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆封缄信封<br><code>envelope-sealed</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_
W_
E_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 印章戒指<br><code>envelopes:signetring-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>waxstick-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 E | 信封<br><code>envelope-unsealed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 火漆封缄信封<br><code>envelope-sealed</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_
W_
E_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "S_,W_,E_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "sealstamp-engraved",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "W": {
        "type": "item",
        "code": "waxstick-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "E": {
        "type": "item",
        "code": "envelope-unsealed"
      }
    },
    "width": 2,
    "height": 3,
    "shapeless": true,
    "copyAttributesFrom": "E",
    "output": {
      "type": "item",
      "code": "envelope-sealed",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "S_,W_,E_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "envelopes:signetring-*",
        "isTool": true
      },
      "W": {
        "type": "item",
        "code": "waxstick-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "E": {
        "type": "item",
        "code": "envelope-unsealed"
      }
    },
    "width": 2,
    "height": 3,
    "shapeless": true,
    "copyAttributesFrom": "E",
    "output": {
      "type": "item",
      "code": "envelope-sealed",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>红色火漆棒、黑色火漆棒、绿色火漆棒、蓝色火漆棒、黄色火漆棒、紫色火漆棒、橙色火漆棒、灰色火漆棒、粉色火漆棒、白色火漆棒、原色火漆棒 · waxstick</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 红色火漆棒<br><code>waxstick-red</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 黑色火漆棒<br><code>waxstick-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 绿色火漆棒<br><code>waxstick-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蓝色火漆棒<br><code>waxstick-blue</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蓝色火漆棒<br><code>waxstick-blue</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 黄色火漆棒<br><code>waxstick-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 紫色火漆棒<br><code>waxstick-purple</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 橙色火漆棒<br><code>waxstick-orange</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 灰色火漆棒<br><code>waxstick-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 粉色火漆棒<br><code>waxstick-pink</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 白色火漆棒<br><code>waxstick-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
D
W
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 D | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 原色火漆棒<br><code>waxstick-uncolored</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
W
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-red"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick red",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-red"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-black"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick black",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-black"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-green"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick green",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-green"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-blue"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick blue",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-blue"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-woad"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick woad blue",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-blue"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-yellow"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick yellow",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-yellow"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-purple"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick purple",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-purple"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-orange"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick orange",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-orange"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-gray"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick gray",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-gray"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-pink"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick pink",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-pink"
    }
  },
  {
    "ingredientPattern": "D,W",
    "ingredients": {
      "D": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-white"
        },
        "requiresLitres": 0.2,
        "consumeContainer": false
      }
    },
    "name": "wax stick white",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-white"
    }
  },
  {
    "ingredientPattern": "W,W",
    "ingredients": {
      "D": {
        "type": "item",
        "code": "game:beeswax"
      },
      "W": {
        "type": "item",
        "code": "game:beeswax"
      }
    },
    "width": 1,
    "height": 2,
    "name": "wax stick uncolored",
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "waxstick-uncolored"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
