# -*- coding: utf-8 -*-
"""Reviewed display taxonomy. Categories describe installed features, not enablement."""
import json, html
from pathlib import Path
from wiki_content import ROOT, write_generated

GROUPS = {
 '三个核心模组': 'vsscsmod=文明模拟|vsslssmod=生存模拟|vsscpmod=文明兼容补丁',
 '农业、饮食与卫生': 'butchering=屠宰与肉类加工|farmingrevamped=农业改造|fieldsofsalt=盐田|foodshelves=食物架|foragersgamble=采集收获|fromgoldencombs=蜂箱与养蜂|invfarming=无脊椎动物养殖|longtermfood=长期储存食品|naturalfertilizer=天然肥料|offlinenospoil=离线防腐|ovensmoking=炉内烟熏|primitivesurvival=原始生存|rusticcookery=乡野烹饪|soapandlyecontinued=肥皂与碱液|stickroast=串烤|stonebakeoven=石砌烤炉|tankardsandgoblets=酒杯与高脚杯|wildfarmingfork=野生种植',
 '建筑、工业与工艺': 'thetruearchimedesscrew=阿基米德螺旋提水|betternails=钉子制作|bricklayers=砖瓦与陶艺|brickyard=砖厂|candela=灯具|cbr=雕刻方块保留|chiseledgroundplacement=雕刻方块地面放置|chiseledwallmounting=雕刻方块墙面安装|chiseltools=雕刻工具|clickuptorches=拾取火把|comfybeds=舒适床铺|cottageindustry=家庭工坊|duncansgrass=草类材料|easybuilding=便捷建造|em=扩展材料|fastpackeddirtpaths=夯土道路|glazedpots=上釉陶罐|grasstoropes=草绳工艺|vscngroundworks=地面施工|spinningwheel=纺纱与纤维工艺|hideracks=皮革加工|kevinsfurniture=家具|loggingmod=伐木与原木加工|oillampsanywhere=油灯放置|purposefulstorage=专用储存|pyrogenesiscontinued=生火工艺|rkncrafting=制作系统|scaffolding=脚手架|smithingplusplus=锻造改进|stonequarryrepckfipil=采石工艺|storagetweaks=储存调整|toolsmith=工具锻造|ashes=灰烬材料|vsroofing=屋顶建造',
 '交通、地图与搬运': 'carryon=背负搬运|cartwrightscaravan=马车与商队|chinesecompass=司南与罗盘|crawlanddive=爬行与潜水|equusferus=野马|immersivemaps=沉浸地图|jaunt=旅行与移动|mountlogoutguard=坐骑离线保护|roughseas=海浪|shipwright=造船|spyglassfork=望远镜|vscnroping=绳索交互|walkableentities=实体表面行走',
 '身体、战斗与成长': 'bloodtrail=血迹追踪|classesremoved=职业限制调整|dead=死亡扩展|downed=倒地系统|progressivebleeding=渐进出血|seraphleveling=技能成长|slowtox=毒性效果|survivalcomplements=生存补充|toolsmithweapons=武器锻造|vscnfirearrows=火箭矢',
 '世界、气候与环境': 'watersheds=流域生成|betterandimprovedweather2=天气改进|creaturefootsteps=生物脚步|desirepaths=踩踏路径|dynamicseasonaltemperature=季节温度|extremeweather=极端天气|footprints=足迹|realsmoke=真实烟雾|realisticrapids=真实急流|realisticwater=真实水流|seasonalflowers=季节花卉|smokescent=烟雾与气味|terraprety=地形生成|torchesheat=火把热量|visibleoresandminerals=可见矿石',
 '交易、社交与创作': 'billposting=告示张贴|coinage=铸币|commercially=商业交易|envelopes=信封与邮件|vsmechanicallocks=机械锁|scribe=书写|simplevoicechat=语音聊天|vinconomy=经济系统|vintagecanvas=绘画画布|vsinstrumentsredux=乐器|vsinstrumentsreduxexpansionc=乐器扩展|vsrestraints=束缚交互',
 '界面、汉化与客户端工具': 'betterhandbook=手册改进|extrainfo=额外信息|gui=界面工具|hudclockpatch=时钟显示补丁|unbindhotkeys=快捷键解绑|vscnlangpack=整合包汉化|vscnlangpackupdater=汉化更新|chineselinebreak=中文换行|fontsettings=字体设置|pinyinsearch=拼音搜索|betterentityinteraction=实体交互改进|betterchinese=中文显示改进|precisepickedup=拾取提示',
 '依赖、兼容与管理工具': 'algernonsterrainsampler=地形采样工具|butcheringseraphlevelingcompatibility=屠宰与技能兼容|carryonlib=搬运依赖库|cartcarryonpatch=马车搬运兼容|genelib=遗传系统依赖库|jsonpatcheslib=资源补丁依赖库|launchergoserverbridge=启动器服务器桥接|launchergoauth=启动器认证|realsmokeqppatch=烟雾兼容补丁|tandemwaterwheelfix=串联水轮修复|vsslssmoddebug=生存调试工具'
}

