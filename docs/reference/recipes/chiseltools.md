<!-- generated:start -->
# 雕刻工具：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：凿子工具指南

来源：`assets/chiseltools/config/handbook/chiseltools.json`。

欢迎使用凿子工具！

[handbook://item-chiseltools:handplaner-iron] 手刨

在雕凿方块上使用可快速添加和移除材料。

- 按 F 进行选择模式

- 左键单击移除平面

- 右键单击添加平面

- 添加/移除匹配模式仅影响目标材料

- 在模式选择中撤消将撤消最后的修改（如果可行）

[handbook://item-chiseltools:handwedge-iron] 手楔

旋转、镜像或移动你的凿子。不适合方块的体素将被删除。

按 F 访问模式选择。变换基于你正在查看的面 （例如：在镜像模式下单击体素的顶部或底部以垂直翻转）

[handbook://item-chiseltools:pantograph-steel] 缩放仪

缩放仪用于将一个雕凿方块的形状复制到其他雕凿方块上

右键执行操作

- 快照模式将复制雕凿方块以在其他模式中使用。

- 替换模式将替换复制方块的整个形状

- 添加模式只会用复制方块替换空白空间

- 材料将以与复制方块相同的顺序使用 （例如：复制具有安山岩和花岗岩的方块，并将其粘贴到具有橡木木板

和砂岩的块上，这些方块将具有相同的形状，但源方块的位置有安山岩，复制的方块将有橡木木板）

- 从模式菜单中撤消最后一个操作

撤消操作：当你对方块进行更改时，会生成其形状的副本。 当你选择撤消时，如果可行，会恢复此副本。

[handbook://item-chiseltools:blockswapper-iron] 方块交换器

一种创造模式工具，可快速将目标方块更改为第一个物品栏中的任何方块。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · chiseledanvil-true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:anvil-*</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>chiseledanvil-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledanvil-true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:anvil-*",
      "name": "metal",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Anvil",
  "output": {
    "type": "block",
    "code": "chiseledanvil-{metal}"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledbarrel-true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 木桶<br><code>game:barrel</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledbarrel</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledbarrel-true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:barrel",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Barrel",
  "output": {
    "type": "block",
    "code": "chiseledbarrel"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledbarrel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 木桶<br><code>game:barrel</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledbarrel</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledbarrel.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:barrel",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledbarrel"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledbed - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:bed-wood-head-north</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledbed-wood-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledbed - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:bed-wood-head-north",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Bed",
  "output": {
    "type": "block",
    "code": "chiseledbed-wood-head-north"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledbed</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:bed-wood-head-north</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledbed-wood-head-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledbed.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:bed-wood-head-north",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Bed",
  "output": {
    "type": "block",
    "code": "chiseledbed-wood-head-north"
  }
}
```

</details>

</details>

<details><summary>装饰书架 · chiseledbookshelf</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 书架<br><code>game:bookshelf</code> | 1 | 未声明附加限制 |
| 产物 | 装饰书架<br><code>decobookshelf</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledbookshelf.json`

```json
[
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:chisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "1row1col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 1x1",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "1row1col",
        "material": "aged"
      }
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:chisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "1row2col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 1x2",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "1row2col",
        "material": "aged"
      }
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:chisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "2row1col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 2x1",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "2row1col",
        "material": "aged"
      }
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:chisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "2row2col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 2x2",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "2row2col",
        "material": "aged"
      }
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "truechisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "1row1col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 1x1 truechisel",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "1row1col",
        "material": "aged"
      }
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "truechisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "1row2col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 1x2 truechisel",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "1row2col",
        "material": "aged"
      }
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "truechisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "2row1col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 2x1 truechisel",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "2row1col",
        "material": "aged"
      }
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "truechisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:bookshelf",
        "attributes": {
          "type": "2row2col"
        },
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Bookshelf 2x2 truechisel",
    "output": {
      "type": "block",
      "code": "decobookshelf",
      "attributes": {
        "type": "2row2col",
        "material": "aged"
      }
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledchest - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 箱<br><code>game:chest-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledchestnerfed-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledchest - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:chest-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledchestnerfed-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledchest</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 箱<br><code>game:chest-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledchestnerfed-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledchest.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:chest-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledchestnerfed-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledchestbig - true - fromdeco</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 名称未汉化（见物品代码）<br><code>chiseledchestnerfed-east</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledchest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HHH
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledchestbig - true - fromdeco.json`

```json
{
  "ingredientPattern": "HHH",
  "ingredients": {
    "H": {
      "type": "block",
      "code": "chiseledchestnerfed-east",
      "quantity": 1
    }
  },
  "width": 3,
  "height": 1,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledchest-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledchestbig - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:trunk-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledchest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledchestbig - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:trunk-*",
      "quantity": 2
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledchest-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledchestbig</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:trunk-*</code> | 2 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledchest-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledchestbig.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:trunk-*",
      "quantity": 2
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledchest-east"
  }
}
```

</details>

</details>

<details><summary>装饰烟囱 · chiseledchimney - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:*claybrickchimney-*</code> | 1 | 未声明附加限制 |
| 产物 | 装饰烟囱<br><code>chiseledchimney</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledchimney - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:*claybrickchimney-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chimney",
  "output": {
    "type": "block",
    "code": "chiseledchimney"
  }
}
```

</details>

</details>

<details><summary>装饰烟囱 · chiseledchimney</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:*claybrickchimney-*</code> | 1 | 未声明附加限制 |
| 产物 | 装饰烟囱<br><code>chiseledchimney</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledchimney.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:*claybrickchimney-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chimney",
  "output": {
    "type": "block",
    "code": "chiseledchimney"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseleddisplaycase - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 展示柜<br><code>game:displaycase-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseleddisplaycase</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseleddisplaycase - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:displaycase-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Display Case",
  "output": {
    "type": "block",
    "code": "chiseleddisplaycase"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseleddisplaycase</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 展示柜<br><code>game:displaycase-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseleddisplaycase</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseleddisplaycase.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:displaycase-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseleddisplaycase"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledfirepit - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 木柴<br><code>game:firewood</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledfirepit-extinct</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledfirepit - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "item",
      "code": "game:firewood",
      "quantity": 4
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Firepit",
  "output": {
    "type": "block",
    "code": "chiseledfirepit-extinct"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledfirepit</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 木柴<br><code>game:firewood</code> | 4 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledfirepit-extinct</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledfirepit.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "item",
      "code": "game:firewood",
      "quantity": 4
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Firepit",
  "output": {
    "type": "block",
    "code": "chiseledfirepit-extinct"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledflowerpot - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:flowerpot-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledflowerpot-deco</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledflowerpot - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:flowerpot-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Flowerpot",
  "output": {
    "type": "block",
    "code": "chiseledflowerpot-deco"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledflowerpot</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:flowerpot-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledflowerpot-deco</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledflowerpot.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:flowerpot-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledflowerpot-deco"
  }
}
```

</details>

</details>

<details><summary>装饰熔炉 · chiseledforge - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 锻炉<br><code>game:forge</code> | 1 | 未声明附加限制 |
| 产物 | 装饰熔炉<br><code>chiseledforge</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledforge - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:forge",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Forge",
  "output": {
    "type": "block",
    "code": "chiseledforge"
  }
}
```

</details>

</details>

<details><summary>装饰熔炉 · chiseledforge</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 锻炉<br><code>game:forge</code> | 1 | 未声明附加限制 |
| 产物 | 装饰熔炉<br><code>chiseledforge</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledforge.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:forge",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledforge"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledoven - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 粘土烤炉<br><code>game:clayoven-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledoven-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledoven - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:clayoven-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Oven",
  "output": {
    "type": "block",
    "code": "chiseledoven-north"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledoven</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 粘土烤炉<br><code>game:clayoven-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledoven-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledoven.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:clayoven-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledoven-north"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledplanter - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:clayplanter-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledplanter-deco</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledplanter - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:clayplanter-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Planter",
  "output": {
    "type": "block",
    "code": "chiseledplanter-deco"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledplanter</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:clayplanter-*</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledplanter-deco</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledplanter.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:clayplanter-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledplanter-deco"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledshelf - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:shelf-normal-east</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledshelf - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:shelf-normal-east",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Shelf",
  "output": {
    "type": "block",
    "code": "chiseledshelf-normal-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledshelf</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:shelf-normal-east</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledshelf-normal-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledshelf.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:shelf-normal-east",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Self",
  "output": {
    "type": "block",
    "code": "chiseledshelf-normal-east"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledsign - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:sign-ground-north</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledsign-ground-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledsign - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:sign-ground-north",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledsign-ground-north"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledsign</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:sign-ground-north</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledsign-ground-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledsign.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:sign-ground-north",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledsign-ground-north"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledstoragevessel - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledstoragevessel-burned</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledstoragevessel - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:storagevessel-*-fired",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Vessel",
  "output": {
    "type": "block",
    "code": "chiseledstoragevessel-burned"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledstoragevessel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:storagevessel-*-fired</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledstoragevessel-burned</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledstoragevessel.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:storagevessel-*-fired",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledstoragevessel-burned"
  }
}
```

</details>

</details>

<details><summary>装饰桌子 · chiseledtable - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:table-*</code> | 1 | 未声明附加限制 |
| 产物 | 装饰桌子<br><code>table-chiseled</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledtable - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:table-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Table",
  "output": {
    "type": "block",
    "code": "table-chiseled"
  }
}
```

</details>

</details>

<details><summary>装饰桌子 · chiseledtable</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:table-*</code> | 1 | 未声明附加限制 |
| 产物 | 装饰桌子<br><code>table-chiseled</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledtable.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:table-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "table-chiseled"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledtoolrack - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:toolrack-north</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledtoolrack-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledtoolrack - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:toolrack-north",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Tool Rack",
  "output": {
    "type": "block",
    "code": "chiseledtoolrack-north"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiseledtoolrack</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 名称未汉化（见物品代码）<br><code>game:toolrack-north</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseledtoolrack-north</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledtoolrack.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:toolrack-north",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Tool Rack",
  "output": {
    "type": "block",
    "code": "chiseledtoolrack-north"
  }
}
```

</details>

</details>

<details><summary>装饰水源 · chiseledwatersource</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 手提木桶<br><code>game:woodbucket</code> | 1 | 未声明附加限制 |
| 产物 | 装饰水源<br><code>chiseledwatersource</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 手提木桶<br><code>game:woodbucket</code> | 1 | 未声明附加限制 |
| 产物 | 装饰水源<br><code>chiseledwatersource</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledwatersource.json`

```json
[
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:chisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:woodbucket",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Water Source",
    "output": {
      "type": "block",
      "code": "chiseledwatersource"
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "truechisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "block",
        "code": "game:woodbucket",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Decorative Water Source Truechisel",
    "output": {
      "type": "block",
      "code": "chiseledwatersource"
    }
  }
]
```

</details>

</details>

<details><summary>装饰栅栏 · chiseledwoodenfence - true</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:woodenfence-*</code> | 1 | 未声明附加限制 |
| 产物 | 装饰栅栏<br><code>chiseledwoodenfence</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledwoodenfence - true.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "truechisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:woodenfence-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Fence",
  "output": {
    "type": "block",
    "code": "chiseledwoodenfence"
  }
}
```

</details>

</details>

<details><summary>装饰栅栏 · chiseledwoodenfence</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:woodenfence-*</code> | 1 | 未声明附加限制 |
| 产物 | 装饰栅栏<br><code>chiseledwoodenfence</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiseledwoodenfence.json`

```json
{
  "ingredientPattern": "L\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "quantity": 1,
      "isTool": true
    },
    "H": {
      "type": "block",
      "code": "game:woodenfence-*",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 2,
  "name": "Decorative Chest",
  "output": {
    "type": "block",
    "code": "chiseledwoodenfence"
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chiselprojector</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>truechisel-*</code> | 1 | 工具 |
| 投入 H | 夜视面具<br><code>game:nightvisiondevice</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiselprojector-chiseled</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 1 | 工具 |
| 投入 H | 夜视面具<br><code>game:nightvisiondevice</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiselprojector-chiseled</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/chiselprojector.json`

```json
[
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "truechisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:nightvisiondevice",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Projector from True Chisel",
    "output": {
      "type": "block",
      "code": "chiselprojector-chiseled"
    }
  },
  {
    "ingredientPattern": "L\tH",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "game:chisel-*",
        "quantity": 1,
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "game:nightvisiondevice",
        "quantity": 1
      }
    },
    "width": 1,
    "height": 2,
    "name": "Projector from Chisel",
    "output": {
      "type": "block",
      "code": "chiselprojector-chiseled"
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · megapantograph</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 钢缩放仪<br><code>chiseltools:pantograph-steel</code> | 1 | 未声明附加限制 |
| 投入 H | 钢手刨<br><code>chiseltools:handplaner-steel</code> | 1 | 未声明附加限制 |
| 投入 W | 钢手楔<br><code>chiseltools:handwedge-steel</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseltools:megapantograph-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P	H	W
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 铁缩放仪<br><code>chiseltools:pantograph-iron</code> | 1 | 未声明附加限制 |
| 投入 H | 铁手刨<br><code>chiseltools:handplaner-iron</code> | 1 | 未声明附加限制 |
| 投入 W | 铁手楔<br><code>chiseltools:handwedge-iron</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseltools:megapantograph-iron</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P	H	W
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 陨铁缩放仪<br><code>chiseltools:pantograph-meteoriciron</code> | 1 | 未声明附加限制 |
| 投入 H | 陨铁手刨<br><code>chiseltools:handplaner-meteoriciron</code> | 1 | 未声明附加限制 |
| 投入 W | 陨铁手楔<br><code>chiseltools:handwedge-meteoriciron</code> | 1 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>chiseltools:megapantograph-meteoriciron</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P	H	W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/megapantograph.json`

```json
[
  {
    "ingredientPattern": "P\tH\tW",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "chiseltools:pantograph-steel",
        "quantity": 1
      },
      "H": {
        "type": "item",
        "code": "chiseltools:handplaner-steel",
        "quantity": 1
      },
      "W": {
        "type": "item",
        "code": "chiseltools:handwedge-steel",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "name": "Multigraph-Steel",
    "output": {
      "type": "item",
      "code": "chiseltools:megapantograph-steel"
    }
  },
  {
    "ingredientPattern": "P\tH\tW",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "chiseltools:pantograph-iron",
        "quantity": 1
      },
      "H": {
        "type": "item",
        "code": "chiseltools:handplaner-iron",
        "quantity": 1
      },
      "W": {
        "type": "item",
        "code": "chiseltools:handwedge-iron",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "name": "Multigraph-Iron",
    "output": {
      "type": "item",
      "code": "chiseltools:megapantograph-iron"
    }
  },
  {
    "ingredientPattern": "P\tH\tW",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "chiseltools:pantograph-meteoriciron",
        "quantity": 1
      },
      "H": {
        "type": "item",
        "code": "chiseltools:handplaner-meteoriciron",
        "quantity": 1
      },
      "W": {
        "type": "item",
        "code": "chiseltools:handwedge-meteoriciron",
        "quantity": 1
      }
    },
    "width": 3,
    "height": 1,
    "name": "Multigraph-meteoric",
    "output": {
      "type": "item",
      "code": "chiseltools:megapantograph-meteoriciron"
    }
  }
]
```

</details>

</details>

<details><summary>发光调色板 · palette-glow</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 64 | 未声明附加限制 |
| 投入 F | 金锭<br><code>game:ingot-gold</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 发光调色板<br><code>palette-glow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 32 | 未声明附加限制 |
| 投入 F | 金锭<br><code>game:ingot-gold</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 发光调色板<br><code>palette-glow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 金锭<br><code>game:ingot-gold</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 发光调色板<br><code>palette-glow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 64 | 未声明附加限制 |
| 投入 F | 银锭<br><code>game:ingot-silver</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 发光调色板<br><code>palette-glow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 32 | 未声明附加限制 |
| 投入 F | 银锭<br><code>game:ingot-silver</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 发光调色板<br><code>palette-glow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 银锭<br><code>game:ingot-silver</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 发光调色板<br><code>palette-glow</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/palette-glow.json`

```json
[
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "item",
        "code": "game:fruit-*",
        "quantity": 64
      },
      "F": {
        "type": "item",
        "code": "game:ingot-gold"
      }
    },
    "width": 3,
    "height": 1,
    "name": "Glowing Palette From Fruit",
    "output": {
      "type": "item",
      "code": "palette-glow"
    }
  },
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "item",
        "code": "game:vegetable-*",
        "quantity": 32
      },
      "F": {
        "type": "item",
        "code": "game:ingot-gold"
      }
    },
    "width": 3,
    "height": 1,
    "name": "Glow Palette From Veg",
    "output": {
      "type": "item",
      "code": "palette-glow"
    }
  },
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "item",
        "code": "game:ingot-gold"
      }
    },
    "width": 3,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "dye-white"
        },
        "requiresLitres": 10,
        "consumeContainer": false
      }
    },
    "name": "Glow Palette From Ink",
    "output": {
      "type": "item",
      "code": "palette-glow"
    }
  },
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "item",
        "code": "game:fruit-*",
        "quantity": 64
      },
      "F": {
        "type": "item",
        "code": "game:ingot-silver"
      }
    },
    "width": 3,
    "height": 1,
    "name": "Glowing Palette From Fruit Silver",
    "output": {
      "type": "item",
      "code": "palette-glow"
    }
  },
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "item",
        "code": "game:vegetable-*",
        "quantity": 32
      },
      "F": {
        "type": "item",
        "code": "game:ingot-silver"
      }
    },
    "width": 3,
    "height": 1,
    "name": "Glow Palette From Veg Silver",
    "output": {
      "type": "item",
      "code": "palette-glow"
    }
  },
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "item",
        "code": "game:ingot-silver"
      }
    },
    "width": 3,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "dye-white"
        },
        "requiresLitres": 10,
        "consumeContainer": false
      }
    },
    "name": "Glow Palette From Ink Silver",
    "output": {
      "type": "item",
      "code": "palette-glow"
    }
  }
]
```

</details>

</details>

<details><summary>乔纳斯调色板 · palette-light</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 标准调色板<br><code>chiseltools:palette-standard</code> | 1 | 未声明附加限制 |
| 投入 F | 白铜锭<br><code>game:ingot-cupronickel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:metalplate-*</code> | 8 | 未声明附加限制 |
| 投入 C | 蜡烛<br><code>game:candle</code> | 8 | 未声明附加限制 |
| 投入 Q | 白水晶<br><code>game:clearquartz</code> | 16 | 未声明附加限制 |
| 产物 | 乔纳斯调色板<br><code>palette-light</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PF_	MCQ
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 标准调色板<br><code>chiseltools:palette-standard</code> | 1 | 未声明附加限制 |
| 投入 F | 白铜锭<br><code>game:ingot-cupronickel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:metalplate-*</code> | 8 | 未声明附加限制 |
| 投入 C | 蜡烛<br><code>game:candle</code> | 8 | 未声明附加限制 |
| 投入 Q | 白水晶<br><code>game:clearquartz</code> | 16 | 未声明附加限制 |
| 产物 | 乔纳斯调色板<br><code>palette-light</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PF_	MCQ
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 标准调色板<br><code>chiseltools:palette-standard</code> | 1 | 未声明附加限制 |
| 投入 F | 白铜锭<br><code>game:ingot-cupronickel</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:metalplate-*</code> | 8 | 未声明附加限制 |
| 投入 C | 蜡烛<br><code>game:candle</code> | 8 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:glassslab-*</code> | 16 | 未声明附加限制 |
| 产物 | 乔纳斯调色板<br><code>palette-light</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PF_	MCQ
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/palette-light.json`

```json
[
  {
    "ingredientPattern": "PF_\tMCQ",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "chiseltools:palette-standard",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:ingot-cupronickel"
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-*",
        "quantity": 8
      },
      "C": {
        "type": "item",
        "code": "game:candle",
        "quantity": 8
      },
      "Q": {
        "type": "item",
        "code": "game:clearquartz",
        "quantity": 16
      }
    },
    "width": 3,
    "height": 2,
    "name": "Lighting Palette From Parts",
    "output": {
      "type": "item",
      "code": "palette-light"
    }
  },
  {
    "ingredientPattern": "PF_\tMCQ",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "chiseltools:palette-standard",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:ingot-cupronickel"
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-*",
        "quantity": 8
      },
      "C": {
        "type": "item",
        "code": "game:candle",
        "quantity": 8
      },
      "Q": {
        "type": "item",
        "code": "game:clearquartz",
        "quantity": 16
      }
    },
    "width": 3,
    "height": 2,
    "name": "Lighting Palette From Parts",
    "output": {
      "type": "item",
      "code": "palette-light"
    }
  },
  {
    "ingredientPattern": "PF_\tMCQ",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "chiseltools:palette-standard",
        "quantity": 1
      },
      "F": {
        "type": "item",
        "code": "game:ingot-cupronickel"
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-*",
        "quantity": 8
      },
      "C": {
        "type": "item",
        "code": "game:candle",
        "quantity": 8
      },
      "Q": {
        "type": "block",
        "code": "game:glassslab-*",
        "quantity": 16
      }
    },
    "width": 3,
    "height": 2,
    "name": "Lighting Palette From Slabs",
    "output": {
      "type": "item",
      "code": "palette-light"
    }
  }
]
```

</details>

</details>

<details><summary>标准调色板 · palette</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:fruit-*</code> | 64 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 标准调色板<br><code>palette-standard</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 变体材料（按代码匹配）<br><code>game:vegetable-*</code> | 32 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 标准调色板<br><code>palette-standard</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 生石灰<br><code>game:quicklime</code> | 4 | 未声明附加限制 |
| 投入 M | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 F | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 标准调色板<br><code>palette-standard</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CMF
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/palette.json`

