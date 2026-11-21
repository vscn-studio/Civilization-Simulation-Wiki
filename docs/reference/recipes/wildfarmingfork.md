<!-- generated:start -->
# 野生种植：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：复兴荒野：植物指南

来源：`assets/wildfarmingfork/config/handbook/botanyguide.json`。

植物学家手册

种子提取与植物培育

将谷物与木制淘盘放入合成栏中,可以提取谷物种子。蔬菜或豆类的种子可以通过与剪刀合成来获取。将芦苇或藤蔓尖与一桶水进行合成来获得两份芦苇根或藤蔓尖。将藤蔓尖种植于高处,藤蔓尖会向下生长长出可收获的藤蔓。将海草尖种植在深水中，会长出可供收获的海草。花卉、水果、仙人掌和蕨类的种子可以通过将对应植物与小刀合成来获得。这类种子不需要耕地和水分,但其对温度及其敏感且会在温室中获得温度增益效果。可以对松树和金合欢树使用小刀划开树皮使其流出树脂。

蘑菇种植

要开始种植蘑菇你需要制作一个 [handbook://block-wildfarmingfork:mushroomsubstrate] 蘑菇培养基并收集一些蘑菇。

手持你想种植的蘑菇右键点击蘑菇培养基来种下蘑菇。地面上生长的蘑菇会在蘑菇培养基周围同一高度的7格范围内的泥土上随机生长。树木上生长的蘑菇会在蘑菇培养基正上方的五块该种类蘑菇喜好的原木的侧边上生长。

树木种植

所有树苗/树木都有独特的生长需求。这些树木都有特定的温度范围需求。树木的树干会显示是否过热或过冷。满足树木需求后且空间没有被阻挡时树木将开始再生其树叶。树木的健康状态由树叶数量和树干健康状态共同决定,各占比50%。破坏或遮挡树叶将会危害其树叶健康。白蚁之类的寄生虫将会危害树木的树干健康。当树木的健康状态大于85%时会生长至下一阶段。树叶及树枝可以再生,但破坏原木部分会杀死树木且树干会变回普通的原木。完全成熟的树木在健康状态大于75%时会吸引不同的野生植物且会在周围种植更多的树苗。注意!完全成熟的树木同样会吸引有害的生物如白蚁。(竹子和高大蕨类不算树木)

树木类型:

桦树

类型: 落叶乔木

最低温度: -7,

最高温度: 39

橡树

类型: 落叶乔木

最低温度: -5,

最高温度: 40

枫树

类型: 落叶乔木

最低温度: -7,

最高温度: 40

松树

类型: 针叶林木

最低温度: -18,

最高温度: 30

金合欢树

类型:非标准类型

最低温度: 21,

最高温度: 50,

木棉树

类型: 热带树木

最低温度: 20,

最高温度: 50,

落叶松

类型: 针叶林木

最低温度: -24,

最高温度: 15,

红杉

类型: 针叶林木

最低温度: 7,

最高温度: 35

落羽杉

类型: 针叶林木

最低温度: 8,

最高温度: 41

黑檀

类型: 针叶林木

最低温度: 21,

最高温度: 50

紫心木

类型: 热带树木

最低温度: 20,

最高温度: 50

胡桃树

类型: 落叶乔木

最低温度: -1,

最高温度: 39

绿竹

类型: 非标准类型

最低温度: 27,

最高温度: 50,

注意: 会生长出大量竹笋,请预留足够的空间。

棕竹

类型: 非标准类型

最低温度: 22,

最高温度: 50,

注意: 会生长出大量竹笋,请预留足够的空间。

蕨树

类型: 非标准类型

最低温度: 19,

最高温度: 50,

注意: 会生长出大量根茎,请预留足够的空间。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>香蒲根 · cattailroot</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 香蒲<br><code>game:cattailtops</code> | 32 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 50 升 | 未声明附加限制 |
| 产物 | 香蒲根<br><code>game:cattailroot</code> | 64 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/barrel/cattailroot.json`

```json
[
  {
    "enabled": true,
    "code": "cattailroot-propagation",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 32
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 50,
        "consumeLitres": 50
      }
    ],
    "output": {
      "type": "item",
      "code": "game:cattailroot",
      "stackSize": 64
    }
  }
]
```

</details>

</details>

<details><summary>纸莎草根 · papyrusroot</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 纸莎草<br><code>game:papyrustops</code> | 32 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 50 升 | 未声明附加限制 |
| 产物 | 纸莎草根<br><code>game:papyrusroot</code> | 64 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/barrel/papyrusroot.json`

