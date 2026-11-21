<!-- generated:start -->
# 肥皂与碱液：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：肥皂与碱液：肥皂基础

来源：`assets/soapandlyecontinued/config/handbook/soapandlyecontinued-basics.json`。

只有肥皂和碱液

木灰：

你的制皂之旅始于在火坑中燃烧原木以产生 [handbook://item-soapandlyecontinued:woodash] 木灰。它是生产 [handbook://item-soapandlyecontinued:lyeportion] 液体碱液的主要原料。

碱液：

液体碱液可以代替石灰水用于浸泡动物生皮，或在桶中与脂肪混合制成 [handbook://item-soapandlyecontinued:soapbar-lye] 碱液皂块。

皂块：

你将制作的第一种皂块是基础的碱液皂块。然后可以立即在桶中与水混合制成 [handbook://item-soapandlyecontinued:soapportion-lye] 液体碱液皂，或用 [handbook://item-soapandlyecontinued:soapportion-honey] 蜂蜜增香。

蜂蜜皂：

[handbook://item-soapandlyecontinued:soapbar-honey] 蜂蜜皂块值得额外费力制作，因为由其制成的液体皂清洗物品所需升数更少。

液体皂：

液体皂可用于去除布料和皮革上的染料、去除布料上的媒染剂，以及清洁脏锅！

钾碱：

现在可以通过在火坑上的烹饪锅中煮沸水和木灰来制作 [handbook://item-potash] 钾肥！

兼容性：

烹饪火炮：液体皂可以装瓶，并从各种商人处出售或购买。

食物搁架：皂块可以放在酒吧搁架上！

野性工艺树木：在野性工艺树木更新之前，焦木和我的木灰之间暂时转换。

羊毛：液体皂可用于清洗羊毛，并去除所有羊毛相关物品上的染料或媒染剂！

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>木灰 · woodash</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 名称未汉化（见物品代码）<br><code>wildcrafttree:log-placed-charred-ud</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木灰<br><code>soapandlyecontinued:woodash</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>wildcrafttree:debarkedlog-charred-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木灰<br><code>soapandlyecontinued:woodash</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/soapandlyecontinued/compatibility/wildcrafttree/recipes/grid/woodash.json`

```json
[
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "wildcrafttree:log-placed-charred-ud"
      }
    },
    "width": 1,
    "height": 1,
    "output": {
      "type": "item",
      "code": "soapandlyecontinued:woodash",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "L",
    "ingredients": {
      "L": {
        "type": "block",
        "code": "wildcrafttree:debarkedlog-charred-*"
      }
    },
    "width": 1,
    "height": 1,
    "output": {
      "type": "item",
      "code": "soapandlyecontinued:woodash",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>媒染羊毛线、羊毛线 · undye_twine</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:twine-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['gray', 'green', 'orange', 'white', 'yellow'] |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:twine-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['gray', 'green', 'orange', 'white', 'yellow'] |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:twine-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['black', 'blue', 'brown', 'purple', 'red', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:twine-wool-*</code> | 未声明；按配方类型判定 | 允许变体：['black', 'blue', 'brown', 'purple', 'red', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 产物 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛线<br><code>wool:twine-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 媒染羊毛线<br><code>wool:twine-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛线<br><code>wool:twine-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/soapandlyecontinued/compatibility/wool/recipes/barrel/undye_twine.json`

```json
[
  {
    "code": "undyingwooltwinelight",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:twine-wool-*",
        "name": "color",
        "allowedVariants": [
          "gray",
          "green",
          "orange",
          "white",
          "yellow"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  },
  {
    "code": "undyingwooltwinelight1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:twine-wool-*",
        "name": "color",
        "allowedVariants": [
          "gray",
          "green",
          "orange",
          "white",
          "yellow"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  },
  {
    "code": "undyingwooltwinedark",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "wool:twine-wool-*",
        "name": "color",
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "purple",
          "red",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  },
  {
    "code": "undyingwooltwinedark1",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:twine-wool-*",
        "name": "color",
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "purple",
          "red",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-mordant"
    }
  },
  {
    "code": "undyingwooltwinemordant",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:twine-wool-mordant"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-plain"
    }
  },
  {
    "code": "undyingwooltwinemordant1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:twine-wool-mordant"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:twine-wool-plain"
    }
  }
]
```

</details>

</details>

<details><summary>媒染羊毛布、素色羊毛布 · undye_wool</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 1 | 允许变体：['gray', 'green', 'orange', 'white', 'yellow'] |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 1 | 允许变体：['gray', 'green', 'orange', 'white', 'yellow'] |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 1 | 允许变体：['black', 'blue', 'brown', 'purple', 'red', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:cloth-wool-*</code> | 1 | 允许变体：['black', 'blue', 'brown', 'purple', 'red', 'darkblue', 'darkbrown', 'darkgreen', 'darkred'] |
| 产物 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 1 | 未声明附加限制 |
| 产物 | 素色羊毛布<br><code>wool:cloth-wool-plain</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 1 | 未声明附加限制 |
| 产物 | 素色羊毛布<br><code>wool:cloth-wool-plain</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/soapandlyecontinued/compatibility/wool/recipes/barrel/undye_wool.json`

```json
[
  {
    "code": "undyeclothwoollight",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "quantity": 1,
        "allowedVariants": [
          "gray",
          "green",
          "orange",
          "white",
          "yellow"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant",
      "stackSize": 1
    }
  },
  {
    "code": "undyeclothwoollight1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "quantity": 1,
        "allowedVariants": [
          "gray",
          "green",
          "orange",
          "white",
          "yellow"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant",
      "stackSize": 1
    }
  },
  {
    "code": "undyeclothwooldark",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "purple",
          "red",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant",
      "stackSize": 1
    }
  },
  {
    "code": "undyeclothwooldark1",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-*",
        "quantity": 1,
        "allowedVariants": [
          "black",
          "blue",
          "brown",
          "purple",
          "red",
          "darkblue",
          "darkbrown",
          "darkgreen",
          "darkred"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-mordant",
      "stackSize": 1
    }
  },
  {
    "code": "undyeclothwoolmordant",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-mordant",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-plain",
      "stackSize": 1
    }
  },
  {
    "code": "undyeclothwoolmordant1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:cloth-wool-mordant",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:cloth-wool-plain",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、棕色羊毛纤维、麝牛毛纤维、白色羊毛纤维、安哥拉羊毛纤维 · washing_fleece</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 棕色羊毛<br><code>wool:fleece-generic-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 棕色羊毛纤维<br><code>wool:fibers-generic-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 麝牛毛<br><code>wool:fleece-muskox-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 麝牛毛纤维<br><code>wool:fibers-muskox-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-redbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-redbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-redbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-redbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-lightbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-lightbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-lightbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-lightbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 白色羊毛<br><code>wool:fleece-generic-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 白色羊毛纤维<br><code>wool:fibers-generic-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 安哥拉羊毛<br><code>wool:fleece-angora-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 安哥拉羊毛纤维<br><code>wool:fibers-angora-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapandlyecontinued:soapportion-lye</code> | 0.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapandlyecontinued:soapportion-honey</code> | 0.25 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>wool:fleece-*-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wool:fibers-{type}-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：6。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/soapandlyecontinued/compatibility/wool/recipes/barrel/washing_fleece.json`

```json
[
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-plain",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-plain"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-*-plain",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-plain"
    }
  },
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-brown",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-brown"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-generic-brown"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-generic-brown"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-muskox-brown"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-muskox-brown"
    }
  },
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-redbrown",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-redbrown"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-*-redbrown",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-redbrown"
    }
  },
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-lightbrown",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-lightbrown"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-*-lightbrown",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-lightbrown"
    }
  },
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-black",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-black"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-*-black",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-black"
    }
  },
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-gray",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-gray"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-*-gray",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-gray"
    }
  },
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-white",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-white"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-generic-white"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-generic-white"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-angora-white"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-angora-white"
    }
  },
  {
    "code": "swashingfleece",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-lye",
        "litres": 0.5,
        "consumeLitres": 0.5
      },
      {
        "type": "item",
        "code": "wool:fleece-*-yellow",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-yellow"
    }
  },
  {
    "code": "swashingfleece1",
    "sealHours": 6,
    "ingredients": [
      {
        "type": "item",
        "code": "soapandlyecontinued:soapportion-honey",
        "litres": 0.25,
        "consumeLitres": 0.25
      },
      {
        "type": "item",
        "code": "wool:fleece-*-yellow",
        "name": "type"
      }
    ],
    "output": {
      "type": "item",
      "code": "wool:fibers-{type}-yellow"
    }
  }
]
```

</details>

</details>

<details><summary>碱液、变体材料（按代码匹配） · lye</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 木灰<br><code>woodash</code> | 2 | 未声明附加限制 |
| 产物 | 碱液<br><code>lyeportion</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 2 | 木灰<br><code>woodash</code> | 2 | 未声明附加限制 |
| 产物 | 碱液<br><code>lyeportion</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：0。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-raw-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 6 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:hide-salted-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:hide-soaked-{species}</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：20。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/soapandlyecontinued/recipes/barrel/lye.json`

```json
[
  {
    "code": "lye",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "woodash",
        "quantity": 2
      }
    ],
    "output": {
      "type": "item",
      "code": "lyeportion",
      "litres": 1
    }
  },
  {
    "code": "lye",
    "sealHours": 0,
    "ingredients": [
      {
        "type": "item",
        "tags": [
          "potable-water"
        ],
        "litres": 1
      },
      {
        "type": "item",
        "code": "woodash",
        "quantity": 2
      }
    ],
    "output": {
      "type": "item",
      "code": "lyeportion",
      "litres": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-raw-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-small"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-medium"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 6,
        "consumeLitres": 6
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-large"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  },
  {
    "code": "soakedhidelime",
    "sealHours": 20,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 10,
        "consumeLitres": 10
      },
      {
        "type": "item",
        "code": "game:hide-salted-*",
        "name": "species",
        "quantity": 1,
        "tags": [
          "size-huge"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:hide-soaked-{species}",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>碱液皂块、碱液皂、蜂蜜皂、蜂蜜皂块、布料、媒染布料、皮革、变体材料（按代码匹配） · soapbar</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液<br><code>lyeportion</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 熬制的脂肪块<br><code>game:fat-rendered</code> | 1 | 未声明附加限制 |
| 产物 | 碱液皂块<br><code>soapbar-lye</code> | 2 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 碱液皂块<br><code>soapbar-lye</code> | 1 | 未声明附加限制 |
| 产物 | 碱液皂<br><code>soapportion-lye</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：1。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapportion-lye</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 蜜脾<br><code>game:honeycomb</code> | 2 | 未声明附加限制 |
| 产物 | 蜂蜜皂<br><code>soapportion-honey</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 蜂蜜皂块<br><code>soapbar-honey</code> | 1 | 未声明附加限制 |
| 产物 | 蜂蜜皂<br><code>soapportion-honey</code> | 1 升 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜<br><code>game:honeyportion</code> | 0.4 升 | 未声明附加限制 |
| 投入 2 | 碱液皂块<br><code>soapbar-lye</code> | 1 | 未声明附加限制 |
| 产物 | 蜂蜜皂块<br><code>soapbar-honey</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapportion-lye</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |
| 产物 | 布料<br><code>game:cloth-plain</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapportion-honey</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |
| 产物 | 布料<br><code>game:cloth-plain</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapportion-lye</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['orange', 'black', 'red', 'blue', 'green', 'yellow', 'white', 'gray', 'purple', 'pink'] |
| 产物 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapportion-honey</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:cloth-*</code> | 未声明；按配方类型判定 | 允许变体：['orange', 'black', 'red', 'blue', 'green', 'yellow', 'white', 'gray', 'purple', 'pink'] |
| 产物 | 媒染布料<br><code>game:cloth-mordant</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapportion-lye</code> | 4 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:leather-normal-*</code> | 未声明；按配方类型判定 | 允许变体：['orange', 'black', 'red', 'blue', 'green', 'yellow', 'white', 'gray', 'purple', 'pink'] |
| 产物 | 皮革<br><code>game:leather-normal-plain</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：24。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapportion-honey</code> | 2 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:leather-normal-*</code> | 未声明；按配方类型判定 | 允许变体：['orange', 'black', 'red', 'blue', 'green', 'yellow', 'white', 'gray', 'purple', 'pink'] |
| 产物 | 皮革<br><code>game:leather-normal-plain</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 碱液皂<br><code>soapportion-lye</code> | 5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:dirtyclaypot-*-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:claypot-{color}-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜜皂<br><code>soapportion-honey</code> | 2.5 升 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:dirtyclaypot-*-empty</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:claypot-{color}-fired</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：12。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/soapandlyecontinued/recipes/barrel/soapbar.json`

```json
[
  {
    "code": "soapbar",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "lyeportion",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:fat-rendered",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "soapbar-lye",
      "quantity": 2
    }
  },
  {
    "code": "soapportion",
    "sealHours": 1,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "soapbar-lye",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "soapportion-lye",
      "litres": 1
    }
  },
  {
    "code": "honeysoapportion",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-lye",
        "litres": 1
      },
      {
        "type": "item",
        "code": "game:honeycomb",
        "quantity": 2
      }
    ],
    "output": {
      "type": "item",
      "code": "soapportion-honey",
      "litres": 1
    }
  },
  {
    "code": "honeysoapportion2",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 1
      },
      {
        "type": "item",
        "code": "soapbar-honey",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "soapportion-honey",
      "litres": 1
    }
  },
  {
    "code": "honeysoapbar",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:honeyportion",
        "litres": 0.4,
        "consumeLitres": 0.4
      },
      {
        "type": "item",
        "code": "soapbar-lye",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "soapbar-honey",
      "quantity": 1
    }
  },
  {
    "code": "removemordant",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-lye",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:cloth-mordant",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-plain",
      "quantity": 1
    }
  },
  {
    "code": "removemordant2",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-honey",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:cloth-mordant",
        "quantity": 1
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-plain",
      "quantity": 1
    }
  },
  {
    "code": "removedyecloth",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-lye",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:cloth-*",
        "name": "color",
        "allowedVariants": [
          "orange",
          "black",
          "red",
          "blue",
          "green",
          "yellow",
          "white",
          "gray",
          "purple",
          "pink"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-mordant",
      "quantity": 1
    }
  },
  {
    "code": "removedyecloth2",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-honey",
        "litres": 1,
        "consumeLitres": 1
      },
      {
        "type": "item",
        "code": "game:cloth-*",
        "name": "color",
        "allowedVariants": [
          "orange",
          "black",
          "red",
          "blue",
          "green",
          "yellow",
          "white",
          "gray",
          "purple",
          "pink"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cloth-mordant",
      "quantity": 1
    }
  },
  {
    "code": "removedyeleather",
    "sealHours": 24,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-lye",
        "litres": 4,
        "consumeLitres": 4
      },
      {
        "type": "item",
        "code": "game:leather-normal-*",
        "name": "color",
        "allowedVariants": [
          "orange",
          "black",
          "red",
          "blue",
          "green",
          "yellow",
          "white",
          "gray",
          "purple",
          "pink"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:leather-normal-plain",
      "quantity": 1
    }
  },
  {
    "code": "removedyeleather2",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-honey",
        "litres": 2,
        "consumeLitres": 2
      },
      {
        "type": "item",
        "code": "game:leather-normal-*",
        "name": "color",
        "allowedVariants": [
          "orange",
          "black",
          "red",
          "blue",
          "green",
          "yellow",
          "white",
          "gray",
          "purple",
          "pink"
        ]
      }
    ],
    "output": {
      "type": "item",
      "code": "game:leather-normal-plain",
      "quantity": 1
    }
  },
  {
    "code": "cleanpot",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-lye",
        "litres": 5,
        "consumeLitres": 5
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-*-empty",
        "name": "color"
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-{color}-fired",
      "quantity": 1
    }
  },
  {
    "code": "cleanpot2",
    "sealHours": 12,
    "ingredients": [
      {
        "type": "item",
        "code": "soapportion-honey",
        "litres": 2.5,
        "consumeLitres": 2.5
      },
      {
        "type": "block",
        "code": "game:dirtyclaypot-*-empty",
        "name": "color"
      }
    ],
    "output": {
      "type": "block",
      "code": "game:claypot-{color}-fired",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>特殊配方 · potash</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>water</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |
| 投入 2 | 木灰<br><code>woodash</code> | 未声明；按配方类型判定 | 最少数量：2；最多数量：2 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/soapandlyecontinued/recipes/cooking/potash.json`

```json
{
  "code": "potashlye",
  "perishableProps": {
    "type": "None",
    "freshHours": {
      "avg": 36
    },
    "transitionHours": {
      "avg": 36
    },
    "transitionRatio": 1,
    "transitionedStack": {
      "type": "item",
      "code": "woodash"
    }
  },
  "shape": {
    "base": "block/food/meal/liquid"
  },
  "ingredients": [
    {
      "code": "water",
      "validStacks": [
        {
          "type": "item",
          "code": "game:waterportion"
        }
      ],
      "minQuantity": 2,
      "maxQuantity": 2,
      "portionSizeLitres": 1
    },
    {
      "code": "woodash",
      "validStacks": [
        {
          "type": "item",
          "code": "woodash"
        }
      ],
      "minQuantity": 2,
      "maxQuantity": 2
    }
  ],
  "cooksInto": {
    "type": "item",
    "code": "game:potash",
    "quantity": 2
  }
}
```

</details>

</details>
<!-- generated:end -->
