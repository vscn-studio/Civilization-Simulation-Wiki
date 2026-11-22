<script setup>
import { ref, shallowRef, computed, watch, onMounted, defineAsyncComponent } from 'vue'
import { withBase } from 'vitepress'
import { categories, formatNumber as fmt } from './terms.mjs'
import { preparations, kinds, coverage, metrics, basisNames, expandCatalogue, searchMatches, displayedDose, csvText } from './nutrition.mjs'
import MealCalculator from './MealCalculator.vue'
const FoodCalibration=defineAsyncComponent(()=>import('./FoodCalibration.vue'))
const data=shallowRef(null), entries=shallowRef([]), error=ref(''), query=ref(''), mod=ref(''), category=ref(''), kind=ref(''), preparation=ref(''), quality=ref(''), edible=ref(''), metric=ref('energy'), minimum=ref(''), maximum=ref(''), sort=ref('name'), page=ref(1), pageSize=ref(25), basis=ref('portion'), quantity=ref(1), spoilage=ref(0), process=ref('current'), pieces=ref(6), selected=ref([]), tab=ref('foods')
const filterRefs={query,mod,category,kind,preparation,quality,edible,metric,minimum,maximum,sort,basis,quantity,spoilage,process,pieces,pageSize}
const optionKeys=['mod','category','kind','preparation','quality','edible']
const optionLabels={mod:'所属模组',category:'营养类别',kind:'食品类型',preparation:'加工状态',quality:'数据类型',edible:'食用方式'}
onMounted(async()=>{
  try {
    const response=await fetch(withBase('/data/nutrition-catalogue.json')); if(!response.ok) throw Error(`HTTP ${response.status}`)
    const result=await response.json(); entries.value=expandCatalogue(result); data.value=result
    const params=new URLSearchParams(location.search)
    for(const [key,state] of Object.entries(filterRefs)) if(params.has(key)) {
      const value=params.get(key)
      if(['quantity','spoilage','pieces','pageSize'].includes(key)) {const n=Number(value);if(Number.isFinite(n))state.value=n}
      else state.value=value
    }
    if(![25,50,100].includes(pageSize.value))pageSize.value=25
    quantity.value=Math.max(.01,Math.min(10000,quantity.value));spoilage.value=Math.max(0,Math.min(100,spoilage.value))
    if(!metrics[metric.value])metric.value='energy'
    if(!['portion','100'].includes(basis.value))basis.value='portion'
    if(!['current','cooked'].includes(process.value))process.value='current'
  } catch(e) {error.value='营养数据加载失败：'+e.message}
})
const options=computed(()=>({basis:basis.value,quantity:quantity.value,spoilage:spoilage.value,process:process.value,pieces:pieces.value}))
const modNames=computed(()=>Object.fromEntries(entries.value.map(r=>[r.mod,r.modName])))
const valuesFor=(row,key)=>key==='quality'?[row.coverage]:key==='edible'?[row.edible?'yes':'ingredient']:key==='mod'?[row.mod,...(row.ingredientMods||[])]:[row[key]]
const searchResults=computed(()=>entries.value.filter(row=>searchMatches(row,query.value)))
const satisfies=(row,except)=>optionKeys.every(key=>key===except||!filterRefs[key].value||valuesFor(row,key).includes(filterRefs[key].value))
const labels=(key,value)=>({mod:modNames.value,category:categories,kind:kinds,preparation:preparations,quality:coverage,edible:{yes:'可直接食用／饮用',ingredient:'需加工的食材'}}[key]?.[value])||value
const facets=computed(()=>Object.fromEntries(optionKeys.map(key=>{
  const counts=new Map()
  for(const row of searchResults.value)if(satisfies(row,key))for(const value of new Set(valuesFor(row,key)))counts.set(value,(counts.get(value)||0)+1)
  const current=filterRefs[key].value;if(current&&!counts.has(current))counts.set(current,0)
  return [key,[...counts].map(([value,count])=>({value,count,label:labels(key,value)})).sort((a,b)=>a.label.localeCompare(b.label,'zh-CN'))]
})))
const calculated=computed(()=>searchResults.value.filter(r=>satisfies(r)).map(row=>({row,dose:displayedDose(row,options.value)})))
const filtered=computed(()=>{
  const list=calculated.value.filter(({dose})=>{const v=dose.values[metric.value];return (minimum.value===''||(v!=null&&v>=Number(minimum.value)))&&(maximum.value===''||(v!=null&&v<=Number(maximum.value)))})
  return list.sort((a,b)=>{
    if(sort.value==='name')return a.row.name.localeCompare(b.row.name,'zh-CN')||a.row.id.localeCompare(b.row.id)
    const av=a.dose.values[metric.value],bv=b.dose.values[metric.value]
    if(av==null||bv==null)return av==null?(bv==null?0:1):-1
    return (sort.value==='asc'?av-bv:bv-av)||a.row.name.localeCompare(b.row.name,'zh-CN')
  })
})
const pages=computed(()=>Math.max(1,Math.ceil(filtered.value.length/pageSize.value)))
const rows=computed(()=>filtered.value.slice((page.value-1)*pageSize.value,page.value*pageSize.value))
const comparison=computed(()=>selected.value.map(id=>entries.value.find(r=>r.id===id)).filter(Boolean))
const active=computed(()=>optionKeys.filter(k=>filterRefs[k].value).map(k=>({key:k,label:optionLabels[k]+'：'+labels(k,filterRefs[k].value)})))
watch(Object.values(filterRefs),()=>{page.value=1})
watch(pages,()=>{page.value=Math.min(page.value,pages.value)})
const toggle=row=>{selected.value=selected.value.includes(row.id)?selected.value.filter(id=>id!==row.id):selected.value.length<4?[...selected.value,row.id]:selected.value}
function reset(){query.value='';for(const key of optionKeys)filterRefs[key].value='';minimum.value='';maximum.value='';sort.value='name';process.value='current';spoilage.value=0;pieces.value=6;quantity.value=1;basis.value='portion'}
function showFood(link){reset();query.value=link.code||entries.value.find(r=>r.id===link.id)?.code||'';kind.value=entries.value.find(r=>r.id===link.id)?.kind||'food'}
const shareStatus=ref('')
async function share(){
  const params=new URLSearchParams();for(const [key,state] of Object.entries(filterRefs))if(state.value!=='')params.set(key,state.value)
  const url=location.origin+location.pathname+'?'+params;history.replaceState(null,'',url)
  try{await navigator.clipboard.writeText(url);shareStatus.value='已复制当前检索链接'}catch{shareStatus.value='地址栏已更新，可直接复制链接'}
}
function download(){const blob=new Blob([csvText(filtered.value.map(x=>x.row),options.value)],{type:'text/csv;charset=utf-8'});const url=URL.createObjectURL(blob);const link=document.createElement('a');link.href=url;link.download='食物营养查询.csv';link.click();setTimeout(()=>URL.revokeObjectURL(url),1000)}
const unitLabel=row=>basis.value==='100'?'每 100 克':`${quantity.value} × ${basisNames[row.basis]}`
</script>