```json
[
  {
    "enabled": true,
    "code": "papyrusroot-propagation",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 32
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 50,
        "consumeLitres": 50
      }
    ],
    "output": {
      "type": "item",
      "code": "game:papyrusroot",
      "stackSize": 64
    }
  }
]
```

</details>

</details>

<details><summary>水三棱草块茎 · tuleroot</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水三棱草块茎<br><code>game:tuleroot</code> | 32 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 50 升 | 未声明附加限制 |
| 产物 | 水三棱草块茎<br><code>game:tuleroot</code> | 64 | 未声明附加限制 |

**加工条件：** 配方开关：True；密封时间（游戏小时）：72。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/barrel/tuleroot.json`

```json
[
  {
    "enabled": true,
    "code": "tuleroot-propagation",
    "sealHours": 72,
    "ingredients": [
      {
        "type": "item",
        "code": "game:tuleroot",
        "quantity": 32
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 50,
        "consumeLitres": 50
      }
    ],
    "output": {
      "type": "item",
      "code": "game:tuleroot",
      "stackSize": 64
    }
  }
]
```

</details>

</details>

<details><summary>巨人柱种子、球形仙人掌种子、银火炬仙人掌种子 · cactiseeds</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 巨人柱果<br><code>game:fruit-saguaro</code> | 1 | 未声明附加限制 |
| 产物 | 巨人柱种子<br><code>wildfarmingfork:wildseeds-saguarocactus-topempty</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 球形仙人掌<br><code>game:barrelcactus-normal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 球形仙人掌种子<br><code>wildfarmingfork:wildseeds-barrelcactus-normal</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 银火炬仙人掌<br><code>game:silvertorchcactus</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 银火炬仙人掌种子<br><code>wildfarmingfork:wildseeds-silvertorchcactus</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/cactiseeds.json`

```json
[
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:fruit-saguaro",
        "quantity": 1
      }
    },
    "name": "saguaroseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-saguarocactus-topempty",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:barrelcactus-normal"
      }
    },
    "name": "barrelseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-barrelcactus-normal",
      "quantity": 3
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:silvertorchcactus"
      }
    },
    "name": "silvertorchseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-silvertorchcactus",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、木薯种子、甘草种子 · cropseeds</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 木制淘盘<br><code>game:pan-wooden</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 2 | 允许变体：['flax', 'rice', 'rye', 'spelt', 'amaranth', 'sunflower'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:seeds-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 2 | 允许变体：['carrot', 'cabbage', 'onion', 'turnip', 'parsnip', 'bellpepper', 'fennel'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:seeds-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:legume-*</code> | 2 | 允许变体：['peanut', 'soybean'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:seeds-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 生木薯<br><code>game:rawcassava-raw</code> | 1 | 未声明附加限制 |
| 产物 | 木薯种子<br><code>game:seeds-cassava</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 甘草根<br><code>game:spice-licorice-raw</code> | 2 | 未声明附加限制 |
| 产物 | 甘草种子<br><code>game:seeds-licorice</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/cropseeds.json`

