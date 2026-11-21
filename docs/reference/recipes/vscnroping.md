<!-- generated:start -->
# 绳索交互：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：套索与捆绑

来源：`assets/vscnroping/config/handbook/roping.json`。

制作

4根绳子或4条同材质金属链，加1根木棍制作普通套索；再加1张原色皮革制作稳固版。支持铜、锡青铜、铋青铜、黑青铜、铁、陨铁和钢，不支持金银。

耐久与套中率

稳固版套中率从绳索25%递进到钢链100%；普通版为对应稳固版的60%。普通金属耐久参考原版同材质金属斧。大型目标最多降低3个百分点，实际概率限制在5%至100%。

投掷与状态

左键投掷最远8格，绳长8格，冷却1秒。普通绳索每次消耗2点耐久，稳固绳索1点，金属套索2点；未命中也消耗。实际命中生物造成一次0.1点基础钝击伤害，不击退，未套住也造成伤害；躲开或被方块遮挡时无伤害。lasso为手持拖拽状态；bound为捆绑；hogtied为反绑并锁定移动控制、跳跃和交互。

绑定、拴点与恢复

对已套中目标右键捆绑，潜行右键反绑。手持连接时右键方块或其他实体设置拴点，右键空处恢复跟随主人。主人普通右键释放会返还原套索和剩余耐久；潜行右键且快捷栏为空可将bound或hogtied恢复为手持套索。主人切换快捷栏、离线或死亡会转为bound；离线或死亡产生的绑定不能由原主人取回。

拖拽与挣脱

普通绳索动物在lasso且绳索接近绷紧时每秒判定一次挣脱；生命值越低、体型越小概率越低，稳固版再降低35%，成功后套索损坏且不返还。绳索连续10次检查无法把受阻目标拉回绳长范围内时直接断裂。金属套索不进行动物挣脱判定，拖拽不消耗耐久，卡墙或高障碍不会导致断裂。玩家在连接后5秒内手持对应小刀或斧头按默认G键一次即可挣脱；绳索、铜、锡青铜、铋青铜、黑青铜、铁、陨铁、钢分别消耗100、200、300、400、500、600、700、800点套索耐久，耐久不足时套索损坏，否则返还已损耗套索。

切断

其他玩家需持续右键3秒并持正确工具：绳索用石刀；铜链用铜斧；三种青铜链用青铜斧；铁、陨铁链用铁斧；钢链用钢斧。切断成功消耗工具耐久，套索不返还。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · lasso-metal</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:metalchain-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'iron', 'meteoriciron', 'steel'] |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>vscnroping:lasso-metal-{metal}-basic</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC
CC
S_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 C | 变体材料（按代码匹配）<br><code>game:metalchain-*</code> | 未声明；按配方类型判定 | 允许变体：['copper', 'tinbronze', 'bismuthbronze', 'blackbronze', 'iron', 'meteoriciron', 'steel'] |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>vscnroping:lasso-metal-{metal}-sturdy</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
CC
CC
LS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vscnroping/recipes/grid/lasso-metal.json`

```json
[
  {
    "ingredientPattern": "CC,CC,S_",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:metalchain-*",
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
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "item",
      "code": "vscnroping:lasso-metal-{metal}-basic"
    }
  },
  {
    "ingredientPattern": "CC,CC,LS",
    "ingredients": {
      "C": {
        "type": "item",
        "code": "game:metalchain-*",
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
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "item",
      "code": "vscnroping:lasso-metal-{metal}-sturdy"
    }
  }
]
```

</details>

</details>

<details><summary>绳索套索、稳固绳索套索 · lasso-rope</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 绳索套索<br><code>vscnroping:lasso-rope-basic</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RR
RR
S_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 稳固绳索套索<br><code>vscnroping:lasso-rope-sturdy</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RR
RR
LS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/vscnroping/recipes/grid/lasso-rope.json`

```json
[
  {
    "ingredientPattern": "RR,RR,S_",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "item",
      "code": "vscnroping:lasso-rope-basic"
    }
  },
  {
    "ingredientPattern": "RR,RR,LS",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 2,
    "height": 3,
    "output": {
      "type": "item",
      "code": "vscnroping:lasso-rope-sturdy"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