CORE_LINKS = {
 'vsscsmod': '[文明与部落](/guide/civilization) · [机制说明](/guide/civilization-source) · [管理员命令](/admin/commands-full)',
 'vsslssmod': '[玩家入门](/guide/start) · [生存系统](/guide/survival) · [开发者 API](/develop/api)',
 'vsscpmod': '[兼容补丁](/guide/patches) · [机制说明](/guide/patches-source) · [管理员命令](/admin/commands-full)',
}


def entry_content(row):
    lines = ['# ' + row['title'], '', '| 项目 | 内容 |', '| --- | --- |',
             '| 模组名称 | ' + html.escape(row['name']) + ' |',
             '| 模组 ID | <code>' + html.escape(row['id']) + '</code> |',
             '| 模组版本 | ' + html.escape(row['version']) + ' |',
             '| 玩法分类 | ' + row['category'] + ' |', '',
             '版本号用于核对整合包清单；实际启用情况请以游戏的模组管理界面和服务器要求为准。', '']
    if row['slug'] in CORE_LINKS:
        lines += ['## 相关教程', '', CORE_LINKS[row['slug']], '']
    if (ROOT/'docs/reference/recipes'/(row['slug']+'.md')).exists():
        lines += ['[配方与游戏内手册](/reference/recipes/' + row['slug'] + ')', '']
    return '\n'.join(lines + ['[返回模组清单](/mods/)', ''])

def main():
    metadata = {}
    for group, listing in GROUPS.items():
        for entry in listing.split('|'):
            slug, title = entry.split('=', 1)
            if slug in metadata: raise ValueError(slug)
            metadata[slug] = (group, title)
    metadata.update({
        'buildwright': ('建筑、工业与工艺', 'Buildwright 建造工具'),
        'buildwrightserver': ('依赖、兼容与管理工具', 'Buildwright 服务端'),
        'vsimgui': ('依赖、兼容与管理工具', 'Dear ImGui 界面依赖'),
    })
    entries = json.loads((ROOT/'scripts/inventory-manifest.json').read_text(encoding='utf-8-sig'))
    for row in entries:
        row['category'], row['title'] = metadata.get(row['slug'], ('待分类的新模组',row['name']))
    order=list(GROUPS)
    entries.sort(key=lambda row:(order.index(row['category']) if row['category'] in order else len(order), row['title']))
    public_entries = [{k: row[k] for k in ('slug','name','id','version','category','title')} for row in entries]
    (ROOT/'docs/public/data/mod-catalogue.json').write_text(json.dumps(public_entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for row in public_entries:
        write_generated(ROOT/'docs/mods/entries'/(row['slug']+'.md'), entry_content(row))
    lines=['# 按玩法查找模组','','按中文功能名称、原名或模组代码搜索。分类用于找资料，是否启用仍以服务器实际加载情况为准。','','<ModCatalogue />','','<details><summary>完整分类清单（无需加载查询组件）</summary>','']
    for group in dict.fromkeys(x['category'] for x in entries):
        lines += [f'## {group}','','| 模组 | 原名与代码 | 版本 |','| --- | --- | --- |']
        for r in entries:
            if r['category']==group:
                lines.append(f"| [{r['title']}](/mods/entries/{r['slug']}) | {html.escape(r['name'])}<br>`{r['id']}` | {r['version']} |")
        lines += ['']
    lines += ['</details>']
    write_generated(ROOT/'docs/mods/index.md','\n'.join(lines))
    print(f'catalogue: {len(entries)} mods, {len(set(x["category"] for x in entries))} groups')

if __name__=='__main__': main()
