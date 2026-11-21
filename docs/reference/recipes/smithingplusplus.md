<!-- generated:start -->
# 锻造改进：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：锻造增强——入门指南

来源：`assets/smithingplus/config/handbook/smithingplusguide.json`。

锻造增强——锻造功能扩展

锻造增强通过多项调整改善原版锻造体验。各功能按类别组织，可在配置文件中分别启用、关闭并细调行为。

碎块锻造

允许使用 [handbook://item-metalbit-copper] 金属碎块和天然金属粒锻造，包括 [handbook://item-nugget-nativecopper] 自然铜、 [handbook://item-nugget-nativesilver] 自然银和 [handbook://item-nugget-nativegold] 自然金。安装 [https://mods.vintagestory.at/show/mod/8054] 地质扩展后，还支持 [handbook://item-nugget-nativeplatinum] 自然铂。

手持烧热的金属碎块，按住shift点击 [handbooksearch://anvil] 铁砧即可锻造，操作与使用 [handbook://item-ingot-copper] 金属锭相同。与原版金属锭一样，碎块须加热至可加工温度以上（通常为熔点的一半）。可将碎块放入 [handbook://block-firepit-lit] 篝火上的 [handbook://block-crucible-burned] 坩埚中加热，并在开始熔化前取出。建议使用 [handbook://item-firewood] 木柴或 [handbook://block-peatbrick] 泥炭等燃烧温度较低的燃料。

可分别配置是否允许用碎块补充已有加工件，以及开始新的锻造项目。

工具回收

工具回收与原版机制差别较大：你可以回收并修复损坏的金属工具。工具损坏时，只要它或其合成材料有对应锻造配方，且符合配置的匹配规则，就会掉落损坏的工具头。该工具头可作为加工件，在 [handbooksearch://anvil] 铁砧上锻造修复。此功能与碎块锻造配合良好。

配置项包括全局调整可修复工具的耐久度，以及多次修复带来的耐久度惩罚。还可设置修复时忽略哪些属性，例如 [https://mods.vintagestory.at/show/mod/247] XSkills 的锻造品质或 [https://mods.vintagestory.at/krpgenchantment] KRPG Enchantment 的附魔，默认会将它们保留到修复后的工具上。此外，可将某些工具头设为不可修复；它们仍可在合成栏中用 [handbooksearch://chisel] 凿子拆解为碎块。

碎块回收

在 [handbooksearch://anvil] 铁砧上分割材料时可回收金属碎块。由于体素与碎块的换算比例不是整数，回收一个碎块所需分割次数会变化，通常为两次，偶尔三次。

还可从装有凝固金属的 [handbook://block-crucible-burned] 坩埚中回收碎块：放下坩埚，手持 [handbooksearch://chisel] 凿子对其点击rightmouse。

锤子调整

新增一种锤子工具模式，可点击rightmouse将加工件上下翻转。可配置为要求副手持有 [handbooksearch://tongs] 钳子。

注意：启用此要求后，点击rightmouse旋转加工件也需要钳子。

铸造调整

目前仅为模铸工具加入可配置的耐久度惩罚。工具经过锻造修复后，视为正式锻制，该惩罚随之移除。

客户端调整

这些是客户端的便利性改进，包括：

• 在手册中补充锻造和金属模铸信息

• 选择锻造配方时显示所需材料数量

• 查看 [handbooksearch://anvil] 铁砧时显示当前及总计体素数量

• 在 [handbook://block-forge] 锻炉、 [handbooksearch://anvil] 铁砧和物品提示中突出显示可加工温度；物品达到可加工温度时以绿色标示。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · 1hook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>alchemy:herbrackhook-{metal}</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/compatibility/alchemy/recipes/smithing/smithingplus/1hook.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:metalbit-*",
    "recipeAttributes": {
      "nuggetRecipe": true
    },
    "name": "metal",
    "allowedVariants": [
      "bismuth",
      "bismuthbronze",
      "blackbronze",
      "brass",
      "chromium",
      "copper",
      "cupronickel",
      "electrum",
      "gold",
      "iron",
      "lead",
      "meteoriciron",
      "molybdochalkos",
      "nickel",
      "platinum",
      "silver",
      "stainlesssteel",
      "steel",
      "tin",
      "tinbronze",
      "titanium",
      "uranium",
      "zinc"
    ]
  },
  "pattern": [
    [
      "###__###_",
      "#_##_#_##"
    ]
  ],
  "name": "2 Herb rack hooks",
  "output": {
    "type": "item",
    "code": "alchemy:herbrackhook-{metal}",
    "stacksize": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · 1hook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>butchering:hook-{metal}</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/compatibility/butchering/recipes/smithing/smithingplus/1hook.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:metalbit-*",
      "recipeAttributes": {
        "nuggetRecipe": true
      },
      "name": "metal",
      "allowedVariants": [
        "copper",
        "tinbronze",
        "bismuthbronze",
        "blackbronze",
        "iron"
      ]
    },
    "name": "1 Butcher hook",
    "pattern": [
      [
        "_________",
        "___##____",
        "___#_____",
        "___#_#___",
        "___###___",
        "_________"
      ]
    ],
    "output": {
      "type": "item",
      "code": "butchering:hook-{metal}",
      "stacksize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · chiselworkitem</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：10 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:workitem-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>game:metalbit-{metal}</code> | 20 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/recipes/grid/chiselworkitem.json`

```json
[
  {
    "code": "chiselworkitem",
    "ingredientPattern": "C,W",
    "shapeless": true,
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true,
        "toolDurabilityCost": 10,
        "recipeAttributes": {
          "recyclingRecipe": true
        }
      },
      "W": {
        "type": "item",
        "code": "game:workitem-*",
        "name": "metal"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:metalbit-{metal}",
      "quantity": 20
    }
  }
]
```

</details>

</details>

<details><summary>绝境者刺剑 · forlornestoc</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | Estoc 刀刃<br><code>forlornblade-meteoriciron</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 绝境者刺剑<br><code>game:blade-forlorn-iron</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：False；网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
F
S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/recipes/grid/forlornestoc.json`

```json
[
  {
    "code": "forlornassembly",
    "ingredientPattern": "B,F,S",
    "enabled": false,
    "shapeless": false,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "forlornblade-meteoriciron"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "F": {
        "type": "item",
        "code": "game:flaxtwine"
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "game:blade-forlorn-iron",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · 1arrowhead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>game:arrowhead-{metal}</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/recipes/smithing/bits/1arrowhead.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:ingot-*",
      "recipeAttributes": {
        "nuggetRecipe": true
      },
      "name": "metal",
      "allowedVariants": [
        "copper",
        "tinbronze",
        "bismuthbronze",
        "blackbronze",
        "silver",
        "gold",
        "iron",
        "meteoriciron",
        "steel"
      ]
    },
    "pattern": [
      [
        "____",
        "_##_",
        "_#__",
        "____"
      ]
    ],
    "name": "1 Arrowhead",
    "code": "1arrowhead-{metal}",
    "output": {
      "type": "item",
      "code": "game:arrowhead-{metal}",
      "stacksize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · 3arrowhead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>game:arrowhead-{metal}</code> | 3 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/recipes/smithing/bits/3arrowhead.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:ingot-*",
      "recipeAttributes": {
        "nuggetRecipe": true
      },
      "name": "metal",
      "allowedVariants": [
        "copper",
        "tinbronze",
        "bismuthbronze",
        "blackbronze",
        "silver",
        "gold",
        "iron",
        "meteoriciron",
        "steel"
      ]
    },
    "pattern": [
      [
        "________",
        "##_##_##",
        "#__#__#_",
        "________"
      ]
    ],
    "name": "3 Arrowheads",
    "code": "3arrowhead-{metal}",
    "output": {
      "type": "item",
      "code": "game:arrowhead-{metal}",
      "stacksize": 3
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · nails</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-{metal}</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/recipes/smithing/bits/nails.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:ingot-*",
      "recipeAttributes": {
        "nuggetRecipe": true
      },
      "name": "metal",
      "allowedVariants": [
        "copper",
        "tinbronze",
        "bismuthbronze",
        "blackbronze",
        "silver",
        "gold",
        "iron",
        "meteoriciron",
        "steel"
      ]
    },
    "pattern": [
      [
        "___##___",
        "___##___",
        "___##___",
        "___##___",
        "___##___"
      ]
    ],
    "name": "1 set of nails",
    "code": "1nails-{metal}",
    "output": {
      "type": "item",
      "code": "game:metalnailsandstrips-{metal}",
      "stacksize": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · forlornblade</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>forlornblade-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/recipes/smithing/forlornblade.json`

```json
{
  "code": "forlornblade-{metal}",
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "recipeAttributes": {
      "repairOnly": true
    },
    "allowedVariants": [
      "meteoriciron"
    ]
  },
  "pattern": [
    [
      "________########",
      "################",
      "________########"
    ]
  ],
  "output": {
    "type": "item",
    "code": "forlornblade-{metal}"
  }
}
```

</details>

</details>

<details><summary>铜锭 · ingot</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 铜锭<br><code>game:ingot-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/smithingplus/recipes/smithing/ingot.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:ingot-copper",
      "name": "metal",
      "recipeAttributes": {
        "workableRecipe": true
      }
    },
    "pattern": [
      [
        "#######",
        "#######",
        "#######"
      ],
      [
        "#######",
        "#######",
        "#######"
      ]
    ],
    "name": "Ingot",
    "code": "ingot-copper",
    "output": {
      "type": "item",
      "code": "game:ingot-copper"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
