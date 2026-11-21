<!-- generated:start -->
# 采石工艺：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：采石场：石材切割指南

来源：`assets/stonequarry/config/handbook/masonguide.json`。

石材切割指南

石头永远不会太多

首先，制造一个 [handbook://stonequarry-quarryguide] 石板。每移除一块岩石，你都会得到一块石板，你可以用它来获得不同类型

的岩石。

有四种工具可以实现此目的：

[handbook://item-stonequarry:chisel-finishing-copper] 精加工凿子- 在石板上使用时，会产生磨制岩石。

[handbook://item-stonequarry:chisel-wedge-copper] 楔形凿子- 在石板上使用时会产生石砖。

[handbook://item-stonequarry:chisel-roughcut-copper] 粗加工凿子- 在石板上使用时会产生岩石。

[handbook://item-stonequarry:rubblehammer-copper] 碎石锤- 在石板上使用时会产生石块。

如果你想从石块中获取沙子或砾石，或者你只需要大量存储，那么请看看 [handbook://stonequarry-rubblestorageguide] 石材储存

## 手册 2：采石场：石材切割指南

来源：`assets/stonequarry/config/handbook/quarryguide.json`。

劈石指南

想开一座采石场吗？

准备一把好用的 [handbook://item-hammer-copper] 锤和一些 [handbook://block-stonequarry:plugandfeather-copper-0-down-north] 楔钉，将楔钉布置在待分离岩块侧面那排石头的顶部或底部。用锤敲击几次，就能取得一块石料。敲击第一个楔钉后，可潜行并点击它，切换工作区域高亮。

楔钉材质决定一次可取得多少石料。默认铜楔钉最多处理 3×3×3（27 格），钢楔钉最多处理 7×7×7（343 格）。限制按体积计算，因此可以切出 1×7×14 这样的细长石料，但不能切出 1×1×343。

得到的石料大小取决于切下的石头数量。各种尺寸都可使用，但较大的石料放置时占用空间更多。

阅读 [handbook://stonequarry-masonguide] 石料加工指南后，就动手采些石料吧。

## 手册 3：采石场：石材存储指南

来源：`assets/stonequarry/config/handbook/rubblestorageguide.json`。

石材储存指南

[handbook://block-stonequarry:rubblestorage-north] 石材储藏室可用于储存石块、砂砾和沙子。

另外，如果你的 [handbook://item-stonequarry:rubblehammer-copper] 碎石锤击中了存储的材料，这些内容将会转化。原则上：两块石块对一个砂砾，

一个砂砾对一个沙子。

在世界互动中

- 添加物品：右键单击手中的物品。你还可以空手右键单击来添加所有合

适的库存物品。

- 获取物品：右键点击前面的按钮，根据需要取材。

- 通过按住冲刺键，你可以一次添加/删除一组材料。

- 你可以通过按住潜行并右键单击相应按钮来锁定材料。锁定的材料不会

用于锤炼，并且也会被优先考虑。

- 你还可以制造 [handbook://block-muddygravel] 泥砾层通过右键单击水容器（桶）从普通砂砾中提取。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · plugandfeather</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>game:toolmold-{color}-raw-stonequarry_plugandfeather</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/clayforming/mold/plugandfeather.json`

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
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############",
      "##############"
    ],
    [
      "##############",
      "##############",
      "##__________##",
      "##__________##",
      "##############",
      "##############",
      "##__________##",
      "##__________##",
      "##############",
      "##############",
      "##__________##",
      "##__________##",
      "##############",
      "##############"
    ]
  ],
  "name": "PlugAndFeather Mold",
  "output": {
    "type": "block",
    "code": "game:toolmold-{color}-raw-stonequarry_plugandfeather"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · rubblestorage</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>rubblestorage-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WPW
WWW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/grid/rubblestorage.json`

```json
{
  "ingredientPattern": "WPW,WWW",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:metalplate-copper"
    },
    "W": {
      "type": "item",
      "code": "game:plank-*"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "rubblestorage-north",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · finishingchisel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>finishingchiselhead-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>chisel-finishing-{material}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
T
S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/grid/tool/finishingchisel.json`

```json
{
  "ingredientPattern": "T,S",
  "ingredients": {
    "T": {
      "type": "item",
      "code": "finishingchiselhead-*",
      "name": "material"
    },
    "S": {
      "type": "item",
      "code": "game:stick"
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "chisel-finishing-{material}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · rubblehammer</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>rubblehammerhead-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>rubblehammer-{material}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
T
S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/grid/tool/rubblehammer.json`

```json
{
  "ingredientPattern": "T,S",
  "ingredients": {
    "T": {
      "type": "item",
      "code": "rubblehammerhead-*",
      "name": "material"
    },
    "S": {
      "type": "item",
      "code": "game:stick"
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "rubblehammer-{material}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · wedgechisel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 T | 变体材料（按代码匹配）<br><code>wedgechiselhead-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>chisel-wedge-{material}</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
T
S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/grid/tool/wedgechisel.json`

```json
{
  "ingredientPattern": "T,S",
  "ingredients": {
    "T": {
      "type": "item",
      "code": "wedgechiselhead-*",
      "name": "material"
    },
    "S": {
      "type": "item",
      "code": "game:stick"
    }
  },
  "width": 1,
  "height": 2,
  "output": {
    "type": "item",
    "code": "chisel-wedge-{material}",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · plugandfeather</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>plugandfeather-{metal}-0-down-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/smithing/plugandfeather.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "copper",
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "iron",
      "meteoriciron",
      "steel"
    ]
  },
  "pattern": [
    [
      "_#####",
      "######"
    ],
    [
      "_#####",
      "######"
    ]
  ],
  "name": "Splitter plug",
  "code": "plugandfeather-{metal}",
  "output": {
    "type": "block",
    "code": "plugandfeather-{metal}-0-down-north"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · finishingchiselhead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>finishingchiselhead-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/smithing/tool/finishingchiselhead.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
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
      "_###__",
      "###___",
      "_###__"
    ]
  ],
  "code": "finishingchiselhead-{metal}",
  "output": {
    "type": "item",
    "code": "finishingchiselhead-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · roughcutchisel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>chisel-roughcut-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/smithing/tool/roughcutchisel.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
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
      "######"
    ]
  ],
  "name": "Rough Cut Chisel",
  "code": "chisel-roughcut-{metal}",
  "output": {
    "type": "item",
    "code": "chisel-roughcut-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · rubblehammerhead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>rubblehammerhead-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/smithing/tool/rubblehammerhead.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
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
      "######",
      "__####",
      "__####",
      "######"
    ],
    [
      "######",
      "__####",
      "__####",
      "######"
    ]
  ],
  "name": "Rubble Hammer",
  "code": "rubblehammerhead-{metal}",
  "output": {
    "type": "item",
    "code": "rubblehammerhead-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · wedgechiselhead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>wedgechiselhead-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/stonequarry/recipes/smithing/tool/wedgechiselhead.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
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
      "__##__",
      "##____",
      "__##__"
    ],
    [
      "__##__",
      "##____",
      "__##__"
    ]
  ],
  "name": "Wedge Chisel",
  "code": "wedgechiselhead-{metal}",
  "output": {
    "type": "item",
    "code": "wedgechiselhead-{metal}"
  }
}
```

</details>

</details>
<!-- generated:end -->
