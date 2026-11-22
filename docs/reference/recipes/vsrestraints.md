<!-- generated:start -->
# 束缚交互：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>铁制手铐 · handcuffs</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 铁锭<br><code>game:ingot-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 铁挂锁<br><code>game:padlock-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 铁制手铐<br><code>vsrestraints:handcuffs</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
I I
 L 
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "I I, L ",
  "ingredients": {
    "I": {
      "type": "item",
      "code": "game:ingot-iron"
    },
    "L": {
      "type": "item",
      "code": "game:padlock-iron"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsrestraints:handcuffs"
  }
}
```

</details>

</details>

<details><summary>铁链 · ironchain</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 铁链<br><code>game:metalchain-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 铁链<br><code>vsrestraints:ironchain</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "C",
  "ingredients": {
    "C": {
      "type": "item",
      "code": "game:metalchain-iron"
    }
  },
  "width": 1,
  "height": 1,
  "output": {
    "type": "item",
    "code": "vsrestraints:ironchain"
  }
}
```

</details>

</details>

<details><summary>铁制脚镣 · legshackles</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 I | 铁锭<br><code>game:ingot-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 铁挂锁<br><code>game:padlock-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 铁制脚镣<br><code>vsrestraints:legshackles</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
I I
ILI
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "I I,ILI",
  "ingredients": {
    "I": {
      "type": "item",
      "code": "game:ingot-iron"
    },
    "L": {
      "type": "item",
      "code": "game:padlock-iron"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "item",
    "code": "vsrestraints:legshackles"
  }
}
```

</details>

</details>

<details><summary>木制颈手枷（打开） · pillory</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 铁挂锁<br><code>game:padlock-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木制颈手枷（打开）<br><code>vsrestraints:pillory-open</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
PLP
P P
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "PPP,PLP,P P",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:plank-*"
    },
    "L": {
      "type": "item",
      "code": "game:padlock-iron"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "vsrestraints:pillory-open"
  }
}
```

</details>

</details>
<!-- generated:end -->
