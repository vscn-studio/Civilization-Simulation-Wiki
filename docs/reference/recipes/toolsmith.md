<!-- generated:start -->
# 工具锻造：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：工具锻造 - 制作与拆解方法

来源：`assets/toolsmith/config/handbook/toolsmithing-craftingmethods.json`。

徒手制作

制作组合工具的主要方法是使用徒手制作。就像合成格一样，它可以在任何地方进行，因为你只需要解放双手。首先，拿起你希望使用的部件，对于普通工具来说，这将是一个工具头、一个手柄和可选的一个绑定件。绑定件不是必需的，但如果它是更高质量的，它将增强你工具的绑定耐久度，并为你的手柄提供一些额外的好处。

要实际使用徒手制作，请将工具头拿在主手中，并将选择的手柄放在副手中。查看工具提示以了解什么是有效的手柄和绑定件！按住右键一小会儿，你就会将该头部与该手柄配对，这是制作过程的第一步。然后，如果你希望使用绑定件，现在将其放入副手，并再次用主手拿着工具对右键单击，再过一小会儿，你就制作好了你的工具！

工作台制作

你也可以在你值得信赖的工作台上制作工具！中间那五个插槽？那就是你放置部件进行制作的宽敞空间——一旦你准备好所有部件，再次拿起你的锤子。用右键单击多次敲打这些部件中的任何一个，就能把工具组装好。此外，这些插槽也可以用来平均任何金属头或锻造工具的耐久度，这些工具的配方会输出多个物品。这对于准备重铸非常有用！

合成格制作

最后，另一个组装工具的选项是经典选项，即使用合成格。如果你将选择的工具头放在任何手柄上方，并将绑定件放在头部的右侧插槽中，则可以选择使用此方法来制作工具。除此之外，它与徒手制作相同！这些配方在游戏加载时生成，因此它们会根据服务器上的配置生成更多。

拆解

如果你想提早取回工具头或手柄，你也可以拆解组合工具！这需要一个砂轮或一个工作台，两者都需要木板来制作，但这通常只在你获得金属工具头之后才需要。关于拆解工具需要注意的一件重要事情是，如果你已经使用过它，你将无法从中回收绑定件，因为你必须将其拆开以免损坏手柄或头部。

要在砂轮上拆解，只需用主手拿着工具看着它，并在右键单击时按住Shift键。按住几秒钟即可将工具拆开！工作台也是如此，只不过你需要看向工作台左侧的虎钳，并以类似的方式与其交互。

## 手册 2：工具锻造 - 耐久度、锋利度与磨损

来源：`assets/toolsmith/config/handbook/toolsmithing-durabilityandwear.json`。

锋利度与耐久度

关于任何锋利工具，首先要注意的是它的锋利度等级。正如锻造工具头所预期的那样，仅凭锻造行为不可能使其完美锋利，因此即使在制作完成后，工具头也需要一些打磨。当你的工具保持锋利时，使用起来会更容易，并提供5%的小幅使用速度加成。此外，当总锋利度保持在98%以上时，你的绑定件和工具头不会受损，并且手柄会抵抗损坏，直到锋利度降至95%以下。对于锻造工具，唯一重要的部分是头部损坏！

如果一个工具足够钝以至于头部开始受到损坏，那么它每次使用都有几率受到损坏。对于锋利工具，这个几率是15%，但对于钝工具，它只有2%。这些值是可配置的！另一方面，手柄和绑定件每次使用会受到1点损坏。

最后，当锋利度低于33%时，你会发现使用工具需要更长的时间。此时它会获得-10%的使用速度惩罚——如果它降到0并完全变钝，工具将保证获得一个负面效果，并且现在工具头每次使用都会受到2点伤害。

磨损与恢复锋利度

有两种方法可以恢复锋利度：磨刀石或砂轮。磨刀石是你首先能获得的，它们只需要从任何可打制的石头中打制出来。砂轮则需要像花岗岩或砂岩这样的研磨石，或者像安山岩或页岩这样的石头来制作石轮部分，以及木板来制作框架。两者之间的主要区别在于，磨刀石的耐久度有限，而砂轮则没有——但它体积庞大且难以携带。要使用它们，只需将磨刀石握在副手，将要打磨的工具握在主手，然后按住右键！对于砂轮，只需将其放下，将工具握在手中，并在看着它时再次按住右键。

关于重新打磨工具使其锋利需要注意的重要一点是，它会消耗工具头部的金属——即耐久度。当你开始打磨工具时，对于你打磨的前20%总锋利度，头部将受到双倍伤害。此后，在20-40%之间，伤害开始降低到1。这几乎是你在打磨工具时工具会受到的所有伤害——在此之后，当打磨到总锋利度的50%时，它会降低到甚至只有5%的几率造成损坏，并一直保持到完全锋利。

## 手册 3：工具锻造 - 其他新增内容

来源：`assets/toolsmith/config/handbook/toolsmithing-miscaddons.json`。

铜的冷锻

作为一个现实元素，Toolsmith允许你冷锻铜！这意味着你不需要加热铜来加工它，因为它是一种非常软的金属，可以在室温下加工。