```json
[
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "item",
        "code": "game:fruit-*",
        "quantity": 64
      },
      "F": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "width": 3,
    "height": 1,
    "name": "Palette From Fruit",
    "output": {
      "type": "item",
      "code": "palette-standard"
    }
  },
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "item",
        "code": "game:vegetable-*",
        "quantity": 32
      },
      "F": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "width": 3,
    "height": 1,
    "name": "Palette From Veg",
    "output": {
      "type": "item",
      "code": "palette-standard"
    }
  },
  {
    "ingredientPattern": "CMF",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:quicklime",
        "quantity": 4
      },
      "M": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "F": {
        "type": "item",
        "code": "game:plank-*"
      }
    },
    "width": 3,
    "height": 1,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "dye-white"
        },
        "requiresLitres": 10,
        "consumeContainer": false
      }
    },
    "name": "Palette From Ink",
    "output": {
      "type": "item",
      "code": "palette-standard"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · pantograph</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>simplepantograph-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuthbronze', 'tinbronze', 'blackbronze', 'steel', 'meteoriciron', 'iron'] |
| 产物 | 变体材料（按代码匹配）<br><code>pantograph-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>pantograph-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuthbronze', 'tinbronze', 'blackbronze', 'steel', 'meteoriciron', 'iron'] |
| 产物 | 变体材料（按代码匹配）<br><code>doortool-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 雕凿门工具<br><code>doortool-*</code> | 未声明；按配方类型判定 | 允许变体：['bismuthbronze', 'tinbronze', 'blackbronze', 'steel', 'meteoriciron', 'iron'] |
| 产物 | 变体材料（按代码匹配）<br><code>simplepantograph-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/pantograph.json`

