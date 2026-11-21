<!-- generated:start -->
# 蜂箱与养蜂：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：养蜂入门 - 来自金色蜂巢

来源：`assets/fromgoldencombs/config/handbook/FGC01-fromgoldencombsguide.json`。

"小小蜜蜂多忙碌，

每时每刻不虚度，

采得百花成蜜后，

为谁辛苦为谁甜？"

- 艾萨克·瓦茨

《来自金色蜂巢》是一个增强《Vintage Story》中养蜂玩法的模组。它引入了两种新型蜂巢：陶瓷蜂巢和朗斯特罗斯蜂巢。每种蜂巢都有其独特的优势，并能比原版蜂巢产出更多的蜂蜜。当前版本的唯一缺点是，这些蜂巢无法像原版蜂巢那样自然繁殖蜂群。这是为了确保原版蜂巢仍然有其存在的价值。

养蜂的历史可以追溯到至少一万年前，这也是已知最早的野生蜂巢采集描绘。人类尝试了许多方法驯养蜜蜂，其中陶罐蜂巢出现在大约九千年前。在《Vintage Story》中，你的高级养蜂之旅也将从这里开始。

陶瓷蜂巢由两部分组成，第一部分是 [handbook://block-fromgoldencombs:ceramicbroodpot-notop] 育雏罐。育雏罐是蜂巢的基础，将成为蜜蜂的新家。第二部分是 [handbook://block-fromgoldencombs:hivetop-empty] 蜜罐，它放置在育雏罐顶部，是蜜蜂储存蜂蜜的地方。两者结合后，将成为无需破坏蜂巢即可获取蜂蜜的永久蜜源。

制作陶瓷蜂巢的第一步是采集黏土。你可以使用蓝黏土或火黏土，通过黏土成型工艺制作蜂巢的两个部分。你将得到一个 [handbook://block-fromgoldencombs:rawceramichive] 未烧制的育雏罐和一个 [handbook://block-fromgoldencombs:hivetop-raw] 未烧制的蜜罐，然后将它们放入坑窑中烧制。烧制完成后，它们就可以使用了！

注意：烧制后的育雏罐无法放入普通物品栏。你需要一个空的背包槽位（Ctrl+1-4）才能拾取它。

现在你有了育雏罐和蜜罐，将育雏罐放置在你想要的位置。和原版蜂巢一样，它们需要附近有花朵才能产出蜂蜜。此外，你必须在蜂巢顶部放置一个 [handbook://block-fromgoldencombs:hivetop-empty] 空的蜜罐供蜜蜂填充。

当然，没有蜜蜂就不会有蜂蜜。你需要通过常规方式获得一个已居住的蜂巢，然后直接与烧制好的育雏罐互动，将蜂群放入其中。这会消耗掉已居住的蜂巢。恭喜！你的陶瓷蜂巢现在可以为你生产蜂蜜了！当蜜罐顶部出现黄色蜡环时，表示可以收获了。

收获蜜罐很简单。取下蜜罐，放在地上，用小刀刮取。你会得到蜂蜜，蜜罐也会变空。将它放回蜂巢上，就可以继续使用了。除了比原版蜂巢更方便外，它们的平均蜂蜜产量也更高。

记住：陶瓷蜂巢无法繁殖新蜂群，你仍然需要原版蜂巢来完成这项工作。

## 手册 2：养蜂进阶 - 蜜蜂与作物

来源：`assets/fromgoldencombs/config/handbook/FGC02-fromgoldencombs-pollination.json`。

"蜂蜜的血统

与蜜蜂无关；

一朵三叶草，任何时候，

都是它的贵族。"

- 艾米莉·狄金森

蜜蜂是优秀的传粉者，可以帮助提高许多作物的产量。现在，蜂巢会在达到“良好”或更高种群时积累“授粉次数”。

每种蜂巢都有不同的有效授粉范围。当范围内的有效作物被收获时，蜂巢会消耗一次授粉次数，并提升作物的所有掉落物。

每个蜂巢都有最大授粉次数上限，如果从零开始积累，大约需要30天达到上限。按住Shift查看蜂巢时，可以显示当前授粉次数和有效范围。

## 手册 3：养蜂进阶 103——朗斯特罗斯蜂箱

来源：`assets/fromgoldencombs/config/handbook/FGC03-fromgoldencombs-langstrothguide.json`。

朗斯特罗斯蜂箱是养蜂人的得意之作，兼顾蜂群与养蜂人的需要。它由一个 [handbook://block-fromgoldencombs:langstrothbase-ebony-baldcypress-east] 底座、一至三个 [handbook://block-fromgoldencombs:langstrothsuper-closed-ebony-baldcypress-east] 继箱和顶部装有蜂群的 [handbook://block-fromgoldencombs:langstrothbrood-ebony-baldcypress-maple-east] 育雏箱组成，每个继箱最多可放十个 [handbook://item-fromgoldencombs:beeframe-ebony-lined] 已加衬的蜂巢框。蜂群安顿下来后，这种蜂箱能提供最丰厚的蜂蜜和蜂蜡产量，也能为作物提供最好的增益。

第一步——准备材料

朗斯特罗斯蜂箱并非初学者的第一只蜂箱。制作它需要田间收获的材料、现有蜂箱产出的蜂蜡，以及木板。付出的努力将换来丰收的作物、果实累累的浆果丛和茁壮的果树。

需要准备：

• 10 块蜂蜡，用于木板浸蜡和制作蜂巢框衬垫。

• 27 块木板。

• 4 根同种原木，用于制作 [handbook://block-fromgoldencombs:langstrothbase-ebony-baldcypress-east] 底座。

• 一把锤子。

• 一块亚麻布，可制成五个衬垫。每个 [handbook://block-fromgoldencombs:langstrothsuper-closed-ebony-baldcypress-east] 继箱可放十个蜂巢框，先准备五个也能开始养蜂。

• 0.5 升沥青胶，用于制作 [handbook://item-fromgoldencombs:beeframe-ebony-empty] 空蜂巢框；也可以使用树脂。

• 15 根木棍。

• 一个有蜂群的草编蜂箱。

用这些材料可制作：

• 两个朗斯特罗斯 [handbook://block-fromgoldencombs:langstrothsuper-closed-ebony-baldcypress-east] 继箱，其中一个将改造成 [handbook://block-fromgoldencombs:langstrothbrood-ebony-baldcypress-maple-east] 育雏箱。

• 一个朗斯特罗斯育雏箱顶盖。

• 一个朗斯特罗斯 [handbook://block-fromgoldencombs:langstrothbase-ebony-baldcypress-east] 底座。

• 一个 [handbook://block-fromgoldencombs:framerack-oak-pine-east] 蜂巢框架，用于加衬、维修和收获蜂巢框。

• 五个 [handbook://item-fromgoldencombs:beeframe-ebony-empty] 空蜂巢框，供蜜蜂筑巢储蜜。

• 五个蜂巢框衬垫。

制作蜂箱——先从面板开始

蜂箱的各个部件都要用朗斯特罗斯面板制作，也就是在木桶中浸过蜂蜡的木板。一块蜂蜡可将四块木板制成四块面板；入门所需材料共计 27 块木板。

还需要为 [handbook://item-fromgoldencombs:beeframe-ebony-empty] 空蜂巢框加衬。浸制木板的同时，将一块亚麻布与一块蜂蜡放入木桶，制成浸蜡亚麻布，再用小刀裁成五个蜂巢框衬垫。

接着制作蜂巢框架与蜂巢框

制作 [handbook://block-fromgoldencombs:framerack-oak-pine-east] 蜂巢框架和 [handbook://item-fromgoldencombs:beeframe-ebony-empty] 空蜂巢框，将空框放到架上。手持衬垫右键点击，为每个框装上衬垫。这个架子也用于后续收获和维修蜂巢框。

为蜜蜂安家

制作 [handbook://block-fromgoldencombs:langstrothbase-ebony-baldcypress-east] 底座、两个 [handbook://block-fromgoldencombs:langstrothsuper-closed-ebony-baldcypress-east] 继箱以及一个 [handbook://block-fromgoldencombs:langstrothbrood-ebony-baldcypress-maple-east] 育雏箱顶盖。其中一个继箱要改造成容纳蜂群的育雏箱。

把一个继箱放在地上，对它使用育雏箱顶盖，即可将其变成育雏箱；外观会沿用原继箱的木材样式。现在就可以用有蜂群的草编蜂箱引入蜂群，也可以等整套蜂箱装好再引入。

注意：装有蜂群的 [handbook://block-fromgoldencombs:langstrothbrood-ebony-baldcypress-maple-east] 育雏箱只能放在背包槽位中，无法放入普通物品栏！

为蜜蜂准备储蜜空间

将另一个 [handbook://block-fromgoldencombs:langstrothsuper-closed-ebony-baldcypress-east] 继箱放到地上，右键点击顶部，顶盖会滑开，露出放置 [handbook://item-fromgoldencombs:beeframe-ebony-lined] 已加衬的蜂巢框的空间。手持蜂巢框右键点击即可装入。放入五个后，还能再容纳五个；每个继箱最多放十个，不放满也能正常使用。

注意：继箱不接受 [handbook://item-fromgoldencombs:beeframe-ebony-empty] 空蜂巢框，因为没有衬垫便无法筑巢。可以在箱内存放 [handbook://item-fromgoldencombs:beeframe-ebony-harvestable] 可收获的蜂巢框，但只有 [handbook://item-fromgoldencombs:beeframe-ebony-lined] 已加衬的蜂巢框才能继续填入蜂巢蜜。

组装蜂箱

右键点击继箱正面关上顶盖，再选中空槽，潜行并右键点击将其拾起。手持继箱右键点击 [handbook://block-fromgoldencombs:langstrothbase-ebony-baldcypress-east] 底座即可放上，随后将育雏箱放在最顶端。只要周围花朵充足，且育雏箱已引入蜂群，蜂箱就能开始工作。

收获蜂巢蜜

与陶制蜂箱和草编蜂箱相比，朗斯特罗斯蜂箱无需每次产蜜后立即重置。草编蜂箱需要破坏、陶制蜜罐需要清空后才能继续产蜜；朗斯特罗斯蜂箱则可连续生产多轮。即使只有一个装满蜂巢框的继箱，也要三至五周才能将所有框填满。

准备收获时，取下育雏箱与继箱，打开继箱顶盖，取出 [handbook://item-fromgoldencombs:beeframe-ebony-harvestable] 可收获的蜂巢框，放到 [handbook://block-fromgoldencombs:framerack-oak-pine-east] 蜂巢框架上，用小刀采收蜂巢蜜。每次采收都会磨损衬垫；衬垫耐久耗尽后，需要重新加衬。也可以手持浸蜡亚麻线点击受损的蜂巢框进行修复。

将 [handbook://item-fromgoldencombs:beeframe-ebony-lined] 已加衬的蜂巢框放回继箱，把继箱装回底座，再盖上 [handbook://block-fromgoldencombs:langstrothbrood-ebony-baldcypress-maple-east] 育雏箱，就可以等待下一次丰收了！

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · langstrothparts</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜡<br><code>game:beeswax</code> | 1 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 4 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>fromgoldencombs:langstrothside-{wood}</code> | 4 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/barrel/langstrothparts.json`

```json
[
  {
    "code": "langstrothpartside",
    "sealHours": 48,
    "ingredients": [
      {
        "type": "item",
        "code": "game:beeswax",
        "quantity": 1
      },
      {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 4,
        "name": "wood",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    ],
    "output": {
      "type": "item",
      "code": "fromgoldencombs:langstrothside-{wood}",
      "stackSize": 4
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · waxedlinen</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜡<br><code>game:beeswax</code> | 1 | 未声明附加限制 |
| 投入 2 | 变体材料（按代码匹配）<br><code>game:linen-*-down</code> | 1 | 允许变体：['square', 'offset', 'normal', 'diamond'] |
| 产物 | 名称未汉化（见物品代码）<br><code>game:linen-waxed-down</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/barrel/waxedlinen.json`

```json
[
  {
    "code": "waxedlinen1",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:beeswax",
        "quantity": 1
      },
      {
        "type": "block",
        "code": "game:linen-*-down",
        "quantity": 1,
        "name": "pattern",
        "allowedVariants": [
          "square",
          "offset",
          "normal",
          "diamond"
        ]
      }
    ],
    "output": {
      "type": "block",
      "code": "game:linen-waxed-down",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>蜡染亚麻线 · waxedtwine</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 蜂蜡<br><code>game:beeswax</code> | 1 | 未声明附加限制 |
| 投入 2 | 亚麻线<br><code>game:flaxtwine</code> | 4 | 未声明附加限制 |
| 产物 | 蜡染亚麻线<br><code>fromgoldencombs:waxedflaxtwine</code> | 4 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：2。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/barrel/waxedtwine.json`

```json
[
  {
    "code": "waxedtwine",
    "sealHours": 2,
    "ingredients": [
      {
        "type": "item",
        "code": "game:beeswax",
        "quantity": 1
      },
      {
        "type": "item",
        "code": "game:flaxtwine",
        "quantity": 4
      }
    ],
    "output": {
      "type": "item",
      "code": "fromgoldencombs:waxedflaxtwine",
      "stackSize": 4
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · hivetop</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>fromgoldencombs:hivetop-{type}-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/clayforming/hivetop.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:clay-*",
    "name": "type",
    "allowedvariants": [
      "fire",
      "blue",
      "red"
    ]
  },
  "pattern": [
    [
      "__________",
      "__________",
      "__######__",
      "__######__",
      "__######__",
      "__######__",
      "__######__",
      "__######__",
      "__________",
      "__________"
    ],
    [
      "__________",
      "__________",
      "__######__",
      "__#____#__",
      "__#____#__",
      "__#____#__",
      "__#____#__",
      "__######__",
      "__________",
      "__________"
    ],
    [
      "__________",
      "_########_",
      "_########_",
      "_##____##_",
      "_##____##_",
      "_##____##_",
      "_##____##_",
      "_########_",
      "_########_",
      "__________"
    ],
    [
      "__________",
      "_########_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_########_",
      "__________"
    ],
    [
      "__________",
      "_########_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_#______#_",
      "_########_",
      "__________"
    ],
    [
      "__________",
      "_########_",
      "_########_",
      "_##____##_",
      "_##____##_",
      "_##____##_",
      "_##____##_",
      "_########_",
      "_########_",
      "__________"
    ],
    [
      "__________",
      "__________",
      "__######__",
      "__#____#__",
      "__#____#__",
      "__#____#__",
      "__#____#__",
      "__######__",
      "__________",
      "__________"
    ]
  ],
  "name": "recipe-clayforming-hivetop-raw",
  "output": {
    "type": "block",
    "code": "fromgoldencombs:hivetop-{type}-raw"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · rawclaypothive</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>fromgoldencombs:ceramicbroodpot-{type}-raw</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/clayforming/rawclaypothive.json`

```json
{
  "ingredient": {
    "type": "item",
    "code": "game:clay-*",
    "name": "type",
    "allowedvariants": [
      "fire",
      "blue",
      "red"
    ]
  },
  "pattern": [
    [
      "______________",
      "______________",
      "______________",
      "___########___",
      "___########___",
      "___########___",
      "___########___",
      "___########___",
      "___########___",
      "___########___",
      "___########___",
      "______________",
      "______________",
      "______________"
    ],
    [
      "______________",
      "______________",
      "__##########__",
      "__##########__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##########__",
      "__##########__",
      "______________",
      "______________"
    ],
    [
      "______________",
      "_############_",
      "_############_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_############_",
      "_############_",
      "______________"
    ],
    [
      "______________",
      "_############_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_############_",
      "______________"
    ],
    [
      "______________",
      "_############_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_############_",
      "______________"
    ],
    [
      "______________",
      "_############_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_#__________#_",
      "_############_",
      "______________"
    ],
    [
      "______________",
      "_############_",
      "_############_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_##________##_",
      "_############_",
      "_############_",
      "______________"
    ],
    [
      "______________",
      "______________",
      "__##########__",
      "__##########__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##########__",
      "__##########__",
      "______________",
      "______________"
    ],
    [
      "______________",
      "______________",
      "__##########__",
      "__##########__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##______##__",
      "__##########__",
      "__##########__",
      "______________",
      "______________"
    ],
    [
      "______________",
      "______________",
      "______________",
      "___########___",
      "___########___",
      "___##_##_##___",
      "___########___",
      "___########___",
      "___##_##_##___",
      "___########___",
      "___########___",
      "______________",
      "______________",
      "______________"
    ]
  ],
  "name": "recipe-clayforming-rawceramichive",
  "output": {
    "type": "block",
    "code": "fromgoldencombs:ceramicbroodpot-{type}-raw"
  }
}
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · framerack</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-aged</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-aged-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-acacia</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-acacia-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-birch</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-birch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-oak</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-oak-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-maple</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-maple-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-pine</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-pine-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-kapok</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-kapok-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-baldcypress</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-baldcypress-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-larch</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-larch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-redwood</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-redwood-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-ebony</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-ebony-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-walnut</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-walnut-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-purpleheart</code> | 2 | 未声明附加限制 |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>framerack-{primary}-purpleheart-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SHS
PAP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/grid/framerack.json`

```json
[
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-aged",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-aged-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-acacia",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-acacia-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-birch",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-birch-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-oak",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-oak-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-maple",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-maple-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-pine",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-pine-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-kapok",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-kapok-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-baldcypress",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-baldcypress-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-larch",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-larch-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-redwood",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-redwood-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-ebony",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-ebony-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-walnut",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-walnut-east"
    }
  },
  {
    "ingredientPattern": "SHS,PAP",
    "ingredients": {
      "A": {
        "type": "item",
        "code": "langstrothside-purpleheart",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "1",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "framerack-{primary}-purpleheart-east"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · langstrothbase</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-aged-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-aged-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PQP
L_L
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-acacia-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-acacia-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-birch-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-birch-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-oak-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-oak-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-maple-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-maple-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-pine-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-pine-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-kapok-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-kapok-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-baldcypress-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-baldcypress-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-larch-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-larch-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-redwood-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-redwood-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-ebony-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-ebony-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-walnut-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-walnut-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 Q | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>game:log-*-purpleheart-*</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbase-{primary}-purpleheart-east</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PPP
L_L
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/grid/langstrothbase.json`

```json
[
  {
    "ingredientPattern": "_H_,PQP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-aged-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-aged-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-acacia-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-acacia-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-birch-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-birch-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-oak-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-oak-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-maple-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-maple-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-pine-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-pine-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-kapok-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-kapok-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-baldcypress-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-baldcypress-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-larch-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-larch-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-redwood-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-redwood-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-ebony-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-ebony-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-walnut-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-walnut-east",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_,PPP,L_L",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "Q": {
        "type": "item",
        "code": "langstrothside-*",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "L": {
        "type": "block",
        "code": "game:log-*-purpleheart-*",
        "quantity": 2,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "langstrothbase-{primary}-purpleheart-east",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · langstrothsuper</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-aged</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-aged-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-acacia</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-acacia-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-birch</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-birch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-oak</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-oak-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-maple</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-maple-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-pine</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-pine-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-kapok</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-kapok-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-baldcypress</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-baldcypress-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-larch</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-larch-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-redwood</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-redwood-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-ebony</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-ebony-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-walnut</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-walnut-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-purpleheart</code> | 2 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothsuper-closed-{primary}-purpleheart-east</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_
PAP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/grid/langstrothsuper.json`

```json
[
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-aged",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-aged-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-acacia",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-acacia-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-birch",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-birch-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-oak",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-oak-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-maple",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-maple-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-pine",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-pine-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-kapok",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-kapok-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-baldcypress",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-baldcypress-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-larch",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-larch-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-redwood",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-redwood-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-ebony",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-ebony-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-walnut",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-walnut-east"
    }
  },
  {
    "ingredientPattern": "_H_,PAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-purpleheart",
        "quantity": "2",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "langstrothsuper-closed-{primary}-purpleheart-east"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · beeframe</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 朗斯特罗斯蜂巢面板<br><code>fromgoldencombs:langstrothside-*</code> | 2 | 未声明附加限制 |
| 投入 R | 木棍<br><code>game:stick</code> | 3 | 未声明附加限制 |
| 投入 S | 树脂<br><code>game:resin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>fromgoldencombs:beeframe-{wood}-empty</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
R
S
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 朗斯特罗斯蜂巢面板<br><code>fromgoldencombs:langstrothside-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 木棍<br><code>game:stick</code> | 3 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>fromgoldencombs:beeframe-{wood}-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
R
S
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 朗斯特罗斯蜂巢面板<br><code>fromgoldencombs:langstrothside-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 木棍<br><code>game:stick</code> | 3 | 未声明附加限制 |
| 投入 S | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>fromgoldencombs:beeframe-{wood}-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
R
S
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 朗斯特罗斯蜂巢面板<br><code>fromgoldencombs:langstrothside-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 木棍<br><code>game:stick</code> | 3 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>fromgoldencombs:beeframe-{wood}-empty</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
R
S
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/grid/parts/beeframe.json`

```json
[
  {
    "ingredientPattern": "B,R,S",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "fromgoldencombs:langstrothside-*",
        "quantity": 2,
        "name": "wood",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "R": {
        "type": "item",
        "code": "game:stick",
        "quantity": "3"
      },
      "S": {
        "type": "item",
        "code": "game:resin"
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "fromgoldencombs:beeframe-{wood}-empty",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "B,R,S",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "fromgoldencombs:langstrothside-*",
        "name": "wood",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "R": {
        "type": "item",
        "code": "game:stick",
        "quantity": "3"
      },
      "S": {
        "type": "block",
        "code": "game:bowl-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "glueportion-pitch-hot"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "fromgoldencombs:beeframe-{wood}-empty",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "B,R,S",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "fromgoldencombs:langstrothside-*",
        "name": "wood",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "R": {
        "type": "item",
        "code": "game:stick",
        "quantity": "3"
      },
      "S": {
        "type": "block",
        "code": "game:woodbucket"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "glueportion-pitch-hot"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "fromgoldencombs:beeframe-{wood}-empty",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "B,R,S",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "fromgoldencombs:langstrothside-*",
        "name": "wood",
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "R": {
        "type": "item",
        "code": "game:stick",
        "quantity": "3"
      },
      "S": {
        "type": "block",
        "code": "game:jug-*-fired"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "glueportion-pitch-hot"
        },
        "requiresLitres": 0.1
      }
    },
    "width": 1,
    "height": 3,
    "output": {
      "type": "item",
      "code": "fromgoldencombs:beeframe-{wood}-empty",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>蜂巢框衬垫 · frameliner</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 蜡染亚麻布<br><code>game:linen-waxed-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蜂巢框衬垫<br><code>fromgoldencombs:frameliner</code> | 5 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
L
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/grid/parts/frameliner.json`

```json
[
  {
    "ingredientPattern": "K,L",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "block",
        "code": "game:linen-waxed-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "fromgoldencombs:frameliner",
      "quantity": 5
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · langstrothpart-brood</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-aged</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-aged</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-acacia</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-acacia</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-birch</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-birch</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-oak</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-oak</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-maple</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-maple</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-pine</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-pine</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-kapok</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-kapok</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-baldcypress</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-baldcypress</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-larch</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-larch</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-redwood</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-redwood</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-ebony</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-ebony</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-walnut</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-walnut</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 H | 变体材料（按代码匹配）<br><code>game:hammer-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 朗斯特罗斯蜂巢面板<br><code>langstrothside-*</code> | 1 | 未声明附加限制 |
| 投入 A | 名称未汉化（见物品代码）<br><code>langstrothside-purpleheart</code> | 1 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>langstrothbroodtop-{primary}-purpleheart</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
_H_	_A_	PAP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/fromgoldencombs/recipes/grid/parts/langstrothpart-brood.json`

```json
[
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-aged",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-aged",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-acacia",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-acacia",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-birch",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-birch",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-oak",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-oak",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-maple",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-maple",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-pine",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-pine",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-kapok",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-kapok",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-baldcypress",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-baldcypress",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-larch",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-larch",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-redwood",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-redwood",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-ebony",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-ebony",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-walnut",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-walnut",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "_H_\t_A_\tPAP",
    "ingredients": {
      "H": {
        "type": "item",
        "code": "game:hammer-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "langstrothside-*",
        "name": "primary",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      },
      "A": {
        "type": "item",
        "code": "langstrothside-purpleheart",
        "quantity": 1,
        "states": [
          "aged"
        ],
        "loadFromProperties": "block/wood"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "langstrothbroodtop-{primary}-purpleheart",
      "quantity": 1
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
