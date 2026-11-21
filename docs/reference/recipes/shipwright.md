<!-- generated:start -->
# 造船：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：船匠：建造船只

来源：`assets/shipwright/config/handbook/shipwrightguide.json`。

船匠建造

建造任何船只都始于一个 [handbooksearch://Shipwrightguide] 建造工地。这些建造物品在手册中列出了各自船只所需的所有资源。制作完成后，在快捷栏中选择它，世界中会出现一个示意图。你可以使用 toolmodeselect 键更改示意图的朝向。将其放置在平坦区域（确保蓝色高亮的示意图条位于水中）。

之后，如果你开启了方块交互帮助（用 blockinteractionhelp 切换），看向建造中的船只将显示下一个所需的材料。

任何使用亚麻帆的船只都可以用 [handbooksearch://sailrecolor] 船帆改色物品重新着色。

只有最小的船只可以再次捡起，其他船只只能拆解。

拆解：你可以用 [handbooksearch://saw] 锯子右键点击任何船只来拆解，以取回一部分材料。你需要按住鼠标按钮一段时间，才能完成。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · dyes</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 5 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-half-*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 变体材料（按代码匹配）<br><code>drakkartent-half-{color}-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：5。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 5 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-half-striped*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 变体材料（按代码匹配）<br><code>drakkartent-half-striped{color}-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：5。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 10 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-full-*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 变体材料（按代码匹配）<br><code>drakkartent-full-{color}-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 10 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-full-striped*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 变体材料（按代码匹配）<br><code>drakkartent-full-striped{color}-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 2 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 名称未汉化（见物品代码）<br><code>boatdeco-flags-normal</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>boatdeco-flags-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 2 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 名称未汉化（见物品代码）<br><code>boatdeco-full-normal</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>boatdeco-full-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>game:dye-*</code> | 2 升 | 允许变体：['white', 'black', 'green', 'blue', 'orange', 'red', 'yellow', 'purple', 'pink', 'gray'] |
| 投入 2 | 未染色的德拉克船旗<br><code>drakkarflag-normal</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>drakkarflag-{color}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/barrel/dyes.json`

```json
[
  {
    "code": "recolor",
    "sealHours": 5,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "drakkartent-half-*-closed",
        "name": "type",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "drakkartent-half-{color}-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 5,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "drakkartent-half-striped*-closed",
        "name": "type",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "drakkartent-half-striped{color}-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "drakkartent-full-*-closed",
        "name": "type",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "drakkartent-full-{color}-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "drakkartent-full-striped*-closed",
        "name": "type",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "drakkartent-full-striped{color}-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "boatdeco-flags-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "boatdeco-flags-{color}",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "boatdeco-full-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "boatdeco-full-{color}",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-*",
        "name": "color",
        "allowedVariants": [
          "white",
          "black",
          "green",
          "blue",
          "orange",
          "red",
          "yellow",
          "purple",
          "pink",
          "gray"
        ],
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "drakkarflag-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "drakkarflag-{color}",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>小型德拉克帐篷（棕色）、小型德拉克帐篷（条纹棕）、大型德拉克帐篷（棕色）、大型德拉克帐篷（条纹棕）、名称未汉化（见物品代码）、德拉克船旗（棕色） · tannin</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-half-*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 小型德拉克帐篷（棕色）<br><code>drakkartent-half-brown-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：5。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-half-striped*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 小型德拉克帐篷（条纹棕）<br><code>drakkartent-half-stripedbrown-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：5。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-full-*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 大型德拉克帐篷（棕色）<br><code>drakkartent-full-brown-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-full-striped*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 大型德拉克帐篷（条纹棕）<br><code>drakkartent-full-stripedbrown-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>boatdeco-flags-normal</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>boatdeco-flags-brown</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>boatdeco-full-normal</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>boatdeco-full-brown</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 强单宁<br><code>game:strongtanninportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 未染色的德拉克船旗<br><code>drakkarflag-normal</code> | 1 | 未声明附加限制 |
| 产物 | 德拉克船旗（棕色）<br><code>drakkarflag-brown</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/barrel/tannin.json`

```json
[
  {
    "code": "recolor",
    "sealHours": 5,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "drakkartent-half-*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-half-brown-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 5,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "drakkartent-half-striped*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-half-stripedbrown-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "drakkartent-full-*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-full-brown-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "drakkartent-full-striped*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-full-stripedbrown-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "boatdeco-flags-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "boatdeco-flags-brown",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "boatdeco-full-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "boatdeco-full-brown",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:strongtanninportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "drakkarflag-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkarflag-brown",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>小型德拉克帐篷（蓝色）、小型德拉克帐篷（条纹蓝）、大型德拉克帐篷（蓝色）、大型德拉克帐篷（条纹蓝）、名称未汉化（见物品代码）、德拉克船旗（蓝色） · woad</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-half-*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 小型德拉克帐篷（蓝色）<br><code>drakkartent-half-blue-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：5。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-half-striped*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 小型德拉克帐篷（条纹蓝）<br><code>drakkartent-half-stripedblue-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：5。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-full-*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 大型德拉克帐篷（蓝色）<br><code>drakkartent-full-blue-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>drakkartent-full-striped*-closed</code> | 1 | 允许变体：['plain'] |
| 产物 | 大型德拉克帐篷（条纹蓝）<br><code>drakkartent-full-stripedblue-closed</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：10。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>boatdeco-flags-normal</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>boatdeco-flags-blue</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>boatdeco-full-normal</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>boatdeco-full-blue</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 未染色的德拉克船旗<br><code>drakkarflag-normal</code> | 1 | 未声明附加限制 |
| 产物 | 德拉克船旗（蓝色）<br><code>drakkarflag-blue</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/barrel/woad.json`

```json
[
  {
    "code": "recolor",
    "sealHours": 5,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "drakkartent-half-*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-half-blue-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 5,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "item",
        "code": "drakkartent-half-striped*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-half-stripedblue-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "drakkartent-full-*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-full-blue-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 10,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "drakkartent-full-striped*-closed",
        "name": "color",
        "allowedVariants": [
          "plain"
        ],
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkartent-full-stripedblue-closed",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "boatdeco-flags-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "boatdeco-flags-blue",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "boatdeco-full-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "boatdeco-full-blue",
      "stackSize": 1
    }
  },
  {
    "code": "recolor",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:dye-woad",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "drakkarflag-normal",
        "quantity": 1
      }
    ],
    "recipeGroup": 3,
    "output": {
      "type": "item",
      "code": "drakkarflag-blue",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码）、变体材料（按代码匹配）、装饰性单桅帆船三角帆、船罩 · boatdeco</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>boatdeco-rope-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KO
OO
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 蜡烛<br><code>game:candle</code> | 6 | 未声明附加限制 |
| 投入 R | 羊皮纸<br><code>game:paper-parchment</code> | 6 | 未声明附加限制 |
| 投入 B | 名称未汉化（见物品代码）<br><code>boatdeco-rope-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>boatdeco-lanterns-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CRB
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 6 | 未声明附加限制 |
| 投入 B | 名称未汉化（见物品代码）<br><code>boatdeco-rope-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>boatdeco-flags-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LB
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>boatdeco-lanterns-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>boatdeco-flags-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>boatdeco-full-{color}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LB
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 变体材料（按代码匹配）<br><code>game:supportbeam-*</code> | 2 | 未声明附加限制 |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 2 | 未声明附加限制 |
| 产物 | 装饰性单桅帆船三角帆<br><code>jibsail-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KO_
LL_
LL_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 2 | 未声明附加限制 |
| 产物 | 船罩<br><code>boatcover</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KO_
LL_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/boatdeco.json`

```json
[
  {
    "ingredientPattern": "KO,OO",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "schematics-shipwright"
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "boatdeco-rope-normal"
    }
  },
  {
    "ingredientPattern": "CRB",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:candle",
        "quantity": 6
      },
      "R": {
        "type": "item",
        "code": "game:paper-parchment",
        "quantity": 6
      },
      "B": {
        "type": "item",
        "code": "boatdeco-rope-normal"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "boatdeco-lanterns-normal"
    }
  },
  {
    "ingredientPattern": "LB",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-normal-down",
        "quantity": 6
      },
      "B": {
        "type": "item",
        "code": "boatdeco-rope-normal"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "boatdeco-flags-normal"
    }
  },
  {
    "ingredientPattern": "LB",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "boatdeco-lanterns-normal"
      },
      "B": {
        "type": "item",
        "code": "boatdeco-flags-*",
        "name": "color"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "boatdeco-full-{color}"
    }
  },
  {
    "ingredientPattern": "KO_,LL_,LL_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "schematics-shipwright"
      },
      "O": {
        "type": "block",
        "code": "game:supportbeam-*",
        "quantity": 2
      },
      "L": {
        "type": "block",
        "code": "game:linen-normal-down",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "jibsail-closed"
    }
  },
  {
    "ingredientPattern": "KO_,LL_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "schematics-shipwright"
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      },
      "L": {
        "type": "block",
        "code": "game:linen-normal-down",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "boatcover"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码）、变体材料（按代码匹配） · dragonhorn</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>draconis:horn-curve-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiphorn-curve-inventory</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>draconis:horn-snake-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiphorn-snake-inventory</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>shiphorn-*-inventory</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>draconis:horn-{type}-unbound</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/dragonhorn.json`

```json
[
  {
    "enabled": false,
    "ingredientPattern": "K",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "draconis:horn-curve-*",
        "name": "type"
      }
    },
    "code": "horna",
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "shiphorn-curve-inventory",
      "quantity": 1
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "K",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "draconis:horn-snake-*",
        "name": "type"
      }
    },
    "code": "hornb",
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "output": {
      "type": "item",
      "code": "shiphorn-snake-inventory",
      "quantity": 1
    }
  },
  {
    "enabled": false,
    "ingredientPattern": "K",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "shiphorn-*-inventory",
        "name": "type"
      }
    },
    "code": "hornc",
    "width": 1,
    "height": 1,
    "recipeGroup": 2,
    "output": {
      "type": "item",
      "code": "draconis:horn-{type}-unbound",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>未染色的德拉克船旗 · drakkarflag</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 1 | 未声明附加限制 |
| 投入 B | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 K | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 未染色的德拉克船旗<br><code>drakkarflag-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LB
LK
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/drakkarflag.json`

```json
[
  {
    "ingredientPattern": "LB,LK",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-normal-down",
        "quantity": 1
      },
      "B": {
        "type": "item",
        "code": "game:rope"
      },
      "K": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "drakkarflag-normal"
    }
  }
]
```

</details>

</details>

<details><summary>小型德拉克帐篷（素色）、大型德拉克帐篷（素色）、变体材料（按代码匹配） · drakkartent</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 2 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 小型德拉克帐篷（素色）<br><code>drakkartent-half-plain-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LWL
LSL
LWL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 4 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 大型德拉克帐篷（素色）<br><code>drakkartent-full-plain-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LLL
WSW
LLL
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>drakkartent-*-plain-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>drakkartent-{type}-stripedplain-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>drakkartent-*-stripedplain-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>drakkartent-{type}-plain-closed</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/drakkartent.json`