未来还会有更多内容！

## 手册 4：工具锻造 - 重铸的秘密

来源：`assets/toolsmith/config/handbook/toolsmithing-reforging.json`。

重铸

当你的工具头耐久度开始降低时，你可能会考虑更换它们。但这已不再必要！现在你可以在用木板制作的工作台上重铸你珍贵的工具头了。要开始重铸，请看向右侧的工具箱及其前方的空位。将你的工具头或锻造工具放在那里，然后拿起你的锤子，只需右键单击该位置即可准备工具进行重铸！这会将其转换为一个工件，你必须将其带到你的锻铁炉上才能修复它。

如果你选择的工具头或锻造工具的配方会输出多个物品，你需要确保你有与配方输出数量相同的物品才能开始重铸。工作台可以帮助解决这个问题！查看工作台制作条目以获取更多详细信息——但你可以用它来合并它们并平均它们之间的耐久度。

## 手册 5：工具锻造 - 基础知识

来源：`assets/toolsmith/config/handbook/toolsmithing-the-basics.json`。

工具锻造

让我来教你如何保养那把斧头。

首先你会注意到，你的一些工具有多个部件，并且在耐久度条上方还有一条锋利度条。任何拥有三个或更多部件的工具都是'组合工具'，而其他可能在合成格中制作或锻造出来成为一个完整工具的则是'锻造工具'。这是重要的区别：组合工具可以定制，其部件可以选择和制作以增加工具的耐久度等属性；而锻造工具则更为单一，但两者都可以进行维护和修理。许多信息也可以在各种工具提示中找到，所以如果你感到困惑，也请阅读它们！

制作方法

如前所述，现在有很多方法可以定制你的工具，以及你选择如何制作它们。旧的可靠选项——合成格制作——仍然可行，并为你的手柄和（可选）绑定件提供了扩展选项。只需将手柄放在工具头下方，并将任何绑定件放在其右侧即可组装。

第二个选项是组合工具的徒手制作！要开始此过程，请拿起你选择的工具头并将其握在主手中，然后将所选手柄放在副手中。按住右键一会儿将它们捆绑成一个部件——然后用主手拿着这对部件，并在副手放上可选的绑定件来完成它！绑定件不是必需的，如果你愿意，可以将副手留空。祝你制作愉快！

锋利度与磨损

最后，第二条进度条——锋利度条——现在出现在任何没有钝刃且需要锋利才能正常工作的工具上。重要的是不要让它耗尽，否则你的工具会受到更多伤害——并且必定会出现一个负面效果（尚未实装！）。要管理工具的锋利度，只需要一个打制的磨刀石（由任何可打制的石头制成）或一个砂轮。

一旦你有了木板和合适的石块，就可以制作砂轮——像砂岩和花岗岩这样的研磨石材非常适合，但也可以用页岩或安山岩。否则，磨刀石非常适合随时随地打磨；而砂轮体积庞大，最好放在你工作室的家里！

## 手册 6：工具锻造 - 工具部件及用途

来源：`assets/toolsmith/config/handbook/toolsmithing-toolhandles.json`。

工具头

工具头可能是最重要的部分。当然，它决定了你正在制作哪种工具！但它的材料也将决定其其余部件的整体耐久度——因此金属优于石头和木材，而更高级的金属可以使用更长时间。如果工具不是钝击型的，它还会有一个锋利度值，你可以通过打磨来增加和恢复，但会消耗头部的耐久度。如果你忘记了，请查看工具提示！

工具手柄

工具手柄可以用几种选项制作，你通常的木棍或骨头可以作为很好的起始材料，但一段时间后你可能希望制作更好的选项，例如粗制手柄或雕刻手柄！雕刻手柄和专业手柄的木材都可以用几种选项进行处理，并且可以安装握柄以保持双手稳定。但是粗制手柄只能可靠地安装握柄，因为它只是从一块备用柴火上切下来的。这两种操作都会增加你的手柄所带来的好处，当你拥有一个手柄时，请务必查看工具提示以获取更具体的信息！你的基础手柄将决定其大部分耐久度，而更高级的手柄还可以为绑定件提供更多支撑和额外耐久度，并让你更快地使用工具。

处理选项

处理你的手柄是可选的，但如果你这样做了，你会发现它能够更长时间地抵抗磨损和自然侵蚀——处理提供了可观的耐久度加成！有几种处理选项，例如脂肪、蜂蜡或油，按此顺序，它们从最简单、效果最差到最强。不过，油只能通过交叉兼容性制作，Expanded Foods 中的亚麻籽油和种子油是非常好的工具处理选项，Oils 模组中的亚麻籽油和核桃油也是如此。此外，两种木器漆都能以更少的消耗量出色地完成工作！

握柄

一个好的手柄握柄会给你的手柄带来两个好处：使用速度增加以及手柄不受任何损坏的几率。一些优质的握柄材料包括麻线、亚麻布块、任何颜色的皮革（也可用于装饰），甚至如果你负担得起的话，还有坚固皮革。再次查看你手柄的工具提示以了解每种材料的具体数值！

工具绑定件

