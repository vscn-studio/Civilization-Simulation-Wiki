<script setup>
import { ref, computed, watch } from 'vue'
import { metrics, combineDoses, scaleDose, searchMatches, assignMeal, pieDose } from './nutrition.mjs'
import { formatNumber as fmt } from './terms.mjs'
const props=defineProps({data:Object,entries:Array})
const mode=ref('meal'), recipeCode=ref('game:porridge'), search=ref(''), slots=ref(['','','','']), crustId=ref(''), covered=ref(true), level=ref(2), fills=ref(['','','','']), fraction=ref(.25), amount=ref(1), spoilage=ref(0)
const names={'game:jam':'果酱','game:meatystew':'炖肉','game:porridge':'谷物粥','game:scrambledeggs':'炒蛋','game:vegetablestew':'炖蔬菜','game:soup':'汤'}
const roleNames={grain:'谷物',fruit:'水果',vegetable:'蔬菜',meat:'肉类',egg:'蛋',cheese:'奶酪',topping:'配料',sweetener:'甜味剂','protein-base':'肉类',stock:'汤底'}
const items=computed(()=>props.entries.filter(r=>r.kind!=='pie'))
const lookup=computed(()=>new Map(items.value.map(r=>[r.id,r])))
const recipe=computed(()=>props.data.mealRecipes.find(r=>r.code===recipeCode.value)||props.data.mealRecipes[0])
const available=computed(()=>{
  const allowed=new Set(recipe.value.roles.flatMap(r=>r.options.map(o=>o.id)))
  return items.value.filter(r=>allowed.has(r.id)).sort((a,b)=>a.name.localeCompare(b.name,'zh-CN'))
})
const crusts=computed(()=>items.value.filter(r=>r.pie?.role==='crust'))
const fillings=computed(()=>items.value.filter(r=>r.pie?.role==='filling'))
const choices=(rows,selected)=>rows.filter(r=>r.id===selected||searchMatches(r,search.value))
watch(recipe,()=>{
  const start=[];for(const role of recipe.value.roles)for(let n=0;n<role.min;n++)start.push(role.options[0]?.id||'')
  slots.value=[...start,...Array(Math.max(0,4-start.length)).fill('')].slice(0,4)
},{immediate:true})
watch(crusts,()=>{crustId.value=crusts.value.find(r=>r.code==='game:dough-spelt')?.id||crusts.value[0]?.id||'';const first=fillings.value.find(r=>r.code==='game:fruit-redapple')?.id||fillings.value[0]?.id||'';fills.value=[first,first,first,first]},{immediate:true})
const assigned=computed(()=>assignMeal(recipe.value,slots.value))
const baseDose=computed(()=>{
  if(mode.value==='pie')return pieDose(lookup.value.get(crustId.value),fills.value.map(id=>lookup.value.get(id)),covered.value,level.value)
  if(!assigned.value)return null
  return combineDoses(assigned.value.map(o=>scaleDose(lookup.value.get(o.id).cookedDose,o.quantity)))
})
const result=computed(()=>{
  if(!baseDose.value)return null
  const d=scaleDose(baseDose.value,mode.value==='pie'?fraction.value:Math.max(0,Number(amount.value)||0)), retained=1-Math.max(0,Math.min(100,Number(spoilage.value)||0))/100
  for(const key of Object.keys(d.values))if(!['water','alcohol','sodium','potassium'].includes(key))d.values[key]*=retained
  return d
})
</script>
<template>
  <section class="meal-calculator" aria-label="自选配料营养计算">
    <p>选择实际配料，计算熟制餐食或混合馅料派的营养。未知的成分保持“未声明”；这里不把不同配方取平均。</p>
    <div class="controls"><label>配方类型<select v-model="mode" aria-label="配方类型"><option value="meal">烹饪锅餐食</option><option value="pie">自选混合馅料派</option></select></label><label>筛选配料名称<input v-model="search" type="search" placeholder="中文或物品代码" /></label><label>成品腐败程度（%）<input v-model.number="spoilage" type="number" min="0" max="100" /></label></div>
    <template v-if="mode==='meal'">
      <div class="controls"><label>烹饪配方<select v-model="recipeCode" aria-label="烹饪配方"><option v-for="r in data.mealRecipes" :key="r.code" :value="r.code">{{ names[r.code]||r.name }}</option></select></label><label>食用份数<input v-model.number="amount" type="number" min="0.01" step="0.25" /></label></div>
      <p>按普通烹饪锅的四个食材槽计算一份餐食。每槽所需物品数、液体升数由所选配方决定；整锅有几份不改变每份配料比例。</p>
      <div class="controls"><label v-for="(_,i) in slots" :key="i">食材槽 {{ i+1 }}<select v-model="slots[i]" :aria-label="'食材槽 '+(i+1)"><option value="">不放食材</option><option v-for="r in choices(available,slots[i])" :key="r.id" :value="r.id">{{ r.name }} · {{ r.code }}</option></select></label></div>
      <details><summary>查看配方数量要求</summary><ul><li v-for="(role,i) in recipe.roles" :key="i">{{ roleNames[role.name]||'附加食材' }}：{{ role.min }}～{{ role.max }} 槽，{{ role.options.length }} 种可选材料。</li></ul></details>
      <p v-if="!assigned" role="alert">配料不符合此配方的数量或类别要求。请补齐必需食材，或移除超过上限的食材。</p>
      <ul v-else><li v-for="(o,i) in assigned" :key="i">{{ lookup.get(o.id).name }} × {{ fmt(o.quantity) }} {{ lookup.get(o.id).kind==='liquid'?'升':'个' }}／份</li></ul>
    </template>
    <template v-else>
      <div class="controls"><label>派皮<select v-model="crustId" aria-label="派皮"><option v-for="r in choices(crusts,crustId)" :key="r.id" :value="r.id">{{ r.name }}</option></select></label><label>顶皮<select v-model="covered" aria-label="顶皮"><option :value="true">带顶皮（共 4 个面团）</option><option :value="false">敞口（2 个面团）</option></select></label><label>烘焙程度<select v-model.number="level" aria-label="烘焙程度"><option :value="0">生派</option><option :value="1">半熟</option><option :value="2">烤熟</option><option :value="3">烤焦</option></select></label><label>食用派的比例<select v-model.number="fraction" aria-label="食用派的比例"><option :value="0.25">1 片（¼ 派）</option><option :value="0.5">2 片（½ 派）</option><option :value="0.75">3 片（¾ 派）</option><option :value="1">整个派</option></select></label></div>
      <p>每个馅料槽投入 2 个食材。混合馅料必须允许混合，并属于相同食物类别或共享兼容的混合标签。</p>
      <div class="controls"><label v-for="(_,i) in fills" :key="i">馅料槽 {{ i+1 }}<select v-model="fills[i]" :aria-label="'馅料槽 '+(i+1)"><option v-for="r in choices(fillings,fills[i])" :key="r.id" :value="r.id">{{ r.name }} · {{ r.code }}</option></select></label></div>
      <button @click="fills=[fills[0],fills[0],fills[0],fills[0]]">四槽使用第一种馅料</button><p v-if="!baseDose" role="alert">这些馅料不能混合制作同一个派，请调整馅料组合。</p>
    </template>
    <div v-if="result" class="summary" aria-live="polite"><h3>本次食用的营养</h3><p>质量 {{ fmt(result.mass) }} g · 能量 {{ fmt(result.values.energy) }} kJ · 水分 {{ fmt(result.values.water) }} g</p><dl><template v-for="([name,unit],key) in metrics" :key="key"><dt>{{ name }}</dt><dd>{{ fmt(result.values[key]) }} {{ unit }}</dd></template></dl></div>
    <p class="note">成品数据按 Seraph 营养规则计算。特殊容器、附加酱汁、勾芡、额外盐分或第三方动态配方可能另有摄入量；请按实际食品内容核对。半熟派与生食配料不等于安全食物。</p>
  </section>
</template>
<style scoped>
.controls{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:16px 0}label{display:flex;flex-direction:column;gap:6px;font-size:14px;min-width:0}input,select,button{border:1px solid var(--vp-c-divider);border-radius:6px;padding:8px;background:var(--vp-c-bg);color:var(--vp-c-text-1);max-width:100%;min-width:0}button,summary{cursor:pointer}.summary{background:var(--vp-c-bg-soft);padding:16px;border-radius:8px;margin-top:16px}.summary h3{margin:0}dl{display:grid;grid-template-columns:minmax(130px,1fr) auto;gap:5px 12px}dd{margin:0}.note{font-size:13px;color:var(--vp-c-text-2)}@media(max-width:500px){.controls{grid-template-columns:minmax(0,1fr)}}
</style>