```json
[
  {
    "ingredientPattern": "LWL,LSL,LWL",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-normal-down",
        "quantity": 2
      },
      "W": {
        "type": "block",
        "code": "game:supportbeam-*"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "drakkartent-half-plain-closed"
    }
  },
  {
    "ingredientPattern": "LLL,WSW,LLL",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-normal-down",
        "quantity": 4
      },
      "W": {
        "type": "block",
        "code": "game:supportbeam-*"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "drakkartent-full-plain-closed"
    }
  },
  {
    "ingredientPattern": "TS",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "drakkartent-*-plain-closed",
        "name": "type"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "drakkartent-{type}-stripedplain-closed"
    }
  },
  {
    "ingredientPattern": "TS",
    "ingredients": {
      "T": {
        "type": "item",
        "code": "drakkartent-*-stripedplain-closed",
        "name": "type"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 2,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "drakkartent-{type}-plain-closed"
    }
  }
]
```

</details>

</details>

<details><summary>老旧船首像（熊）、老旧船首像（齿轮）、老旧船首像（塞壬）、老旧船首像（骷髅）、老旧船首像（狼）、变体材料（按代码匹配） · figurehead</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:log-placed-aged-ud</code> | 2 | 未声明附加限制 |
| 产物 | 老旧船首像（熊）<br><code>agedfigurehead-bear</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLH
ALC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:log-placed-aged-ud</code> | 2 | 未声明附加限制 |
| 产物 | 老旧船首像（齿轮）<br><code>agedfigurehead-gear</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ALH
SLC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:log-placed-aged-ud</code> | 2 | 未声明附加限制 |
| 产物 | 老旧船首像（塞壬）<br><code>agedfigurehead-siren</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HLA
CLS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:log-placed-aged-ud</code> | 3 | 未声明附加限制 |
| 产物 | 老旧船首像（骷髅）<br><code>agedfigurehead-skull</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ALH
CLS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 变体材料（按代码匹配）<br><code>game:axe-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:log-placed-aged-ud</code> | 2 | 未声明附加限制 |
| 产物 | 老旧船首像（狼）<br><code>agedfigurehead-wolf</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HLS
CLA
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:figurehead-*</code> | 1 | 未声明附加限制 |
| 投入 R | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>agedfigurehead-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LRS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/figurehead.json`

```json
[
  {
    "ingredientPattern": "SLH,ALC",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "L": {
        "type": "block",
        "code": "game:log-placed-aged-ud",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "agedfigurehead-bear",
      "quantity": 1,
      "attributes": {}
    }
  },
  {
    "ingredientPattern": "ALH,SLC",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "L": {
        "type": "block",
        "code": "game:log-placed-aged-ud",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "agedfigurehead-gear",
      "quantity": 1,
      "attributes": {}
    }
  },
  {
    "ingredientPattern": "HLA,CLS",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "L": {
        "type": "block",
        "code": "game:log-placed-aged-ud",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "agedfigurehead-siren",
      "quantity": 1,
      "attributes": {}
    }
  },
  {
    "ingredientPattern": "ALH,CLS",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "L": {
        "type": "block",
        "code": "game:log-placed-aged-ud",
        "quantity": 3
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "agedfigurehead-skull",
      "quantity": 1,
      "attributes": {}
    }
  },
  {
    "ingredientPattern": "HLS,CLA",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "game:axe-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 1
      },
      "L": {
        "type": "block",
        "code": "game:log-placed-aged-ud",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "agedfigurehead-wolf",
      "quantity": 1,
      "attributes": {}
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "oak"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "birch"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "maple"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "pine"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "acacia"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "kapok"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "baldcypress"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "larch"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "redwood"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "ebony"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "walnut"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "purpleheart"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "LRS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:figurehead-*",
        "name": "type",
        "attributes": {
          "material": "aged"
        },
        "quantity": 1
      },
      "R": {
        "type": "item",
        "code": "game:resin"
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "agedfigurehead-{type}",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · lanterns</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-copper-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-copper-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-brass-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-brass-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-blackbronze-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-blackbronze-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-bismuth-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-bismuth-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-tinbronze-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-tinbronze-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-bismuthbronze-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-bismuthbronze-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-iron-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-iron-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-molybdochalkos-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-molybdochalkos-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-silver-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-silver-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-gold-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-gold-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 21**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-steel-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 22**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-steel-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 23**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-meteoriciron-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 24**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-meteoriciron-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 25**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shiplantern-electrum-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 26**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>shiplantern-electrum-lit</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:lantern-large-up</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/lanterns.json`

```json
[
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "copper",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-copper-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-copper-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "copper",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "brass",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-brass-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-brass-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "brass",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "blackbronze",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-blackbronze-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-blackbronze-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "blackbronze",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "bismuth",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-bismuth-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-bismuth-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "bismuth",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "tinbronze",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-tinbronze-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-tinbronze-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "tinbronze",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "bismuthbronze",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-bismuthbronze-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-bismuthbronze-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "bismuthbronze",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "iron",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-iron-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-iron-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "iron",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "molybdochalkos",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-molybdochalkos-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-molybdochalkos-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "molybdochalkos",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "silver",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-silver-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-silver-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "silver",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "gold",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-gold-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-gold-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "gold",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "steel",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-steel-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-steel-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "steel",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "meteoriciron",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-meteoriciron-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-meteoriciron-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "meteoriciron",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  },
  {
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:lantern-large-up",
        "attributes": {
          "material": "electrum",
          "lining": "plain",
          "glass": "quartz"
        }
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "shiplantern-electrum-lit"
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "shiplantern-electrum-lit"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 3,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:lantern-large-up",
      "attributes": {
        "material": "electrum",
        "lining": "plain",
        "glass": "quartz"
      }
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、名称未汉化（见物品代码） · oars</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['veryaged'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>oar-long-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WR
WO
WO
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['veryaged'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>oar-basic-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_R
WO
WO
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['veryaged'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>oar-double-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_R_
WOW
_O_
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 排除变体：['veryaged'] |
| 投入 S | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>oarset-packed</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WSW
WWW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/oars.json`

```json
[
  {
    "code": "oar1",
    "ingredientPattern": "WR,WO,WO",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
        "skipVariants": [
          "veryaged"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 1
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "oar-long-{wood}"
    }
  },
  {
    "code": "oar2",
    "ingredientPattern": "_R,WO,WO",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
        "skipVariants": [
          "veryaged"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 1
      }
    },
    "width": 2,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "oar-basic-{wood}"
    }
  },
  {
    "enabled": false,
    "code": "oar2",
    "ingredientPattern": "_R_,WOW,_O_",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
        "skipVariants": [
          "veryaged"
        ]
      },
      "R": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "oar-double-{wood}"
    }
  },
  {
    "code": "oar",
    "ingredientPattern": "WWW,WSW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
        "skipVariants": [
          "veryaged"
        ],
        "Quantity": 4
      },
      "S": {
        "type": "item",
        "code": "schematics-shipwright"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "oarset-packed"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · roller</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:*</code> | 4 | 允许变体：['cattailtops', 'papyrustops'] |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-totora</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RWR
ORO
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 2 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-coracle</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WW_
_O_
WW_
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 2 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-kayak</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W_W
_O_
W_W
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 2 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-catboat</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
_O_
WWW
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 2 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-punter</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W_W
WOW
W_W
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 1 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-drakkar</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WOW
WWW
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:*</code> | 4 | 允许变体：['cattailtops', 'papyrustops'] |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-reedlongboat</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RWR
ORO
RWR
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:*</code> | 4 | 允许变体：['cattailtops', 'papyrustops'] |
| 投入 O | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-sailedreedboat</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
ROR
WRW
ROR
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 木柴<br><code>game:firewood</code> | 1 | 未声明附加限制 |
| 投入 O | 绳索捆<br><code>game:rope</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>shipwrightroller-faering</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
WOW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/roller.json`

```json
[
  {
    "code": "customroller1",
    "ingredientPattern": "RWR,ORO",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood"
      },
      "R": {
        "type": "item",
        "code": "game:*",
        "name": "type",
        "allowedVariants": [
          "cattailtops",
          "papyrustops"
        ],
        "quantity": 4
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-totora"
    }
  },
  {
    "code": "customroller2",
    "ingredientPattern": "WW_,_O_,WW_",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 2
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-coracle"
    }
  },
  {
    "code": "customroller3",
    "ingredientPattern": "W_W,_O_,W_W",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 2
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-kayak"
    }
  },
  {
    "code": "customroller4",
    "ingredientPattern": "WWW,_O_,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 2
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-catboat"
    }
  },
  {
    "code": "customroller5",
    "ingredientPattern": "W_W,WOW,W_W",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 2
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-punter"
    }
  },
  {
    "code": "customroller6",
    "ingredientPattern": "WWW,WOW,WWW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 1
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-drakkar"
    }
  },
  {
    "code": "customroller7",
    "ingredientPattern": "RWR,ORO,RWR",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood"
      },
      "R": {
        "type": "item",
        "code": "game:*",
        "name": "type",
        "allowedVariants": [
          "cattailtops",
          "papyrustops"
        ],
        "quantity": 4
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-reedlongboat"
    }
  },
  {
    "code": "customroller8",
    "ingredientPattern": "ROR,WRW,ROR",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood"
      },
      "R": {
        "type": "item",
        "code": "game:*",
        "name": "type",
        "allowedVariants": [
          "cattailtops",
          "papyrustops"
        ],
        "quantity": 4
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-sailedreedboat"
    }
  },
  {
    "code": "customroller6",
    "ingredientPattern": "WWW,WOW",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "game:firewood",
        "quantity": 1
      },
      "O": {
        "type": "item",
        "code": "game:rope",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "shipwrightroller-faering"
    }
  }
]
```

</details>

</details>

<details><summary>船用梯绳、名称未汉化（见物品代码） · ropeladderswap</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:ladder-rope-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船用梯绳<br><code>ladderrope</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 船用梯绳<br><code>ladderrope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:ladder-rope-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/ropeladderswap.json`

