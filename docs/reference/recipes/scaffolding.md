<!-- generated:start -->
# 脚手架：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>名称未汉化（见物品代码） · scaffolding</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>scaffolding-top-ns</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BBB
SRS
S_S
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "BBB,SRS,S_S",
  "ingredients": {
    "B": {
      "type": "item",
      "code": "game:plank-*"
    },
    "R": {
      "type": "item",
      "code": "game:rope"
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
    "code": "scaffolding-top-ns",
    "quantity": 4
  }
}
```

</details>

</details>
<!-- generated:end -->
