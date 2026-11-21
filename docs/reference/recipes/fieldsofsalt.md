<!-- generated:start -->
# 盐田：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：盐领域：蒸发

来源：`assets/fieldsofsalt/config/handbook/evaporation.json`。

盐的蒸发

烘干池

蒸发是最简单的过程之一，可以让你毫不费力地获得资源。但同时也是最耗时的过程之一，需要数天或数周的时间才能取得成果。因此，要想获得最大的收益，就必须使用完全覆盖着蒸发池的巨大区域。由于蒸发池经常被用来生产食盐，因此这些地方被称为 “盐田”。

要开始用海水制盐，你需要蒸发池。你可以使用坚固的抛光石材作为边框，并铺设抛光石板的底部来建造蒸发池。接下来，你需要用 [handbook://item-fieldsofsalt:pondtemplate] 模板检查一切，池塘就准备好了！

但用水桶不断注水似乎相当困难，因此可以使用通道系统直接从蓄水池注水。

放置一个 [handbook://block-fieldsofsalt:source-north] 水闸来过滤杂物和生物，然后将水闸的 [handbook://block-fieldsofsalt:channel-ns] 通道 引入池塘的 [handbook://block-fieldsofsalt:connector-granite-ns] 沟槽中。现在，你的池塘里就会经常充满海水了。

等待一段时间后，你可以看到沉淀物正在底部聚集。现在你需要用东西把它刮掉，很可能一把锄头就足够了。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>盐 · salt</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 盐<br><code>game:salt</code> | 1 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fieldsofsalt/recipes/evaporationpond/salt.json`

```json
{
  "input": {
    "code": "game:saltwaterportion",
    "type": "item",
    "litres": 2
  },
  "output": {
    "code": "game:salt",
    "type": "item",
    "quantity": 1
  },
  "outputTexture": {
    "base": "game:block/stone/rock/halite1"
  },
  "evaporationTime": 24
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · channel</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plankslab-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>channel-ns</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
P_P
PSP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fieldsofsalt/recipes/grid/channel.json`

```json
{
  "ingredientPattern": "P_P,PSP",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:plank-*"
    },
    "S": {
      "type": "block",
      "code": "game:plankslab-*"
    }
  },
  "width": 3,
  "height": 2,
  "output": {
    "type": "block",
    "code": "channel-ns",
    "quantity": 2
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · connector</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 变体材料（按代码匹配）<br><code>game:rockpolished-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 变体材料（按代码匹配）<br><code>game:chisel-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 产物 | 变体材料（按代码匹配）<br><code>connector-{rock}-ns</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HS_
CPP
R__
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fieldsofsalt/recipes/grid/connector.json`

```json
{
  "ingredientPattern": "HS_,CPP,R__",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:plank-*"
    },
    "R": {
      "name": "rock",
      "type": "block",
      "code": "game:rockpolished-*"
    },
    "C": {
      "type": "item",
      "code": "game:chisel-*",
      "isTool": true
    },
    "H": {
      "type": "item",
      "code": "game:hammer-*",
      "isTool": true
    },
    "S": {
      "type": "item",
      "code": "game:saw-*",
      "isTool": true
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "connector-{rock}-ns",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>蒸发池（模板） · pondtemplate</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:paper-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 蒸发池连接器<br><code>connector-*</code> | 0 | 未声明附加限制 |
| 投入 B | 木炭<br><code>game:charcoal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蒸发池（模板）<br><code>pondtemplate</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PB
C_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fieldsofsalt/recipes/grid/pondtemplate.json`

```json
{
  "ingredientPattern": "PB,C_",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:paper-*"
    },
    "C": {
      "type": "block",
      "code": "connector-*",
      "quantity": 0
    },
    "B": {
      "type": "item",
      "code": "game:charcoal"
    }
  },
  "width": 2,
  "height": 2,
  "output": {
    "type": "item",
    "code": "pondtemplate",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · source</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:plankslab-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>source-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
TTT
P_P
PSP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fieldsofsalt/recipes/grid/source.json`

```json
{
  "ingredientPattern": "TTT,P_P,PSP",
  "ingredients": {
    "P": {
      "type": "item",
      "code": "game:plank-*"
    },
    "S": {
      "type": "block",
      "code": "game:plankslab-*"
    },
    "T": {
      "type": "item",
      "code": "game:stick"
    }
  },
  "width": 3,
  "height": 3,
  "output": {
    "type": "block",
    "code": "source-north",
    "quantity": 1
  }
}
```

</details>

</details>
<!-- generated:end -->