```json
[
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "block",
        "code": "game:pan-wooden",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 2,
        "name": "type",
        "allowedVariants": [
          "flax",
          "rice",
          "rye",
          "spelt",
          "amaranth",
          "sunflower"
        ]
      }
    },
    "name": "grainseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:seeds-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:shears-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:vegetable-*",
        "quantity": 2,
        "name": "type",
        "allowedVariants": [
          "carrot",
          "cabbage",
          "onion",
          "turnip",
          "parsnip",
          "bellpepper",
          "fennel"
        ]
      }
    },
    "name": "vegetableseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:seeds-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:shears-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:legume-*",
        "quantity": 2,
        "name": "type",
        "allowedVariants": [
          "peanut",
          "soybean"
        ]
      }
    },
    "name": "vegetableseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:seeds-{type}",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:shears-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:rawcassava-raw",
        "quantity": 1
      }
    },
    "name": "vegetableseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:seeds-cassava",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:shears-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:spice-licorice-raw",
        "quantity": 2
      }
    },
    "name": "vegetableseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:seeds-licorice",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、高大的蕨孢子 · flowerseeds</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:flower-*-free</code> | 1 | 允许变体：['catmint', 'cornflower', 'forgetmenot', 'edelweiss', 'heather', 'horsetail', 'orangemallow', 'wilddaisy', 'westerngorse', 'cowparsley', 'goldenpoppy', 'lilyofthevalley', 'woad', 'redtopgrass', 'lupine-blue', 'lupine-orange', 'lupine-purple', 'lupine-red', 'lupine-white', 'bluebell', 'daffodil', 'mugwort'] |
| 产物 | 变体材料（按代码匹配）<br><code>wildfarmingfork:wildseeds-flower-{type}-free</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:flower-*</code> | 1 | 允许变体：['rafflesia-brown', 'rafflesia-red', 'croton-small-crimson-brown-green', 'croton-small-crimson-green', 'croton-small-crimson-orange', 'croton-small-darkgreen-gold', 'croton-small-darkgreen-gold-crimson', 'croton-small-green-orange', 'croton-small-lemongreen', 'croton-small-lemongreen-crimson', 'croton-medium-crimson-brown-green', 'croton-medium-crimson-green', 'croton-medium-crimson-orange', 'croton-medium-darkgreen-gold', 'croton-medium-darkgreen-gold-crimson', 'croton-medium-green-orange', 'croton-medium-lemongreen', 'croton-medium-lemongreen-crimson'] |
| 产物 | 变体材料（按代码匹配）<br><code>wildfarmingfork:wildseeds-flower-{type}</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:fern-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>wildfarmingfork:wildseeds-fern-{type}</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 高大的蕨<br><code>game:tallfern</code> | 1 | 未声明附加限制 |
| 产物 | 高大的蕨孢子<br><code>wildfarmingfork:wildseeds-fern-tallfern</code> | 3 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/flowerseeds.json`

```json
[
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:flower-*-free",
        "quantity": 1,
        "name": "type",
        "allowedVariants": [
          "catmint",
          "cornflower",
          "forgetmenot",
          "edelweiss",
          "heather",
          "horsetail",
          "orangemallow",
          "wilddaisy",
          "westerngorse",
          "cowparsley",
          "goldenpoppy",
          "lilyofthevalley",
          "woad",
          "redtopgrass",
          "lupine-blue",
          "lupine-orange",
          "lupine-purple",
          "lupine-red",
          "lupine-white",
          "bluebell",
          "daffodil",
          "mugwort"
        ]
      }
    },
    "name": "flowerseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-flower-{type}-free",
      "quantity": 3
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:flower-*",
        "quantity": 1,
        "name": "type",
        "allowedVariants": [
          "rafflesia-brown",
          "rafflesia-red",
          "croton-small-crimson-brown-green",
          "croton-small-crimson-green",
          "croton-small-crimson-orange",
          "croton-small-darkgreen-gold",
          "croton-small-darkgreen-gold-crimson",
          "croton-small-green-orange",
          "croton-small-lemongreen",
          "croton-small-lemongreen-crimson",
          "croton-medium-crimson-brown-green",
          "croton-medium-crimson-green",
          "croton-medium-crimson-orange",
          "croton-medium-darkgreen-gold",
          "croton-medium-darkgreen-gold-crimson",
          "croton-medium-green-orange",
          "croton-medium-lemongreen",
          "croton-medium-lemongreen-crimson"
        ]
      }
    },
    "name": "flowerseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-flower-{type}",
      "quantity": 3
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:fern-*",
        "quantity": 1,
        "name": "type"
      }
    },
    "name": "fernseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-fern-{type}",
      "quantity": 3
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:tallfern",
        "quantity": 1
      }
    },
    "name": "tallfernseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-fern-tallfern",
      "quantity": 3
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · fruitingbushcutting</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 2 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 2 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KF
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/fruitingbushcutting.json`

