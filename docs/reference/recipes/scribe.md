<!-- generated:start -->
# 书写：配方与手册

[返回资料库](/reference/) · [食物检索](/guide/food-catalogue)

配方显示安装包原始条件，`*` 和 `{变量}` 需要代入允许的变体；未声明 enabled 不等于最终启用。数量未声明时以游戏配方类型的默认规则为准。

## 手册 1：Scribe 模组：入门

来源：`assets/scribe/config/handbook/00-getting-started.json`。

欢迎使用 Scribe

Scribe 是一个帮助你追踪自己想做之事的模组。用 Scribe 记写任务和笔记、将它们置顶到持久的 HUD 上，或丰富你与其他玩家的互动体验。

如何开始？

Scribe 提供了若干你可制作的方块和物品：

[handbook://item-scribe:scribetablet-clay-red] 黏土泥板 —— 你随身携带的一块石板。这是你在 Scribe 中能制作的第一样东西。一个简单而有限的任务管理器。会干燥硬化，但可用水再次软化。

[handbook://item-scribe:scribetablet-wax] 蜡板 —— 一种更可靠的泥板。需要锯子，但仍有限制。

[handbook://block-scribe:scribelectern] 讲台 —— 一个放置的方块。人人皆可共享与阅读，带有编辑锁和一本"访客留言簿"。

[handbook://block-scribe:chalkboard-north] 黑板 —— 与讲台相同的标签页，像画一样挂在墙上。

[handbook://block-scribe:scriptorium] 缮写室 —— 一个专用的共享书写站，聚落的协作中心。

[handbook://item-scribe:scribenotebook] 笔记本 —— 一份个人携带的文档，随你的物品栏移动，并保有它自己的"历史记录"编年史。

[handbook://item-scribe:scribeclockmakernotebook] 钟表匠笔记本 —— 一本增加了倒计时"计时器"的笔记本。

使用 Scribe

Scribe 力求易于使用。手持 Scribe 物品时，按 rightmouse 打开它。对于泥板，你随后可以点击"添加任务"按钮，或按 Enter 来创建一个。你可以删除任务、将它置顶到 HUD，或调整它的顺序。更多细节见手册中的  [handbook://craftinginfo-scribe-editor-reference] Scribe 模组：编辑器参考。

视图

更高级的 Scribe 物品（笔记本、讲台）拥有高级的多重视图。

"阅读"：滚动、完成任务并将其置顶到你的 HUD。

"任务编辑器"：还可添加、编辑、重排和删除行。在讲台上，同一时间只有一名玩家可以编辑。

"置顶"：你在每一块讲台和每一本笔记本上的所有置顶项，均可就地编辑。

"设置"：所有 Scribe 偏好设置。

其他："访客留言簿"（讲台、缮写室和黑板）、"历史记录"（笔记本）、"计时器"（钟表匠笔记本）

要完整浏览每个标签页，请参阅  [handbook://craftinginfo-scribe-views] Scribe 模组：标签页与视图。

任务类型

除了普通任务和笔记，Scribe 还有三种绑定物品的任务类型："物品计数器"（你所携带物品的实时 拥有 / 需要 计数）、"链接"（快速的手册交叉引用）和"制作任务"（绑定配方、自动生成原料采购清单的目标）。这三种都从物品自己的手册页添加。参阅  [handbook://craftinginfo-scribe-task-types] Scribe 模组：任务与笔记类型。

置顶任务 HUD

置顶任何任务，使其常驻于游戏世界之上的常显叠加层。有关置顶、勾选完成和折叠 HUD 的工作方式，参阅  [handbook://craftinginfo-scribe-pinned-hud] Scribe 模组：置顶任务 HUD。

分配与任务

从  [handbook://block-scribe:scribeassignmentdesk] 任务分配台直接把一项任务交给另一名玩家，并在你自己的或一个独立的  [handbook://block-scribe:scribeinbox-up] 收件箱中接收——当面交付，或在服务器要求时由  [handbook://item-scribe:tasknotice] 任务通知手工携带。参阅  [handbook://craftinginfo-scribe-assignments] Scribe 模组：分配任务。如果你还使用任务（quest）模组，Scribe 也能链接甚至自动追踪它的任务——参阅  [handbook://craftinginfo-scribe-quests] Scribe 模组：任务链接。

## 手册 2：Scribe 模组：编辑器参考

来源：`assets/scribe/config/handbook/01-editor-reference.json`。

编辑器功能

以下功能在你能编辑 Scribe 物品中任务的任何地方均可用。请注意，所有输入都会自动保存，无需担心按下 escapemenudialog。

以下许多按键是硬编码的，无法修改或重新映射。

行导航

Tab —— 移动到下一行。

Shift+Tab —— 移动到上一行。

Cmd+Up（macOS）或 Ctrl+Up / Ctrl+Home（Windows） —— 跳到第一行。

Cmd+Down 或 Ctrl+Down / Ctrl+End —— 跳到最后一行。

Enter —— 插入一个新的空任务。

Shift+Enter —— 在当前行内插入一个硬换行。

Esc —— 提交并关闭讲台。

光标移动

方向键 —— 移动一个字符或一行。

Alt/Option+Left/Right —— 按整词跳过。

Cmd+Left/Right（macOS）或 Home/End —— 跳到行首或行尾。

Ctrl+Left/Right（Windows） —— 按整词跳过。

在任意移动键上按住 Shift 可扩展选区。

选择与剪贴板

Ctrl/Cmd+A —— 选中焦点字段中的全部文本。

Ctrl/Cmd+C —— 复制。Ctrl/Cmd+X —— 剪切。Ctrl/Cmd+V —— 粘贴。

在文本被选中时输入会替换选区。

添加任务

"添加任务"按钮：位于"编辑器"底部。

Enter：在当前行正下方插入一个任务。两者都会创建一个可立即输入的空行。

快速添加（对讲台、笔记本或湿润泥板执行 Shift+secondarymouse）：会打开编辑器，并在列表顶部放置一个全新的空任务，光标就绪。

选择种类："添加任务"按钮旁的小箭头会打开一个下拉菜单，列出下面的每一种类型；在那里选择 Task 或 Note 会立即添加，并成为按钮的新默认值。"物品计数器"、"链接"和"制作任务"也出现在同一下拉菜单中，但在那里点击它们只会打开指南，因为每种都需要绑定到具体的物品或配方。要真正添加一个，请打开该物品自己的手册页，滚动到底部它的"添加到 Scribe"标题处，改为点击"添加物品计数器"、"添加链接"或"添加制作任务"。轻点行的拖动手柄（不按住以重排）可将其缩进为子任务，再次轻点则可提升它。

任务与笔记的类型

Scribe 可容纳五种条目。完整说明参阅  [handbook://craftinginfo-scribe-task-types] Scribe 模组：任务与笔记类型。

"任务"：一个可勾选完成、置顶到 HUD 并重排的复选框条目。

"笔记"：一段没有复选框或完成状态的自由格式文本。

"物品计数器"：基于你所携带之物、对某特定物品的实时 拥有/需要 计数。

"链接"：一键打开某物品手册页的快捷方式。

"制作任务"：一个绑定配方、附带你仍需原料清单的目标。

空任务行为

当你将焦点移离一个任务行时（Tab、Shift+Tab、Enter、Esc 或点击别处），该行会被保存。然而，空行会被删除。仍处于焦点的空行不会被删除。

提交时，非空行的尾部空行和尾部空白会被修剪。（由 Shift+Enter 产生的）内部换行会被保留。

## 手册 3：Scribe 模组：置顶任务 HUD

来源：`assets/scribe/config/handbook/02-pinned-hud.json`。

置顶任务 HUD 是一个常显叠加层，它在游戏世界之上显示你的置顶任务，让你追踪的事项无需打开任何 Scribe 物品即可保持在视野中。

置顶任务

在"阅读"或"任务编辑器"视图中将鼠标悬停在任务行上，点击置顶图标即可将其加入你的 HUD。置顶是每名玩家各自独立的——在共享讲台上置顶一项任务只影响你自己的 HUD，绝不会影响他人。你的置顶项会从你使用的每一件 Scribe 物品（泥板、笔记本和讲台）中汇集，并全部一起列在"置顶"标签页中，可就地编辑。

物品计数器、链接和制作任务

你也可以置顶"物品计数器"、"链接"和"制作任务"行：置顶的物品计数器或制作任务会在 HUD 上直接显示其实时的 拥有 / 需要 计数，点击置顶的链接则会打开其手册页。参阅  [handbook://craftinginfo-scribe-task-types] Scribe 模组：任务与笔记类型。

勾选完成任务

从 HUD 勾选完成一项任务会开始 1.5 秒的撤销窗口。在该窗口期间任务文字会随倒计时淡出，取消勾选则完全撤销该操作。窗口结束后，完成将按你选择的策略执行——保持置顶、取消置顶、沉至底部或删除任务。你在讲台或笔记本内完成的任务也适用相同的策略。

折叠 HUD

按 scribepinhud（可在控制：Scribe 模组 类别下重新绑定）或点击"置顶"标题栏，即可将 HUD 收缩为仅剩标题栏。你也可以通过 Scribe 设置中的"折叠 HUD"让它启动时即为折叠状态。

溢出

HUD 一次显示的行数有限（由设置中的"HUD 最大行数"决定，1–10）。当你的置顶项多于此数时，多出的会在底部汇总为一行"+N more"。

位置与大小

有关 HUD 摆放的一切都在 Scribe 设置中："HUD 位置"选择它锚定的屏幕角落或边缘，"HUD 偏移"从该处微调，"HUD 任务宽度"设定每行的宽度，"HUD 文字大小"缩放文字。

计时器

一个正在运行的  [handbook://item-scribe:scribeclockmakernotebook] 钟表匠笔记本计时器也会出现在 HUD 上倒计时；结束时它会闪烁并摇晃以引起你的注意。

时空风暴

在时空风暴期间——或当你的稳定度降得很低时——HUD 会打乱它的文字，其标题会显示为"挺过风暴"。在设置中关闭"风暴扰乱"可让它保持完全清晰易读。

## 手册 4：Scribe 模组：任务与笔记类型

来源：`assets/scribe/config/handbook/03-task-types.json`。

Scribe 有五种可以添加到任务清单的行：两种你自己添加的自由格式类型，以及三种绑定到特定物品或配方的类型。

任务

任务是一个可勾选完成、置顶到 HUD 并重排的复选框条目。用"添加任务"按钮（或 Enter 键）在"任务编辑器"中添加一个。

笔记

笔记是一段没有复选框或完成状态的自由格式文本，用于你只想保留而非完成的信息。用同一个按钮添加：点击"添加任务"旁的小箭头，从下拉菜单中选择"笔记"。

物品计数器

物品计数器是一个绑定到某物品的行，显示实时的 拥有 / 需要 计数，跟随你所携带的物品。例如，一个针对 20 根铁锭的物品计数器，在你携带十二根时显示 12/20，并在你集齐全部二十根后自动完成。用该行的上/下步进器设定目标数量。

链接

链接是一个行，点击它的标签会打开所链接物品的手册页，是放在相关任务旁的快速交叉引用。链接没有复选框，也没有完成状态。熟食手册页也提供"添加链接"，因此一份炖菜或馅饼可以摆在你其他目标旁边。

制作任务

制作任务是一个绑定到某物品某个网格配方的目标。它像物品计数器一样追踪产出，并在其下方构建一份原料子任务采购清单：每种原料一个物品计数器，数量为这批次所需的量。如果该物品有多个配方变体，手册页会为每个提供一个带标签的链接。液体原料以升为单位追踪。完成产出使用与物品计数器相同的计数器完成设置。

添加物品计数器、链接或制作任务

这三种无法从编辑器的添加任务按钮添加，因为它们需要知道你指的是哪个物品（以及哪个配方）。而是要打开该物品的手册页，滚动到底部，点击"添加物品计数器"、"添加链接"或"添加制作任务"，它们位于"添加到 Scribe"标题下。

它落在哪里

点击"添加物品计数器"、"添加链接"或"添加制作任务"会把该行添加到你打开着的任意 Scribe 界面。如果没有打开任何界面，它会被添加到你最近使用的 Scribe 物品（或你携带的第一件）。如果你完全没有 Scribe 物品，系统会告诉你需要先有一件。

## 手册 5：Scribe 模组：转录标签页

来源：`assets/scribe/config/handbook/04-transcribe.json`。

"转录"标签页位于  [handbook://block-scribe:scriptorium] 缮写室上，它会把一件 Scribe 物品上的内容复制到另一件上——用来复制一份清单、分发计划的副本，或把笔记本备份到泥板上。

复制

把你想从中复制的物品放入"复制来源"槽，把你想复制到的物品放入"粘贴至"槽。两个槽都只接受 Scribe 物品（笔记本、泥板，以及拾起的讲台或缮写室）。按下"复制"，来源的任务和笔记就会被写入目标，替换它原有的一切。

此后两份文档完全独立：编辑其一绝不会改变另一份。来源保持不变——只有目标被覆盖。

覆盖

如果"粘贴至"的物品已有任务，第一次按下"复制"会变红并警告它将覆盖多少任务；再按第二次以确认。改动任一槽都会取消待确认操作。复制到空白物品会立即发生，无需确认。

无法复制时

"复制"会被禁用（变灰），直到两个槽都放有 Scribe 物品且目标能够接受该复制。硬化或烧制的泥板无法写入。泥板还有任务数上限，因此任务数多于目标容量的来源会被拒绝。按钮的工具提示会说明是哪条规则在阻止它。

导入 / 导出

该标签页的下半部分通过你系统的剪贴板以纯文本形式移动 Scribe 文档——用于备份清单、分享清单，或在另一个程序中编辑它。把一件 Scribe 物品放入"导入 / 导出"槽，然后：

这里有两条通道，对应两项工作。JSON 是精确通道——一份完整、无损的副本，最适合备份清单或在物品间原样搬移。TSV 是宽容通道——一个电子表格友好的表格（类似 CSV），易于手动编辑，回导时能容忍小错误，代价是损失一点细节。想要文档被精确保留时用 JSON；想要编辑它时用 TSV。

"复制为 JSON"会把精确副本写入剪贴板。请把它粘贴到纯文本编辑器——Windows 上的 Notepad++ 或 macOS 上的 CotEditor——而不是文字处理软件，后者可能会悄悄"修正"引号或空格而破坏导入。保存或分享该文本，稍后再"导入"回来。

"复制为 TSV"会写出一个制表符分隔的表格——把它直接粘贴到电子表格（Excel、Google Sheets）中，即可在 Type, Done, Text, Special, Count, Depth 各列下看到每个任务一行。编辑文字或某物品计数器的数量，把这些行复制回来，再"导入"它们。

"导入"会读取剪贴板，自行判断它是 JSON 还是 TSV，并用上面"覆盖 / 追加"的选择将其写入槽中的物品——"覆盖"会替换该物品的任务（当它非空时，采用与复制相同的红色两次按下确认），"追加"则把它们加在现有任务之后。其物品在本游戏中找不到的计数器或链接会被作为普通任务导入，并会有消息告知你有多少。剪贴板上任何不是 Scribe 导出内容的东西都会被拒绝，不作任何改动。

导入的任务始终是未置顶的——导入绝不会触及你的置顶项，无论在本世界还是其他任何世界。

## 手册 6：Scribe 模组：标签页与视图

来源：`assets/scribe/config/handbook/05-views.json`。

大多数 Scribe 界面共享同一组标签页，通过右侧边栏的图标按钮切换。出现哪些标签页取决于界面——一个放置的方块、一件携带的物品，还是缮写室。

"阅读" —— 以可滚动的列表查看所有任务和笔记。在此阅读、置顶和勾选完成任务。

"任务编辑器" —— 完整的文档编辑：添加任务、编辑文字、置顶行、拖动重排以及删除行。更改会在你输入时自动保存。在共享的放置界面上，同一时间只有一名玩家可以编辑。

"置顶" —— 你所有的置顶任务，从你使用的每一件 Scribe 物品中汇集而来，可就地编辑。

"设置" —— 打开 Scribe 设置面板（与置顶任务 HUD 上齿轮图标所打开的面板相同）。

取决于界面的标签页

"访客留言簿" —— 在放置界面上： [handbook://block-scribe:scribelectern] 讲台、 [handbook://block-scribe:scriptorium] 缮写室和黑板。一份公开的日志，记录谁曾到访，每条都带有到访日期和一条可选的简短留言。由于放置的方块是共享的，它的"访客留言簿"是供所有打开它的人查看的。

"历史记录" —— 在携带的物品上： [handbook://item-scribe:scribenotebook] 笔记本和钟表匠笔记本。一份私人的、每件物品独立的编年史，会自动填充并随物品移动——是共享"访客留言簿"的个人对应物。

"转录"和"导入 / 导出" —— 仅在  [handbook://block-scribe:scriptorium] 缮写室上，这是你唯一可以在 Scribe 物品之间复制、合并、导入和导出整份文档的地方。参阅  [handbook://craftinginfo-scribe-transcribe] Scribe 模组：转录标签页。

"计时器" —— 仅在  [handbook://item-scribe:scribeclockmakernotebook] 钟表匠笔记本上，一个显示在你置顶任务 HUD 上的单一倒计时。

有关键盘快捷键和文本编辑机制，参阅  [handbook://craftinginfo-scribe-editor-reference] Scribe 模组：编辑器参考。

## 手册 7：Scribe 模组：分配任务

来源：`assets/scribe/config/handbook/06-assignments.json`。

任务分配台

[handbook://block-scribe:scribeassignmentdesk] 任务分配台方块是唯一能把任务直接交给另一名玩家的地方，通过它的"创建任务分配"标签页进行。这个标签页并非一个空白的撰写框，而是暂存一份现有文档：把一本  [handbook://item-scribe:scribenotebook] 笔记本、泥板或任何其他 Scribe 物品放入它的槽中——或点击"从分配台取用"改用分配台自己的文档——然后勾选你想发送的行。选择一名接收者并按发送：每个勾选的行都会成为它自己独立的任务分配，因此一次发送可以把几项不同的任务同时交给同一名玩家。一个可选的"从来源删除"开关会在发送时把已发送的行从暂存文档中移除。

任务分配实际如何送达接收者——即时进入他们的"收件箱"，还是封入一份手工携带的  [handbook://item-scribe:tasknotice] 任务通知——取决于服务器的投递策略；参阅  [handbook://craftinginfo-scribe-delivery] Scribe 模组：投递任务分配。

你曾从这个分配台发送过的每一项任务分配，都会长久保留在它自己的只读"已发送任务分配记录"标签页上，即便它早已脱手。

收件箱

你收到的任务分配会落入一个"收件箱"——要么是独立的  [handbook://block-scribe:scribeinbox-up] 收件箱方块（仅接收和存储，没有创建表单），要么是共享的"收件箱"标签页，它可通过导航按钮从任务分配台、 [handbook://block-scribe:scribelectern] 讲台、缮写室和黑板打开（该按钮只有在你收到第一项任务分配后才会出现）。每个收件箱界面都显示相同的行：任务文字、子任务的缩进深度，以及一个紧凑的状态标签。点击一行前缘的箭头可展开它，查看分配者的名字、发送时的游戏内日期，以及此刻对你适用的各种操作按钮。

列表上方有一行筛选药丸——"全部"、"新"、"已接受"、"已取消"和"已完成"——每个都显示一个计数，并将列表缩窄到仅该组；同一时间只有一个处于激活状态。标题栏中的一个按钮可一次性展开或折叠当前所有可见的行。

状态

一项任务分配会经历一小组基本单向的状态："新"（刚到达——你可以接受或拒绝；发送者仍可取消）→"已接受"（现在归你了——发送者的取消窗口已关闭）→"已完成"（在你勾选完成任务的那一刻自动发生——没有单独的"标记完成"按钮）。拒绝、取消或丢弃一项已接受的任务则会使它结束于"已拒绝"、"已取消"或"已丢弃"——筛选药丸把这三者一并归入"已取消"。任务通知在这一切之前还会增加一个状态，"已发送"，已在上面的投递指南中说明。无论结局如何，都是最终的——重试永远是一份全新的任务分配，绝不会复活旧的——但一旦一条记录到达任何最终状态，你就可以展开它的行，从任一方将它永久删除。

接受任务

接受会把任务放入一件 Scribe 物品：你当前手持的那件，或（若你双手空空）你物品栏中的一件——如果你携带了不止一件，会请你挑选。如果你完全没有携带 Scribe 物品，"接受"会被禁用，直到你携带为止。一旦接受，任务的文字就固定了（它来自发送者，而非你），但它的复选框、置顶和在你文档中的位置都与其他任何任务完全一样地工作——包括"删除"，对于已接受的任务，它执行的是"丢弃"转换而非单纯移除，因此发送者的记录始终与你实际所做的相符。

留意新的任务分配

一项未查看的任务分配会在附近每一个具备收件功能的方块上柔和地发光，直到你打开该方块的"收件箱"并看到它。放在某个收件箱自身存储中的实体任务通知，会专门为那个"收件箱"增添它自己的光效，直到它被取走。

## 手册 8：Scribe 模组：任务链接

来源：`assets/scribe/config/handbook/07-quests.json`。

除非你运行 VS Quest 或 Progression Framework，否则本节保持不激活。当两个模组都未安装时，Scribe 会完全禁用任务集成。

任务链接

在正常游玩中，当你在世界各处接取任务时，Scribe 会为你构建任务链接。你也可以作为备用，通过"编辑器"中的"新建任务"下拉菜单手动构建一个。选择"任务链接"并从列表中挑选你的目标。任务链接作为一个简单的参考点与你的目标并列。Scribe 会在你建立链接的那一刻捕获任务文本，即使你之后移除了任务模组，也会保留该记录。

自动检测

Scribe 会在任务更新发生时于聊天中通报。你可以使用 Scribe 设置中的两个选项来控制自动追踪行为，将其设为"始终"、"从不"或"询问"。

"任务接受策略"：控制 Scribe 是把新任务直接送入你手持的物品、置之不理，还是通过 HUD 横幅询问你。

"任务完成策略"：控制 Scribe 是否在底层任务完成时立即把你现有的任务链接标记为完成。

实时进度

保持一个 VS Quest 对话框打开，可在你的条目内显示击杀、放置或破坏目标的实时计数。涉及物品收集的任务保持静态。Progression Framework 链接会在所有视图中被动地追踪进度，即时更新单一和多部分的目标。

## 手册 9：Scribe 模组：投递任务分配

来源：`assets/scribe/config/handbook/08-delivery.json`。

你服务器的世界设置决定任务分配的投递规则。在"始终即时"的服务器上，任务会送达收件人位于世界任何位置的"收件箱"。"始终实体"的服务器强制你亲手投递每一条消息。"混合"服务器则通过一个交互式开关同时提供这两种方式。

本地收件箱

在短距离内即时发送任务。目标玩家必须站在分配台的有效半径内，默认设为 200 格（每个服务器可配置）。

发送通知

使用分配台供应槽中储备的空白纸张，创建一份实体  [handbook://item-scribe:tasknotice] 任务通知。在该文档进入收件人之手或他们能访问的箱子之前，不会有任何东西送达。一旦任务分配台将通知封缄，你的"已发送任务分配记录"就会立即将该通知登记为已发送。在收件人实际拾起该物品之前，他们不会看到任何通知。

打开已封缄的通知

手持已封缄的通知并副手点击即可阅读其内容。一个小小的文档窗口会显示任务以及接受和拒绝按钮。接受会像"收件箱"转移一样，将任务移入你当前使用的 Scribe 物品中。空白通知不含数据，无法打开。

混合范围逻辑

混合分配台会在你选择收件人的那一刻评估玩家距离。范围内的玩家会自动切换为"本地收件箱"。离线或距离过远的目标会将界面切换为"发送通知"。在发送之前，你完全可以自由地在这些选项之间切换。

## 配方清单

每个折叠项保留完整配方；`ingredients` 是投入，`output` 是产物，`pattern` 是网格或逐层锻造/陶塑图。

<details><summary>任务分配台 · assignmentdesk</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 羽毛<br><code>game:feather</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 I | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 任务分配台<br><code>scribe:scribeassignmentdesk</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FPL
IBB
BNB
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/assignmentdesk.json`

```json
[
  {
    "ingredientPattern": "FPL,IBB,BNB",
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:feather"
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "I": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "B": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      }
    },
    "width": 3,
    "height": 3,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-black"
        },
        "requiresLitres": 1,
        "consumeContainer": true
      }
    },
    "name": "scribe:scribeassignmentdesk",
    "output": {
      "type": "block",
      "code": "scribe:scribeassignmentdesk",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · chalkboard</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 白垩岩石块<br><code>game:stone-chalk</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 板岩岩石<br><code>game:rock-slate</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>scribe:chalkboard-north</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
HPP
ISC
NPP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/chalkboard.json`

```json
[
  {
    "ingredientPattern": "HPP,ISC,NPP",
    "ingredients": {
      "H": {
        "type": "item",
        "tags": [
          "tool-hammer"
        ],
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "I": {
        "type": "item",
        "tags": [
          "tool-chisel"
        ],
        "isTool": true
      },
      "C": {
        "type": "item",
        "code": "game:stone-chalk"
      },
      "S": {
        "type": "block",
        "code": "game:rock-slate"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      }
    },
    "width": 3,
    "height": 3,
    "name": "scribe:chalkboard",
    "output": {
      "type": "block",
      "code": "scribe:chalkboard-north",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>名称未汉化（见物品代码） · inbox</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 名称未汉化（见物品代码）<br><code>scribe:scribeinbox-up</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
B_B
BNB
B_B
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/inbox.json`

```json
[
  {
    "ingredientPattern": "B_B,BNB,B_B",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "game:plank-*"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      }
    },
    "width": 3,
    "height": 3,
    "name": "scribe:scribeinbox",
    "output": {
      "type": "block",
      "code": "scribe:scribeinbox-up",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>钟表匠笔记本 · scribeclockmakernotebook-schematic</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 笔记本<br><code>scribe:scribenotebook</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 金属零件<br><code>game:metal-parts</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 S | 钟表匠笔记本图纸<br><code>scribe:clockmakerschematic</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 钟表匠笔记本<br><code>scribe:scribeclockmakernotebook</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BGM
S__
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/scribeclockmakernotebook-schematic.json`

```json
[
  {
    "ingredientPattern": "BGM,S__",
    "recipegroup": 2,
    "ingredients": {
      "B": {
        "type": "item",
        "code": "scribe:scribenotebook"
      },
      "G": {
        "type": "item",
        "code": "game:gear-temporal"
      },
      "M": {
        "type": "block",
        "code": "game:metal-parts"
      },
      "S": {
        "type": "item",
        "code": "scribe:clockmakerschematic",
        "consume": false
      }
    },
    "width": 3,
    "height": 2,
    "name": "scribe:scribeclockmakernotebook-schematic",
    "output": {
      "type": "item",
      "code": "scribe:scribeclockmakernotebook",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>钟表匠笔记本 · scribeclockmakernotebook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 B | 笔记本<br><code>scribe:scribenotebook</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 G | 时空齿轮<br><code>game:gear-temporal</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 M | 金属零件<br><code>game:metal-parts</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 钟表匠笔记本<br><code>scribe:scribeclockmakernotebook</code> | 1 | 未声明附加限制 |

**加工条件：** 所需特性：tinkerer；网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
BGM
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/scribeclockmakernotebook.json`

```json
[
  {
    "ingredientPattern": "BGM",
    "recipegroup": 1,
    "requiresTrait": "tinkerer",
    "ingredients": {
      "B": {
        "type": "item",
        "code": "scribe:scribenotebook"
      },
      "G": {
        "type": "item",
        "code": "game:gear-temporal"
      },
      "M": {
        "type": "block",
        "code": "game:metal-parts"
      }
    },
    "width": 3,
    "height": 1,
    "name": "scribe:scribeclockmakernotebook",
    "output": {
      "type": "item",
      "code": "scribe:scribeclockmakernotebook",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>讲台 · scribelectern</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 羽毛<br><code>game:feather</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 讲台<br><code>scribe:scribelectern</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FRL
PPP
BPN
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/scribelectern.json`

```json
[
  {
    "ingredientPattern": "FRL,PPP,BPN",
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:feather"
      },
      "R": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*"
      },
      "B": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      }
    },
    "width": 3,
    "height": 3,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-black"
        },
        "requiresLitres": 1,
        "consumeContainer": true
      }
    },
    "name": "scribe:scribelectern",
    "output": {
      "type": "block",
      "code": "scribe:scribelectern",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>笔记本 · scribenotebook</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 羽毛<br><code>game:feather</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 笔记本<br><code>scribe:scribenotebook</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：2。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FRN
BL_
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/scribenotebook.json`

```json
[
  {
    "ingredientPattern": "FRN,BL_",
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:feather"
      },
      "R": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      },
      "B": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      }
    },
    "width": 3,
    "height": 2,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-black"
        },
        "requiresLitres": 1,
        "consumeContainer": true
      }
    },
    "name": "scribe:scribenotebook",
    "output": {
      "type": "item",
      "code": "scribe:scribenotebook",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>红泥板、蓝泥板、耐火泥板 · scribetablet-clay</summary>

**方案 1**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 红色粘土<br><code>game:clay-red</code> | 2 | 未声明附加限制 |
| 产物 | 红泥板<br><code>scribe:scribetablet-clay-red</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KCC
SCC
_CC
```

**方案 2**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 蓝色粘土<br><code>game:clay-blue</code> | 2 | 未声明附加限制 |
| 产物 | 蓝泥板<br><code>scribe:scribetablet-clay-blue</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KCC
SCC
_CC
```

**方案 3**

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 S | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 C | 耐火粘土<br><code>game:clay-fire</code> | 2 | 未声明附加限制 |
| 产物 | 耐火泥板<br><code>scribe:scribetablet-clay-fire</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KCC
SCC
_CC
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/scribetablet-clay.json`

```json
[
  {
    "ingredientPattern": "KCC,SCC,_CC",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true,
        "toolDurabilityCost": 3
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "C": {
        "type": "item",
        "code": "game:clay-red",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "name": "scribe:scribetablet-clay-red",
    "output": {
      "type": "item",
      "code": "scribe:scribetablet-clay-red",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KCC,SCC,_CC",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true,
        "toolDurabilityCost": 3
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "C": {
        "type": "item",
        "code": "game:clay-blue",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "name": "scribe:scribetablet-clay-blue",
    "output": {
      "type": "item",
      "code": "scribe:scribetablet-clay-blue",
      "quantity": 1
    }
  },
  {
    "ingredientPattern": "KCC,SCC,_CC",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true,
        "toolDurabilityCost": 3
      },
      "S": {
        "type": "item",
        "code": "game:stick"
      },
      "C": {
        "type": "item",
        "code": "game:clay-fire",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 3,
    "name": "scribe:scribetablet-clay-fire",
    "output": {
      "type": "item",
      "code": "scribe:scribetablet-clay-fire",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>蜡板 · scribetablet-wax</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 T | 木棍<br><code>game:stick</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 W | 蜂蜡<br><code>game:beeswax</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 蜡板<br><code>scribe:scribetablet-wax</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
SPP
TWW
_WW
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/scribetablet-wax.json`

```json
{
  "ingredientPattern": "SPP,TWW,_WW",
  "ingredients": {
    "S": {
      "type": "item",
      "tags": [
        "tool-saw"
      ],
      "isTool": true,
      "toolDurabilityCost": 3
    },
    "P": {
      "type": "item",
      "code": "game:plank-*"
    },
    "T": {
      "type": "item",
      "code": "game:stick"
    },
    "W": {
      "type": "item",
      "code": "game:beeswax"
    }
  },
  "width": 3,
  "height": 3,
  "name": "scribe:scribetablet-wax",
  "output": {
    "type": "item",
    "code": "scribe:scribetablet-wax",
    "quantity": 1
  }
}
```

</details>

</details>

<details><summary>缮写室 · scriptorium</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 F | 羽毛<br><code>game:feather</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 L | 皮革<br><code>game:leather-normal-plain</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 B | 变体材料（按代码匹配）<br><code>game:bowl-*-fired</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 P | 变体材料（按代码匹配）<br><code>game:plank-*</code> | 2 | 未声明附加限制 |
| 投入 N | 变体材料（按代码匹配）<br><code>game:metalnailsandstrips-*</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 产物 | 缮写室<br><code>scribe:scriptorium</code> | 1 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：3。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
FRL
BPP
NPP
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/scriptorium.json`

```json
[
  {
    "ingredientPattern": "FRL,BPP,NPP",
    "ingredients": {
      "F": {
        "type": "item",
        "code": "game:feather"
      },
      "R": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "L": {
        "type": "item",
        "code": "game:leather-normal-plain"
      },
      "B": {
        "type": "block",
        "code": "game:bowl-*-fired"
      },
      "P": {
        "type": "item",
        "code": "game:plank-*",
        "quantity": 2
      },
      "N": {
        "type": "item",
        "code": "game:metalnailsandstrips-*"
      }
    },
    "width": 3,
    "height": 3,
    "attributes": {
      "liquidContainerProps": {
        "requiresContent": {
          "type": "item",
          "code": "game:dye-black"
        },
        "requiresLitres": 1,
        "consumeContainer": true
      }
    },
    "name": "scribe:scriptorium",
    "output": {
      "type": "block",
      "code": "scribe:scriptorium",
      "quantity": 1
    }
  }
]
```

</details>

</details>

<details><summary>任务通知 · tasknotice</summary>

| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |
| --- | --- | --- | --- |
| 投入 P | 羊皮纸<br><code>game:paper-parchment</code> | 未声明；按配方类型判定 | 未声明附加限制 |
| 投入 R | 香蒲<br><code>game:cattailtops</code> | 2 | 未声明附加限制 |
| 产物 | 任务通知<br><code>scribe:tasknotice</code> | 8 | 未声明附加限制 |

**加工条件：** 网格宽度：3；网格高度：1。

**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。

```text
KPR
```

<details><summary>技术说明：完整配方与资源路径</summary>

来源：`assets/scribe/recipes/grid/tasknotice.json`

```json
[
  {
    "ingredientPattern": "KPR",
    "ingredients": {
      "K": {
        "type": "item",
        "tags": [
          "tool-knife"
        ],
        "isTool": true
      },
      "P": {
        "type": "item",
        "code": "game:paper-parchment"
      },
      "R": {
        "type": "item",
        "code": "game:cattailtops",
        "quantity": 2
      }
    },
    "width": 3,
    "height": 1,
    "name": "scribe:tasknotice",
    "output": {
      "type": "item",
      "code": "scribe:tasknotice",
      "quantity": 8
    }
  }
]
```

</details>

</details>
<!-- generated:end -->
