"""One-time editorial pass; keeps detailed technical records in expandable sections."""
import re
from reorganize_wiki import DOCS, save, cards, BACKUP

def fold_sections(text, sections):
    for title,summary in sections.items():
        pattern=r'(^## '+re.escape(title)+r'\n)(.*?)(?=^## |\Z)'
        def change(m):
            if '<summary>技术说明与来源</summary>' in m[2]: return m[0]
            return m[1]+'\n'+summary+'\n\n<details><summary>技术说明与来源</summary>\n\n'+m[2].strip()+'\n\n</details>\n\n'
        text=re.sub(pattern,change,text,flags=re.M|re.S)
    return text

def main():
    if (BACKUP/'polish-complete').exists(): raise SystemExit('Editorial polish already applied.')
    # Core player guides: retain all commands/configs, but keep them out of the reading path.
    for name in ['survival','civilization','patches']:
        rel=f'guide/{name}.md'; text=(DOCS/rel).read_text(encoding='utf-8')
        text=text.replace('\nEnglish\n','\n').replace('# Seraph A Living Survival Simulation','# 生存模拟：功能与操作',1).replace('# Seraph Civilization Patches','# 文明补丁：兼容功能与操作',1)
        text=re.sub(r'^> 本页按 .*?\n', '> 以下介绍依据源码与资源整理；实际规则可能受服务器配置影响。\n', text, count=1, flags=re.M)
        text=fold_sections(text,{
          '指令':'玩家常用操作见上文。需要命令或权限时，查阅[管理员命令参考](/admin/commands-full)，完整原始清单也保留在下面。',
          '配置':'配置由服务器管理员维护；玩家无需修改配置文件。详见[管理员入口](/admin/)。',
          '配置与数据文件':'世界数据与配置分别保存。具体位置和修改步骤见[管理员入口](/admin/)。',
          '数据文件':'迁移备份与日志位置供管理员排障使用。',
        })
        if name=='survival':
            # Stop presenting an unrelated calendar command as the physiology-speed interface.
            text=text.replace('查看游戏日历调速提示，实际调速使用原版 `/time speed`','查看速度配置提示；生理速度设置与原版日历速度不是同一项')
            text=text.replace('项目代码采用 MIT。模型、图标、音效、游戏衍生素材和数据来源见 素材声明 与 第三方许可。第三方素材遵循各自授权；发行包保留版权声明，不包含此 README。','项目代码采用 MIT；素材和第三方内容分别遵循原作者授权，参见项目随包许可说明。')
        save(rel,text)
    # Clear player steps before detailed treatment contracts.
    rel='guide/treatments.md'; old=(DOCS/rel).read_text(encoding='utf-8').split('\n',1)[1]
    save(rel,'''# 治疗与恢复：选对方法，避免重复用药

## 先区分要解决的问题

| 问题 | 对应操作 | 如何判断效果 |
| --- | --- | --- |
| 仍在出血 | 按压后包扎 | 出血速率下降，再观察血量。 |
| 伤口或皮肤污染 | 使用符合条件的洁净水清洗，按物品说明护理 | 查看脏污、伤口污染和保护状态。 |
| 感染或不适症状 | 使用当前模组实际提供、且适用于该病原或症状的物品 | 查看疾病阶段、症状及剩余时间。 |
| 失血后的恢复 | 停止新失血，保障水、已吸收蛋白质、能量及休息 | 血量与实际造血速度逐渐改善。 |

## 使用治疗物品

1. 按 C 查看疾病与伤口，确认需要治疗的对象。
2. 区分口服和外用。外用治疗是否要求伤口，要看该物品定义；要求伤口的物品不能对不存在的伤口使用。
3. 按物品操作提示使用，并保持动作要求。进度条出现不等于效果已完成。
4. 查看是否已经有同组治疗生效，再决定是否继续使用。

## 为什么不能连续重复使用

同组有效治疗不会简单叠加、无限延长时间。5 个生理小时内同组重复剂量会被记录，第二次及以后可能增加恶心和毒性；部分支持睡眠的治疗还会带来镇静效果。治疗本身也可能存在生效延迟。

具体止血、绷带与清洁操作见[护理教程](/guide/care-tutorial)，感染来源见[疾病百科](/guide/diseases)。治疗接口存在，不代表每种疾病都配有内置药品。

<details><summary>技术说明：治疗定义、参数与应用规则</summary>

'''+old.replace('投诉','不适症状')+'\n</details>')
    # Windows: Chinese purpose first; implementation columns remain available per row.
    rel='guide/windows.md'; text=(DOCS/rel).read_text(encoding='utf-8')
    text=text.replace('C 键角色窗口（Living Survival Simulation）','C 键角色窗口（生存模拟）').replace('文明核心窗口（Civilization Simulation）','文明核心窗口（文明模拟）').replace('投诉','不适症状').replace('综合症','综合征')
    lines=[]; mode=None
    for line in text.splitlines():
        if line.startswith('| 区域 | 源码组件 |'):
            mode='survival'; lines.append('| 区域 | 显示内容 | 技术说明 |'); continue
        if line.startswith('| 窗口/页面 | 源码类 |'):
            mode='civilization'; lines.append('| 窗口／页面 | 用途 | 技术说明 |'); continue
        if mode and line.startswith('| ---'):
            lines.append('| --- | --- | --- |'); continue
        if mode and line.startswith('| '):
            c=[x.strip() for x in line.strip('|').split(' | ')]
            evidence=c[1]+('；'+c[3] if len(c)>3 else '')
            evidence=re.sub(r'`([^`]+)`',r'<code>\1</code>',evidence)
            lines.append(f'| {c[0]} | {c[2]} | <details><summary>组件与数据来源</summary>{evidence}</details> |'); continue
        if not line.startswith('|'): mode=None
        lines.append(line)
    text='\n'.join(lines)
    text=text.replace('营养手册窗口由 `NutritionHandbookDialog` 打开，搜索和份量数据来自服务器同源食品表；没有服务器快照时不会显示伪造的原版值。趋势箭头来自 `MetricTrendDisplay`，只是快照变化，不是独立属性。','在文明菜单中点击营养手册入口，可搜索食物和份量。数据由服务器提供；未连接时不能据空值判断食物没有营养。趋势箭头表示最近数值变化，不是额外属性。\n\n<details><summary>技术说明：营养手册与趋势</summary>\n\n对应组件为 `NutritionHandbookDialog` 和 `MetricTrendDisplay`。\n\n</details>')
    save(rel,text)
    rel='guide/character-panel.md'; old=(DOCS/rel).read_text(encoding='utf-8').split('\n',1)[1]
    save(rel,'''# C 键窗口：看懂自己的身体

## 打开、查看与固定窗口

按 **C** 打开角色窗口，将鼠标停在数值上查看解释与变化来源。窗口有滚动条时可以向下查看；身体、血液循环、疾病恢复、功能、能量平衡和体温调节窗口可通过标题栏按钮固定，关闭 C 后继续显示。退出世界会清除本次固定记录。

## 按问题选择窗口

| 现在的问题 | 先看哪个窗口 | 接着观察 |
| --- | --- | --- |
| 喝水却仍口渴 | 身体与营养 | 胃水是否正在吸收，身体水量是否持续流失。 |
| 吃饱仍没有力气 | 能量平衡与营养 | 糖原、耐力、疲劳、睡压是否分别恢复。 |
| 受伤后状态恶化 | 血液循环与疾病恢复 | 出血速率、血量、伤口、疼痛与感染。 |
| 移动或劳动变慢 | 功能 | 查看对应倍率，再检查腿伤、体力和负重。 |
| 太冷、太热或发热 | 体温调节与环境 | 核心温度、调节目标、产热、散热、风和湿润度。 |
| 不清楚吃什么 | 营养与食品手册 | 已吸收营养储备和缺乏项，配合食物表选择。 |

全部指标的单位、含义和数值来源集中在[身体属性速查](/guide/metric-sources)；其他菜单见[全部窗口](/guide/windows)。

## 数值与趋势怎么读

胃内食物不等于已吸收营养；百分比有时表示能力倍率，有时表示储备或强度，不都代表概率。快照缺失、过期或空白也不代表零。热流显示正负方向，冷热适应显示的是效果增幅，不是完整训练进度。

<details><summary>技术说明：原始面板清单、显示字段与计算依据</summary>

'''+old.replace('投诉','不适症状').replace('tooltip','悬停说明').replace('由服务器 metric.Unit','由服务端提供单位')+'\n</details>')
    # Care: every source detail retained, with an actionable Chinese guide preceding it.
    rel='guide/care-tutorial.md'; old=(DOCS/rel).read_text(encoding='utf-8').split('\n',1)[1]
    save(rel,'''# 护理操作：止血、包扎与清洁

## 受伤后先做这几步

1. 离开危险，按 C 看出血速率、血量与伤口列表。
2. 保持静止并按住 **P** 按压；也可使用 `/vsslssmod pressure`。服务器处理出血最快的开放伤口，按压约减少该伤口 90% 的出血，其他伤口仍需处理。
3. 使用绷带或适用药膏。清洁绷带可以止血，但不能代替清洁污染。
4. 观察实际出血和血量，再补充水、营养并休息。感染另按[疾病百科](/guide/diseases)处理。

## 绷带和药膏有什么不同

| 物品 | 主要作用 | 注意 |
| --- | --- | --- |
| 清洁绷带 | 包扎并止血 | 不降低污染与伤口病原。 |
| 酒精绷带 | 止血，并减少伤口污染和病原 | 污染与病原保留原来的 30%，不是立即完成愈合。 |
| 木贼药膏（芦苇或亚麻） | 缓解疼痛、止血并支持伤口修复 | 一次剂量可作用于多处未愈合伤口；不要连续重复同组治疗。 |
| 蜂蜜硫磺药膏（芦苇或亚麻） | 在药膏作用外提供匹配病原的抗菌效果 | 仍受剂量、酒精或药物负担规则约束。 |

## 用水清洁

**桶洗：** 使用有效水源并保持潜行，温度需在 0～45°C，至少有 0.25 升水，且身体或开放伤口确有清洁需求。完成一次消耗 0.25 升。保持准星目标和手持物不变，观察进度是否完成。

**浴缸：** 在浴缸中保持所需占用状态及潜行或坐姿，水量至少 40 升，温度 0～45°C。完成一次清洁消耗 10 升；肥皂可提供额外清洁效果。低于 10°C 的冷水还会降低身体温度。

清水与脏水的效果不同。脏水可能把病原带到皮肤和开放伤口，不能当作消毒水。洗净身体也不会立即删除已经开始的疾病病程。

## 动作为何中断

移动、跳跃、游泳、骑乘、受伤、传送、睡眠、切换物品或开始另一项交互，都可能中断当前护理。按压还要求持续保持动作；界面进度条出现不代表服务器已经完成结算。需要主动停止时使用 `/vsslssmod cancel`。

## 排泄之后

使用厕所或处理地面污染，完成后清洁双手，再接触食物与饮水容器。排泄动作完成不代表环境已经卫生；厕所和肥料存储是否连接，需要按实际设施核对。

<details><summary>技术说明：中断阈值、物品代码、剂量及服务端结算</summary>

'''+old.replace('投诉','不适症状')+'\n</details>')
    # Pack pages: remove development-only instructions from the player path, preserve as notes.
    for p in (DOCS/'pack').glob('*.md'):
        text=p.read_text(encoding='utf-8')
        changes={
          '# 整合包真实资源与玩法路线':'# 整合包玩法路线',
          '闭环':'流程','症状投诉':'不适症状','匹配的治疗定义':'适用于该病原或症状的治疗物品',
          '可校准食品':'营养信息明确的食物','capability owner':'功能负责方','唯一能力所有者':'唯一功能负责方',
          '动作由 Exertion 类型分别计费':'动作按不同活动类型结算消耗',
          'HUD 的客户端进度当作已提交事务':'界面进度条当作已经完成护理',
          '使用过滤/排水/浴缸相关方块':'按需要使用过滤、排水和洗浴设施',
          '只饮用经过服务器验证的液体':'结合水质信息确认处理结果，避免再次污染',
          'pemmican':'肉干油脂食品（pemmican）',
          '`manureslurryportion`':'粪便浆料（`manureslurryportion`）',
          '`manuremixportion`':'粪肥混合料（`manuremixportion`）',
          '`maturefertilizer`':'成熟肥料（`maturefertilizer`）',
          '`ecoli`、`salmonella`':'致病性大肠杆菌、沙门氏菌',
          'Natural Fertilizer':'天然肥料模组（Natural Fertilizer）',
          'Archimedes Screw':'阿基米德螺旋提水模组（Archimedes Screw）',
          'Cottage Industry':'家庭工坊（Cottage Industry）',
          'Cartwrights Caravan':'马车与商队（Cartwrights Caravan）',
          'Shipwright':'造船模组（Shipwright）',
          'Stone Quarry':'采石模组（Stone Quarry）',
          'Primitive Survival':'原始生存（Primitive Survival）',
          'Long-term food':'长期储存食品（Long-term food）',
          '`dyes` 或 `tannin`':'染料或鞣酸（原字段 `dyes`、`tannin`）',
          '输出代码中的 `{material}`、`{color}`':'配方允许的材料和颜色变体',
        }
        for a,b in changes.items(): text=text.replace(a,b)
        paragraphs=text.split('\n\n'); revised=[]
        for para in paragraphs:
            if para.startswith(('开发者接入时遵守','交通模组若提供','食品摄入通过服务端')):
                revised+=['<details><summary>技术说明与来源</summary>\n\n'+para+'\n\n</details>']
            else: revised.append(para)
        save(p.relative_to(DOCS),'\n\n'.join(revised))
    rel='pack/food-and-nutrition.md'
    save(rel,'''# 农业、烹饪与食物储存

## 从食材到一日补给

1. 通过种植、采集、养蜂或屠宰获得食材；按安装模组的配方与手册确认工具和产物。
2. 将动物肉实际做熟，尤其不要直接吃生野味。加工名称不等于已经熟制，需确认产物状态。
3. 在[中文食物表](/guide/food-catalogue)查每份质量、能量、水分与营养，搭配短缺项。
4. 在 C 键里观察胃内容物和已吸收储备，安排进食、饮水与休息；胃满不等于身体储备充足。

## 按目标找加工路线

| 目标 | 查阅内容 | 核对重点 |
| --- | --- | --- |
| 种植食材 | [农业改造手册与配方](/reference/recipes/farmingrevamped) | 当前种子、作物与服务器规则。 |
| 利用动物原料 | [屠宰与加工](/reference/recipes/butchering) | 工具、处理阶段、生熟状态与产物。 |
| 延长保存 | [长期食品](/reference/recipes/longtermfood)、[炉内烟熏模组](/mods/entries/ovensmoking) | 实际配方、保存方式与加工后营养。 |
| 改善烹饪 | [乡野烹饪](/reference/recipes/rusticcookery)、[石砌烤炉](/reference/recipes/stonebakeoven) | 容器、配料、加工条件和成品份量。 |
| 储存和陈列 | [食物架](/reference/recipes/foodshelves) | 适用物品和容器，不能把陈列效果当成额外营养。 |

## 查不到营养时

食品校准和原版营养分支分别保留在查询表中。没有静态声明或没有匹配到具体校准，不代表食物没有营养；服务器可能使用分类基线或运行时配料。混合餐以实际内容和游戏内食品手册为准。

<details><summary>技术说明：校准与摄入记录</summary>

当前发布资源包含 414 条校准记录，来自 `foods.json`；`PortionG` 是份量质量，`EnergyKJPer100G` 是每 100 克能量，微量字段另有单位。真正无法生成组成的摄入会计入 `UnmappedPortions`。摄入通过服务端记录（receipt）去重；客户端食品手册使用服务器同源数据。

</details>
''')
    rel='pack/overview.md'; text=(DOCS/rel).read_text(encoding='utf-8')
    heading,body=text.split('\n',1)
    text=heading+'\n\n'+cards([('开局与阶段推进','先获得稳定饮水、食物和休息条件。','/pack/progression'),('农业、烹饪与储存','从食材、加工到营养搭配。','/pack/food-and-nutrition'),('水与卫生设施','取水、处理、洗浴和排泄物处理。','/pack/water-and-sanitation'),('工业与交通','查看加工设备、生产和搬运路线。','/pack/industry')])+'\n'+body
    text=text.replace('查看 `UnmappedPortions` 再处理真正无法生成组成的分支','查询表中没有记录时，再请管理员检查实际摄入是否无法生成营养组成')
    save(rel,text)
    # Fold package file/type evidence everywhere, not only the three core entries.
    for p in (DOCS/'mods/entries').glob('*.md'):
        text=p.read_text(encoding='utf-8')
        text=re.sub(r'(<!-- package-evidence:start -->)(.*?)(<!-- package-evidence:end -->)',lambda m: m[0] if '<summary>安装包技术资料' in m[2] else m[1]+'\n<details><summary>安装包技术资料与实现证据</summary>\n\n'+m[2].strip()+'\n\n</details>\n'+m[3],text,flags=re.S)
        save(p.relative_to(DOCS),text)
    (BACKUP/'polish-complete').write_text('1',encoding='utf-8')

if __name__=='__main__': main()
