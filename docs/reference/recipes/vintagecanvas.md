<!-- generated:start -->
# 绘画画布：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：复古画布入门

来源：`assets/vintagecanvas/config/handbook/1-basics.json`。

复古画布的第一步

欢迎使用复古画布！开启创作之旅，至少需要一副画架、任意形状的画布和一根炭条。

将画架放在地上，最好选光线充足的地方。按rightmousebutton将画布放上画架，然后手持炭条，尽情勾画吧！

想展示作品时，空手从画架上取下画布，再挂到墙上。画布挂好后，可用任意木板为它装上画框！

晕染

若觉得线条过于粗糙，可制作一支 [handbooksearch://brush] 画笔。不带颜料的画笔可以晕染已有笔迹，画出平滑的渐变和更浅的颜色。想修正画面，可制作一根白垩条。

## 手册 2：绘制画布画

来源：`assets/vintagecanvas/config/handbook/2-painting.json`。

颜料绘画

准备好迎接新挑战，就来制作颜料吧！制作几个 [handbooksearch://paint jar] 颜料罐，装入 [handbooksearch://oil] 油，再加入色粉。色粉可用粉碎的青金石、朱砂、木炭，也可用复古画布新增的 [handbooksearch://pigment] 色粉。若缺少油，可向装满水的颜料罐中加入鸡蛋，制作替代用的“蛋彩媒介剂”。

接着制作一种或多种 [handbooksearch://brush] 画笔。右键点击所需的颜料罐蘸取颜料，即可作画！

若不满足于基础色粉的单一颜色，可尝试稀释和混色。

稀释颜料

将带颜料的画笔蘸入 [handbooksearch://turpentine] 松节油，可以降低颜料的不透明度。蘸取次数越多，颜色越透明，很适合叠色！

混合颜料

想调出更多颜色，就制作一块 [handbooksearch://palette] 调色板吧！放在地上后，调色板提供九个混色格。手持颜料罐点击任意格子，将颜色加入其中；继续加入其他颜料，直到调出理想色调。和颜料罐一样，手持画笔右键点击格子即可蘸取颜料。要清空格子，手持松节油罐右键点击即可。

晕染

干净且不带颜料的画笔可以在画布上晕染颜色。要清洗画笔，手持画笔，潜行并右键点击松节油罐。

## 手册 3：绘制壁画

来源：`assets/vintagecanvas/config/handbook/3-frescos.json`。

最直接的作画方式

除了画布，复古画布也支持绘制壁画。制作一些 [handbooksearch://fresco plaster] 壁画灰泥或 [handbooksearch://primer] 底漆，涂在雕凿过的方块上，再用绘画工具直接在墙面作画。目前不支持未经雕凿的方块。白色灰泥可形成类似画布的底色；透明底漆则能保留原方块的外观。

用 [handbooksearch://turpentine rag] 松节油抹布可以擦除部分图案。

壁画很脆弱，无法完整取下；若想携带作品，请使用画布。

## 手册 4：画布升级与装饰

来源：`assets/vintagecanvas/config/handbook/4-largepaintings.json`。

大幅画作

绘制大画布需要 [handbooksearch://large easel] 大画架。准备好后，将两张相同规格的画布合成，即可升级为对应的大号画布。材料只需两倍，绘画面积却有四倍！

画框

把画布挂好，手持木板右键点击即可加上画框。继续点击可切换样式或移除画框。

命名与署名

手持墨水与羽毛笔右键点击画架，即可给画作命名并签署作者姓名。署名后，其他人无法更改。

## 手册 5：无限颜料与其他设置

来源：`assets/vintagecanvas/config/handbook/5-finitepaint.json`。

默认情况下，使用画笔、调色板和颜料罐会缓慢消耗颜料。若想不受颜料用量限制地作画，可在模组配置中关闭此设置（PaintDepletion: false）。也可调整设置，让同样数量的颜料能画得更多。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>巴西木红色粉 · brazilwood</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 水<br><code>game:waterportion</code> | 10 升 | 未声明附加限制 |
| 投入 2 | 名称未汉化（见物品代码）<br><code>game:log-placed-purpleheart-ud</code> | 1 | 未声明附加限制 |
| 产物 | 巴西木红色粉<br><code>vintagecanvas:pigment-brazilwood</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/barrel/brazilwood.json`

```json
{
  "code": "brazilwood",
  "sealHours": 48,
  "ingredients": [
    {
      "type": "item",
      "code": "game:waterportion",
      "litres": 10
    },
    {
      "type": "block",
      "code": "game:log-placed-purpleheart-ud",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "vintagecanvas:pigment-brazilwood",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>铅锡黄色粉 · leadwhite</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 铅白色粉<br><code>pigment-leadwhite</code> | 1 | 未声明附加限制 |
| 产物 | 铅锡黄色粉<br><code>pigment-leadtin</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/barrel/leadwhite.json`

```json
{
  "code": "leadwhite",
  "ingredients": [
    {
      "type": "item",
      "code": "game:dilutedcassiteriteportion",
      "litres": 1
    },
    {
      "type": "item",
      "code": "pigment-leadwhite",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "pigment-leadtin",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>群青色粉 · ultramarine</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 稀释锡石<br><code>game:dilutedcassiteriteportion</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 青金石粉<br><code>game:powder-lapislazuli</code> | 1 | 未声明附加限制 |
| 产物 | 群青色粉<br><code>vintagecanvas:pigment-ultramarine</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/barrel/ultramarine.json`

```json
{
  "code": "ultramarine",
  "sealHours": 4,
  "ingredients": [
    {
      "type": "item",
      "code": "game:dilutedcassiteriteportion",
      "litres": 1
    },
    {
      "type": "item",
      "code": "game:powder-lapislazuli",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "vintagecanvas:pigment-ultramarine",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>铜绿色粉 · verdigris</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 酒精<br><code>game:alcoholportion</code> | 0.2 升 | 未声明附加限制 |
| 投入 2 | 自然铜金属粒<br><code>game:nugget-nativecopper</code> | 1 | 未声明附加限制 |
| 产物 | 铜绿色粉<br><code>vintagecanvas:pigment-verdigris</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/barrel/verdigris.json`

```json
{
  "code": "verdigris",
  "sealHours": 48,
  "ingredients": [
    {
      "type": "item",
      "code": "game:alcoholportion",
      "litres": 0.2
    },
    {
      "type": "item",
      "code": "game:nugget-nativecopper",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "vintagecanvas:pigment-verdigris",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>朱红色粉 · vermillion</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 红色染料<br><code>game:dye-red</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 骨粉<br><code>game:bonemeal</code> | 1 | 未声明附加限制 |
| 产物 | 朱红色粉<br><code>vintagecanvas:pigment-vermillion</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/barrel/vermillion.json`

```json
{
  "code": "vermillion",
  "sealHours": 4,
  "ingredients": [
    {
      "type": "item",
      "code": "game:dye-red",
      "litres": 1
    },
    {
      "type": "item",
      "code": "game:bonemeal",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "vintagecanvas:pigment-vermillion",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>菘蓝色粉 · woadpigment</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 靛蓝染料<br><code>game:dye-woad</code> | 1 升 | 未声明附加限制 |
| 投入 2 | 骨粉<br><code>game:bonemeal</code> | 1 | 未声明附加限制 |
| 产物 | 菘蓝色粉<br><code>vintagecanvas:pigment-woad</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：4。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/barrel/woadpigment.json`

```json
{
  "code": "woadpigment",
  "sealHours": 4,
  "ingredients": [
    {
      "type": "item",
      "code": "game:dye-woad",
      "litres": 1
    },
    {
      "type": "item",
      "code": "game:bonemeal",
      "quantity": 1
    }
  ],
  "output": {
    "type": "item",
    "code": "vintagecanvas:pigment-woad",
    "stackSize": 1
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · fourpaintjars</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vintagecanvas:paintjar-{color}-raw</code> | 4 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/clayforming/fourpaintjars.json`

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
      "_____________",
      "_####___####_",
      "_####___####_",
      "_####___####_",
      "_####___####_",
      "_____________",
      "_____________",
      "_____________",
      "_####___####_",
      "_####___####_",
      "_####___####_",
      "_####___####_",
      "_____________"
    ],
    [
      "######_######",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "######_######",
      "_____________",
      "######_######",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "######_######"
    ],
    [
      "######_######",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "######_######",
      "_____________",
      "######_######",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "######_######"
    ],
    [
      "######_######",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "######_######",
      "_____________",
      "######_######",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "#____#_#____#",
      "######_######"
    ],
    [
      "_____________",
      "_####___####_",
      "_#__#___#__#_",
      "_#__#___#__#_",
      "_####___####_",
      "_____________",
      "_____________",
      "_____________",
      "_####___####_",
      "_#__#___#__#_",
      "_#__#___#__#_",
      "_####___####_",
      "_____________"
    ]
  ],
  "name": "Paint Jar 4",
  "output": {
    "type": "item",
    "code": "vintagecanvas:paintjar-{color}-raw",
    "stacksize": 4
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · paintjar</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>vintagecanvas:paintjar-{color}-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/clayforming/paintjar.json`

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
      "______",
      "_####_",
      "_####_",
      "_####_",
      "_####_",
      "______"
    ],
    [
      "######",
      "#____#",
      "#____#",
      "#____#",
      "#____#",
      "######"
    ],
    [
      "######",
      "#____#",
      "#____#",
      "#____#",
      "#____#",
      "######"
    ],
    [
      "######",
      "#____#",
      "#____#",
      "#____#",
      "#____#",
      "######"
    ],
    [
      "______",
      "_####_",
      "_#__#_",
      "_#__#_",
      "_####_",
      "______"
    ]
  ],
  "name": "Paint Jar",
  "output": {
    "type": "item",
    "code": "vintagecanvas:paintjar-{color}-raw"
  }
}
```

</details>

</details>

<details><summary>特殊配方 · turpentine</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>resin</code> | 未声明；按配方类型判定 | 最少数量：1；最多数量：1 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/cooking/turpentine.json`

```json
{
  "code": "turpentine",
  "perishableProps": {
    "type": "None",
    "freshHours": {
      "avg": 48
    },
    "transitionHours": {
      "avg": 48
    },
    "transitionRatio": 1,
    "transitionedStack": {
      "type": "item",
      "code": "turpentine"
    }
  },
  "shape": {
    "base": "block/food/meal/liquid"
  },
  "ingredients": [
    {
      "code": "resin",
      "validStacks": [
        {
          "type": "item",
          "code": "game:resin"
        }
      ],
      "minQuantity": 1,
      "maxQuantity": 1
    }
  ],
  "cooksInto": {
    "type": "Item",
    "code": "turpentine",
    "quantity": 100
  }
}
```

</details>

</details>

<details><summary>画家贝雷帽 · beret</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 红色布料<br><code>game:cloth-red</code> | 1 | 未声明附加限制 |
| 产物 | 画家贝雷帽<br><code>clothes-head-beret</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CSC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 小型狐狸毛皮<br><code>game:hide-pelt-fox-red</code> | 1 | 未声明附加限制 |
| 产物 | 画家贝雷帽<br><code>clothes-head-beret</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CSC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/beret.json`

```json
[
  {
    "ingredientPattern": "CSC",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-red",
        "name": "cloth",
        "quantity": 1
      }
    },
    "name": "beret",
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "clothes-head-beret",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CSC",
    "ingredients": {
      "S": {
        "type": "item",
        "tags": [
          "tool-shears"
        ],
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:hide-pelt-fox-red",
        "name": "pelt",
        "quantity": 1
      }
    },
    "name": "beret",
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "clothes-head-beret",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>小画笔、中画笔、大画笔 · brush</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 香蒲<br><code>game:cattailtops</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 小画笔<br><code>brush-small</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
C__
_S_
__S
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 香蒲<br><code>game:cattailtops</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 中画笔<br><code>brush-medium</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_C_
CS_
__S
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 香蒲<br><code>game:cattailtops</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 大画笔<br><code>brush-large</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC_
CS_
__S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/brush.json`

```json
[
  {
    "ingredientPattern": "C__,_S_,__S",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "C": {
        "type": "item",
        "code": "game:cattailtops"
      }
    },
    "name": "Small Brush",
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "brush-small",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_C_,CS_,__S",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "C": {
        "type": "item",
        "code": "game:cattailtops"
      }
    },
    "name": "Medium Brush",
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "brush-medium",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CC_,CS_,__S",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "C": {
        "type": "item",
        "code": "game:cattailtops"
      }
    },
    "name": "Large Brush",
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "brush-large",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · canvas-vellum</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 犊皮纸<br><code>vellum</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-portrait-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
SLS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 犊皮纸<br><code>vellum</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-portrait-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
SLS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 犊皮纸<br><code>vellum</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-landscape-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SS
LL
SS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 犊皮纸<br><code>vellum</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-landscape-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SS
LL
SS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 犊皮纸<br><code>vellum</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-square-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
SLS
_S_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 犊皮纸<br><code>vellum</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-square-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
SLS
_S_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/canvas-vellum.json`

```json
[
  {
    "ingredientPattern": "SLS,SLS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "L": {
        "type": "item",
        "code": "vellum"
      }
    },
    "name": "Portrait Canvas",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "canvas-portrait-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SLS,SLS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:plank-*"
      },
      "L": {
        "type": "item",
        "code": "vellum"
      }
    },
    "name": "Portrait Canvas",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "canvas-portrait-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SS,LL,SS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "L": {
        "type": "item",
        "code": "vellum"
      }
    },
    "name": "Landscape Canvas",
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-landscape-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SS,LL,SS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:plank-*"
      },
      "L": {
        "type": "item",
        "code": "vellum"
      }
    },
    "name": "Landscape Canvas",
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-landscape-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,SLS,_S_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "L": {
        "type": "item",
        "code": "vellum",
        "quantity": 2
      }
    },
    "name": "Square Canvas",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-square-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,SLS,_S_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:plank-*"
      },
      "L": {
        "type": "item",
        "code": "vellum",
        "quantity": 2
      }
    },
    "name": "Square Canvas",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-square-none-oak-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · canvas</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-portrait-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
SLS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-portrait-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SLS
SLS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-landscape-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SS
LL
SS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-landscape-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SS
LL
SS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-square-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
SLS
_S_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>canvas-square-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
SLS
_S_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/canvas.json`

```json
[
  {
    "ingredientPattern": "SLS,SLS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "Portrait Canvas",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "canvas-portrait-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SLS,SLS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:plank-*"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "Portrait Canvas",
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "canvas-portrait-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SS,LL,SS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "Landscape Canvas",
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-landscape-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "SS,LL,SS",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:plank-*"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*"
      }
    },
    "name": "Landscape Canvas",
    "width": 2,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-landscape-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,SLS,_S_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*",
        "quantity": 2
      }
    },
    "name": "Square Canvas",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-square-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_S_,SLS,_S_",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:plank-*"
      },
      "L": {
        "type": "block",
        "code": "game:linen-*",
        "quantity": 2
      }
    },
    "name": "Square Canvas",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "canvas-square-none-oak-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · easel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>easel-{wood}-none-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_S_
PSP
P_P
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/easel.json`

```json
[
  {
    "ingredientPattern": "_S_,PSP,P_P",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
        "quantity": 1,
        "skipVariant": [
          "agedebony",
          "rottenebony"
        ]
      }
    },
    "name": "easel",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "easel-{wood}-none-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>壁画灰泥、底漆 · frescoplaster</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 Q | 生石灰<br><code>game:quicklime</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 J | 变体材料（按代码匹配）<br><code>paintjar-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 壁画灰泥<br><code>frescoplaster-white</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
QJS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 Q | 生石灰<br><code>game:quicklime</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 J | 变体材料（按代码匹配）<br><code>paintjar-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 壁画灰泥<br><code>frescoplaster-white</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
QJS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 Q | 生石灰<br><code>game:quicklime</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 J | 变体材料（按代码匹配）<br><code>paintjar-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 底漆<br><code>frescoplaster-transparent</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
QJS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/frescoplaster.json`

```json
[
  {
    "ingredientPattern": "QJS",
    "ingredients": {
      "Q": {
        "type": "item",
        "code": "game:quicklime"
      },
      "J": {
        "type": "block",
        "code": "paintjar-*-fired"
      },
      "S": {
        "type": "block",
        "code": "game:sand*"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "paint-chalkwhite*"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "frescoplaster-white",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "QJS",
    "ingredients": {
      "Q": {
        "type": "item",
        "code": "game:quicklime"
      },
      "J": {
        "type": "block",
        "code": "paintjar-*-fired"
      },
      "S": {
        "type": "block",
        "code": "game:sand*"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "paint-leadwhite*"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "frescoplaster-white",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "QJS",
    "ingredients": {
      "Q": {
        "type": "item",
        "code": "game:quicklime"
      },
      "J": {
        "type": "block",
        "code": "paintjar-*-fired"
      },
      "S": {
        "type": "block",
        "code": "game:sand*"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "turpentine*"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "frescoplaster-transparent",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · heasel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>heasel-{wood}-none-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
PNP
PSP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/heasel.json`

```json
[
  {
    "ingredientPattern": "PSP,PNP,PSP",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
        "quantity": 1,
        "skipVariant": [
          "agedebony",
          "rottenebony"
        ]
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*",
        "quantity": 2
      }
    },
    "name": "heasel",
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "heasel-{wood}-none-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · largecanvas</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 小竖幅画布<br><code>canvas-portrait-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>largecanvas-portrait-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 小横幅画布<br><code>canvas-landscape-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>largecanvas-landscape-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 小方形画布<br><code>canvas-square-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>largecanvas-square-none-oak-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/largecanvas.json`

```json
[
  {
    "ingredientPattern": "CC",
    "ingredients": {
      "C": {
        "type": "block",
        "code": "canvas-portrait-*"
      }
    },
    "name": "Large Portrait Canvas",
    "width": 2,
    "height": 1,
    "output": {
      "type": "block",
      "code": "largecanvas-portrait-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CC",
    "ingredients": {
      "C": {
        "type": "block",
        "code": "canvas-landscape-*"
      }
    },
    "name": "Large Landscape Canvas",
    "width": 2,
    "height": 1,
    "output": {
      "type": "block",
      "code": "largecanvas-landscape-none-oak-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CC",
    "ingredients": {
      "C": {
        "type": "block",
        "code": "canvas-square-*"
      }
    },
    "name": "Large Square Canvas",
    "width": 2,
    "height": 1,
    "output": {
      "type": "block",
      "code": "largecanvas-square-none-oak-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>调色板 · palette</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 1 | 未声明附加限制 |
| 产物 | 调色板<br><code>palette</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/palette.json`

```json
[
  {
    "ingredientPattern": "KP",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "name": "wood",
        "quantity": 1,
        "skipVariant": [
          "agedebony",
          "rottenebony"
        ]
      }
    },
    "name": "palette",
    "width": 2,
    "height": 1,
    "output": {
      "type": "block",
      "code": "palette",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>炭条、白垩条 · pastel</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 木炭<br><code>game:charcoal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 炭条<br><code>pastel-carbonblack</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CK
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 白垩岩石块<br><code>game:stone-chalk</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 白垩条<br><code>pastel-chalkwhite</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CK
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 石灰岩石块<br><code>game:stone-limestone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 白垩条<br><code>pastel-chalkwhite</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CK
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/pastel.json`

```json
[
  {
    "ingredientPattern": "CK",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:charcoal"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      }
    },
    "name": "Charcoal stick",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pastel-carbonblack",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CK",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:stone-chalk"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      }
    },
    "name": "Chalk stick",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pastel-chalkwhite",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "CK",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:stone-limestone"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      }
    },
    "name": "Chalk stick",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "pastel-chalkwhite",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>松节油抹布 · rag</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:linen-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 J | 变体材料（按代码匹配）<br><code>paintjar-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 松节油抹布<br><code>rag</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PKJ
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/rag.json`

```json
[
  {
    "ingredientPattern": "PKJ",
    "ingredients": {
      "P": {
        "type": "block",
        "code": "game:linen-*"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "J": {
        "type": "block",
        "code": "paintjar-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "turpentine*"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "rag",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · roller</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 布料<br><code>game:cloth-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:rod-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 H | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>roller-none</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
R
S
H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/roller.json`

```json
[
  {
    "ingredientPattern": "R,S,H",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:cloth-plain"
      },
      "S": {
        "type": "item",
        "code": "game:rod-*"
      },
      "H": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "name": "Roller",
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "roller-none",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>犊皮纸 · vellum</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 中型毛皮<br><code>game:hide-pelt-medium</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 J | 变体材料（按代码匹配）<br><code>paintjar-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 犊皮纸<br><code>vellum</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PKJ
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 大型毛皮<br><code>game:hide-pelt-large</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 J | 变体材料（按代码匹配）<br><code>paintjar-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 犊皮纸<br><code>vellum</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PKJ
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 巨型毛皮<br><code>game:hide-pelt-huge</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 J | 变体材料（按代码匹配）<br><code>paintjar-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 犊皮纸<br><code>vellum</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PKJ
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vintagecanvas/recipes/grid/vellum.json`

```json
[
  {
    "ingredientPattern": "PKJ",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:hide-pelt-medium"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "J": {
        "type": "block",
        "code": "paintjar-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "paint-chalkwhite*"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "vellum",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PKJ",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:hide-pelt-large"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "J": {
        "type": "block",
        "code": "paintjar-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "paint-chalkwhite*"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "vellum",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "PKJ",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "game:hide-pelt-huge"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "J": {
        "type": "block",
        "code": "paintjar-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "paint-chalkwhite*"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 3,
    "height": 1,
    "output": {
      "type": "item",
      "code": "vellum",
      "quantity": 4
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
