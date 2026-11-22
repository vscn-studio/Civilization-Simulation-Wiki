<!-- generated:start -->
# 采集收获：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · booktoknowledge</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:book-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>foragersgamble:knowledgebook-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "B",
  "ingredients": {
    "B": {
      "type": "item",
      "code": "game:book-*",
      "name": "color"
    }
  },
  "width": 1,
  "height": 1,
  "shapeless": true,
  "output": {
    "type": "item",
    "code": "foragersgamble:knowledgebook-{color}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · knowledgetobook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>foragersgamble:knowledgebook-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:book-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "B",
  "ingredients": {
    "B": {
      "type": "item",
      "code": "foragersgamble:knowledgebook-*",
      "name": "color"
    }
  },
  "width": 1,
  "height": 1,
  "shapeless": true,
  "output": {
    "type": "item",
    "code": "game:book-{color}",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