<template>
  <div class="food-catalogue" aria-label="食物营养检索">
    <p v-if="error" role="alert">{{ error }}</p><p v-else-if="!data" role="status">正在读取完整营养目录……</p>
    <template v-else>
      <div class="overview"><strong>{{ fmt(data.counts.records) }} 条可检索记录</strong><span>{{ data.counts.items }} 种具体食物与液体 · {{ fmt(data.counts.pies) }} 种馅饼配方及烘焙状态 · {{ data.counts.mealRecipes }} 类自选烹饪配方</span></div>
      <div class="tabs" aria-label="营养查询方式"><button :aria-pressed="tab==='foods'" @click="tab='foods'">食品检索与对比</button><button :aria-pressed="tab==='meal'" @click="tab='meal'">自选配料计算</button><button :aria-pressed="tab==='profiles'" @click="tab='profiles'">校准与原版分支</button></div>
      <MealCalculator v-if="tab==='meal'" :data="data" :entries="entries" />
      <FoodCalibration v-if="tab==='profiles'" />
      <section v-if="tab==='foods'">
        <div class="filters"><label class="search">名称或代码<input v-model="query" type="search" placeholder="例如：苹果 烤熟、胡萝卜、game:fruit-redapple" /></label><label v-for="key in optionKeys" :key="key">{{ optionLabels[key] }}<select v-model="filterRefs[key].value" :aria-label="optionLabels[key]"><option value="">全部</option><option v-for="f in facets[key]" :key="f.value" :value="f.value">{{ f.label }}（{{ f.count }}）</option></select></label></div>
        <p class="hint">空格分隔的关键词同时匹配名称、代码、加工状态或配料。模组筛选包含该模组食材参与制作的派；下拉数字随搜索条件联动。</p>
        <div class="chips"><button v-for="a in active" :key="a.key" @click="filterRefs[a.key].value=''">{{ a.label }} ×</button><button @click="reset">重置筛选与计算</button></div>
        <details class="calculator" open><summary>份量、加工与腐败计算</summary><div class="filters">
          <label>营养计量<select v-model="basis" aria-label="营养计量"><option value="portion">按食用单位（个／升／片）</option><option value="100">每 100 克</option></select></label>
          <label v-if="basis==='portion'">食用数量<input v-model.number="quantity" type="number" min="0.01" max="10000" step="0.25" /></label>
          <label>计算场景<select v-model="process" aria-label="计算场景"><option value="current">当前食品状态</option><option value="cooked">作为熟制餐食配料</option></select></label>
          <label>腐败程度（%）<input v-model.number="spoilage" type="number" min="0" max="100" step="5" /></label>
          <label>肉排剩余切块<select v-model.number="pieces" aria-label="肉排剩余切块"><option v-for="n in 6" :key="n" :value="n">{{ n }} / 6（只影响 Rustic 肉排）</option></select></label>
        </div><p class="hint">熟制场景按熟食校准或维生素保留率计算；实际能否入锅取决于配方。派使用自身烘焙状态。腐败减少有效营养与能量，重量、水分和物理钠钾量保持不变。微量营养列是计入营养储备的折算量，未声明值不是零。</p></details>
        <div class="filters numeric">
          <label>比较营养项<select v-model="metric" aria-label="比较营养项"><option v-for="([name,unit],key) in metrics" :key="key" :value="key">{{ name }}（{{ unit }}）</option></select></label>
          <label>最低含量<input v-model="minimum" type="number" min="0" step="any" placeholder="不限" /></label><label>最高含量<input v-model="maximum" type="number" min="0" step="any" placeholder="不限" /></label>
          <label>排序方式<select v-model="sort" aria-label="排序方式"><option value="name">名称顺序</option><option value="desc">所选营养：从高到低</option><option value="asc">所选营养：从低到高</option></select></label>
          <label>每页条数<select v-model.number="pageSize" aria-label="每页条数"><option :value="25">25 条</option><option :value="50">50 条</option><option :value="100">100 条</option></select></label>
        </div>
        <div class="result-tools"><p aria-live="polite">找到 {{ filtered.length }} 条记录 · 第 {{ page }} / {{ pages }} 页</p><button @click="share">复制检索链接</button><button :disabled="!filtered.length" @click="download">导出筛选结果 CSV</button><span role="status">{{ shareStatus }}</span></div>
        <section v-if="comparison.length" class="comparison" aria-label="食物营养对比"><h3>已选对比（{{ comparison.length }} / 4）</h3><p>跨食物比较建议选择每 100 克。</p><div class="table-scroll"><table><thead><tr><th>营养项</th><th v-for="r in comparison" :key="r.id">{{ r.name }}<br><small>{{ unitLabel(r) }}</small><br><button @click="toggle(r)">移除</button></th></tr></thead><tbody><tr v-for="([name,unit],key) in metrics" :key="key"><th>{{ name }}（{{ unit }}）</th><td v-for="r in comparison" :key="r.id">{{ fmt(displayedDose(r,options).values[key]) }}</td></tr></tbody></table></div></section>
        <div class="table-scroll results" tabindex="0" aria-label="食物表，可横向滚动"><table><thead><tr><th>对比</th><th>食物与状态</th><th>计量与质量</th><th>{{ metrics[metric][0] }}（{{ metrics[metric][1] }}）</th><th>主要营养（g）</th><th>完整营养与加工</th></tr></thead><tbody><tr v-for="{row:r,dose} in rows" :key="r.id">
          <td><input type="checkbox" :aria-label="'对比 '+r.name" :checked="selected.includes(r.id)" :disabled="selected.length>=4&&!selected.includes(r.id)" @change="toggle(r)" /></td>
          <td><strong>{{ r.name }}</strong><br><small>{{ preparations[r.preparation] }} · {{ r.modName }}</small><br><span class="badge">{{ coverage[r.coverage] }}</span><br><code>{{ r.code }}</code></td>
          <td>{{ unitLabel(r) }}<br>{{ fmt(dose.mass) }} g</td><td class="value">{{ fmt(dose.values[metric]) }}</td>
          <td>碳水 {{ fmt(dose.values.carbohydrate) }}<br>蛋白质 {{ fmt(dose.values.protein) }}<br>脂肪 {{ fmt(dose.values.fat) }}<br>纤维 {{ fmt(dose.values.fiber) }}<br>水分 {{ fmt(dose.values.water) }}</td>
          <td><details><summary>完整营养</summary><dl><template v-for="([name,unit],key) in metrics" :key="key"><dt>{{ name }}</dt><dd>{{ fmt(dose.values[key]) }} {{ unit }}</dd></template></dl><p v-if="r.coverage==='fallback'">采用原版饱食度和类别估算份量；未知微量营养不补零。</p></details>
            <details><summary>配料与加工说明</summary><p v-if="r.note">{{ r.note }}</p><ul v-if="r.ingredients"><li v-for="i in r.ingredients" :key="i.id">{{ i.name }} × {{ i.quantity }} <button @click="showFood(i)">查食材</button></li></ul><p v-if="!r.edible">此记录是加工材料／生派，需要完成相应制作步骤。</p><p>原版营养类别：{{ categories[r.category] || r.category }}；原版饱食度：{{ fmt(r.satiety) }}；健康值：{{ fmt(r.health) }}。</p><ul v-if="r.transitions"><li v-for="t in r.transitions" :key="t.id">{{ t.action }} → <button @click="showFood(t)">{{ t.name }}</button></li></ul><p v-if="!r.ingredients&&!r.transitions">可结合游戏内手册查找配方；具体成品和烹饪状态可直接按名称筛选。</p><p v-if="r.kind==='pie'">单一馅料示例；混合馅料请使用“自选配料计算”。</p></details>
          </td></tr></tbody></table></div>
        <p v-if="!rows.length" role="status">没有符合条件的食物。可移除筛选标签或清空含量范围；未知数值不参与含量范围筛选。</p>
        <div class="pagination"><button :disabled="page<=1" @click="page=1">首页</button><button :disabled="page<=1" @click="page--">上一页</button><label>跳转页码<input v-model.number="page" type="number" min="1" :max="pages" @change="page=Math.max(1,Math.min(pages,Number(page)||1))" /></label><span>/ {{ pages }}</span><button :disabled="page>=pages" @click="page++">下一页</button><button :disabled="page>=pages" @click="page=pages">末页</button></div>
      </section>
    </template>
  </div>
