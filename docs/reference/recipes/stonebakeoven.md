<!-- generated:start -->
# 石砌烤炉：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：石制烤炉


石制烤炉

“当人类用树枝和石头生火时，只是希望有一天能用这样的炉子烤面包。”

准备工作

本模组最基础的烤炉只需要 3 块铜板和任意类型的石头（岩石、磨制岩石、圆石和石砖）。

制作

[handbooksearch://Oven Baking Space] 1 个烤炉烘焙空间

[handbooksearch://Oven Heat Distribution] 1 个烤炉均热器

[handbooksearch://Oven Heat Source] 1 个烤炉热源

搭建

要制作最基本的烤炉，先放置烤炉热源，然后在烤炉热源的左侧或右侧放置烤炉均热器，再在烤炉均热器前方放置烤炉烘焙空间。

这是最基本的烤炉布置方法，还可以进一步扩展（更多信息请参阅 Mod DB 页面或以下简略指南）。

用法

烤炉的工作原理是从烤炉热源获取热量，并通过烤炉均热器将热量传递到烤炉烘焙空间。具体做法是将可燃材料放入烤炉热源，再用火把点燃。最后将想要烘烤的物品放到烤炉烘焙空间上，就像使用黏土烤炉一样，然后等待烘烤完成。

布局变化

你可以尝试几种不同的布局，唯一的限制是烤炉烘焙空间离热源越远温度越低，但从中央烤炉热源向外约 4 个方块的距离内仍能保持 300℃。

请尝试添加额外的烤炉均热器和烤炉烘焙空间。

注意——除非你要制作一个能喂饱一千个炽天使的烤炉，否则整套装置只需要 1 个烤炉热源。

问与答

为什么用它而不用黏土烤炉？

经测试，这种烤炉烹饪更快；在大型烘焙任务中，一旦达到温度，燃料消耗也更少（但会被更高的材料与科技成本抵消）。

为什么设计得这么简单？

烤炉的设计之所以如此简单，是为了让玩家可以凿刻周围方块，并按自己的喜好建造烤炉外壳。

它能烘烤模组物品吗？

该烤炉（至少在测试中）允许你烘烤任何可以在原版黏土烤炉中正常烘烤的物品。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · brick</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:stonebricks-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 4 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovenbakingtopbrick-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
FMF
_R_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 2 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:stonebricks-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 8 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovencontrollerbrick-{rock}-extinct-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HRC
FMF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:stonebricks-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillbrick-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
R_R
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:stonebricks-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillbrickextra-corner-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
_RR
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:stonebricks-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillbrickextra-endcap-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
_R_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:stonebricks-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillbrickextra-tjunction-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
RRR
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:polishedrockslab-*-down-free</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:chutesection-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:stonebricks-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'suevite'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 8 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovencookingtopbrick-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
FSM
_R_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "HPC,FMF,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "R": {
        "type": "block",
        "code": "game:stonebricks-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "ovenbakingtopbrick-{rock}"
    }
  },
  {
    "ingredientPattern": "HRC,FMF",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper",
        "quantity": 2
      },
      "R": {
        "type": "block",
        "code": "game:stonebricks-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovencontrollerbrick-{rock}-extinct-east"
    }
  },
  {
    "ingredientPattern": "HPC,R_R",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:stonebricks-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillbrick-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,_RR",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:stonebricks-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillbrickextra-corner-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:stonebricks-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillbrickextra-endcap-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,RRR",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:stonebricks-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillbrickextra-tjunction-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,FSM,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:polishedrockslab-*-down-free",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "S": {
        "type": "item",
        "code": "game:chutesection-copper"
      },
      "R": {
        "type": "block",
        "code": "game:stonebricks-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "suevite"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "ovencookingtopbrick-{rock}"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · cobble</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:cobblestone-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 4 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovenbakingtopcobble-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
FMF
_R_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 2 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:cobblestone-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 8 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovencontrollercobble-{rock}-extinct-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HRC
FMF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:cobblestone-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillcobble-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
R_R
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:cobblestone-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillcobbleextra-corner-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
_RR
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:cobblestone-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillcobbleextra-endcap-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
_R_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:cobblestone-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillcobbleextra-tjunction-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
RRR
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:polishedrockslab-*-down-free</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:chutesection-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:cobblestone-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 8 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovencookingtopcobble-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
FSM
_R_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "HPC,FMF,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "R": {
        "type": "block",
        "code": "game:cobblestone-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "ovenbakingtopcobble-{rock}"
    }
  },
  {
    "ingredientPattern": "HRC,FMF",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper",
        "quantity": 2
      },
      "R": {
        "type": "block",
        "code": "game:cobblestone-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovencontrollercobble-{rock}-extinct-east"
    }
  },
  {
    "ingredientPattern": "HPC,R_R",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:cobblestone-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillcobble-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,_RR",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:cobblestone-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillcobbleextra-corner-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:cobblestone-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillcobbleextra-endcap-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,RRR",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:cobblestone-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillcobbleextra-tjunction-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,FSM,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:polishedrockslab-*-down-free",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "S": {
        "type": "item",
        "code": "game:chutesection-copper"
      },
      "R": {
        "type": "block",
        "code": "game:cobblestone-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "ovencookingtopcobble-{rock}"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · plain</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rock-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 4 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovenbakingtopplain-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
FMF
_R_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 2 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rock-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 8 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovencontrollerplain-{rock}-extinct-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HRC
FMF
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rock-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillplain-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
R_R
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rock-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillplainextra-corner-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
_RR
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rock-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillplainextra-endcap-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
_R_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rock-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 产物 | 变体材料（按代码匹配）<br><code>ovengrillplainextra-tjunction-{rock}-cold-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
RRR
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:polishedrockslab-*-down-free</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 M | 铜板<br><code>game:metalplate-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:chutesection-copper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rock-*</code> | 未声明；按配方类型判定 | 允许变体：['andesite', 'chalk', 'chert', 'conglomerate', 'limestone', 'claystone', 'granite', 'sandstone', 'shale', 'basalt', 'peridotite', 'phyllite', 'slate', 'bauxite', 'kimberlite', 'suevite', 'whitemarble', 'redmarble', 'greenmarble'] |
| 投入 F | 耐火粘土<br><code>game:clay-fire</code> | 8 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>ovencookingtopplain-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPC
FSM
_R_
```

<details><summary>技术说明：完整配方</summary>


```json
[
  {
    "ingredientPattern": "HPC,FMF,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "R": {
        "type": "block",
        "code": "game:rock-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 4
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "ovenbakingtopplain-{rock}"
    }
  },
  {
    "ingredientPattern": "HRC,FMF",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper",
        "quantity": 2
      },
      "R": {
        "type": "block",
        "code": "game:rock-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovencontrollerplain-{rock}-extinct-east"
    }
  },
  {
    "ingredientPattern": "HPC,R_R",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:rock-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillplain-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,_RR",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:rock-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillplainextra-corner-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:rock-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillplainextra-endcap-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,RRR",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:rockpolished-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "R": {
        "type": "block",
        "code": "game:rock-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "ovengrillplainextra-tjunction-{rock}-cold-east"
    }
  },
  {
    "ingredientPattern": "HPC,FSM,_R_",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:chisel-*",
        "isTool": true
      },
      "P": {
        "type": "block",
        "code": "game:polishedrockslab-*-down-free",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "M": {
        "type": "item",
        "code": "game:metalplate-copper"
      },
      "S": {
        "type": "item",
        "code": "game:chutesection-copper"
      },
      "R": {
        "type": "block",
        "code": "game:rock-*",
        "name": "rock",
        "allowedVariants": [
          "andesite",
          "chalk",
          "chert",
          "conglomerate",
          "limestone",
          "claystone",
          "granite",
          "sandstone",
          "shale",
          "basalt",
          "peridotite",
          "phyllite",
          "slate",
          "bauxite",
          "kimberlite",
          "suevite",
          "whitemarble",
          "redmarble",
          "greenmarble"
        ]
      },
      "F": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 8
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "ovencookingtopplain-{rock}"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
