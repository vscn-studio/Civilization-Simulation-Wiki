<!-- generated:start -->
# 海浪：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：惊涛骇浪：出海

来源：`assets/roughseas/config/handbook/00-goingtosea.json`。

出海

大海有自己的天气。风起风落，风暴掠过海面，浪在岸边破碎。

每种船都会开裂、灌水或沉没，各有各的方式。

出航之前

- 观察天空和树木：风暴来临之前会露出征兆。参见 [handbook://roughseas-weather] 风、风暴与洋流。

- 选一艘适合这趟航程的船，检查船体有没有裂损。参见 [handbook://roughseas-vessels] 船只及其修理。

- 带上一只舀水用的碗或手提木桶，再带上修补这艘船的材料。参见 [handbook://roughseas-surf] 拍岸浪、进水与舀水。

- 想好要把船留在哪里，又怎样把它留住。参见 [handbook://roughseas-mooring] 系泊与抛锚。

- 把工具和武器从快捷栏移进背包。在水中，盔甲和快捷栏会把你往下拽，穿一整套板甲会很快沉底。

在水中

你漂浮着，水面齐到脸，浪把你托上、放下，并带着你走。

在湖里或河里，不游就会慢慢下沉。按住jump，让头露出水面。

在你头上破碎的浪峰会把你压到水下，并带着你随浪而去。在拍岸浪里，最高的浪会破碎，靠近海滩时几乎每道浪都会破碎。

世界设置

在新建世界界面选择惊涛骇浪游戏风格，世界里会有更多开阔海洋。

大海的每种机制在惊涛骇浪下都有自己的世界设置，默认全部开启。关闭其中一项，就能把它从游戏中去掉。无论开关，风和风暴照样来去。

要在已创建的世界中更改设置，请使用/worldconfig命令，然后重新载入世界。

## 手册 2：惊涛骇浪：风、风暴与洋流

来源：`assets/roughseas/config/handbook/01-weather.json`。

风

风有方向和强度，会在几个小时里变化。

风越大，在开阔水面上吹得越久，浪就越高。大湖也会掀起自己的浪。

树木、云、雨和船的摇晃都随风而动。离岸之前先四下看看，了解风怎么刮。

风暴

风暴在世界中移动，它们生成的地点和季节与真实的风暴相同。

- 飑规模小，多见于温暖湿润的夏季，几小时就过去。

- 大风横扫中纬度地区，冬季最强。它们覆盖大片区域，一刮就是几天。

- 飓风从夏末到秋季在温暖的热带海面上形成。它们持续几天，带来最猛烈的风。

风暴来临前会露出征兆：树梢开始摇摆，天色变暗，涌浪升高。看到这些，就驶向岸边。

闪电

暖风暴会打雷，闪电在风暴中落下。冷大风不打雷。

别让帆船或边架艇驶进雷暴：桅杆会引来闪电，而你就坐在桅杆底下。

雷击会把轻船体打得粉碎：库拉船、树皮舟、木筏或圆皮舟。

洋流

各大洋以巨大而缓慢的环流旋转。最强的洋流沿大洋西岸流动，小海几乎不动。

在中纬度，这股洋流带来暖水，大洋东侧较凉。靠近赤道和靠近两极的地方正好相反。

无人看管的船会随洋流漂走。上岸之前先把它系好或抛锚。行进中的船也会被洋流带着走：逆流划桨或扬帆，走得就少；顺流而行，走得就多。

## 手册 3：惊涛骇浪：船只及其修理

来源：`assets/roughseas/config/handbook/02-vessels.json`。

选择船只

-  [handbook://item-roughseas:reedboat-cattailtops-cattailtops] 芦苇船：两捆芦苇用绳子扎成。造得快，船身低，乘员浑身湿，一次只能在水上待一天。

-  [handbook://item-roughseas:dugout-oak] 独木舟：在水边用五根原木烧空、凿成。江河湖泊上最结实的船体，但在海上横摇剧烈。

-  [handbook://item-roughseas:coracle] 圆皮舟：在地上摆一张木条网格，向上弯成筐形，再蒙上兽皮。它能原地转向，可以背在背上。

-  [handbook://item-roughseas:barkcanoe-birch] 树皮舟：从活的桦树、榆树或云杉上剥下一整张树皮，就地装上骨架。速度快，脆弱，能闯急流。

-  [handbook://item-roughseas:currach] 皮面库拉船：在地上把两根长木条绑成舷缘，倒扣着在兽皮下搭好骨架，再翻过来。能载货，能越过涌浪。

-  [handbook://item-roughseas:outrigger-oak] 边架艇：一条独木舟就地装上浮木、横杆和船帆。在开阔海面上又快又稳。

-  [handbook://item-boat-sailed-oak] 帆船：坚固宽敞，适合远航。

每种船的手册页面都写明了建造方法。

行船

坐在掌舵的座位上，手持工具。walkforward和walkbackward让船前进和后退，walkleft和walkright让船转向。

- 手持 [handbook://item-roughseas:paddle-oak] 单叶桨，在任何深度的水里都能划。

- 手持 [handbook://item-roughseas:pole-oak-3] 木杆撑水底。水深比木杆短约一米时，木杆能撑到水底。简易 [handbook://item-oar-crude-aged] 桨就是这样一根两米长的木杆。

- 库拉船空手划：它在桨桩上有两支自带的长桨。

又长又窄的船体走得快，圆的或宽的走得慢。载货会让任何船变慢。

划桨、撑船和摇长桨都会让你饥饿。

状态

每种船都有船体，撞击会让被撞的部位开裂：船首、船舷、船尾一侧或船底。

看向船只，就能看到每处裂损的程度，从有划痕、开裂、破裂到破洞。你还能看到每分钟漏进多少升水，以及干舷，也就是船舷高出水面多少。

每处裂损都会显示在船体上相应的位置。

把船拿起再放下，状态保持不变。

什么会撞裂船体

- 高速撞上礁石、岸边或别的船。船上载得越多，撞得越重：乘员、货物，尤其是舱底水。缓缓靠岸，船体就不会受损。

- 急流，它会重创除树皮舟和圆皮舟外所有船体的船底。

- 碎浪、闪电、爆炸和武器。

船体的材料决定它能承受多少：能撞裂树皮舟的一击，在帆船上只留下一道划痕。

用硬木造独木舟或边架艇，因为木材越硬，船体越结实。任何树都能用，其他模组的树也行。

木头几乎不会磨损，所以木制船体不需要保养。

漏水

船底的裂缝总会漏水。船舷的裂缝要等载重把船压低后才会漏。

漏进的水积在舱底，直到船被灌满。裂缝一多，怎么舀水都赶不上。参见 [handbook://roughseas-surf] 拍岸浪、进水与舀水。

只有极其猛烈的一击，或把最后一处完好部位撞出破洞的一击，才会让船体当场解体。

木筏、芦苇与兽皮

- 木筏没有能积水的船体，撞击会让它的绑扎松动。绑扎全部松脱后，木筏就散成原木和绳子。

- 芦苇船的芦苇捆受撞击时会变形，本身不受损。但芦苇会吸水：下水一天后乘员就坐在与水面齐平的位置，不出四天船就沉到水底。把它放在岸上晒太阳晾干。每晾干一次，它就腐烂一点。

- 兽皮蒙面的接缝会渗水。每隔几天用炼制脂肪涂抹一次，就能止住。未经鞣制的兽皮漂在温水里几天就会腐烂，所以要把船放在岸上晾干。看向船只，就知道它什么时候需要这些处理。

- 边架艇的浮木伸在一侧，所以从那一侧来的撞击会让浮木的绑扎松动，而不会撞裂船体。在绑扎脱落之前用 [handbook://item-flaxtwine] 亚麻线重新绑紧，否则浮木和帆具会散掉，只剩一条普通的独木舟。

修补

手持这艘船自己的材料对着船体，按住rightmouse不放。每块补丁都要花些时间，按住够久才会补上。

补丁打在你看着的部位；那里若完好，就打在裂得最重的地方。

每打一块补丁都是重活，会让你饥饿。船体没有可补之处时，会告诉你。

[handbook://item-flaxtwine] 亚麻线能重新绑紧木筏的绑扎，同种木材的木板能修补帆船。每种船的手册页面都写明了用什么修补。

芦苇船无法修补。毁坏的船就没了，只剩漂浮的残骸。

## 手册 4：惊涛骇浪：拍岸浪、进水与舀水

来源：`assets/roughseas/config/handbook/03-surf.json`。

拍岸浪

水深不够浪高时，浪就会破碎。恶劣天气下，靠近海滩的最后一段水面全是拍岸浪。

碎浪打在船的哪一侧，就可能撞裂那一侧的船体。

在陡峭的海滩上，大多数浪会卷碎，而卷碎的浪峰打得猛烈得多：能把兽皮船打出破洞。

要在天气平静时或在避风的海湾里靠岸，那里浪很低。

在远海，浪也会时不时破碎，风越大，破碎得越频繁。

每个碎浪都会化作一层薄薄的水冲上海滩，再退回去。风暴中，浪会冲得更远。

浪遇到悬崖、码头或你砌的墙时，会贴着墙面立起，再退回海里。碎浪会把水沫高高溅上墙面。在阶梯状的海滩上，薄薄的水层爬不上去的每一级台阶，都会溅起自己的水沫。

海滩下面有水，一直延伸到浪冲到的地方。在那里挖个坑，挖到水面的高度，坑里就会灌满水。

船上进水

比船舷高的浪会打进船里，裂缝会让水从下面渗进来。

有船体的船会把这些水积在舱底。木筏和芦苇船不积水：水直接从中流过。

看向船只，就能看到舱底积了多少升水，每分钟漏进多少升水，以及干舷，也就是船舷高出水面多少。船里的水也看得见。

舱底的水会让船变沉：它吃水更深，更容易上浪，摇晃更剧烈，走得更慢。乘员和货物也同样让船变沉。

干舷一旦耗尽，不管船有没有裂缝，海水都会漫过船舷把船灌满。

灌满水

舱底积满水，船就被灌满了。被灌满的船既不能划，也不能坐。

轻船被灌满后与水面齐平，漂着不沉。重船会沉下去：带压舱物的帆船、用比水重的木材造的船，或载货过重的船。

抓住被灌满的船，等海面平静后把水舀干，或者游开。

沉没的船连同货物躺在水底。潜下去把货物取出来，或者用斧头把船拆成残骸。

木筏不会被灌满，即使被压进水里也能托住乘员。芦苇船会一直吸水，直到沉没。

舀水

手持空的 [handbook://block-bowl-red-fired] 碗、 [handbook://block-jug-red-fired] 水壶或 [handbook://block-woodbucket] 手提木桶。

站在船边或坐在船里，看向船内，按住rightmouse。每舀一下，就把水泼出舷外。

如果看向海面，你会从海里舀水装进容器。

手提木桶舀得最快，能跟上一处严重的漏水。漏处一多，怎么舀都赶不上，所以要修补裂缝。

风暴中要不停地舀水，因为每道浪都会打进更多的水。风暴中别把船独自留在海上：没人舀水，它就会被灌满。

## 手册 5：惊涛骇浪：系泊与抛锚

来源：`assets/roughseas/config/handbook/04-mooring.json`。

无人看管的船会随洋流漂走，风暴还可能把它抛上岸。离开船之前，把它系好或抛锚。

系泊

用 [handbook://item-rope] 绳子把船系在岸上的 [handbook://block-woodenfence-oak-ew-free] 栅栏柱上，就像拴牲畜一样：手拿绳子对船按rightmouse，再对栅栏柱按一次。一条船只能系一根绳子。

手拿绳子按toolmodeselect，可以把绳子收短或放长，范围是1.5到10米。船在绳长范围内自由漂动，到了绳子尽头就被绳子拉住。

- 绳子短，船就离得近，但每当浪把船推到绳子尽头，绳子都会猛地一拽。

- 绳子长，拽得就轻，但船摆动的范围更大，离岸更近。

一拽之力超过绳子能承受的，绳子就会断，掉在栅栏柱旁。在平静的海湾里什么都不会断；风暴中，长绳比短绳撑得更久。

抛锚

帆船的船首载着一只 [handbook://item-anchor-stone] 石锚。只有帆船能抛锚。

空手对锚按rightmouse抛锚，再按一次起锚。

锚会放出水深五倍的锚绳。它自带的锚绳长120米。

水更深时，对着桅杆脚按ctrl + rightmouse，在那里存放一卷 [handbook://item-roughseas:anchorwarp] 锚缆。它能多放出90米。

- 锚靠自身重量抓住：在开阔海域的洋流中，它能把船拴住，涌浪则会让它慢慢走锚。

- 遇到强流或风暴时会走锚，船随锚一起漂，比水流慢。

- 水深超过锚绳长度，锚就悬在水中，什么也抓不住。

- 锚绳一断，锚也跟着丢了。

不管船上有没有人坐着，锚和锚绳都会把船拴住：划船离开，到了锚绳尽头就会被拦住。

离船

抛了锚的船受浪更平缓，但仍会上浪进水。

在岸边又没人在附近时，风暴可能把系泊的船抛上海滩。把船停在远离岸边的地方并抛稳锚，免得被冲上海滩，船上也别留下要紧的东西。

## 手册 6：惊涛骇浪：游泳

来源：`assets/roughseas/config/handbook/05-swimming.json`。

游泳

你靠身体排开的水浮起来，并以训练有素的游泳者的力气游动。浪、水流和破碎的浪峰会像推动船一样推动你。

浮在水面

- 在海里，你漂浮时脸露出水面。浪峰盖过你的脸时，你就吸不到气，直到它过去。

- 在湖里或河里，你浮得更低，水面齐到嘴边。按住jump，在原地踩水，让头露出水面。

- 你的肺里一直充满空气。潜得深了，水会压缩这些空气，你就会下沉。往上游才能回来。

游动

- 按住方向键，朝你看的方向游。往下看就下潜，往上看就浮出水面。

- 比你快的水流会带着你走。要横着穿过水流游向岸边，而不是逆流而游。

- 在你头上破碎的浪峰会把你压到水下，并带着你随浪而去。靠近海滩时几乎每道浪都会破碎。

身上带的东西

- 盔甲以及快捷栏里的工具和武器会把你往下拽。背包和材料不会。

- 工具的金属或石头头部会把你往下拽，木柄会把你托起。木盔甲像浮子一样托起你，金属盔甲会让你下沉。

- 带的东西太重、游不上去时，游戏会告诉你带了多重。把工具移进背包，或者沿着水底走到岸边。

在水底

- 不管带了多少东西，你都能在水底用双脚站立和行走。

- 按jump用双腿蹬离水底，向上升起。双脚一离开水底，你就在游泳了。

上岸

- 游到岸边，就能从深水里爬上去。

- 水只到胸口的地方，像在陆地上一样走动并跳上台阶。

世界设置

- 关闭真实游泳，就会像原版游戏一样游泳。

- 把游泳力量设为2×或3×，划水更有力，游得更快。游戏自带的行走速度设置也会改变你的划水。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>变体材料（按代码匹配） · lath</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>roughseas:lath-*-2-dry</code> | 1 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 0.16 升 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lath-{wood}-2-wet</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>roughseas:lath-*-3-dry</code> | 1 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 0.24 升 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lath-{wood}-3-wet</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>roughseas:lath-*-4-dry</code> | 1 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 0.32 升 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lath-{wood}-4-wet</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 1 | 变体材料（按代码匹配）<br><code>roughseas:lath-*-5-dry</code> | 1 | 未声明附加限制 |
| 投入 2 | 水<br><code>game:waterportion</code> | 0.4 升 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lath-{wood}-5-wet</code> | 1 | 未声明附加限制 |

**加工条件：** 密封时间（游戏小时）：48。

**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/roughseas/recipes/barrel/lath.json`

```json
[
  {
    "code": "soakedlath2",
    "sealHours": 48,
    "ingredients": [
      {
        "type": "item",
        "code": "roughseas:lath-*-2-dry",
        "name": "wood",
        "quantity": 1
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 0.16,
        "consumeLitres": 0.16
      }
    ],
    "output": {
      "type": "item",
      "code": "roughseas:lath-{wood}-2-wet",
      "stackSize": 1
    }
  },
  {
    "code": "soakedlath3",
    "sealHours": 48,
    "ingredients": [
      {
        "type": "item",
        "code": "roughseas:lath-*-3-dry",
        "name": "wood",
        "quantity": 1
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 0.24,
        "consumeLitres": 0.24
      }
    ],
    "output": {
      "type": "item",
      "code": "roughseas:lath-{wood}-3-wet",
      "stackSize": 1
    }
  },
  {
    "code": "soakedlath4",
    "sealHours": 48,
    "ingredients": [
      {
        "type": "item",
        "code": "roughseas:lath-*-4-dry",
        "name": "wood",
        "quantity": 1
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 0.32,
        "consumeLitres": 0.32
      }
    ],
    "output": {
      "type": "item",
      "code": "roughseas:lath-{wood}-4-wet",
      "stackSize": 1
    }
  },
  {
    "code": "soakedlath5",
    "sealHours": 48,
    "ingredients": [
      {
        "type": "item",
        "code": "roughseas:lath-*-5-dry",
        "name": "wood",
        "quantity": 1
      },
      {
        "type": "item",
        "code": "game:waterportion",
        "litres": 0.4,
        "consumeLitres": 0.4
      }
    ],
    "output": {
      "type": "item",
      "code": "roughseas:lath-{wood}-5-wet",
      "stackSize": 1
    }
  }
]
```

</details>

</details>

<details><summary>锚缆、绳索捆 · anchorwarp</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 锚缆<br><code>roughseas:anchorwarp</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RRR
RRR
RRR
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 W | 锚缆<br><code>roughseas:anchorwarp</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 绳索捆<br><code>game:rope</code> | 9 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
W
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/roughseas/recipes/grid/anchorwarp.json`

```json
[
  {
    "ingredientPattern": "RRR,RRR,RRR",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:rope"
      }
    },
    "width": 3,
    "height": 3,
    "output": {
      "type": "item",
      "code": "roughseas:anchorwarp"
    }
  },
  {
    "ingredientPattern": "W",
    "ingredients": {
      "W": {
        "type": "item",
        "code": "roughseas:anchorwarp"
      }
    },
    "width": 1,
    "height": 1,
    "output": {
      "type": "item",
      "code": "game:rope",
      "quantity": 9
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · lathbundles</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>roughseas:lath-*-2-dry</code> | 32 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 26 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lathbundle-{wood}-2-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>roughseas:lath-*-3-dry</code> | 32 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 38 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lathbundle-{wood}-3-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>roughseas:lath-*-4-dry</code> | 32 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 51 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lathbundle-{wood}-4-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 4**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 L | 变体材料（按代码匹配）<br><code>roughseas:lath-*-5-dry</code> | 32 | 未声明附加限制 |
| 投入 S | 变体材料（按代码匹配）<br><code>game:stone-*</code> | 64 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lathbundle-{wood}-5-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
LS
```

**方案 5**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 泡透的{0}木条捆，{1}米<br><code>roughseas:lathbundle-*-soaked</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lath-{bundle}-wet</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

**方案 6**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | {0}木条捆，{1}米<br><code>roughseas:lathbundle-*-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lath-{bundle}-dry</code> | 32 | 未声明附加限制 |

**加工条件：** 网格宽度：1；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/roughseas/recipes/grid/lathbundles.json`

```json
[
  {
    "name": "2 m laths weighted with stones into a bundle",
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "roughseas:lath-*-2-dry",
        "name": "wood",
        "quantity": 32
      },
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 26
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "roughseas:lathbundle-{wood}-2-dry"
    }
  },
  {
    "name": "3 m laths weighted with stones into a bundle",
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "roughseas:lath-*-3-dry",
        "name": "wood",
        "quantity": 32
      },
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 38
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "roughseas:lathbundle-{wood}-3-dry"
    }
  },
  {
    "name": "4 m laths weighted with stones into a bundle",
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "roughseas:lath-*-4-dry",
        "name": "wood",
        "quantity": 32
      },
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 51
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "roughseas:lathbundle-{wood}-4-dry"
    }
  },
  {
    "name": "5 m laths weighted with stones into a bundle",
    "ingredientPattern": "LS",
    "ingredients": {
      "L": {
        "type": "item",
        "code": "roughseas:lath-*-5-dry",
        "name": "wood",
        "quantity": 32
      },
      "S": {
        "type": "item",
        "code": "game:stone-*",
        "quantity": 64
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "roughseas:lathbundle-{wood}-5-dry"
    }
  },
  {
    "name": "A soaked bundle untied into wet laths",
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "roughseas:lathbundle-*-soaked",
        "name": "bundle"
      }
    },
    "width": 1,
    "height": 1,
    "output": {
      "type": "item",
      "code": "roughseas:lath-{bundle}-wet",
      "quantity": 32
    }
  },
  {
    "name": "A dry bundle untied into its laths",
    "ingredientPattern": "B",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "roughseas:lathbundle-*-dry",
        "name": "bundle"
      }
    },
    "width": 1,
    "height": 1,
    "output": {
      "type": "item",
      "code": "roughseas:lath-{bundle}-dry",
      "quantity": 32
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · laths</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | {0}木杆，{1}米<br><code>roughseas:pole-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:lath-{pole}-dry</code> | 16 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/roughseas/recipes/grid/laths.json`

```json
[
  {
    "name": "Laths split from a pole",
    "ingredientPattern": "AP",
    "ingredients": {
      "A": {
        "type": "item",
        "tags": [
          "tool-axe"
        ],
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "roughseas:pole-*",
        "name": "pole"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "roughseas:lath-{pole}-dry",
      "quantity": 16
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配） · propulsion</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>roughseas:pole-*-2</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:paddle-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AKP
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>roughseas:pole-*-3</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 变体材料（按代码匹配）<br><code>roughseas:lath-*-2-dry</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:tholeoar-{wood}</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
AK
PL
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/roughseas/recipes/grid/propulsion.json`

```json
[
  {
    "name": "Paddle",
    "ingredientPattern": "AKP",
    "ingredients": {
      "A": {
        "type": "item",
        "tags": [
          "tool-axe"
        ],
        "isTool": true
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "roughseas:pole-*-2",
        "name": "wood"
      }
    },
    "width": 3,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "roughseas:paddle-{wood}"
    }
  },
  {
    "name": "Thole oar",
    "ingredientPattern": "AK,PL",
    "ingredients": {
      "A": {
        "type": "item",
        "tags": [
          "tool-axe"
        ],
        "isTool": true
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "roughseas:pole-*-3",
        "name": "wood"
      },
      "L": {
        "type": "item",
        "code": "roughseas:lath-*-2-dry"
      }
    },
    "width": 2,
    "height": 2,
    "shapeless": true,
    "output": {
      "type": "item",
      "code": "roughseas:tholeoar-{wood}"
    }
  }
]
```

</details>

</details>

<details><summary>变体材料（按代码匹配）、名称未汉化（见物品代码） · vessels</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 R | 变体材料（按代码匹配）<br><code>game:*</code> | 48 | 允许变体：['papyrustops', 'cattailtops', 'thatch'] |
| 投入 L | 绳索捆<br><code>game:rope</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 变体材料（按代码匹配）<br><code>roughseas:reedbundle-{reeds}-none-we</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
RRR
LKL
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 木柴<br><code>game:firewood</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>roughseas:wedge-we-0</code> | 未声明；按配方类型判定 | 未声明附加限制 |

**加工条件：** 网格宽度：2；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KF
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/roughseas/recipes/grid/vessels.json`

```json
[
  {
    "name": "Reed bundle",
    "ingredientPattern": "RRR,LKL",
    "ingredients": {
      "R": {
        "type": "item",
        "code": "game:*",
        "name": "reeds",
        "allowedVariants": [
          "papyrustops",
          "cattailtops",
          "thatch"
        ],
        "quantity": 48
      },
      "L": {
        "type": "item",
        "code": "game:rope"
      },
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      }
    },
    "width": 3,
    "height": 2,
    "output": {
      "type": "block",
      "code": "roughseas:reedbundle-{reeds}-none-we"
    }
  },
  {
    "name": "Splitting wedge",
    "ingredientPattern": "KF",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "F": {
        "type": "item",
        "code": "game:firewood"
      }
    },
    "width": 2,
    "height": 1,
    "shapeless": true,
    "output": {
      "type": "block",
      "code": "roughseas:wedge-we-0"
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
