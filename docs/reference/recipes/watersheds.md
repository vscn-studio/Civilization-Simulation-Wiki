<!-- generated:start -->
# 流域生成：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · wellpulley</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wellpulley-{wood}-down</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AK_
FLF
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/watersheds/recipes/grid/wellpulley.json`

```json
{
  "ingredientPattern": "AK_,FLF",
  "ingredients": {
    "A": {
      "type": "item",
      "code": "game:axe-*",
      "isTool": true,
      "toolDurabilityCost": 1
    },
    "K": {
      "type": "item",
      "code": "game:knife-*",
      "isTool": true,
      "toolDurabilityCost": 1
    },
    "L": {
      "type": "block",
      "code": "game:log-placed-*-ud",
      "name": "wood"
    },
    "F": {
      "type": "item",
      "code": "game:firewood"
    }
  },
  "width": 3,
  "height": 2,
  "shapeless": false,
  "output": {
    "type": "block",
    "code": "wellpulley-{wood}-down",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
