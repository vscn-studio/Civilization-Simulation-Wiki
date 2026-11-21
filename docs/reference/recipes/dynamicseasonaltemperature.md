<!-- generated:start -->
# 季节温度：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>时序温度预报器 · Temporaltempforecaster</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 G | 玻璃<br><code>game:glass-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 黄铜锭<br><code>game:ingot-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 黄铜板<br><code>game:metalplate-brass</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 时序温度预报器<br><code>dynamicseasonaltemperature:temporaltempforecaster</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GPG
PMP
 B 
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/dynamicseasonaltemperature/recipes/grid/Temporaltempforecaster.json`

```json
{
  "ingredientPattern": "GPG,PMP, B ",
  "width": 3,
  "height": 3,
  "ingredients": {
    "G": {
      "type": "block",
      "code": "game:glass-plain"
    },
    "P": {
      "type": "item",
      "code": "game:ingot-brass"
    },
    "M": {
      "type": "item",
      "code": "game:gear-temporal"
    },
    "B": {
      "type": "item",
      "code": "game:metalplate-brass"
    }
  },
  "output": {
    "type": "block",
    "code": "dynamicseasonaltemperature:temporaltempforecaster",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
