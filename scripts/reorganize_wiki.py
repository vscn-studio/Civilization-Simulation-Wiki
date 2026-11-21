"""One-time editorial migration. Routine refresh uses the individual data generators."""
from pathlib import Path
import json, re, html
from wiki_content import ROOT, adopt

DOCS=ROOT/'docs'
BACKUP=ROOT/'scripts/editorial-backup'

def save(path,text):
    p=DOCS/path
    if p.exists():
        b=BACKUP/path
        if not b.exists():
            b.parent.mkdir(parents=True,exist_ok=True); b.write_bytes(p.read_bytes())
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(text.rstrip()+'\n',encoding='utf-8')

def cards(items):
    values=[dict(title=t,description=d,link=l) for t,d,l in items]
    return '<PortalCards :items=\''+html.escape(json.dumps(values,ensure_ascii=False),quote=True)+'\' />\n'

def portal(title,intro,items): return '# '+title+'\n\n'+intro+'\n\n'+cards(items)

def main():
    if (BACKUP/'migration-complete').exists():
        raise SystemExit('Editorial migration already applied. Use refresh commands, not this migration.')
    save('index.md','''---
layout: home
hero:
  name: 炽天使文明模拟
  text: 从生存到文明
  tagline: 按你现在要做的事，找到教程、数据和工具。
  actions:
    - theme: brand
      text: 第一次加入服务器
      link: /guide/start
    - theme: alt
      text: 查询食物、疾病与属性
      link: /reference/
---

'''+portal('选择阅读入口','玩法、资料、管理与开发分开阅读；每个栏目有独立目录。',[
      ('玩家指南','从饮水、进食和休息开始，学习看懂身体状态与处理伤病。','/guide/start'),
      ('三个核心模组','了解文明模拟、生存模拟和文明补丁各自提供什么。','/core/'),
      ('整合包玩法','按农业、加工、工业和交通路线推进。','/pack/overview'),
      ('资料查询','查询食物营养、疾病、属性、配方及模组。','/reference/'),
      ('管理员','查命令、配置当前值、生效方式与故障诊断。','/admin/'),
      ('开发者','查看 API、集成契约、公式和源码索引。','/develop/')]))
    save('core/index.md',portal('三个 Seraph 核心模组','先了解各模组负责的系统，再进入对应教程。详细源码索引集中在开发者栏目。',[
      ('文明模拟','角色身份、生命、部落、领地、地图、交易与公告。','/mods/entries/vsscsmod'),
      ('生存模拟','饮食消化、水分、体温、体力、伤口、疾病与卫生。','/mods/entries/vsslssmod'),
      ('文明补丁','连接制作、采石搬运、车船、地图及界面的兼容行为。','/mods/entries/vsscpmod')]))
    old=(DOCS/'reference/index.md').read_text(encoding='utf-8')
    save('reference/recipes/index.md',old.replace('# 整合包配方与手册资料库','# 配方与游戏内手册',1))
    adopt(DOCS/'reference/recipes/index.md')
    save('reference/index.md',portal('资料查询','按问题查表。玩家页面先讲中文含义，计算过程和原始代码可展开查看。',[
      ('食物营养表','查每份或每 100 克营养、原版饱食度与食物来源。','/guide/food-catalogue'),
      ('疾病百科','查感染来源、病程、表现和应对方法。','/guide/diseases'),
      ('身体属性速查','查 C 键中的单位、升降原因和读法。','/guide/metric-sources'),
      ('配方与手册','按模组查看材料、加工条件和手册正文。','/reference/recipes/'),
      ('模组分类目录','按玩法分类，支持中文名称、原名和代码搜索。','/mods/'),
      ('常用术语','理解生理时间、病原负担、校准值和配置实值。','/reference/glossary')]))
    save('reference/glossary.md','''# 常用术语

| 术语 | 中文含义 | 阅读时注意 |
| --- | --- | --- |
| 生理时间／生物时间 | 身体模拟使用的推进时间 | 不等于现实等待时间；病程以此计算。 |
| 游戏小时 | 世界日历中的游戏时间单位 | 不要直接当作现实小时。具体换算取决于调用系统。 |
| 现实秒 | 现实经过的秒数 | 常用于按键冷却和部分体力恢复。 |
| 病原剂量／负荷 | 接触或摄入的病原数量参数 | 不是“感染百分比”。 |
| 疾病负担 | 当前感染影响身体的程度 | 与一次暴露剂量、是否处于症状期分别判断。 |
| 潜伏期 | 已进入病程但尚未出现症状的阶段 | 没有症状不代表没有感染。 |
| 不适症状 | 治疗或疾病系统记录的不适效果 | 原代码可能称为 `Complaint`，不是玩家提交的投诉。 |
| 免疫储备 | 身体积累的基础抗感染能力 | 实际免疫效率还受营养、毒性、伤势影响。 |
| 饱食度 | 原版食物系统的计量值 | 不应直接等同于克数或热量。 |
| 营养校准 | 为具体食物提供份量和组成数据 | 每 100 克与每份需按质量换算。 |
| 分类基线／回退 | 缺少具体校准时按类别提供的组成依据 | 没匹配到校准不意味着零营养。 |
| 服务器快照 | 服务器某次发送的状态数据 | 快照过期或缺失应显示未知，不能解释为零。 |
| 默认值 | 源码或发布资源中规定的初始设置 | 当前服务器可能已经修改。 |
| 当前值／实值 | 读取指定服务器配置文件得到的值 | 不证明运行中的服务器已重载该值。 |
| 功能负责方 | 在多个模组共存时实际负责某项功能的提供者 | 技术诊断中可能显示 `capability owner` 或 `provider`。 |
| 游戏接口（API） | 供代码接入功能的契约 | 主要面向模组开发者，不是玩家操作步骤。 |
| 模组代码／物品代码 | 程序识别模组或物品的名称 | 如 `game:bushmeat-raw` 对应原版“生野味”。 |

英文代码保留用于搜索和排障。物品中文名优先参考游戏与整合包的中文语言资源，未知名称会标记，不凭代码推断功能。
''')
    for rel,items in {
      'admin/index.md': [('命令与排障','按实际操作查命令和权限。','/admin/commands-full'),('配置当前值','查看指定服务器全部配置字段。','/admin/config-tables'),('核心模组配置','查已安装 Seraph 配置实值。','/admin/installed-configs'),('修改配置的步骤','备份、修改、重载与验证。','/pack/configuration')],
      'develop/index.md': [('API 与接入','治疗接口、适配器契约和单位要求。','/develop/api'),('公式与单位','追溯身体模拟的数值来源。','/develop/formulas'),('源码索引','按模块定位文件和实现。','/develop/source-inventory'),('文档维护','了解来源、生成流程和校验方式。','/develop/maintenance')],
    }.items():
        s=(DOCS/rel).read_text(encoding='utf-8'); head,body=s.split('\n',1)
        body=body.replace('本页描述模组默认行为，不公布测试服务器实际配置。','本页说明配置文件与运行流程；字段表会另行标注源码默认值和当前服务器配置快照。')
        save(rel,head+'\n\n'+cards(items)+'\n'+body.lstrip())
    old=(DOCS/'guide/nutrition.md').read_text(encoding='utf-8')
    save('develop/food-calibration.md',old.replace('# 营养系统与完整食物清单','# 食品校准原始表与实现依据',1).replace('| 水 g | 能量 kJ |','| 水 g/100g | 能量 kJ/100g |'))
    save('guide/nutrition.md','''# 营养与消化：吃下去之后发生什么

食物进入胃以后还要经过消化和吸收，才会补充身体里的水、能量和营养。胃里有食物、原版饱食度很高，都不代表身体储备已经充足。

## 先看哪几个数值

| 你想知道 | 在 C 键中查看 | 如何判断 |
| --- | --- | --- |
| 是否真正补到水 | 胃水、水量、消化能力 | 胃水仍要吸收；出汗、出血和疾病可能同时造成损失。 |
| 为什么吃饱仍乏力 | 糖原、耐力、疲劳、睡压 | 储备能量、短时体力和休息需求是不同指标。 |
| 饮食是否单一 | 已吸收营养与微量营养储备 | 查看缺乏持续时间和恢复趋势，避免只盯一顿饭。 |
| 食物是否容易利用 | 消化能力、胃肠内容物、疾病阶段 | 伤势、体温和肠道感染都会影响处理速度。 |

## 如何安排饮食

1. 在[食物营养表](/guide/food-catalogue)按中文名称查找食物，先确认生熟状态和每份质量。
2. 查看碳水、蛋白质、脂肪、纤维及微量营养；搭配不同食物补充短缺项。
3. 进食后留出消化时间，观察已吸收储备。大量劳动期间还要安排饮水和休息。
4. 感染期间先停止污染来源。食物中毒可能分流新摄入营养，持续吃东西不一定解决短缺。

## 营养种类

| 营养 | 主要读法 |
| --- | --- |
| 碳水化合物 | 参与可利用能量和糖原补充。 |
| 蛋白质 | 支持组织修复、造血和肌肉相关过程。 |
| 脂肪 | 支持能量储备；不能代替所有其他营养。 |
| 膳食纤维 | 进入肠道残渣，不成为同样的身体能量储备。 |
| 电解质 | 与钠、钾及水分调节有关。 |
| 钙、铁、锌 | 分别参与骨骼支持、恢复和组织修复等过程。 |
| 维生素 A、C、B 族 | 储备和持续缺乏会影响相应身体功能。 |

## 查表时不要混淆单位

营养表可以切换“每 100 克”和“每份”。例如一份 182 克的食物，其每份含量是每 100 克数值的 1.82 倍。液体还要核对每升物品数、密度与实际饮用量，混合餐按实际配料结算。

空白或“未声明”不代表零。没有命中具体食品校准时，服务器还可能使用原版营养属性、分类基线或已审查回退；只有无法得到有效组成时才计入未映射诊断。

## 运行时营养槽位

玩家请优先查看 C 键里的中文营养名称。完整槽位、初始值及计算依据见[技术参考](/develop/food-calibration#运行时营养槽位)。

## 食品校准字段

每条校准包含份量、加工方式、含水量、能量、宏量与微量营养。原始字段与来源说明保留在[食品校准参考](/develop/food-calibration#食品校准字段)。

## 当前发布资源的完整食物表

[打开可搜索的中文营养表](/guide/food-catalogue)，可查看全部校准记录及原版、整合包资源分支。原始校准表另见[开发者参考](/develop/food-calibration#当前发布资源的完整食物表)。

## 原版与整合包覆盖边界

静态校准与资源表不执行所有模组补丁和运行时代码。以当前服务器的游戏内食品手册核对最终份量；本站同时保留未解析资源清单与原始数据下载。
''')
    # Retain every generated source record once; entry pages become short gateways.
    for modid,title in [('vsscsmod','文明模拟'),('vsslssmod','生存模拟'),('vsscpmod','文明补丁')]:
        rel=f'mods/entries/{modid}.md'; s=(DOCS/rel).read_text(encoding='utf-8')
        marker='## 源码实现矩阵（当前源码树）'; evidence='<!-- package-evidence:start -->'
        if marker in s:
            before,rest=s.split(marker,1)
            matrix=marker+rest.split(marker,1)[0].split(evidence,1)[0]
            save(f'develop/sources/{modid}.md',f'# {title}源码索引\n\n[返回模组介绍](/mods/entries/{modid})\n\n'+matrix)
            adopt(DOCS/f'develop/sources/{modid}.md')
            tail=evidence+s.split(evidence,1)[1] if evidence in s else ''
            source_link=f'## 源码实现矩阵（当前源码树）\n\n逐文件类型、方法及哈希已集中到[开发者源码索引](/develop/sources/{modid})。\n\n'
            s=before+source_link+tail
        s=s.replace('A dedicated mod for Seraph Civilization Simulation. ','文明模拟提供多人世界中的身份、部落与公共生活系统。')
        s=s.replace('Compatibility fixes for crafting, hauling, vehicles, maps and painting in Seraph Civilization. ','文明补丁处理制作、搬运、载具、地图和绘画之间的兼容。')
        s=s.replace('A survival simulation featuring nutrition and digestion, hydration and water treatment, stamina and sleep, temperature, wounds and disease, hygiene, smoke exposure, wells and bathtubs.','生存模拟把饮食消化、饮水、水处理、体力、睡眠、体温、伤病和卫生连接起来，并提供井、浴缸及烟雾暴露等玩法。')
        if evidence in s:
            a,b=s.split(evidence,1)
            end='<!-- package-evidence:end -->'
            if end in b:
                body,after=b.split(end,1)
                s=a+evidence+'\n<details><summary>安装包技术资料与实现证据</summary>\n'+body+'\n</details>\n'+end+after
        save(rel,s)
    # Make existing generated outputs explicitly owned before refresh.
    for rel in ['guide/diseases.md','guide/metric-sources.md','guide/conditions.md','mods/index.md','admin/seraph-config-semantics.md']:
        p=DOCS/rel; save(rel,p.read_text(encoding='utf-8')); adopt(p)
    for p in (DOCS/'reference/recipes').glob('*.md'): adopt(p)
    BACKUP.mkdir(parents=True,exist_ok=True); (BACKUP/'migration-complete').write_text('1',encoding='utf-8')

if __name__=='__main__': main()
