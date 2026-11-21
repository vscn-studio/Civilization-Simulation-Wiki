import { defineConfig } from 'vitepress'
import { nav, sidebar, pagePresentation } from './navigation.mjs'
export default defineConfig({
  lang: 'zh-CN', title: '炽天使文明模拟', description: '玩家教程、整合包百科与管理开发参考',
  base: process.env.WIKI_BASE || '/', cleanUrls: false,
  transformPageData: pagePresentation,
  themeConfig: {
    nav, sidebar,
    search: { provider: 'local', options: {
      // Recipe summaries retain material codes; duplicated raw JSON need not inflate search.
      _render: (src, env, md) => md.render(src.replace(/^```json\s*\n[\s\S]*?^```\s*$/gm, ''), env),
      locales: { root: { translations: {
      button: { buttonText: '搜索百科', buttonAriaLabel: '搜索百科' },
      modal: { noResultsText: '没有找到相关内容', resetButtonTitle: '清空搜索',
        footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' } }
    } } } } },
    outline: { label: '本页目录', level: [2, 3] },
    docFooter: { prev: '上一篇', next: '下一篇' }, returnToTopLabel: '返回顶部',
    sidebarMenuLabel: '栏目目录', darkModeSwitchLabel: '切换主题',
    footer: { message: '依据源码、资源与服务器配置整理 · 数值以当前服务器为准' }
  }
})