```json
[
  {
    "enabled": true,
    "ingredientPattern": "KF",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "F": {
        "type": "item",
        "code": "game:fruit-*",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 2
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "KF",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "F": {
        "type": "item",
        "code": "game:fruit-*",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 2
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": ""
      }
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · fruitingbushgrafting-handbook</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；所需特性：仅供参考；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/fruitingbushgrafting-handbook.json`

```json
[
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer,thickskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted,strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer,strongrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit,strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer,strongclusteredberries"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit,strongrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer,thinskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted,weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer,weakrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit,weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer,weakclusteredberries"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit,weakrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": "heavybearer,thickskinnedfruit,strongrooted,strongclusteredberries"
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": ""
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 2
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "requiresTrait": "仅供参考",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": "shybearer,thinskinnedfruit,weakrooted,weakclusteredberries"
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": ""
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free"
    },
    "quantity": 2
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · fruitingbushgrafting</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 18**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 未声明；按配方类型判定 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 19**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

**方案 20**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 X | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 投入 Y | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-*-free</code> | 1 | 允许变体：['beautyberry', 'blackberry', 'blueberry', 'cloudberry', 'cranberry', 'blackcurrant', 'raspberry', 'redcurrant', 'whitecurrant', 'strawberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:fruitingbushcutting-{fruit}-free</code> | 2 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
XYS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/fruitingbushgrafting.json`

```json
[
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "heavybearer,thickskinnedfruit"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "heavybearer,strongrooted"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "heavybearer,strongclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "thickskinnedfruit,strongrooted"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "thickskinnedfruit,strongclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "strongrooted,strongclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer,thickskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "strongrooted,strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "heavybearer,thickskinnedfruit,strongrooted,strongclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer,strongrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit,strongclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "heavybearer,thickskinnedfruit,strongrooted,strongclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "heavybearer,strongclusteredberries"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thickskinnedfruit,strongrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "heavybearer,thickskinnedfruit,strongrooted,strongclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "shybearer,thinskinnedfruit"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "shybearer,weakrooted"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "shybearer,weakclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "thinskinnedfruit,weakrooted"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "thinskinnedfruit,weakclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "weakrooted,weakclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer,thinskinnedfruit"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "weakrooted,weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "shybearer,thinskinnedfruit,weakrooted,weakclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer,weakrooted"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit,weakclusteredberries"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "shybearer,thinskinnedfruit,weakrooted,weakclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "shybearer,weakclusteredberries"
        }
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "attributes": {
          "traits": "thinskinnedfruit,weakrooted"
        }
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "shybearer,thinskinnedfruit,weakrooted,weakclusteredberries"
      }
    },
    "quantity": 1
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": "heavybearer,thickskinnedfruit,strongrooted,strongclusteredberries"
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": ""
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "heavybearer,thickskinnedfruit,strongrooted,strongclusteredberries"
      },
      "quantity": 2
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "XYS",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "X": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": "shybearer,thinskinnedfruit,weakrooted,weakclusteredberries"
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      },
      "Y": {
        "type": "Block",
        "code": "game:fruitingbushcutting-*-free",
        "attributes": {
          "traits": ""
        },
        "name": "fruit",
        "allowedVariants": [
          "beautyberry",
          "blackberry",
          "blueberry",
          "cloudberry",
          "cranberry",
          "blackcurrant",
          "raspberry",
          "redcurrant",
          "whitecurrant",
          "strawberry"
        ],
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "recipeGroup": 1,
    "shapeless": true,
    "output": {
      "type": "Block",
      "code": "game:fruitingbushcutting-{fruit}-free",
      "attributes": {
        "traits": "shybearer,thinskinnedfruit,weakrooted,weakclusteredberries"
      },
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · fruitseeds</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 1 | 允许变体：['cranberry', 'blueberry'] |
| 产物 | 变体材料（按代码匹配）<br><code>wildfarmingfork:wildseeds-smallberrybush-{type}-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 1 | 允许变体：['redcurrant', 'blackcurrant', 'whitecurrant'] |
| 产物 | 变体材料（按代码匹配）<br><code>wildfarmingfork:wildseeds-bigberrybush-{type}-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 1 | 允许变体：['pineapple'] |
| 产物 | 变体材料（按代码匹配）<br><code>game:seeds-{type}</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/fruitseeds.json`