一个坚固耐用的工具离不开好的绑定件！你可以制作一个没有绑定件的组合工具，但请注意，工具头很快就会从手柄上飞脱，需要重新安装。要解决这个问题，你只需要使用干草或任何形式的芦苇将头部重新绑在手柄上即可。你选择的绑定件主要影响其耐久度等级、对手柄耐久度的小幅加成，以及最后是绑定件的恢复能力，即如果工具的其他部分损坏，绑定件在剩余耐久度百分比为多少时可以被回收。一些更高级的绑定件选项包括麻线、绳索、任何颜色的皮革、热沥青胶以及来自Butchery的其他胶水选项、大多数金属的钉子和金属零件。请查阅手册并查看物品工具提示以获取更多信息！

## 手册 7：工具锻造 - 工具类型与你

来源：`assets/toolsmith/config/handbook/toolsmithing-tooltypes.json`。

组合工具

组合工具是指任何由工具头和木棍制成的常规工具。通过Toolsmith，这些工具可以升级以使用更好的手柄，这些手柄可以经过处理以保护木材，甚至可以配备合适的握柄，以及合适的绑定材料，以真正使工具头更长时间地固定在手柄上。现在，你工具的每个部件都有独立的耐久度，较弱或不太高级的选项在使用较短时间后可能会散架或折断。记住！制作它们的方法也有几种，请查看手册页面以获得更详细的分解——但组合工具需要一个工具头来确定它是什么工具，以及一个手柄。绑定是可选的，但你会发现你的工具头很快就会从手柄上飞脱！

锻造工具

如果一个工具不是组合工具，那么它将是锻造工具！这些是通过锻造创造的任何工具，一旦你完成了工件，你就会收到完整的功能性物品——比如凿子！它还包括任何功能更独特或制作独特的工具，主要来自其他模组：例如QP Chisel Tools中的许多凿子工具，或Age of Growing中的压痕器或脱粒连枷。这些工具只有一个功能部件充当工具的头部，或者在这种情况下，充当工具本身！如果它们是由金属制成的，当耐久度较低时，你仍然可以重铸它们。

钝击工具