```json
[
  {
    "ingredientPattern": "P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "simplepantograph-*",
        "name": "metal",
        "allowedVariants": [
          "bismuthbronze",
          "tinbronze",
          "blackbronze",
          "steel",
          "meteoriciron",
          "iron"
        ]
      }
    },
    "width": 1,
    "height": 1,
    "name": "Simple Pantograph To Regular",
    "output": {
      "type": "item",
      "code": "pantograph-{metal}"
    }
  },
  {
    "ingredientPattern": "P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "pantograph-*",
        "name": "metal",
        "allowedVariants": [
          "bismuthbronze",
          "tinbronze",
          "blackbronze",
          "steel",
          "meteoriciron",
          "iron"
        ]
      }
    },
    "width": 1,
    "height": 1,
    "name": "Regular Pantograph To Door Tool",
    "output": {
      "type": "item",
      "code": "doortool-{metal}"
    }
  },
  {
    "ingredientPattern": "P",
    "ingredients": {
      "P": {
        "type": "item",
        "code": "doortool-*",
        "name": "metal",
        "allowedVariants": [
          "bismuthbronze",
          "tinbronze",
          "blackbronze",
          "steel",
          "meteoriciron",
          "iron"
        ]
      }
    },
    "width": 1,
    "height": 1,
    "name": "Door Tool to Simple Pantograph",
    "output": {
      "type": "item",
      "code": "simplepantograph-{metal}"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · qpchisel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 允许变体：['blackbronze', 'tinbronze', 'bismuthbronze', 'iron', 'meteoriciron'] |
| 投入 P | 变体材料（按代码匹配）<br><code>pantograph-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>truechisel-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/qpchisel.json`

