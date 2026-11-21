<!-- generated:start -->
# 阿基米德螺旋提水：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：阿基米德螺旋泵指南

来源：`assets/archimedes_screw/config/handbook/101-overview.json`。

阿基米德螺旋泵

一种用于提升水的动力泵。

阿基米德螺旋泵是一种垂直多方块结构，在进水口抽水，并在出水口产生单个水源方块。只要结构有效、有机械动力且进水口保持在水里，水源就会维持。如果螺旋泵失去动力、结构损坏或进水口离开水面，产生的水源方块就会被移除。

组装基础

从下往上建造：在底部放置端盖以形成进水口，在其上方堆叠直螺旋泵段，并在顶部放置端盖以形成出水口。有效的结构需要底部一个进水口、顶部一个出水口，并且它们之间只有直段。进水口可以无水放置，但只有进水口处有水时螺旋泵才会运行。你可以右键点击任何阿基米德螺旋泵部件来查看结构的当前状态。机械动力可以从结构的顶部或底部输入。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>水阿基米德螺旋泵端盖 · waterarchimedesscrew-ported</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 X | 铅板<br><code>game:metalplate-lead</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铅管段<br><code>archimedes_screw:chutesection-lead</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 水阿基米德螺旋泵端盖<br><code>archimedes_screw:water-archimedesscrew-ported-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
H_
X_
CS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/archimedes_screw/recipes/grid/waterarchimedesscrew-ported.json`

```json
{
  "ingredientPattern": "H_,X_,CS",
  "ingredients": {
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 20
    },
    "S": {
      "type": "item",
      "code": "game:shears-*",
      "isTool": true,
      "toolDurabilityCost": 20
    },
    "X": {
      "type": "item",
      "code": "game:metalplate-lead"
    },
    "C": {
      "type": "item",
      "code": "archimedes_screw:chutesection-lead"
    }
  },
  "width": 2,
  "height": 3,
  "output": {
    "type": "block",
    "code": "archimedes_screw:water-archimedesscrew-ported-north",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>水阿基米德螺旋泵 · waterarchimedesscrew-straight</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:shears-*</code> | 未声明；按配方类型判定 | 工具；耐久消耗：20 |
| 投入 X | 铅板<br><code>game:metalplate-lead</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 铅管段<br><code>archimedes_screw:chutesection-lead</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 水阿基米德螺旋泵<br><code>archimedes_screw:water-archimedesscrew-straight</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HS
X_
C_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/archimedes_screw/recipes/grid/waterarchimedesscrew-straight.json`

```json
{
  "ingredientPattern": "HS,X_,C_",
  "ingredients": {
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true,
      "toolDurabilityCost": 20
    },
    "S": {
      "type": "item",
      "code": "game:shears-*",
      "isTool": true,
      "toolDurabilityCost": 20
    },
    "X": {
      "type": "item",
      "code": "game:metalplate-lead"
    },
    "C": {
      "type": "item",
      "code": "archimedes_screw:chutesection-lead"
    }
  },
  "width": 2,
  "height": 3,
  "output": {
    "type": "block",
    "code": "archimedes_screw:water-archimedesscrew-straight",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>铅管段 · chutesection-lead</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 铅管段<br><code>archimedes_screw:chutesection-lead</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/archimedes_screw/recipes/smithing/chutesection-lead.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:ingot-lead"
  },
  "pattern": [
    [
      "#####",
      "#___#",
      "#___#",
      "#___#",
      "#####"
    ],
    [
      "#####",
      "#___#",
      "#___#",
      "#___#",
      "#####"
    ]
  ],
  "name": "chutesection",
  "output": {
    "type": "item",
    "code": "archimedes_screw:chutesection-lead"
  },
  "code": "chutesection-lead"
}
```

</details>

</details>
<!-- generated:end -->
