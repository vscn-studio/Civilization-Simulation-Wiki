<!-- generated:start -->
# 乡野烹饪：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · roastingdish</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>rusticcookery:roastingdish-{color}-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "game:clay-*",
    "name": "color",
    "allowedVariants": [
      "blue",
      "fire",
      "red"
    ]
  },
  "pattern": [
    [
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############"
    ],
    [
      "############",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "############"
    ],
    [
      "############",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "############"
    ]
  ],
  "name": "Roasting dish",
  "output": {
    "type": "block",
    "code": "rusticcookery:roastingdish-{color}-raw"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · roastingdishlid</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>rusticcookery:roastingdishlid-{color}-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredient": {
    "type": "item",
    "code": "game:clay-*",
    "name": "color",
    "allowedVariants": [
      "blue",
      "fire",
      "red"
    ]
  },
  "pattern": [
    [
      "############",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "############"
    ],
    [
      "############",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "#__________#",
      "############"
    ],
    [
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############",
      "############"
    ],
    [
      "____________",
      "____________",
      "____________",
      "____________",
      "____________",
      "____####____",
      "____####____",
      "____________",
      "____________",
      "____________",
      "____________",
      "____________"
    ]
  ],
  "name": "Roasting dish lid",
  "output": {
    "type": "block",
    "code": "rusticcookery:roastingdishlid-{color}-raw"
  }
}
```

</details>

</details>

<details><summary>熏肉钩 · smokehook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 熏肉钩<br><code>rusticcookery:smokehook</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
S
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "L,S",
  "ingredients": {
    "L": {
      "type": "block",
      "code": "game:log-placed-*-ud"
    },
    "S": {
      "type": "item",
      "code": "game:stick"
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "block",
    "code": "rusticcookery:smokehook",
    "quantity": 2
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · smokerack</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-placed-*-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>rusticcookery:smokerack-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LSL
SSS
SSS
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "LSL,SSS,SSS",
  "ingredients": {
    "L": {
      "type": "block",
      "code": "game:log-placed-*-ud"
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
    "code": "rusticcookery:smokerack-east",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