```json
{
  "ingredientPattern": "LP",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-*",
      "name": "metal",
      "allowedVariants": [
        "blackbronze",
        "tinbronze",
        "bismuthbronze",
        "iron",
        "meteoriciron"
      ]
    },
    "P": {
      "type": "item",
      "code": "pantograph-*",
      "isTool": true
    }
  },
  "width": 2,
  "height": 1,
  "name": "The True Chisel",
  "output": {
    "type": "item",
    "code": "truechisel-{metal}"
  }
}
```

</details>

</details>

<details><summary>真正的凿子 · truechisel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 钢凿子<br><code>game:chisel-steel</code> | 1 | 未声明附加限制 |
| 投入 H | 钢锤<br><code>game:hammer-steel</code> | 1 | 未声明附加限制 |
| 产物 | 真正的凿子<br><code>truechisel-steel</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
L	L	H
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/grid/truechisel.json`

```json
{
  "ingredientPattern": "L\tL\tH",
  "ingredients": {
    "L": {
      "type": "item",
      "code": "game:chisel-steel",
      "quantity": 1
    },
    "H": {
      "type": "item",
      "code": "game:hammer-steel",
      "quantity": 1
    }
  },
  "width": 1,
  "height": 3,
  "name": "The True Chisel",
  "output": {
    "type": "item",
    "code": "truechisel-steel"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · doortool</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>doortool-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/doortool.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "bismuthbronze",
      "tinbronze",
      "blackbronze",
      "steel",
      "meteoriciron",
      "iron"
    ]
  },
  "pattern": [
    [
      "#####_#####",
      "#___#______",
      "#####_#####"
    ]
  ],
  "name": "Door tool-{metal}",
  "code": "Door tool-{metal}",
  "output": {
    "type": "item",
    "code": "doortool-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · handplaner</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>handplaner-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/handplaner.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "iron",
      "meteoriciron",
      "steel",
      "blackbronze",
      "tinbronze",
      "bismuthbronze",
      "copper"
    ]
  },
  "pattern": [
    [
      "________#####__",
      "_############__",
      "________#####__"
    ]
  ],
  "name": "Hand Planer-{metal}",
  "code": "Hand Planer-{metal}",
  "output": {
    "type": "item",
    "code": "handplaner-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · handwedge</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>handwedge-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/handwedge.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "iron",
      "meteoriciron",
      "steel",
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "copper"
    ]
  },
  "pattern": [
    [
      "________#######",
      "_##############",
      "________#######"
    ]
  ],
  "name": "Hand Wedge-{metal}",
  "code": "Hand Wedge-{metal}",
  "output": {
    "type": "item",
    "code": "handwedge-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · laddermaker</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>laddermaker-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/laddermaker.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "iron",
      "meteoriciron",
      "steel"
    ]
  },
  "pattern": [
    [
      "________#####__",
      "_########_#_#__",
      "________#####__"
    ]
  ],
  "name": "Ladder Maker-{metal}",
  "code": "Ladder Maker-{metal}",
  "output": {
    "type": "item",
    "code": "laddermaker-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · locktool</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>locktool-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/locktool.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "bismuthbronze",
      "tinbronze",
      "blackbronze",
      "steel",
      "meteoriciron",
      "iron"
    ]
  },
  "pattern": [
    [
      "_####_#####",
      "#_###__#_#_",
      "_####_#####"
    ]
  ],
  "name": "Lock Tool-{metal}",
  "code": "Lock Tool-{metal}",
  "output": {
    "type": "item",
    "code": "locktool-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · paintbrush</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>paintbrush-{metal}</code> | 2 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/paintbrush.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "iron",
      "meteoriciron",
      "steel"
    ]
  },
  "pattern": [
    [
      "________##",
      "_########_",
      "_##_____##",
      "__########",
      "_##_______"
    ]
  ],
  "name": "Paint Brush Handles (x2)-{metal}",
  "code": "Paint Brush Handles (x2)-{metal}",
  "output": {
    "type": "item",
    "code": "paintbrush-{metal}",
    "stacksize": 2
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · paintscraper</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>paintscraper-{metal}</code> | 2 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/paintscraper.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "iron",
      "meteoriciron",
      "steel",
      "tinbronze",
      "bismuthbronze",
      "blackbronze",
      "copper"
    ]
  },
  "pattern": [
    [
      "________##",
      "_#########",
      "_##_____##",
      "_#########",
      "_##_______"
    ]
  ],
  "name": "Paint Scrapers (x2)-{metal}",
  "code": "Paint Scrapers (x2)-{metal}",
  "output": {
    "type": "item",
    "code": "paintscraper-{metal}",
    "stacksize": 2
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · pantograph</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>pantograph-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/pantograph.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "bismuthbronze",
      "tinbronze",
      "blackbronze",
      "steel",
      "meteoriciron",
      "iron"
    ]
  },
  "pattern": [
    [
      "#####_#####",
      "_#_#___#_#_",
      "#####_#####"
    ]
  ],
  "name": "Pantograph-{metal}",
  "code": "Pantograph-{metal}",
  "output": {
    "type": "item",
    "code": "pantograph-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · pathmaker</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>pathmaker-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/pathmaker.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "iron",
      "meteoriciron",
      "steel",
      "tinbronze",
      "blackbronze",
      "bismuthbronze"
    ]
  },
  "pattern": [
    [
      "________#####__",
      "_########_#_#__",
      "________#####__"
    ]
  ],
  "name": "Path Maker-{metal}",
  "code": "Path Maker-{metal}",
  "output": {
    "type": "item",
    "code": "pathmaker-{metal}"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · simple-pantograph</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>simplepantograph-{metal}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/chiseltools/recipes/smithing/simple-pantograph.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-*",
    "name": "metal",
    "allowedVariants": [
      "copper",
      "bismuthbronze",
      "tinbronze",
      "blackbronze",
      "steel",
      "meteoriciron",
      "iron"
    ]
  },
  "pattern": [
    [
      "#####_#####",
      "_#_#___#_#_",
      "#####_#####"
    ]
  ],
  "name": "Simple Pantograph-{metal}",
  "code": "Simple Pantograph-{metal}",
  "output": {
    "type": "item",
    "code": "simplepantograph-{metal}"
  }
}
```

</details>

</details>
<!-- generated:end -->
