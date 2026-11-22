import { test, expect } from '@playwright/test'

const routes = ['/', '/guide/diseases.html', '/guide/food-catalogue.html', '/admin/seraph-config-semantics.html', '/develop/api.html', '/mods/']
for (const width of [375,768,1440]) {
  for (const theme of ['light','dark']) {
    test(`阅读布局 ${width}px / ${theme}`, async ({page}) => {
      await page.setViewportSize({width,height:900})
      await page.addInitScript(value => localStorage.setItem('vitepress-theme-appearance',value),theme)
      const errors=[]; page.on('pageerror',e=>errors.push(e.message))
      for (const route of routes) {
        await page.goto(route)
        await expect(page.locator('h1').first()).toBeVisible()
        await expect(page.locator('html')).toHaveClass(theme==='dark' ? /dark/ : /^(?!.*\bdark\b)/)
        if (route.includes('food-catalogue')) await expect(page.getByText(/找到 \d+ 条记录/)).toBeVisible()
        if (route==='/mods/') await expect(page.getByText('132 个模组',{exact:true})).toBeVisible()
        expect(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth+1),route).toBeTruthy()
        if ((width===375 && route.includes('/guide/')) || (width===1440 && (route==='/' || route.includes('/admin/')))) {
          await page.screenshot({path:test.info().outputPath(route.replace(/[^a-z0-9]/gi,'_')+'.png'),fullPage:false})
        }
      }
      expect(errors).toEqual([])
    })
  }
}

test('栏目导航与中文疾病说明',async ({page})=>{
  await page.setViewportSize({width:1440,height:900})
  await page.goto('/guide/diseases.html#trichinosis')
  await expect(page.locator('#trichinosis')).toBeVisible()
  await expect(page.locator('#trichinosis').locator('xpath=following-sibling::p[1]')).toContainText('生吃被系统识别为“生野味”的肉')
  const technical = page.locator('#trichinosis').locator('xpath=following-sibling::details[1]')
  await expect(technical).not.toHaveAttribute('open','')
  await technical.locator('summary').click()
  await expect(technical).toHaveAttribute('open','')
  await expect(technical).toContainText('不是感染概率')
  await expect(page.locator('.VPSidebar').getByText('疾病与护理',{exact:true})).toBeVisible()
  await expect(page.locator('.VPSidebar').getByText('全部配置字段',{exact:true})).toHaveCount(0)
  await page.goto('/admin/')
  await expect(page.locator('.VPSidebar').getByText('全部配置字段',{exact:true})).toBeVisible()
})

test('营养校准完整性、中文搜索、份量与分页',async ({page})=>{
  await page.goto('/guide/food-catalogue.html')
  await expect(page.getByText('找到 414 条记录',{exact:false})).toBeVisible()
  await page.getByRole('button',{name:'下一页',exact:true}).click()
  await expect(page.getByText('第 2 /',{exact:false})).toBeVisible()
  await page.getByLabel('名称或代码').fill('game:fruit-redapple')
  await expect(page.getByText('找到 1 条记录',{exact:false})).toBeVisible()
  await expect(page.getByText('第 1 /',{exact:false})).toBeVisible()
  const before=await page.locator('.food-catalogue tbody tr').first().locator('td').nth(3).innerText()
  await page.getByLabel('营养计量').selectOption('portion')
  const after=await page.locator('.food-catalogue tbody tr').first().locator('td').nth(3).innerText()
  expect(Number(after.replaceAll(',',''))).toBeCloseTo(Number(before.replaceAll(',',''))*1.82,2)
  await page.getByLabel('名称或代码').fill('胡萝卜')
  await expect(page.locator('.food-catalogue tbody tr').first()).toContainText('胡萝卜')
  await page.getByLabel('名称或代码').fill('')
  await page.getByLabel('查看数据').selectOption('native')
  await expect(page.getByText('找到 352 条记录',{exact:false})).toBeVisible()
  await page.getByLabel('来源模组').selectOption('game')
  const filtered=await page.getByText(/找到 \d+ 条记录/).innerText()
  expect(filtered).not.toContain('352 条')
})

test('模组目录中文分类及代码搜索',async ({page})=>{
  await page.goto('/mods/')
  await expect(page.getByText('132 个模组',{exact:true})).toBeVisible()
  await page.getByLabel('搜索名称或模组代码').fill('采石')
  await expect(page.locator('.mod-catalogue tbody tr')).toHaveCount(1)
  await page.getByLabel('搜索名称或模组代码').fill('vsslssmod')
  await expect(page.locator('.mod-catalogue tbody tr')).toHaveCount(2)
  await page.getByLabel('玩法分类').selectOption('三个核心模组')
  await expect(page.locator('.mod-catalogue tbody tr')).toHaveCount(1)
})

test('旧锚点自动展开技术附录与搜索',async ({page})=>{
  await page.goto('/guide/character-panel.html#逐项属性')
  await expect(page.locator('#逐项属性')).toBeVisible()
  await page.goto('/')
  await page.locator('.VPNavBarSearch').getByRole('button').click()
  const input=page.locator('#localsearch-input')
  await input.fill('旋毛虫')
  await expect(page.locator('.VPLocalSearchBox')).toContainText('疾病',{timeout:15000})
  await page.keyboard.press('Escape')
  await page.locator('.VPNavBarSearch').getByRole('button').click()
  await page.locator('#localsearch-input').fill('trichinosis')
  await expect(page.locator('.VPLocalSearchBox')).toContainText('疾病',{timeout:15000})
})

test('平板菜单可展开并切换栏目',async ({page})=>{
  await page.setViewportSize({width:768,height:900})
  await page.goto('/')
  await page.locator('.VPNavBarHamburger').click()
  await expect(page.locator('.VPNavScreen')).toBeVisible()
  await page.locator('.VPNavScreen').getByRole('link',{name:'管理员',exact:true}).click()
  await expect(page).toHaveURL(/\/admin\//)
  await expect(page.locator('.VPNavScreen')).toHaveCount(0)
})
