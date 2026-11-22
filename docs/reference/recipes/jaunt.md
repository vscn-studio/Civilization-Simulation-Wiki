<!-- generated:start -->
# 旅行与移动：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>短途旅行 长笛、骨笛 · jauntflute</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 木炭粉<br><code>game:powder-charcoal</code> | 3 | 未声明附加限制 |
| 投入 L | 骨头<br><code>game:bone</code> | 1 | 未声明附加限制 |
| 产物 | 短途旅行 长笛<br><code>jaunt:instrument-flute</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KCL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 骨笛<br><code>game:instrument-flute1</code> | 1 | 未声明附加限制 |
| 投入 C | 木炭粉<br><code>game:powder-charcoal</code> | 3 | 未声明附加限制 |
| 产物 | 短途旅行 长笛<br><code>jaunt:instrument-flute</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 J | 短途旅行 长笛<br><code>jaunt:instrument-flute</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 骨笛<br><code>game:instrument-flute1</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
JK
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "KCL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:powder-charcoal",
        "quantity": 3
      },
      "L": {
        "type": "item",
        "code": "game:bone",
        "quantity": 1
      }
    },
    "shapeless": true,
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "jaunt:instrument-flute",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "FC",
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:instrument-flute1",
        "quantity": 1
      },
      "C": {
        "type": "item",
        "code": "game:powder-charcoal",
        "quantity": 3
      }
    },
    "shapeless": true,
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "jaunt:instrument-flute",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "JK",
    "ingredients": {
      "J": {
        "type": "item",
        "code": "jaunt:instrument-flute"
      },
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      }
    },
    "shapeless": true,
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:instrument-flute1",
      "quantity": 1
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