```json
[
  {
    "code": "ropeladder1",
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:ladder-rope-north"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "ladderrope"
    }
  },
  {
    "code": "ropeladder2",
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "ladderrope"
      }
    },
    "width": 1,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "block",
      "code": "game:ladder-rope-north"
    }
  }
]
```

</details>

</details>

<details><summary>德拉克船徽章画布、名称未汉化（见物品代码） · saillogos</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_W_
WLW
_W_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['stone-chalk', 'stone-limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-alpine-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LW
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-alpine-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LW
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-alpine-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LW
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-cross-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WL
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-cross-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WL
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-cross-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WL
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-dave-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
L
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-dave-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
L
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-dave-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
L
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-yggdrasil-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
W
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-yggdrasil-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
W
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-yggdrasil-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
W
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-helmofawe-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L_
_W
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-helmofawe-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L_
_W
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-helmofawe-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L_
_W
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-knot-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W_
_L
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-knot-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W_
_L
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-knot-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W_
_L
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-raven-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_W
L_
```

**方案 21**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-raven-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_W
L_
```

**方案 22**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-raven-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_W
L_
```

**方案 23**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-spider-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_L
W_
```

**方案 24**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-spider-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_L
W_
```

**方案 25**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-spider-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_L
W_
```

**方案 26**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 未声明；按配方类型判定 | 允许变体：['chalk', 'limestone'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-gear-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WLW
```

**方案 27**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 褐煤<br><code>game:ore-lignite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-gear-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WLW
```

**方案 28**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 德拉克船徽章画布<br><code>saillogo-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:*</code> | 未声明；按配方类型判定 | 允许变体：['charcoal', 'bituminouscoal'] |
| 产物 | 名称未汉化（见物品代码）<br><code>saillogo-gear-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WLW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/saillogos.json`

```json
[
  {
    "ingredientPattern": "_W_,WLW,_W_",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "game:linen-normal-down"
      },
      "W": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 3,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-empty"
    }
  },
  {
    "ingredientPattern": "LW",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "stone-chalk",
          "stone-limestone"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-alpine-white"
    }
  },
  {
    "ingredientPattern": "LW",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-alpine-brown"
    }
  },
  {
    "ingredientPattern": "LW",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-alpine-black"
    }
  },
  {
    "ingredientPattern": "WL",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-cross-white"
    }
  },
  {
    "ingredientPattern": "WL",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-cross-brown"
    }
  },
  {
    "ingredientPattern": "WL",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-cross-black"
    }
  },
  {
    "ingredientPattern": "W,L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-dave-white"
    }
  },
  {
    "ingredientPattern": "W,L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-dave-brown"
    }
  },
  {
    "ingredientPattern": "W,L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-dave-black"
    }
  },
  {
    "ingredientPattern": "L,W",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-yggdrasil-white"
    }
  },
  {
    "ingredientPattern": "L,W",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-yggdrasil-brown"
    }
  },
  {
    "ingredientPattern": "L,W",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 1,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-yggdrasil-black"
    }
  },
  {
    "ingredientPattern": "L_,_W",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-helmofawe-white"
    }
  },
  {
    "ingredientPattern": "L_,_W",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-helmofawe-brown"
    }
  },
  {
    "ingredientPattern": "L_,_W",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-helmofawe-black"
    }
  },
  {
    "ingredientPattern": "W_,_L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-knot-white"
    }
  },
  {
    "ingredientPattern": "W_,_L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-knot-brown"
    }
  },
  {
    "ingredientPattern": "W_,_L",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-knot-black"
    }
  },
  {
    "ingredientPattern": "_W,L_",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-raven-white"
    }
  },
  {
    "ingredientPattern": "_W,L_",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-raven-brown"
    }
  },
  {
    "ingredientPattern": "_W,L_",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-raven-black"
    }
  },
  {
    "ingredientPattern": "_L,W_",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-spider-white"
    }
  },
  {
    "ingredientPattern": "_L,W_",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-spider-brown"
    }
  },
  {
    "ingredientPattern": "_L,W_",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-spider-black"
    }
  },
  {
    "ingredientPattern": "WLW",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:stone-*",
        "allowedVariants": [
          "chalk",
          "limestone"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-gear-white"
    }
  },
  {
    "ingredientPattern": "WLW",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:ore-lignite"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-gear-brown"
    }
  },
  {
    "ingredientPattern": "WLW",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "saillogo-empty"
      },
      "W": {
        "type": "item",
        "code": "game:*",
        "allowedVariants": [
          "charcoal",
          "bituminouscoal"
        ]
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "saillogo-gear-black"
    }
  }
]
```

</details>

</details>

<details><summary>船帆改色（白色）、船帆改色（条纹白）、船帆改色（黑色）、船帆改色（条纹黑）、船帆改色（绿色）、船帆改色（条纹绿）、船帆改色（蓝色）、船帆改色（条纹蓝）、船帆改色（橙色）、船帆改色（条纹橙）、船帆改色（红色）、船帆改色（条纹红）、船帆改色（黄色）、船帆改色（条纹黄）、船帆改色（紫色）、船帆改色（条纹紫）、船帆改色（粉色）、船帆改色（条纹粉）、船帆改色（灰色）、船帆改色（条纹灰）、船帆改色（棕色）、船帆改色（条纹棕） · sailrecolor</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（白色）<br><code>sailrecolor-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹白）<br><code>sailrecolor-stripedwhite</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（黑色）<br><code>sailrecolor-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹黑）<br><code>sailrecolor-stripedblack</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（绿色）<br><code>sailrecolor-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹绿）<br><code>sailrecolor-stripedgreen</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（蓝色）<br><code>sailrecolor-blue</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹蓝）<br><code>sailrecolor-stripedblue</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（蓝色）<br><code>sailrecolor-blue</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹蓝）<br><code>sailrecolor-stripedblue</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（橙色）<br><code>sailrecolor-orange</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹橙）<br><code>sailrecolor-stripedorange</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（红色）<br><code>sailrecolor-red</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹红）<br><code>sailrecolor-stripedred</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（黄色）<br><code>sailrecolor-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹黄）<br><code>sailrecolor-stripedyellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（紫色）<br><code>sailrecolor-purple</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹紫）<br><code>sailrecolor-stripedpurple</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（粉色）<br><code>sailrecolor-pink</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹粉）<br><code>sailrecolor-stripedpink</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 21**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（灰色）<br><code>sailrecolor-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 22**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹灰）<br><code>sailrecolor-stripedgray</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 23**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（棕色）<br><code>sailrecolor-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 24**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹棕）<br><code>sailrecolor-stripedbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

**方案 25**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（棕色）<br><code>sailrecolor-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BSB
```