钝击工具可以是任何工具类型——它更多的是对工具类型的描述。顾名思义，钝击工具完全不关心锋利度，也不需要打磨就能很好地工作！它不会从锋利度中获得任何好处或坏处。但你会发现它们异常坚固，使用时损坏头部的几率远低于锋利工具——如果它是一个钝击组合工具，你仍然需要注意手柄和绑定件。留意那些！

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>皮革条 · fabricstrips-atleather-cloth</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-acacia</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-aged</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-baldcypress</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-birch</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-cypress</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-ebony</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-kapok</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-larch</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-maple</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-pine</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-purpleheart</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-redwood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:leather-normal-walnut</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>ancienttools:buckskin</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-atleather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/ancienttools/recipes/grid/fabricstrips-atleather-cloth.json`

```json
[
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-acacia"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/acacia"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-aged"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/aged"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-baldcypress"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/baldcypress"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-birch"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/birch"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-cypress"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/cypress"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-ebony"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/ebony"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-kapok"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/kapok"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-larch"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/larch"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-maple"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/maple"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-pine"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/pine"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-purpleheart"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/purpleheart"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-redwood"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/redwood"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:leather-normal-walnut"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/leather/walnut"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "ancienttools:buckskin"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-atleather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "ancienttools:item/resource/buckskin"
          }
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>砂纸 · sandpaper-from-glues</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/butchering/recipes/grid/sandpaper-from-glues.json`

```json
[
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:glueportion-sinew-cold"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:glueportion-sinew-cold"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:glueportion-sinew-cold"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:glueportion-hide-hot"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:glueportion-hide-hot"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "butchering:glueportion-hide-hot"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>专业工具手柄 · cape-carpentedhandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 砂纸<br><code>toolsmith:sandpaper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonescaperegion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-carpentedhandle.json`

```json
[
  {
    "ingredientPattern": "KS,W_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "toolsmith:sandpaper"
      },
      "W": {
        "type": "block",
        "code": "floralzonescaperegion:supportbeam-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:carpentedhandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>花岗岩砂轮、砂岩砂轮、页岩砂轮、安山岩砂轮 · cape-grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 花岗岩岩石<br><code>game:rock-granite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 花岗岩砂轮<br><code>toolsmith:grindstone-granite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 砂岩岩石<br><code>game:rock-sandstone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 砂岩砂轮<br><code>toolsmith:grindstone-sandstone-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 页岩岩石<br><code>game:rock-shale</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 页岩砂轮<br><code>toolsmith:grindstone-shale-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 安山岩岩石<br><code>game:rock-andesite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 安山岩砂轮<br><code>toolsmith:grindstone-andesite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-granite"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-granite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-sandstone"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-sandstone-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-shale"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-shale-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-andesite"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-andesite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>雕刻工具手柄 · cape-handle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonescaperegion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 雕刻工具手柄<br><code>toolsmith:handle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-handle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "block",
        "code": "floralzonescaperegion:supportbeam-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:handle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>工作台 · cape-workbench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 3 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaperegion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 工作台<br><code>toolsmith:workbench-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
QSQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaperegion/recipes/grid/cape-workbench.json`

```json
[
  {
    "ingredientPattern": "PPP,QSQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*",
        "quantity": 3
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaperegion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:workbench-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>专业工具手柄 · caribbean-carpentedhandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 砂纸<br><code>toolsmith:sandpaper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-carpentedhandle.json`

```json
[
  {
    "ingredientPattern": "KS,W_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "toolsmith:sandpaper"
      },
      "W": {
        "type": "block",
        "code": "floralzonescaribbeanregion:supportbeam-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:carpentedhandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>花岗岩砂轮、砂岩砂轮、页岩砂轮、安山岩砂轮 · caribbean-grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 花岗岩岩石<br><code>game:rock-granite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 花岗岩砂轮<br><code>toolsmith:grindstone-granite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 砂岩岩石<br><code>game:rock-sandstone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 砂岩砂轮<br><code>toolsmith:grindstone-sandstone-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 页岩岩石<br><code>game:rock-shale</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 页岩砂轮<br><code>toolsmith:grindstone-shale-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 安山岩岩石<br><code>game:rock-andesite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 安山岩砂轮<br><code>toolsmith:grindstone-andesite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-granite"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-granite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-sandstone"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-sandstone-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-shale"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-shale-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-andesite"
      },
      "P": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-andesite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>雕刻工具手柄 · caribbean-handle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 雕刻工具手柄<br><code>toolsmith:handle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-handle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "block",
        "code": "floralzonescaribbeanregion:supportbeam-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:handle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>工作台 · caribbean-workbench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 3 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescaribbeanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 工作台<br><code>toolsmith:workbench-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
QSQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescaribbeanregion/recipes/grid/caribbean-workbench.json`

```json
[
  {
    "ingredientPattern": "PPP,QSQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*",
        "quantity": 3
      },
      "Q": {
        "type": "item",
        "code": "floralzonescaribbeanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:workbench-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>专业工具手柄 · centralaustralian-carpentedhandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 砂纸<br><code>toolsmith:sandpaper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescentralaustralianregion/recipes/grid/centralaustralian-carpentedhandle.json`

```json
[
  {
    "ingredientPattern": "KS,W_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "toolsmith:sandpaper"
      },
      "W": {
        "type": "block",
        "code": "floralzonescentralaustralianregion:supportbeam-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:carpentedhandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>花岗岩砂轮、砂岩砂轮、页岩砂轮、安山岩砂轮 · centralaustralian-grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 花岗岩岩石<br><code>game:rock-granite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 花岗岩砂轮<br><code>toolsmith:grindstone-granite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 砂岩岩石<br><code>game:rock-sandstone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 砂岩砂轮<br><code>toolsmith:grindstone-sandstone-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 页岩岩石<br><code>game:rock-shale</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 页岩砂轮<br><code>toolsmith:grindstone-shale-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 安山岩岩石<br><code>game:rock-andesite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 安山岩砂轮<br><code>toolsmith:grindstone-andesite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescentralaustralianregion/recipes/grid/centralaustralian-grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-granite"
      },
      "P": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-granite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-sandstone"
      },
      "P": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-sandstone-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-shale"
      },
      "P": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-shale-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-andesite"
      },
      "P": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-andesite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>雕刻工具手柄 · centralaustralian-handle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 雕刻工具手柄<br><code>toolsmith:handle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescentralaustralianregion/recipes/grid/centralaustralian-handle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "block",
        "code": "floralzonescentralaustralianregion:supportbeam-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:handle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>工作台 · centralaustralian-workbench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 3 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonescentralaustralianregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 工作台<br><code>toolsmith:workbench-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
QSQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonescentralaustralianregion/recipes/grid/centralaustralian-workbench.json`

```json
[
  {
    "ingredientPattern": "PPP,QSQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*",
        "quantity": 3
      },
      "Q": {
        "type": "item",
        "code": "floralzonescentralaustralianregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:workbench-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>专业工具手柄 · mediterranean-carpentedhandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 砂纸<br><code>toolsmith:sandpaper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesmediterraneanregion/recipes/grid/mediterranean-carpentedhandle.json`

```json
[
  {
    "ingredientPattern": "KS,W_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "toolsmith:sandpaper"
      },
      "W": {
        "type": "block",
        "code": "floralzonesmediterraneanregion:supportbeam-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:carpentedhandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>花岗岩砂轮、砂岩砂轮、页岩砂轮、安山岩砂轮 · mediterranean-grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 花岗岩岩石<br><code>game:rock-granite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 花岗岩砂轮<br><code>toolsmith:grindstone-granite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 砂岩岩石<br><code>game:rock-sandstone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 砂岩砂轮<br><code>toolsmith:grindstone-sandstone-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 页岩岩石<br><code>game:rock-shale</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 页岩砂轮<br><code>toolsmith:grindstone-shale-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 安山岩岩石<br><code>game:rock-andesite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 安山岩砂轮<br><code>toolsmith:grindstone-andesite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesmediterraneanregion/recipes/grid/mediterranean-grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-granite"
      },
      "P": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-granite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-sandstone"
      },
      "P": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-sandstone-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-shale"
      },
      "P": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-shale-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-andesite"
      },
      "P": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-andesite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>雕刻工具手柄 · mediterranean-handle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 雕刻工具手柄<br><code>toolsmith:handle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesmediterraneanregion/recipes/grid/mediterranean-handle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "block",
        "code": "floralzonesmediterraneanregion:supportbeam-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:handle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>工作台 · mediterranean-workbench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 3 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesmediterraneanregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 工作台<br><code>toolsmith:workbench-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
QSQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesmediterraneanregion/recipes/grid/mediterranean-workbench.json`

```json
[
  {
    "ingredientPattern": "PPP,QSQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*",
        "quantity": 3
      },
      "Q": {
        "type": "item",
        "code": "floralzonesmediterraneanregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:workbench-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>专业工具手柄 · neozeylandicregion-carpentedhandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 砂纸<br><code>toolsmith:sandpaper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesneozeylandicregion/recipes/grid/neozeylandicregion-carpentedhandle.json`

```json
[
  {
    "ingredientPattern": "KS,W_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "toolsmith:sandpaper"
      },
      "W": {
        "type": "block",
        "code": "floralzonesneozeylandicregion:supportbeam-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:carpentedhandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>花岗岩砂轮、砂岩砂轮、页岩砂轮、安山岩砂轮 · neozeylandicregion-grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 花岗岩岩石<br><code>game:rock-granite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 花岗岩砂轮<br><code>toolsmith:grindstone-granite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 砂岩岩石<br><code>game:rock-sandstone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 砂岩砂轮<br><code>toolsmith:grindstone-sandstone-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 页岩岩石<br><code>game:rock-shale</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 页岩砂轮<br><code>toolsmith:grindstone-shale-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 安山岩岩石<br><code>game:rock-andesite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 安山岩砂轮<br><code>toolsmith:grindstone-andesite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesneozeylandicregion/recipes/grid/neozeylandicregion-grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-granite"
      },
      "P": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-granite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-sandstone"
      },
      "P": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-sandstone-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-shale"
      },
      "P": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-shale-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-andesite"
      },
      "P": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-andesite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>雕刻工具手柄 · neozeylandicregion-handle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 雕刻工具手柄<br><code>toolsmith:handle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesneozeylandicregion/recipes/grid/neozeylandicregion-handle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "block",
        "code": "floralzonesneozeylandicregion:supportbeam-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:handle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>工作台 · neozeylandicregion-workbench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 3 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>floralzonesneozeylandicregion:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 工作台<br><code>toolsmith:workbench-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
QSQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/floralzonesneozeylandicregion/recipes/grid/neozeylandicregion-workbench.json`

```json
[
  {
    "ingredientPattern": "PPP,QSQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*",
        "quantity": 3
      },
      "Q": {
        "type": "item",
        "code": "floralzonesneozeylandicregion:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:workbench-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>闪长岩砂轮、辉长岩砂轮、石英岩砂轮 · grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:rock-diorite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 闪长岩砂轮<br><code>toolsmith:grindstone-diorite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:rock-gabbro</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 辉长岩砂轮<br><code>toolsmith:grindstone-gabbro-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 名称未汉化（见物品代码）<br><code>game:rock-quartzite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 石英岩砂轮<br><code>toolsmith:grindstone-quartzite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/geoaddons/recipes/grid/grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-diorite"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-diorite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-gabbro"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-gabbro-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-quartzite"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-quartzite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · whetstone</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>toolsmith:whetstone-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/geoaddons/recipes/knapping/whetstone.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:stone-*",
      "name": "rock",
      "allowedVariants": [
        "diorite",
        "gabbro",
        "quartzite",
        "jade",
        "jasper"
      ]
    },
    "pattern": [
      [
        "__________",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "__________"
      ]
    ],
    "name": "Stone whetstone",
    "output": {
      "type": "item",
      "code": "toolsmith:whetstone-{rock}"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · whetstone</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>toolsmith:whetstone-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/mngeology/recipes/knapping/whetstone.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:stone-*",
      "name": "rock",
      "allowedVariants": [
        "komatiite",
        "monzonite",
        "pyroxenite",
        "serpentinite",
        "syenite"
      ]
    },
    "pattern": [
      [
        "__________",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "__________"
      ]
    ],
    "name": "Stone whetstone",
    "output": {
      "type": "item",
      "code": "toolsmith:whetstone-{rock}"
    }
  }
]
```

</details>

</details>

<details><summary>布条 · fabricstrips-tailorsdelight-cloth</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深蓝布料<br><code>tailorsdelight:cloth-darkblue</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深棕布料<br><code>tailorsdelight:cloth-darkbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深绿布料<br><code>tailorsdelight:cloth-darkgreen</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深红布料<br><code>tailorsdelight:cloth-darkred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/tailorsdelight/recipes/grid/fabricstrips-tailorsdelight-cloth.json`

```json
[
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-darkblue"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "tailorsdelight:block/cloth/dark/darkblue"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-darkbrown"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "tailorsdelight:block/cloth/dark/darkbrown"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-darkgreen"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "tailorsdelight:block/cloth/dark/darkgreen"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "tailorsdelight:cloth-darkred"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "tailorsdelight:block/cloth/dark/darkred"
          }
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>皮革条 · fabricstrips-tailorsdelight-leather</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 深蓝皮革<br><code>tailorsdelight:leather-darkblue</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 深棕皮革<br><code>tailorsdelight:leather-darkbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 深绿皮革<br><code>tailorsdelight:leather-darkgreen</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 深红皮革<br><code>tailorsdelight:leather-darkred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 纳迪安皮革<br><code>tailorsdelight:leather-nadiyan</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/tailorsdelight/recipes/grid/fabricstrips-tailorsdelight-leather.json`

```json
[
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "tailorsdelight:leather-darkblue"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/blue",
            "material-overlay": "tailorsdelight:overlays/darkblue"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "tailorsdelight:leather-darkbrown"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/plain",
            "material-overlay": "tailorsdelight:overlays/darkbrown"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "tailorsdelight:leather-darkgreen"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/green",
            "material-overlay": "tailorsdelight:overlays/darkgreen"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "tailorsdelight:leather-darkred"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/red",
            "material-overlay": "tailorsdelight:overlays/darkred"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "tailorsdelight:leather-nadiyan"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/plain",
            "material-overlay": "tailorsdelight:overlays/lighten2"
          }
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>专业工具手柄 · tree-carpentedhandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 砂纸<br><code>toolsmith:sandpaper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>wildcrafttree:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/wildcrafttree/recipes/grid/tree-carpentedhandle.json`

```json
[
  {
    "ingredientPattern": "KS,W_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "toolsmith:sandpaper"
      },
      "W": {
        "type": "block",
        "code": "wildcrafttree:supportbeam-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:carpentedhandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>雕刻工具手柄 · tree-handle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>wildcrafttree:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 雕刻工具手柄<br><code>toolsmith:handle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/wildcrafttree/recipes/grid/tree-handle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "block",
        "code": "wildcrafttree:supportbeam-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:handle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>花岗岩砂轮、砂岩砂轮、页岩砂轮、安山岩砂轮 · trees-grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 花岗岩岩石<br><code>game:rock-granite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 花岗岩砂轮<br><code>toolsmith:grindstone-granite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 砂岩岩石<br><code>game:rock-sandstone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 砂岩砂轮<br><code>toolsmith:grindstone-sandstone-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 页岩岩石<br><code>game:rock-shale</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 页岩砂轮<br><code>toolsmith:grindstone-shale-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 安山岩岩石<br><code>game:rock-andesite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 安山岩砂轮<br><code>toolsmith:grindstone-andesite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/wildcrafttree/recipes/grid/trees-grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-granite"
      },
      "P": {
        "type": "item",
        "code": "wildcrafttree:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "wildcrafttree:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-granite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-sandstone"
      },
      "P": {
        "type": "item",
        "code": "wildcrafttree:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "wildcrafttree:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-sandstone-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-shale"
      },
      "P": {
        "type": "item",
        "code": "wildcrafttree:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "wildcrafttree:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-shale-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-andesite"
      },
      "P": {
        "type": "item",
        "code": "wildcrafttree:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "wildcrafttree:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-andesite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>工作台 · trees-workbench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 3 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>wildcrafttree:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 工作台<br><code>toolsmith:workbench-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
QSQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/wildcrafttree/recipes/grid/trees-workbench.json`

```json
[
  {
    "ingredientPattern": "PPP,QSQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "wildcrafttree:plank-*",
        "quantity": 3
      },
      "Q": {
        "type": "item",
        "code": "wildcrafttree:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:workbench-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>羊毛布条 · fabricstrips-wool-cloth</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 素色羊毛布<br><code>wool:cloth-wool-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 媒染羊毛布<br><code>wool:cloth-wool-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 蓝色羊毛布<br><code>wool:cloth-wool-blue</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 红色羊毛布<br><code>wool:cloth-wool-red</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 黄色羊毛布<br><code>wool:cloth-wool-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 绿色羊毛布<br><code>wool:cloth-wool-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 紫色羊毛布<br><code>wool:cloth-wool-purple</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 粉色羊毛布<br><code>wool:cloth-wool-pink</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 橙色羊毛布<br><code>wool:cloth-wool-orange</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 棕色羊毛布<br><code>wool:cloth-wool-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 灰色羊毛布<br><code>wool:cloth-wool-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 黑色羊毛布<br><code>wool:cloth-wool-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 白色羊毛布<br><code>wool:cloth-wool-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深蓝色羊毛布<br><code>wool:cloth-wool-darkblue</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深棕色羊毛布<br><code>wool:cloth-wool-darkbrown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深绿色羊毛布<br><code>wool:cloth-wool-darkgreen</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 深红色羊毛布<br><code>wool:cloth-wool-darkred</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 羊毛布条<br><code>toolsmith:fabricstrips-wool</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/compatibility/wool/recipes/grid/fabricstrips-wool-cloth.json`

```json
[
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-plain"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/plain"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-mordant"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/mordant"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-blue"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/blue"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-red"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/red"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-yellow"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/yellow"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-green"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/green"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-purple"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/purple"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-pink"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/pink"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-orange"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/orange"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-brown"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/brown"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-gray"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/gray"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-black"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/black"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-white"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/white"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-darkblue"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/darkblue"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-darkbrown"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/darkbrown"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-darkgreen"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/darkgreen"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "wool:cloth-wool-darkred"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-wool",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "wool:block/cloth/wool/darkred"
          }
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>专业工具手柄 · carpentedhandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 砂纸<br><code>toolsmith:sandpaper</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
W_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/carpentedhandle.json`

```json
[
  {
    "ingredientPattern": "KS,W_",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "toolsmith:sandpaper"
      },
      "W": {
        "type": "block",
        "code": "game:supportbeam-*"
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:carpentedhandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>粗糙的工具手柄 · crudehandle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 粗糙的工具手柄<br><code>toolsmith:crudehandle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/crudehandle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "item",
        "code": "game:firewood"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:crudehandle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>布条 · fabricstrips-cloth</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 布料<br><code>game:cloth-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 媒染布料<br><code>game:cloth-mordant</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 蓝色布料<br><code>game:cloth-blue</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 红色布料<br><code>game:cloth-red</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 黄色布料<br><code>game:cloth-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 绿色布料<br><code>game:cloth-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 紫色布料<br><code>game:cloth-purple</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 粉色布料<br><code>game:cloth-pink</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 橙色布料<br><code>game:cloth-orange</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 棕色布料<br><code>game:cloth-brown</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 灰色布料<br><code>game:cloth-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 12**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 黑色布料<br><code>game:cloth-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 13**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 白色布料<br><code>game:cloth-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 14**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:linen-diamond-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 15**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:linen-normal-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 16**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:linen-offset-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

**方案 17**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 C | 名称未汉化（见物品代码）<br><code>game:linen-square-down</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 布条<br><code>toolsmith:fabricstrips-cloth</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/fabricstrips-cloth.json`

```json
[
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-plain"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/plain"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-mordant"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/mordant"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-blue"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/blue"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-red"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/red"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-yellow"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/yellow"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-green"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/green"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-purple"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/purple"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-pink"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/pink"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-orange"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/orange"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-brown"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/brown"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-gray"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/gray"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-black"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/black"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:cloth-white"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/white"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "block",
        "code": "game:linen-diamond-down"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/plain"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "block",
        "code": "game:linen-normal-down"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/plain"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "block",
        "code": "game:linen-offset-down"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/plain"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KC",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "C": {
        "type": "block",
        "code": "game:linen-square-down"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-cloth",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/cloth/linen/plain"
          }
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>皮革条 · fabricstrips-leather</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 橙色皮革<br><code>game:leather-normal-orange</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 黑色皮革<br><code>game:leather-normal-black</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 红色皮革<br><code>game:leather-normal-red</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 蓝色皮革<br><code>game:leather-normal-blue</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 紫色皮革<br><code>game:leather-normal-purple</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 7**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 粉色皮革<br><code>game:leather-normal-pink</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 8**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 白色皮革<br><code>game:leather-normal-white</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 9**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 黄色皮革<br><code>game:leather-normal-yellow</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 10**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 灰色皮革<br><code>game:leather-normal-gray</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

**方案 11**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 L | 绿色皮革<br><code>game:leather-normal-green</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 皮革条<br><code>toolsmith:fabricstrips-leather</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KL
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/fabricstrips-leather.json`

```json
[
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/plain"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-orange"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/orange"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-black"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/black"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-red"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/red"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-blue"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/blue"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-purple"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/purple"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-pink"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/pink"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-white"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/white"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-yellow"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/yellow"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-gray"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/gray"
          }
        }
      }
    }
  },
  {
    "ingredientPattern": "KL",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-green"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-leather",
      "quantity": 2,
      "attributes": {
        "modularPartRenderData": {
          "partTextures": {
            "material": "game:block/leather/green"
          }
        }
      }
    }
  }
]
```

</details>

</details>

<details><summary>生皮条 · fabricstrips-rawhide</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 R | 小型生皮<br><code>game:hide-raw-small</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生皮条<br><code>toolsmith:fabricstrips-rawhide</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KR
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 R | 中型生皮<br><code>game:hide-raw-medium</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生皮条<br><code>toolsmith:fabricstrips-rawhide</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KR
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 R | 大型生皮<br><code>game:hide-raw-large</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生皮条<br><code>toolsmith:fabricstrips-rawhide</code> | 6 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KR
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 R | 巨型生皮<br><code>game:hide-raw-huge</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 生皮条<br><code>toolsmith:fabricstrips-rawhide</code> | 10 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KR
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/fabricstrips-rawhide.json`

```json
[
  {
    "ingredientPattern": "KR",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "R": {
        "type": "item",
        "code": "game:hide-raw-small"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-rawhide",
      "quantity": 2
    }
  },
  {
    "ingredientPattern": "KR",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "R": {
        "type": "item",
        "code": "game:hide-raw-medium"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-rawhide",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "KR",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "R": {
        "type": "item",
        "code": "game:hide-raw-large"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-rawhide",
      "quantity": 6
    }
  },
  {
    "ingredientPattern": "KR",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "R": {
        "type": "item",
        "code": "game:hide-raw-huge"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-rawhide",
      "quantity": 10
    }
  }
]
```

</details>

</details>

<details><summary>坚固皮革条 · fabricstrips-sturdy</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 S | 坚固皮革<br><code>game:leather-sturdy-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 坚固皮革条<br><code>toolsmith:fabricstrips-sturdy</code> | 2 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KS
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/fabricstrips-sturdy.json`

```json
[
  {
    "ingredientPattern": "KS",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "S": {
        "type": "item",
        "code": "game:leather-sturdy-plain"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "toolsmith:fabricstrips-sturdy",
      "quantity": 2
    }
  }
]
```

</details>

</details>

<details><summary>花岗岩砂轮、砂岩砂轮、页岩砂轮、安山岩砂轮 · grindstone</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 花岗岩岩石<br><code>game:rock-granite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 花岗岩砂轮<br><code>toolsmith:grindstone-granite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 砂岩岩石<br><code>game:rock-sandstone</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 砂岩砂轮<br><code>toolsmith:grindstone-sandstone-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 页岩岩石<br><code>game:rock-shale</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 页岩砂轮<br><code>toolsmith:grindstone-shale-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 安山岩岩石<br><code>game:rock-andesite</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 安山岩砂轮<br><code>toolsmith:grindstone-andesite-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PSP
QQQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/grindstone.json`

```json
[
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-granite"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-granite-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-sandstone"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-sandstone-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-shale"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-shale-north",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "PSP,QQQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:rock-andesite"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:grindstone-andesite-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>雕刻工具手柄 · handle</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 W | 变体材料（按代码匹配）<br><code>game:supportbeam-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 雕刻工具手柄<br><code>toolsmith:handle</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
K
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/handle.json`

```json
[
  {
    "ingredientPattern": "K,W",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "W": {
        "type": "block",
        "code": "game:supportbeam-*"
      }
    },
    "width": 1,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:handle",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>木棍、木柴 · recyclehandles</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 粗糙的工具手柄<br><code>toolsmith:crudehandle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木棍<br><code>game:stick</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KH
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 雕刻工具手柄<br><code>toolsmith:handle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木柴<br><code>game:firewood</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KH
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 K | 变体材料（按代码匹配）<br><code>game:knife-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 H | 专业工具手柄<br><code>toolsmith:carpentedhandle</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 木柴<br><code>game:firewood</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KH
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/recyclehandles.json`

```json
[
  {
    "ingredientPattern": "KH",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "toolsmith:crudehandle"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:stick",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KH",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "toolsmith:handle"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:firewood",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KH",
    "ingredients": {
      "K": {
        "type": "item",
        "code": "game:knife-*",
        "isTool": true
      },
      "H": {
        "type": "item",
        "code": "toolsmith:carpentedhandle"
      }
    },
    "width": 2,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:firewood",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>砂纸 · sandpaper</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 手提木桶<br><code>game:woodbucket</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:sand-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 变体材料（按代码匹配）<br><code>game:jug-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 砂纸<br><code>toolsmith:sandpaper</code> | 4 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SG
P_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/sandpaper.json`

```json
[
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:woodbucket"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:glueportion-pitch-hot"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:glueportion-pitch-hot"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  },
  {
    "ingredientPattern": "SG,P_",
    "ingredients": {
      "S": {
        "type": "block",
        "code": "game:sand-*"
      },
      "G": {
        "type": "block",
        "code": "game:jug-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      }
    },
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:glueportion-pitch-hot"
        },
        "requiresLitres": 0.5
      }
    },
    "width": 2,
    "height": 2,
    "output": {
      "type": "item",
      "code": "toolsmith:sandpaper",
      "quantity": 4
    }
  }
]
```

</details>

</details>

<details><summary>工作台 · workbench</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 变体材料（按代码匹配）<br><code>game:saw-*</code> | 未声明；按配方类型判定 | 工具 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 3 | 未声明附加限制 |
| 投入 Q | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 产物 | 工作台<br><code>toolsmith:workbench-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
PPP
QSQ
Q_Q
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/grid/workbench.json`

```json
[
  {
    "ingredientPattern": "PPP,QSQ,Q_Q",
    "ingredients": {
      "S": {
        "type": "item",
        "code": "game:saw-*",
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 3
      },
      "Q": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "block",
      "code": "toolsmith:workbench-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · whetstone</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 产物 | 变体材料（按代码匹配）<br><code>toolsmith:whetstone-{rock}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/toolsmith/recipes/knapping/whetstone.json`

```json
[
  {
    "ingredient": {
      "type": "item",
      "code": "game:stone-*",
      "name": "rock",
      "allowedVariants": [
        "chert",
        "granite",
        "andesite",
        "basalt",
        "peridotite"
      ]
    },
    "pattern": [
      [
        "__________",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "___####___",
        "__________"
      ]
    ],
    "name": "Stone whetstone",
    "output": {
      "type": "item",
      "code": "toolsmith:whetstone-{rock}"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
