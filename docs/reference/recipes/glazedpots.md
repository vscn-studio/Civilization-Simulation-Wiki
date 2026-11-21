<!-- generated:start -->
# 上釉陶罐：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>铬铁釉 · blueglaze</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬釉<br><code>glaze-greenglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 铁粉<br><code>game:crushed-iron</code> | 1 | 未声明附加限制 |
| 产物 | 铬铁釉<br><code>glaze-blueglaze</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/blueglaze.json`

```json
[
  {
    "code": "glaze-blueglaze",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-greenglaze",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:crushed-iron",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "glaze-blueglaze",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>铁釉 · brownglaze</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 无色基础釉<br><code>glaze-uncolored</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 铁粉<br><code>game:crushed-iron</code> | 1 | 未声明附加限制 |
| 产物 | 铁釉<br><code>glaze-brownglaze</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/brownglaze.json`

```json
[
  {
    "code": "glaze-brownglaze",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-uncolored",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:crushed-iron",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "glaze-brownglaze",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · glazedflowerpot</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬铁釉<br><code>glaze-blueglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:flowerpot-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>flowerpot-{color}-blueglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铁釉<br><code>glaze-brownglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:flowerpot-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>flowerpot-{color}-brownglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬釉<br><code>glaze-greenglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:flowerpot-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>flowerpot-{color}-greenglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬锡釉<br><code>glaze-redglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:flowerpot-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>flowerpot-{color}-redglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 钛釉<br><code>glaze-whiteglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:flowerpot-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>flowerpot-{color}-whiteglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铁钛釉<br><code>glaze-yellowglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:flowerpot-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>flowerpot-{color}-yellowglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/glazedflowerpot.json`

```json
[
  {
    "code": "glazedflowerpot",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-blueglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:flowerpot-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "flowerpot-{color}-blueglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedflowerpot",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-brownglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:flowerpot-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "flowerpot-{color}-brownglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedflowerpot",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-greenglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:flowerpot-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "flowerpot-{color}-greenglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedflowerpot",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-redglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:flowerpot-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "flowerpot-{color}-redglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedflowerpot",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-whiteglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:flowerpot-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "flowerpot-{color}-whiteglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedflowerpot",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-yellowglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:flowerpot-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "flowerpot-{color}-yellowglaze-glaze",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · glazedplanter</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬铁釉<br><code>glaze-blueglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:clayplanter-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>clayplanter-{color}-blueglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铁釉<br><code>glaze-brownglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:clayplanter-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>clayplanter-{color}-brownglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬釉<br><code>glaze-greenglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:clayplanter-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>clayplanter-{color}-greenglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬锡釉<br><code>glaze-redglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:clayplanter-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>clayplanter-{color}-redglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 钛釉<br><code>glaze-whiteglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:clayplanter-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>clayplanter-{color}-whiteglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铁钛釉<br><code>glaze-yellowglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:clayplanter-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'earthyorange', 'gray', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>clayplanter-{color}-yellowglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/glazedplanter.json`

```json
[
  {
    "code": "glazedplanter",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-blueglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:clayplanter-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "clayplanter-{color}-blueglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedplanter",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-brownglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:clayplanter-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "clayplanter-{color}-brownglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedplanter",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-greenglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:clayplanter-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "clayplanter-{color}-greenglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedplanter",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-redglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:clayplanter-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "clayplanter-{color}-redglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedplanter",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-whiteglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:clayplanter-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "clayplanter-{color}-whiteglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedplanter",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-yellowglaze",
        "litres": 1,
        "consumelitres": 1
      },
      {
        "type": "block",
        "code": "game:clayplanter-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "earthyorange",
          "gray",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "clayplanter-{color}-yellowglaze-glaze",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · glazedvessel</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬铁釉<br><code>glaze-blueglaze</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'gray', 'earthyorange', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>storagevessel-{color}-blueglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铁釉<br><code>glaze-brownglaze</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'gray', 'earthyorange', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>storagevessel-{color}-brownglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬釉<br><code>glaze-greenglaze</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'gray', 'earthyorange', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>storagevessel-{color}-greenglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬锡釉<br><code>glaze-redglaze</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'gray', 'earthyorange', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>storagevessel-{color}-redglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 钛釉<br><code>glaze-whiteglaze</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'gray', 'earthyorange', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>storagevessel-{color}-whiteglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铁钛釉<br><code>glaze-yellowglaze</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 允许变体：['black', 'blue', 'brown', 'cream', 'fire', 'gray', 'earthyorange', 'orange', 'red', 'tan'] |
| 产物 | 变体材料（按代码匹配）<br><code>storagevessel-{color}-yellowglaze-glaze</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/glazedvessel.json`

```json
[
  {
    "code": "glazedvessel",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-blueglaze",
        "litres": 2,
        "consumelitres": 2
      },
      {
        "type": "block",
        "code": "game:storagevessel-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "gray",
          "earthyorange",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "storagevessel-{color}-blueglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedvessel",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-brownglaze",
        "litres": 2,
        "consumelitres": 2
      },
      {
        "type": "block",
        "code": "game:storagevessel-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "gray",
          "earthyorange",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "storagevessel-{color}-brownglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedvessel",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-greenglaze",
        "litres": 2,
        "consumelitres": 2
      },
      {
        "type": "block",
        "code": "game:storagevessel-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "gray",
          "earthyorange",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "storagevessel-{color}-greenglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedvessel",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-redglaze",
        "litres": 2,
        "consumelitres": 2
      },
      {
        "type": "block",
        "code": "game:storagevessel-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "gray",
          "earthyorange",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "storagevessel-{color}-redglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedvessel",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-whiteglaze",
        "litres": 2,
        "consumelitres": 2
      },
      {
        "type": "block",
        "code": "game:storagevessel-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "gray",
          "earthyorange",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "storagevessel-{color}-whiteglaze-glaze",
      "stackSize": 1
    }
  },
  {
    "code": "glazedvessel",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-yellowglaze",
        "litres": 2,
        "consumelitres": 2
      },
      {
        "type": "block",
        "code": "game:storagevessel-*-fired",
        "name": "color",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "cream",
          "fire",
          "gray",
          "earthyorange",
          "orange",
          "red",
          "tan"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "storagevessel-{color}-yellowglaze-glaze",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>铬釉 · greenglaze</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 无色基础釉<br><code>glaze-uncolored</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉碎的铬铁矿<br><code>game:crushed-chromite</code> | 1 | 未声明附加限制 |
| 产物 | 铬釉<br><code>glaze-greenglaze</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/greenglaze.json`

```json
[
  {
    "code": "glaze-greenglaze",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-uncolored",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:crushed-chromite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "glaze-greenglaze",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>铬锡釉 · redglaze</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铬釉<br><code>glaze-greenglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉碎的锡石<br><code>game:crushed-cassiterite</code> | 1 | 未声明附加限制 |
| 产物 | 铬锡釉<br><code>glaze-redglaze</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/redglaze.json`

```json
[
  {
    "code": "glaze-redglaze",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-greenglaze",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:crushed-cassiterite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "glaze-redglaze",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>无色基础釉 · uncolored</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 基础釉料<br><code>glaze-base</code> | 1 | 未声明附加限制 |
| 产物 | 无色基础釉<br><code>glaze-uncolored</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/uncolored.json`

```json
[
  {
    "code": "glaze-uncolored",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "glaze-base",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "glaze-uncolored",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>钛釉 · whiteglaze</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 无色基础釉<br><code>glaze-uncolored</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉碎的钛铁矿<br><code>game:crushed-ilmenite</code> | 1 | 未声明附加限制 |
| 产物 | 钛釉<br><code>glaze-whiteglaze</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/whiteglaze.json`

```json
[
  {
    "code": "glaze-whiteglaze",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-uncolored",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:crushed-ilmenite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "glaze-whiteglaze",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>铁钛釉 · yellowglaze</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 铁釉<br><code>glaze-brownglaze</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 粉碎的钛铁矿<br><code>game:crushed-ilmenite</code> | 1 | 未声明附加限制 |
| 产物 | 铁钛釉<br><code>glaze-yellowglaze</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/barrel/glaze/yellowglaze.json`

```json
[
  {
    "code": "glaze-yellowglaze",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "glaze-brownglaze",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:crushed-ilmenite",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "glaze-yellowglaze",
      "litres": 1
    }
  }
]
```

</details>

</details>

<details><summary>基础釉料 · glaze-base</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 粉碎的明矾<br><code>game:crushed-alum</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 粉碎的石英<br><code>game:crushed-quartz</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 A | 粉碎的铝土矿<br><code>game:crushed-bauxite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 基础釉料<br><code>glazedpots:glaze-base</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
LAL
SLS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/glazedpots/recipes/grid/glaze-base.json`

```json
{
  "ingredientPattern": "SLS,LAL,SLS",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:crushed-alum"
    },
    "S": {
      "type": "item",
      "code": "game:crushed-quartz"
    },
    "A": {
      "type": "item",
      "code": "game:crushed-bauxite"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "item",
    "code": "glazedpots:glaze-base",
    "quantity": 4
  }
}
```

</details>

</details>
<!-- generated:end -->