**方案 26**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船帆改色（条纹棕）<br><code>sailrecolor-stripedbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/sailrecolor.json`

```json
[
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-white"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-white"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-white"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedwhite"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-black"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-black"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-black"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedblack"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-green"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-green"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-green"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedgreen"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-blue"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-blue"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-blue"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedblue"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-woad"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-blue"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-woad"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedblue"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-orange"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-orange"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-orange"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedorange"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-red"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-red"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-red"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedred"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-yellow"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-yellow"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-yellow"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedyellow"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-purple"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-purple"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-purple"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedpurple"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-pink"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-pink"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-pink"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedpink"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-gray"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-gray"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-gray"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedgray"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:weaktanninportion"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-brown"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:weaktanninportion"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedbrown"
    }
  },
  {
    "ingredientPattern": "BSB",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:strongtanninportion"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-brown"
    }
  },
  {
    "ingredientPattern": "BS",
    "ingredients": {
      "B": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 1,
    "recipeGroup": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:strongtanninportion"
        },
        "requiresLitres": 10
      }
    },
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "sailrecolor-stripedbrown"
    }
  }
]
```

</details>

</details>

<details><summary>船匠图纸 · schematics</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 木炭<br><code>game:charcoal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 船匠图纸<br><code>schematics-shipwright</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RCS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/shipwright/recipes/grid/schematics.json`

```json
[
  {
    "code": "cartsschematic",
    "ingredientPattern": "RCS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "C": {
        "type": "item",
        "code": "game:charcoal"
      },
      "R": {
        "type": "item",
        "code": "game:rope"
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": false,
    "output": {
      "type": "item",
      "code": "schematics-shipwright"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
