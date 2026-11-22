import { test, expect } from '@playwright/test'

const base = process.env.WIKI_BASE || '/'

test('发布路径下的导航、营养与模组数据', async ({ page }) => {
  const errors = []
  const failedResponses = []
  page.on('pageerror', error => errors.push(error.message))
  page.on('response', response => {
    if (response.status() >= 400) failedResponses.push(`${response.status()} ${response.url()}`)
  })
  await page.setViewportSize({ width: 1440, height: 900 })
  await page.goto(base)
  await page.locator('.VPNavBarMenu').getByRole('link', { name: '资料查询', exact: true }).click()
  await expect.poll(() => new URL(page.url()).pathname).toBe(`${base}reference/`)
  await page.goto(`${base}guide/food-catalogue.html`)
  await expect(page.getByText('找到 414 条记录', { exact: false })).toBeVisible()
  await page.getByLabel('名称或代码').fill('胡萝卜')
  await expect(page.locator('.food-catalogue tbody tr').first()).toContainText('胡萝卜')
  await page.goto(`${base}mods/`)
  await expect(page.getByText('132 个模组', { exact: true })).toBeVisible()
  const firstEntry = page.locator('.mod-catalogue tbody a').first()
  const entryTitle = await firstEntry.innerText()
  expect(await firstEntry.getAttribute('href')).toContain(`${base}mods/entries/`)
  await firstEntry.click()
  await expect(page.getByRole('heading', { level: 1, name: entryTitle })).toBeVisible()
  expect(errors).toEqual([])
  expect(failedResponses).toEqual([])
})

test('发布路径下搜索索引与结果跳转', async ({ page }) => {
  await page.goto(base)
  await page.locator('.VPNavBarSearch').getByRole('button').click()
  await page.locator('#localsearch-input').fill('旋毛虫')
  const result = page.locator('.VPLocalSearchBox a').filter({ hasText: '疾病' }).first()
  await expect(result).toBeVisible({ timeout: 20000 })
  await result.click()
  await expect.poll(() => new URL(page.url()).pathname).toBe(`${base}guide/diseases.html`)
  await expect(page.getByRole('heading', { level: 1, name: /疾病百科/ })).toBeVisible()
})
