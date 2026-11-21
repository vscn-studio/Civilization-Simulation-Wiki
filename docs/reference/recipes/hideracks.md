<!-- generated:start -->
# 皮革加工：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：沉浸式制皮

来源：`assets/hideracks/config/handbook/101-hideworking.json`。

沉浸式制皮

在传统木架上准备、绷展、刮削、盐渍和熟化兽皮。

盐渍、涂油和刮皮都需要制皮架。两种架子每次都只能绷上一张兽皮，并用绳子固定。加工过程中，兽皮的外观也会变化。兽皮仍可存放在地面上，但浸泡过的兽皮不能在地面上刮削。后续还将加入更多沉浸式储存方式。

搭建制皮架

[handbook://block-hideracks:rack-small-ns] 小制皮架（占地 2 × 2 × 1 格；用于小型和中型兽皮）

[handbook://block-hideracks:rack-large-ns] 大制皮架（占地 3 × 3 × 1 格；用于大型和巨型兽皮）

两种架子都能朝四个方向放置。将合适大小的兽皮放到空架子上，即可开始加工。

盐渍与保存

先绷上一张生皮。手持 [handbook://item-salt] 盐，右键点击架上的兽皮进行盐渍。

用盐量：小型 1 · 中型 2 · 大型 4 · 巨型 8

盐渍兽皮须在架上放置 48 个游戏小时，之后才能取下或涂油。已禁用在合成栏中盐渍兽皮。未完成盐渍就拆掉架子，会损毁兽皮。

涂油与毛皮

绷上一张生皮，或等盐渍兽皮静置满 48 小时。

涂油前，先在合成栏中用小刀或切肉刀将原版脂肪块切成 [handbook://item-hideracks:fat-chunk] 熬炼脂肪小块。这些小块可直接涂在架上绷展的兽皮上。

手持脂肪小块，右键点击架上的兽皮进行涂油。

脂肪小块用量：小型 1 · 中型 2 · 大型 4 · 巨型 8

制皮架只接受本模组的脂肪小块，不能直接使用原版脂肪块。已禁用在合成栏中给兽皮涂油。

涂油兽皮须在架上放置 48 个游戏小时，才能变成毛皮。熟化完成前拆掉架子，会损毁兽皮。

浸泡与刮皮

按照原版制革流程浸泡兽皮。将浸泡过的兽皮绷上架子，装备小刀，瞄准兽皮并按住右键刮削。顶部进度条会显示进展。你可以随时停下，稍后继续。已禁用在合成栏中或地面上用小刀刮削浸泡兽皮。

刮削时，依据兽皮大小和概率，还可能获得 [handbook://item-hideracks:fleshings] 刮皮碎屑。可让碎屑腐烂后用于施肥，也可将其熬炼为 [handbook://item-hideracks:fat-chunk] 熬炼脂肪小块。

熊皮与去头

黑熊、棕熊、熊猫、北极熊和马来熊的毛皮在架上保留各自的外观。

完整熊皮带有头部。用小刀对放在地面上或绷在架上的完整熊皮操作，即可切除头部。已禁用在合成栏中去头。

剩下的无头熊皮仍可按相应流程加工。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>特殊配方 · fleshings-to-fat</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 刮皮碎屑<br><code>fleshings</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/hideracks/recipes/cooking/fleshings-to-fat.json`

```json
{
  "code": "hideracks-fleshings-to-fat",
  "shape": {
    "base": "block/food/meal/porridge"
  },
  "ingredients": [
    {
      "code": "fleshings",
      "validStacks": [
        {
          "type": "item",
          "code": "hideracks:fleshings"
        }
      ],
      "minQuantity": 4,
      "maxQuantity": 4
    }
  ],
  "cooksInto": {
    "type": "item",
    "code": "hideracks:fat-chunk",
    "quantity": 1
  },
  "isFood": false,
  "perishableProps": {
    "freshHours": {
      "avg": 100000
    },
    "transitionHours": {
      "avg": 100000
    },
    "transitionRatio": 1,
    "transitionedStack": {
      "type": "item",
      "code": "game:rot"
    }
  }
}
```

</details>

</details>

<details><summary>特殊配方 · recombine-fat</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 名称未汉化（见物品代码）<br><code>fat</code> | 未声明；按配方类型判定 | 最少数量：4；最多数量：4 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/hideracks/recipes/cooking/recombine-fat.json`

```json
{
  "code": "hideracks-refat",
  "shape": {
    "base": "block/food/meal/porridge"
  },
  "ingredients": [
    {
      "code": "fat",
      "validStacks": [
        {
          "type": "item",
          "code": "hideracks:fat-chunk"
        }
      ],
      "minQuantity": 4,
      "maxQuantity": 4
    }
  ],
  "cooksInto": {
    "type": "item",
    "code": "game:fat-rendered",
    "quantity": 1
  },
  "isFood": false,
  "perishableProps": {
    "freshHours": {
      "avg": 100000
    },
    "transitionHours": {
      "avg": 100000
    },
    "transitionRatio": 1,
    "transitionedStack": {
      "type": "item",
      "code": "game:rot"
    }
  }
}
```

</details>

</details>

<details><summary>熬炼脂肪小块 · cut-fat</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 产物 | 熬炼脂肪小块<br><code>hideracks:fat-chunk</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FT
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 熬制的脂肪块<br><code>game:fat-rendered</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 变体材料（按代码匹配）<br><code>game:cleaver-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：1 |
| 产物 | 熬炼脂肪小块<br><code>hideracks:fat-chunk</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FT
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/hideracks/recipes/grid/cut-fat.json`

```json
[
  {
    "ingredientPattern": "FT",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      },
      "T": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true,
        "toolDurabilityCost": 1
      }
    },
    "output": {
      "type": "item",
      "code": "hideracks:fat-chunk",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "FT",
    "width": 2,
    "height": 1,
    "shapeless": true,
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:fat-rendered"
      },
      "T": {
        "type": "item",
        "code": "game:cleaver-*",
        "isTool": true,
        "toolDurabilityCost": 1
      }
    },
    "output": {
      "type": "item",
      "code": "hideracks:fat-chunk",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>大制皮架 · rack-large</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 2 | 未声明附加限制 |
| 投入 T | 亚麻线<br><code>game:flaxtwine</code> | 2 | 未声明附加限制 |
| 产物 | 大制皮架<br><code>hideracks:rack-large-ns</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SSS
RTR
SSS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/hideracks/recipes/grid/rack-large.json`

```json
{
  "ingredientPattern": "SSS,RTR,SSS",
  "width": 3,
  "height": 3,
  "ingredients": {
    "S": {
      "type": "item",
      "code": "game:stick"
    },
    "R": {
      "type": "item",
      "code": "game:rope",
      "quantity": 2
    },
    "T": {
      "type": "item",
      "code": "game:flaxtwine",
      "quantity": 2
    }
  },
  "output": {
    "type": "block",
    "code": "hideracks:rack-large-ns",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>小制皮架 · rack-small</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 亚麻线<br><code>game:flaxtwine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 小制皮架<br><code>hideracks:rack-small-ns</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_S
RTR
S_S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/hideracks/recipes/grid/rack-small.json`

```json
{
  "ingredientPattern": "S_S,RTR,S_S",
  "width": 3,
  "height": 3,
  "ingredients": {
    "S": {
      "type": "item",
      "code": "game:stick"
    },
    "R": {
      "type": "item",
      "code": "game:rope"
    },
    "T": {
      "type": "item",
      "code": "game:flaxtwine"
    }
  },
  "output": {
    "type": "block",
    "code": "hideracks:rack-small-ns",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