```json
[
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:fruit-*",
        "quantity": 1,
        "name": "type",
        "allowedVariants": [
          "cranberry",
          "blueberry"
        ]
      }
    },
    "name": "fruitseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-smallberrybush-{type}-empty",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:fruit-*",
        "quantity": 1,
        "name": "type",
        "allowedVariants": [
          "redcurrant",
          "blackcurrant",
          "whitecurrant"
        ]
      }
    },
    "name": "fruitseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "wildfarmingfork:wildseeds-bigberrybush-{type}-empty",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "K,H",
    "enabled": true,
    "shapeless": true,
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:fruit-*",
        "quantity": 1,
        "name": "type",
        "allowedVariants": [
          "pineapple"
        ]
      }
    },
    "name": "fruitseeds",
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "game:seeds-{type}",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>蘑菇培养基 · mushroomsubstrate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:soil-*-none</code> | 未声明；按配方类型判定 | 允许变体：['high', 'compost'] |
| 投入 G | 变体材料（按代码匹配）<br><code>game:grain-*</code> | 4 | 未声明附加限制 |
| 投入 H | 干草<br><code>game:drygrass</code> | 4 | 未声明附加限制 |
| 产物 | 蘑菇培养基<br><code>wildfarmingfork:mushroomsubstrate</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
GLG
SLS
HWH
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/mushroomsubstrate.json`

```json
[
  {
    "enabled": true,
    "ingredientPattern": "GLG,SLS,HWH",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "L": {
        "type": "block",
        "code": "game:log-*"
      },
      "S": {
        "type": "block",
        "code": "game:soil-*-none",
        "allowedVariants": [
          "high",
          "compost"
        ]
      },
      "G": {
        "type": "item",
        "code": "game:grain-*",
        "quantity": 4
      },
      "H": {
        "type": "item",
        "code": "game:drygrass",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:alcoholportion"
        },
        "requiresLitres": 1
      }
    },
    "output": {
      "type": "block",
      "code": "wildfarmingfork:mushroomsubstrate"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码）、绳索捆 · vinetrimming</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 名称未汉化（见物品代码）<br><code>game:wildvine-tropical-section-north</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:wildvine-end-north</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 名称未汉化（见物品代码）<br><code>game:wildvine-section-north</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>game:wildvine-end-north</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 名称未汉化（见物品代码）<br><code>game:wildvine-tropical-section-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 绳索捆<br><code>game:rope</code> | 1 | 未声明附加限制 |

**加工条件：** 配方开关：True；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
WWW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/wildfarmingfork/recipes/grid/vinetrimming.json`

```json
[
  {
    "enabled": true,
    "ingredientPattern": "WF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "block",
        "code": "game:wildvine-tropical-section-north",
        "quantity": 2,
        "name": "dir"
      }
    },
    "width": 2,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:waterportion"
        },
        "requiresLitres": 1
      }
    },
    "name": "vines",
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:wildvine-end-north",
      "quantity": 1
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "WF",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "block",
        "code": "game:wildvine-section-north",
        "quantity": 2,
        "name": "dir"
      }
    },
    "width": 2,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:waterportion"
        },
        "requiresLitres": 1
      }
    },
    "name": "vines",
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "game:wildvine-end-north",
      "quantity": 1
    }
  },
  {
    "enabled": true,
    "ingredientPattern": "WWW",
    "ingredients": {
      "W": {
        "type": "block",
        "code": "game:wildvine-tropical-section-north",
        "name": "wildvine"
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:rope",
      "quantity": 1
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
