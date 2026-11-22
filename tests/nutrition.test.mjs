import { test } from 'node:test'
import assert from 'node:assert/strict'
import fs from 'node:fs'
import { expandCatalogue, displayedDose, assignMeal, pieDose, searchMatches, csvText } from '../docs/.vitepress/theme/nutrition.mjs'
const data=JSON.parse(fs.readFileSync(new URL('../docs/public/data/nutrition-catalogue.json',import.meta.url),'utf8'))
const rows=expandCatalogue(data), find=code=>rows.find(r=>r.code===code&&r.kind!=='pie')
const near=(a,b)=>assert(Math.abs(a-b)<1e-5,`${a} != ${b}`)
test('真实物品、组合与唯一性，隐藏旧物品不参与计数',()=>{
  assert.equal(rows.length,data.counts.records);assert.equal(new Set(rows.map(r=>r.id)).size,rows.length)
  assert(rows.length>9000);assert(data.rows.length>400)
  assert(data.rows.every(r=>!r.code.includes('-harvested')))
  assert(data.rows.every(r=>/[\u4e00-\u9fff]/.test(r.name)))
  assert(data.pieVariants.every(([c,f])=>data.rows[c].pie.role==='crust'&&data.rows[f].pie.role==='filling'))
})
test('苹果每个、每100克及食用数量使用独立质量基准',()=>{
  const apple=find('game:fruit-redapple')
  near(apple.dose.mass,182);near(apple.dose.values.protein,.26*1.82)
  near(displayedDose(apple,{basis:'100'}).values.protein,.26)
  near(displayedDose(apple,{quantity:.5}).values.protein,.26*.91)
})
test('腐败减少能量和营养，不减少水、物理质量和钠钾',()=>{
  const apple=find('game:fruit-redapple'), fresh=displayedDose(apple), spoiled=displayedDose(apple,{spoilage:25})
  for(const key of ['protein','energy','vitaminCMg','electrolytes'])near(spoiled.values[key],fresh.values[key]*.75)
  for(const key of ['water','sodium','potassium','alcohol'])near(spoiled.values[key],fresh.values[key])
  near(spoiled.mass,fresh.mass)
})
test('派按真实面团、馅料和四分之一份量相加，失水不产生热量',()=>{
  const crust=find('game:dough-spelt'), apple=find('game:fruit-redapple')
  const open=rows.find(r=>r.kind==='pie'&&r.preparation==='baked'&&r.ingredients[0].id===crust.id&&r.ingredients[1].id===apple.id&&r.ingredients[0].quantity===2)
  const whole=pieDose(crust,[apple,apple,apple,apple],false,2)
  near(open.dose.mass,whole.mass/4);near(open.dose.values.energy,whole.values.energy/4)
  near(whole.values.protein,crust.cookedDose.values.protein*2+apple.cookedDose.values.protein*8)
  const charred=pieDose(crust,[apple,apple,apple,apple],false,3)
  assert(charred.values.water<whole.values.water);near(charred.values.energy,whole.values.energy)
  const covered=pieDose(crust,[apple,apple,apple,apple],true,2)
  near(covered.values.energy-whole.values.energy,crust.cookedDose.values.energy*2)
})
test('可混合配料验证：不能把肉与水果随意视为合法派',()=>{
  const crust=find('game:dough-spelt'),apple=find('game:fruit-redapple'),meat=find('game:redmeat-raw')
  assert.equal(pieDose(crust,[apple,meat,apple,apple],false,2),null)
})
test('锅中角色匹配守住最低数量与液体配方份量',()=>{
  const recipe=data.mealRecipes.find(r=>r.code==='game:porridge'),grain=find('game:grain-spelt'),apple=find('game:fruit-redapple')
  assert.equal(assignMeal(recipe,[grain.id,apple.id,'','']),null)
  assert.equal(assignMeal(recipe,[grain.id,grain.id,apple.id,'']).length,3)
  assert.equal(assignMeal(recipe,Array(4).fill(apple.id)),null)
})
test('液体按升和肉排剩余块数，不改每100克浓度',()=>{
  const liquid=rows.find(r=>r.kind==='liquid'),slab=find('rusticcookery:meatslab-raw')||rows.find(r=>r.code.startsWith('rusticcookery:meatslab-'))
  assert(liquid&&slab);near(displayedDose(liquid,{quantity:.25}).mass,liquid.dose.mass/4)
  near(displayedDose(slab,{pieces:3}).mass,slab.dose.mass/2)
  near(displayedDose(slab,{pieces:3,basis:'100'}).values.protein,displayedDose(slab,{pieces:6,basis:'100'}).values.protein)
})
test('中文多词、大小写物品代码与完整CSV导出',()=>{
  assert(rows.filter(r=>searchMatches(r,'苹果 烤熟')).length>10)
  assert(searchMatches(find('game:fruit-redapple'),'GAME:FRUIT-REDAPPLE'))
  const csv=csvText(rows.slice(0,37),{basis:'100',quantity:1})
  assert.equal(csv.split('\r\n').length,38);assert(csv.includes('维生素 C'));assert(csv.includes('每100克'))
})
