<!-- generated:start -->
# 望远镜：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · spyglass-glass</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>spytube-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:glass-*</code> | 未声明；按配方类型判定 | 允许变体：['quartz', 'green', 'blue', 'violet', 'red', 'yellow', 'brown', 'vintage', 'smoky', 'pink'] |
| 产物 | 变体材料（按代码匹配）<br><code>spyglass-{metal}-{glass}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
T
G
T
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/spyglassfork/recipes/grid/spyglass-glass.json`

```json
{
  "ingredientPattern": "T,G,T",
  "ingredients": {
    "T": {
      "type": "item",
      "code": "spytube-*",
      "name": "metal"
    },
    "G": {
      "type": "block",
      "code": "game:glass-*",
      "name": "glass",
      "allowedVariants": [
        "quartz",
        "green",
        "blue",
        "violet",
        "red",
        "yellow",
        "brown",
        "vintage",
        "smoky",
        "pink"
      ]
    }
  },
  "width": 1,
  "height": 3,
  "output": {
    "type": "item",
    "code": "spyglass-{metal}-{glass}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · spyglass</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>spytube-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 玻璃<br><code>game:glass-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>spyglass-{metal}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
T
G
T
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/spyglassfork/recipes/grid/spyglass.json`

```json
{
  "ingredientPattern": "T,G,T",
  "ingredients": {
    "T": {
      "type": "item",
      "code": "spytube-*",
      "name": "metal"
    },
    "G": {
      "type": "block",
      "code": "game:glass-plain"
    }
  },
  "width": 1,
  "height": 3,
  "output": {
    "type": "item",
    "code": "spyglass-{metal}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · spytube</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>spytube-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/spyglassfork/recipes/smithing/spytube.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "copper",
      "tinbronze",
      "bismuth",
      "bismuthbronze",
      "blackbronze",
      "gold",
      "silver",
      "iron",
      "meteoriciron",
      "brass",
      "steel"
    ]
  },
  "pattern": [
    [
      "########",
      "########",
      "########"
    ],
    [
      "________",
      "________",
      "########"
    ]
  ],
  "name": "Spyglass Tube",
  "code": "spyglassfork:spytube-{metal}",
  "output": {
    "type": "item",
    "code": "spytube-{metal}"
  }
}
```

</details>

</details>
<!-- generated:end -->
