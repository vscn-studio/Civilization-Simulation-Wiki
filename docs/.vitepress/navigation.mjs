const item = (text, link) => ({ text, link })
const group = (text, items) => ({ text, collapsed: false, items })
export const nav = [item('玩家指南', '/guide/start'), item('核心模组', '/core/'), item('整合包玩法', '/pack/overview'), item('资料查询', '/reference/'), item('管理员', '/admin/'), item('开发者', '/develop/')]
const player = [
  group('开始游戏', [item('新玩家入门', '/guide/start'), item('生存系统概览', '/guide/survival')]),
  group('饮食与饮水', [item('营养与消化', '/guide/nutrition'), item('食物营养查询 ↗', '/guide/food-catalogue'), item('饮水与卫生教程 ↗', '/pack/water-and-sanitation')]),
  group('身体与休息', [item('C 键窗口使用', '/guide/character-panel'), item('身体属性速查', '/guide/metric-sources'), item('全部窗口与快捷入口', '/guide/windows')]),
  group('疾病与护理', [item('疾病百科', '/guide/diseases'), item('身体异常与症状', '/guide/conditions'), item('受伤后的护理操作', '/guide/care-tutorial'), item('治疗与恢复规则', '/guide/treatments')]),
  group('进阶阅读', [item('文明与部落', '/guide/civilization'), item('兼容补丁说明', '/guide/patches'), item('游戏内生存手册', '/guide/handbook'), item('常用术语 ↗', '/reference/glossary')])
]
const core = [group('三个核心模组', [item('模组总览', '/core/'), item('文明模拟', '/mods/entries/vsscsmod'), item('生存模拟', '/mods/entries/vsslssmod'), item('文明补丁', '/mods/entries/vsscpmod')])]
const pack = [
  group('安装与开局', [item('整合包玩法路线', '/pack/overview'), item('安装与启动', '/pack/install'), item('阶段推进', '/pack/progression')]),
  group('生产与生活', [item('农业、食物与储存', '/pack/food-and-nutrition'), item('水与卫生设施', '/pack/water-and-sanitation'), item('建筑、工业与自动化', '/pack/industry'), item('交通与搬运', '/pack/transport')]),
  group('遇到问题', [item('兼容与排障', '/pack/compatibility'), item('配置操作 ↗', '/pack/configuration'), item('按玩法查找模组 ↗', '/mods/')])
]
const reference = [group('快速查阅', [item('资料查询首页', '/reference/'), item('食物营养表', '/guide/food-catalogue'), item('疾病速查 ↗', '/guide/diseases'), item('属性速查 ↗', '/guide/metric-sources'), item('配方与手册', '/reference/recipes/'), item('模组分类目录', '/mods/'), item('常用术语', '/reference/glossary')])]
const admin = [
  group('运行与维护', [item('管理员首页', '/admin/'), item('配置修改流程', '/pack/configuration'), item('命令与故障排查', '/admin/commands'), item('命令参考', '/admin/commands-full')]),
  group('核心模组配置', [item('文明模拟配置', '/admin/civilization-config'), item('生存配置说明', '/admin/survival-config'), item('生存配置默认值', '/admin/survival-config-full'), item('生存配置字段与校验', '/admin/seraph-config-semantics'), item('已安装配置实值', '/admin/installed-configs')]),
  group('整合包配置', [item('全部配置字段', '/admin/config-tables'), item('配置文件清单', '/admin/modconfig-inventory')])
]
const develop = [
  group('接入与实现', [item('开发者首页', '/develop/'), item('API 与适配器', '/develop/api'), item('生理公式与单位', '/develop/formulas'), item('文明系统实现', '/guide/civilization-source'), item('生存系统实现', '/guide/survival-source'), item('兼容补丁实现', '/guide/patches-source')]),
  group('营养参数', [item('食品校准参数表', '/develop/food-calibration')])
]
export const sidebar = {
  '/guide/': player, '/core/': core, '/pack/': pack, '/mods/': reference,
  '/reference/': reference, '/admin/': admin, '/develop/': develop,
  '/reference/configs/': admin, '/guide/food-catalogue': reference, '/pack/configuration': admin,
  '/mods/entries/vsslssmoddebug': develop,
  ...Object.fromEntries(['civilization', 'survival', 'patches'].map(id => ['/guide/' + id + '-source', develop])),
  ...Object.fromEntries(['vsscsmod', 'vsslssmod', 'vsscpmod'].map(id => ['/mods/entries/' + id, core]))
}

export function pagePresentation(page) {
  const route = '/' + page.relativePath.replace(/\.md$/, '').replace(/(^|\/)index$/, '$1')
  const prefix = Object.keys(sidebar).sort((a,b) => b.length-a.length).find(p => route.startsWith(p))
  const links = prefix ? sidebar[prefix].flatMap(g => g.items).filter(x => !x.text.includes('↗')) : []
  const at = links.findIndex(x => x.link === route)
  page.frontmatter.prev = at > 0 ? links[at-1] : false
  page.frontmatter.next = at >= 0 && at < links.length-1 ? links[at+1] : false
  if (/^\/(reference|mods|develop\/sources)\//.test(route) || route === '/guide/food-catalogue' || route === '/admin/seraph-config-semantics') {
    page.frontmatter.pageClass = 'wide-page'
  }
}
