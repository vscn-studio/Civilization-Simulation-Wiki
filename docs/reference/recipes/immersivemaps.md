<!-- generated:start -->
# 沉浸地图：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：游戏机制：地图


地图

沉浸式地图 - Woeful_Wolf

地图是定位自己和了解周围环境的简单方法。

地图有两个等级，等级越高，可覆盖的区域越大。

第一个也是最容易获得的地图是 [handbook://item-immersivemaps:map-papyrus] 纸莎草地图。第二个是 [handbook://item-immersivemaps:map-parchment] 羊皮纸地图。

请注意，当你第一次拿住地图时，它会以你当前的位置为中心。

不过别担心，地图可以随时更新，只需副手拿着绘图工具，然后按 rightmouse。最容易获得的是 [handbook://item-immersivemaps:charcoal-pencil] 木炭铅笔，之后是 [handbook://item-immersivemaps:penner-and-inkhorn] 笔盒与墨水瓶（暂无配方），其耐久度更高。

它还可以在你移动时持续更新！

在绘制新地图时，你可能会有点迷失方向，这很正常，毕竟真正的北方不是你能凭直觉感受到的（好吧，至少我希望不是）。

幸运的是，你可以随时按 map-rotate-hk 顺时针旋转手中的地图，或按 map-rotate-reverse-hk 逆时针旋转。

这一切都很好，但如果没有路径点，地图有什么用？你不可能记得 3000 格外的地表铜矿在哪里，对吧？

按 map-waypoints-gui 可以管理你手中地图的路径点。添加新路径点或编辑现有路径点也需要副手持有绘图工具。

你也可以标记信件中找到的坐标。只需在与信件互动时副手拿着地图，即可将其添加为路径点。

外出勘探？每次使用 [handbook://item-prospectingpick-copper] 探矿镐读取时，聊天中都会出现“添加到你的地图”链接。手中拿着地图，副手拿着绘图工具，点击它即可标记该地点。

厌倦了重绘？将任意地图与 [handbook://item-gear-temporal] 时隙齿轮一起制作，即可将其变为时隙地图。它会以持有者为中心，并跟随他们到任何地方。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>木炭铅笔 · charcoal-pencil-recipe</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 1 | 工具；耐久消耗：0 |
| 投入 C | 木炭<br><code>game:charcoal</code> | 1 | 未声明附加限制 |
| 投入 F | 亚麻纤维<br><code>game:flaxfibers</code> | 1 | 未声明附加限制 |
| 产物 | 木炭铅笔<br><code>charcoal-pencil</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S
C
F
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "S,C,F",
  "shapeless": true,
  "ingredients": {
    "S": {
      "type": "item",
      "code": "game:stone-*",
      "quantity": 1,
      "isTool": true,
      "toolDurabilityCost": 0
    },
    "C": {
      "type": "item",
      "code": "game:charcoal",
      "quantity": 1
    },
    "F": {
      "type": "item",
      "code": "game:flaxfibers",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 3,
  "output": {
    "type": "item",
    "code": "charcoal-pencil"
  }
}
```

</details>

</details>

<details><summary>纸莎草地图 · map-papyrus-recipe</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 纸莎草纸<br><code>paper-papyrus</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 纸莎草地图<br><code>map-papyrus</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
PPP
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "PPP,PPP,PPP",
  "width": 3,
  "height": 3,
  "ingredients": {
    "P": {
      "type": "item",
      "code": "paper-papyrus"
    }
  },
  "output": {
    "type": "item",
    "code": "map-papyrus"
  }
}
```

</details>

</details>

<details><summary>时隙纸莎草地图 · map-papyrus-temporal-recipe</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 纸莎草地图<br><code>map-papyrus</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 时隙纸莎草地图<br><code>map-papyrus-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
M
G
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "M,G",
  "width": 1,
  "height": 2,
  "shapeless": true,
  "ingredients": {
    "M": {
      "type": "item",
      "code": "map-papyrus"
    },
    "G": {
      "type": "item",
      "code": "game:gear-temporal"
    }
  },
  "copyAttributesFrom": "M",
  "output": {
    "type": "item",
    "code": "map-papyrus-temporal"
  }
}
```

</details>

</details>

<details><summary>羊皮纸地图 · map-parchment-recipe</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊皮纸地图<br><code>map-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
PPP
PPP
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "PPP,PPP,PPP",
  "width": 3,
  "height": 3,
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:paper-parchment"
    }
  },
  "output": {
    "type": "item",
    "code": "map-parchment"
  }
}
```

</details>

</details>

<details><summary>时隙羊皮纸地图 · map-parchment-temporal-recipe</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 M | 羊皮纸地图<br><code>map-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 时隙羊皮纸地图<br><code>map-parchment-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
M
G
```

<details><summary>技术说明：完整配方</summary>


```json
{
  "ingredientPattern": "M,G",
  "width": 1,
  "height": 2,
  "shapeless": true,
  "ingredients": {
    "M": {
      "type": "item",
      "code": "map-parchment"
    },
    "G": {
      "type": "item",
      "code": "game:gear-temporal"
    }
  },
  "copyAttributesFrom": "M",
  "output": {
    "type": "item",
    "code": "map-parchment-temporal"
  }
}
```

</details>

</details>

<details><summary>纸莎草纸 · paper-papyrus-recipe</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 1 | 工具；耐久消耗：0 |
| 投入 P | 纸莎草<br><code>game:papyrustops</code> | 4 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 1 | 工具；耐久消耗：4 |
| 产物 | 纸莎草纸<br><code>paper-papyrus</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_
PK
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 1 | 工具；耐久消耗：0 |
| 投入 C | 香蒲<br><code>game:cattailtops</code> | 4 | 未声明附加限制 |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 1 | 工具；耐久消耗：4 |
| 产物 | 纸莎草纸<br><code>paper-papyrus</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
S_
CK
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "S_,PK",
    "shapeless": true,
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 1,
        "isTool": true,
        "toolDurabilityCost": 0
      },
      "P": {
        "type": "item",
        "code": "game:papyrustops",
        "quantity": 4
      },
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "quantity": 1,
        "isTool": true,
        "toolDurabilityCost": 4
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "paper-papyrus"
    }
  },
  {
    "ingredientPattern": "S_,CK",
    "shapeless": true,
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 1,
        "isTool": true,
        "toolDurabilityCost": 0
      },
      "C": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 4
      },
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "quantity": 1,
        "isTool": true,
        "toolDurabilityCost": 4
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "paper-papyrus"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
