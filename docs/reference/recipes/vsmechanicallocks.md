<!-- generated:start -->
# 机械锁：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · keymold-bulk</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:keymold-raw{type}-bulk-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/clayforming/keymold-bulk.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:clay-*",
    "name": "type",
    "allowedVariants": [
      "blue",
      "red"
    ]
  },
  "pattern": [
    [
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################",
      "################"
    ],
    [
      "################",
      "################",
      "################",
      "################",
      "#______##______#",
      "#_#____##_#____#",
      "#___#####___####",
      "################",
      "################",
      "#______##______#",
      "#_#____##_#____#",
      "#___#####___####",
      "################",
      "################",
      "################",
      "################"
    ]
  ],
  "name": "Key Mold (x4)",
  "output": {
    "type": "block",
    "code": "vsmechanicallocks:keymold-raw{type}-bulk-north"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · keymold-normal</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:keymold-raw{type}-normal-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/clayforming/keymold-normal.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:clay-*",
    "name": "type",
    "allowedVariants": [
      "blue",
      "red"
    ]
  },
  "pattern": [
    [
      "###############",
      "###############",
      "###############",
      "###############",
      "###############",
      "###############",
      "###############",
      "###############",
      "###############",
      "###############"
    ],
    [
      "###############",
      "###############",
      "###############",
      "##___####____##",
      "##_#_####____##",
      "##_#_________##",
      "##___##########",
      "###############",
      "###############",
      "###############"
    ]
  ],
  "name": "Key Mold",
  "output": {
    "type": "block",
    "code": "vsmechanicallocks:keymold-raw{type}-normal-north"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · key-jeweled</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:ore-*</code> | 未声明；按配方类型判定 | 允许变体：['cinnabar', 'lapislazuli', 'olivine', 'quartz'] |
| 投入 P | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'brass', 'tinbronze', 'bismuthbronze', 'blackbronze', 'silver', 'gold', 'iron', 'lead', 'tin', 'zinc', 'bismuth', 'chromium', 'electrum', 'platinum', 'titanium', 'molybdochalkos', 'meteoriciron', 'steel'] |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-jeweled-{metal}-{gem}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:gem-*-rough</code> | 未声明；按配方类型判定 | 允许变体：['diamond', 'emerald'] |
| 投入 P | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'brass', 'tinbronze', 'bismuthbronze', 'blackbronze', 'silver', 'gold', 'iron', 'lead', 'tin', 'zinc', 'bismuth', 'chromium', 'electrum', 'platinum', 'titanium', 'molybdochalkos', 'meteoriciron', 'steel'] |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-jeweled-{metal}-{gem}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:nugget-*</code> | 4 | 允许变体：['malachite'] |
| 投入 P | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'brass', 'tinbronze', 'bismuthbronze', 'blackbronze', 'silver', 'gold', 'iron', 'lead', 'tin', 'zinc', 'bismuth', 'chromium', 'electrum', 'platinum', 'titanium', 'molybdochalkos', 'meteoriciron', 'steel'] |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-jeweled-{metal}-{gem}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 G | 粉水晶<br><code>game:rosequartz</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'brass', 'tinbronze', 'bismuthbronze', 'blackbronze', 'silver', 'gold', 'iron', 'lead', 'tin', 'zinc', 'bismuth', 'chromium', 'electrum', 'platinum', 'titanium', 'molybdochalkos', 'meteoriciron', 'steel'] |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-jeweled-{metal}-rosequartz</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：5 |
| 投入 G | 紫水晶<br><code>game:amethyst</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'brass', 'tinbronze', 'bismuthbronze', 'blackbronze', 'silver', 'gold', 'iron', 'lead', 'tin', 'zinc', 'bismuth', 'chromium', 'electrum', 'platinum', 'titanium', 'molybdochalkos', 'meteoriciron', 'steel'] |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-jeweled-{metal}-amethyst</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HC
GP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/grid/key-jeweled.json`

```json
[
  {
    "ingredientPattern": "HC,GP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "G": {
        "type": "item",
        "code": "game:ore-*",
        "name": "gem",
        "allowedVariants": [
          "cinnabar",
          "lapislazuli",
          "olivine",
          "quartz"
        ]
      },
      "P": {
        "type": "item",
        "code": "vsmechanicallocks:key-*",
        "name": "metal",
        "allowedVariants": [
          "copper",
          "brass",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "silver",
          "gold",
          "iron",
          "lead",
          "tin",
          "zinc",
          "bismuth",
          "chromium",
          "electrum",
          "platinum",
          "titanium",
          "molybdochalkos",
          "meteoriciron",
          "steel"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "vsmechanicallocks:key-jeweled-{metal}-{gem}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "G": {
        "type": "item",
        "code": "game:gem-*-rough",
        "name": "gem",
        "allowedVariants": [
          "diamond",
          "emerald"
        ]
      },
      "P": {
        "type": "item",
        "code": "vsmechanicallocks:key-*",
        "name": "metal",
        "allowedVariants": [
          "copper",
          "brass",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "silver",
          "gold",
          "iron",
          "lead",
          "tin",
          "zinc",
          "bismuth",
          "chromium",
          "electrum",
          "platinum",
          "titanium",
          "molybdochalkos",
          "meteoriciron",
          "steel"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "vsmechanicallocks:key-jeweled-{metal}-{gem}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "G": {
        "type": "item",
        "code": "game:nugget-*",
        "name": "gem",
        "allowedVariants": [
          "malachite"
        ],
        "quantity": 4
      },
      "P": {
        "type": "item",
        "code": "vsmechanicallocks:key-*",
        "name": "metal",
        "allowedVariants": [
          "copper",
          "brass",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "silver",
          "gold",
          "iron",
          "lead",
          "tin",
          "zinc",
          "bismuth",
          "chromium",
          "electrum",
          "platinum",
          "titanium",
          "molybdochalkos",
          "meteoriciron",
          "steel"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "vsmechanicallocks:key-jeweled-{metal}-{gem}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "G": {
        "type": "item",
        "code": "game:rosequartz"
      },
      "P": {
        "type": "item",
        "code": "vsmechanicallocks:key-*",
        "name": "metal",
        "allowedVariants": [
          "copper",
          "brass",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "silver",
          "gold",
          "iron",
          "lead",
          "tin",
          "zinc",
          "bismuth",
          "chromium",
          "electrum",
          "platinum",
          "titanium",
          "molybdochalkos",
          "meteoriciron",
          "steel"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "vsmechanicallocks:key-jeweled-{metal}-rosequartz",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "HC,GP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 5
      },
      "G": {
        "type": "item",
        "code": "game:amethyst"
      },
      "P": {
        "type": "item",
        "code": "vsmechanicallocks:key-*",
        "name": "metal",
        "allowedVariants": [
          "copper",
          "brass",
          "tinbronze",
          "bismuthbronze",
          "blackbronze",
          "silver",
          "gold",
          "iron",
          "lead",
          "tin",
          "zinc",
          "bismuth",
          "chromium",
          "electrum",
          "platinum",
          "titanium",
          "molybdochalkos",
          "meteoriciron",
          "steel"
        ]
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "vsmechanicallocks:key-jeweled-{metal}-amethyst",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>绳钥匙环 · keyring-rope</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 绳钥匙环<br><code>vsmechanicallocks:keyring-rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_R_
R_R
_R_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/grid/keyring-rope.json`

```json
{
  "ingredientPattern": "_R_,R_R,_R_",
  "width": 3,
  "height": 3,
  "ingredients": {
    "R": {
      "type": "item",
      "code": "game:rope"
    }
  },
  "output": {
    "type": "item",
    "code": "vsmechanicallocks:keyring-rope"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · key-bulk</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-{metal}</code> | 4 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/smithing/key-bulk.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "iron",
      "meteoriciron",
      "steel"
    ]
  },
  "name": "Key blank (x4)",
  "pattern": [
    [
      "____###_____###_",
      "#####_#_#####_#_",
      "#######_#######_",
      "________________",
      "____###_____###_",
      "#####_#_#####_#_",
      "#######_#######_"
    ],
    [
      "____###_____###_",
      "#####_#_#####_#_",
      "#######_#######_",
      "________________",
      "____###_____###_",
      "#####_#_#####_#_",
      "#######_#######_"
    ]
  ],
  "output": {
    "type": "item",
    "code": "vsmechanicallocks:key-{metal}",
    "quantity": 4
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · key</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:key-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/smithing/key.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "copper",
      "brass",
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "silver",
      "gold",
      "iron",
      "lead",
      "tin",
      "zinc",
      "bismuth",
      "chromium",
      "electrum",
      "platinum",
      "titanium",
      "molybdochalkos",
      "meteoriciron",
      "steel"
    ]
  },
  "name": "Key blank",
  "pattern": [
    [
      "_________###____",
      "___#######_#____",
      "___#########____"
    ],
    [
      "_________###____",
      "___#######_#____",
      "___#########____"
    ]
  ],
  "output": {
    "type": "item",
    "code": "vsmechanicallocks:key-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · keyfile</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:keyfile-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/smithing/keyfile.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "iron",
      "meteoriciron",
      "steel"
    ]
  },
  "name": "Key File",
  "pattern": [
    [
      "___#######______",
      "___###########__",
      "___#######______"
    ]
  ],
  "output": {
    "type": "item",
    "code": "vsmechanicallocks:keyfile-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · keyring</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vsmechanicallocks:keyring-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vsmechanicallocks/recipes/smithing/keyring.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "iron",
      "meteoriciron",
      "steel"
    ]
  },
  "name": "Keyring",
  "pattern": [
    [
      "_#####_",
      "#_____#",
      "#_____#",
      "#_____#",
      "#_____#",
      "#_____#",
      "_#####_",
      "__#_#__",
      "___#___"
    ]
  ],
  "output": {
    "type": "item",
    "code": "vsmechanicallocks:keyring-{metal}"
  }
}
```

</details>

</details>
<!-- generated:end -->