</template>

<style scoped>
.overview{display:grid;gap:6px;padding:16px;background:var(--vp-c-bg-soft);border-radius:10px;margin:18px 0}.overview strong{font-size:20px}.overview span,.hint,small{color:var(--vp-c-text-2);font-size:13px}.tabs,.chips,.result-tools,.pagination{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:16px 0}.tabs button[aria-pressed=true]{background:var(--vp-c-brand-soft);border-color:var(--vp-c-brand-1);color:var(--vp-c-brand-1)}.filters{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:12px}.search{grid-column:1/-1}label{display:flex;flex-direction:column;gap:5px;font-size:14px;min-width:0}input,select,button{border:1px solid var(--vp-c-divider);border-radius:6px;padding:8px;background:var(--vp-c-bg);color:var(--vp-c-text-1);max-width:100%;min-width:0}button{cursor:pointer;font-size:13px}button:disabled{opacity:.4;cursor:default}input[type=checkbox]{width:18px;height:18px}.calculator{max-width:none;border:1px solid var(--vp-c-divider);padding:12px;border-radius:8px;margin:16px 0}.calculator summary{margin-bottom:12px;cursor:pointer}.table-scroll{overflow:auto;max-width:100%}.table-scroll table{display:table;min-width:800px;margin:0}.table-scroll td{vertical-align:top}.table-scroll td:nth-child(2){min-width:200px;max-width:300px}.table-scroll code{font-size:11px;overflow-wrap:anywhere}.badge{display:inline-block;padding:1px 6px;border-radius:4px;background:var(--vp-c-bg-soft);font-size:12px}.value{font-weight:600;font-variant-numeric:tabular-nums}details{min-width:140px;max-width:470px}details summary{cursor:pointer}dl{display:grid;grid-template-columns:minmax(100px,1fr) auto;gap:4px 12px}dd{margin:0;white-space:nowrap}.pagination label{max-width:90px}.comparison{padding:12px;background:var(--vp-c-bg-soft);border-radius:8px;margin:16px 0}.comparison h3{margin:0}.result-tools p{margin:0}.result-tools span{font-size:12px}.numeric{margin-top:14px}@media(max-width:500px){.filters{grid-template-columns:minmax(0,1fr)}.overview strong{font-size:18px}}
</style>
