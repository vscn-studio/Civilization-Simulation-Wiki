<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { withBase } from 'vitepress'
import { nutrients, categories, preparations, confidence, formatNumber as fmt } from './terms.mjs'
const data = ref(null), error = ref(''), query = ref(''), mod = ref(''), category = ref(''), mode = ref('calibration'), basis = ref('100'), page = ref(1)
const pageSize = 25
onMounted(async () => {
  try { const r = await fetch(withBase('/data/food-catalogue.json')); if (!r.ok) throw new Error('HTTP '+r.status); data.value = await r.json() }
  catch (e) { error.value = '食物数据加载失败：'+e.message+'。可通过下方链接下载数据。' }
})
const calibrationRows = computed(() => (data.value?.calibrations || []).map((c,i) => {
  const names = data.value.calibrationNames?.[i] || []
  const matches = data.value.foods.filter(r => r.calibrations.includes(i))
  return { c, i, names: names.length ? names : [...new Set(matches.flatMap(r=>r.names))], mods:[...new Set(matches.map(r=>r.mod))] }
}))
const mods = computed(() => [...new Map((data.value?.foods || []).map(r=>[r.mod,r.modName])).entries()])
const foodCategories = computed(() => [...new Set((data.value?.foods || []).map(r=>r.category))])
const search = values => values.join(' ').toLowerCase().includes(query.value.trim().toLowerCase())
const filtered = computed(() => mode.value === 'calibration'
  ? calibrationRows.value.filter(r => (!mod.value || r.mods.includes(mod.value)) && search([...r.names,...r.c.Codes]))
  : (data.value?.foods || []).filter(r => (!mod.value || mod.value===r.mod) && (!category.value || category.value===r.category) && search([...r.names,...r.codes,r.code,r.modName,r.condition])))
const pages = computed(() => Math.max(1,Math.ceil(filtered.value.length/pageSize)))
const rows = computed(() => filtered.value.slice((page.value-1)*pageSize,page.value*pageSize))
watch([query,mod,category,mode],()=>{ page.value=1 })
watch(mode,()=>{ category.value=''; mod.value='' })
const factor = c => basis.value==='portion' ? (c.PortionG > 0 ? c.PortionG/100 : null) : 1
const amount = (c,v) => v == null || factor(c)==null ? '未声明' : fmt(v*factor(c))
const nutrientRows = c => Object.entries(nutrients).map(([key,[label,unit]])=>({key,label,unit,value:c.Per100G?.[key] ?? c.MicroPer100G?.[key]}))
const names = row => row.names.filter(n=>/[\u4e00-\u9fff]/.test(n)).slice(0,3).join('、') || '暂无中文名称（按物品代码查询）'
</script>

<template>
  <div class="food-catalogue" aria-label="食物营养检索">
    <p v-if="error" role="alert">{{ error }}</p>
    <p v-else-if="!data" role="status">正在读取食物表……</p>
    <template v-else>
      <div class="filters">
        <label>查看数据<select v-model="mode"><option value="calibration">Seraph 全部营养校准（{{ data.calibrations.length }} 条）</option><option value="native">原版与整合包营养分支（{{ data.foods.length }} 条）</option></select></label>
        <label>名称或代码<input v-model="query" type="search" placeholder="例如：胡萝卜、carrot" /></label>
        <label>来源模组<select v-model="mod"><option value="">全部来源</option><option v-for="[id,name] in mods" :key="id" :value="id">{{ name }}</option></select></label>
        <label v-if="mode==='native'">原版营养类别<select v-model="category"><option value="">全部类别</option><option v-for="c in foodCategories" :key="c" :value="c">{{ categories[c] || c }}</option></select></label>
        <label v-else>营养计量<select v-model="basis"><option value="100">每 100 克</option><option value="portion">每份（校准份量）</option></select></label>
      </div>
      <p v-if="mode==='calibration'">每份按校准食用质量换算；液体和混合餐需结合实际内容核对。</p>
      <p v-else>原版饱食度与 Seraph 营养采用不同计量方式。此处保留资源中的条件分支，不将其合并为游戏最终数值。</p>
      <p aria-live="polite">找到 {{ filtered.length }} 条记录 · 第 {{ page }} / {{ pages }} 页</p>
      <div class="table-scroll" tabindex="0" aria-label="食物表，可横向滚动">
        <table v-if="mode==='calibration'"><thead><tr><th>食物</th><th>校准份量</th><th>水分（g）</th><th>能量（kJ）</th><th>宏量营养（g）</th><th>完整营养</th></tr></thead>
          <tbody><tr v-for="r in rows" :key="r.i">
            <td>{{ names(r) }}<br><small>{{ preparations[r.c.Preparation] || '加工状态见原始记录' }}</small></td>
            <td>{{ fmt(r.c.PortionG) }} g</td><td>{{ amount(r.c,r.c.WaterGPer100G) }}</td><td>{{ amount(r.c,r.c.EnergyKJPer100G) }}</td>
            <td>碳水 {{ amount(r.c,r.c.Per100G?.carbohydrate) }}<br>蛋白质 {{ amount(r.c,r.c.Per100G?.protein) }}<br>脂肪 {{ amount(r.c,r.c.Per100G?.fat) }}<br>纤维 {{ amount(r.c,r.c.Per100G?.fiber) }}</td>
            <td><details><summary>微量营养与电解质</summary>
              <p>以下按{{ basis==='100' ? '每 100 克' : '每份校准质量' }}显示。</p>
              <dl><template v-for="n in nutrientRows(r.c)" :key="n.key"><dt>{{ n.label }}</dt><dd>{{ amount(r.c,n.value) }} {{ n.unit }}</dd></template>
              <dt>钠</dt><dd>{{ amount(r.c,r.c.SodiumMgPer100G) }} mg</dd><dt>钾</dt><dd>{{ amount(r.c,r.c.PotassiumMgPer100G) }} mg</dd>
              <dt>酒精</dt><dd>{{ amount(r.c,r.c.AlcoholGPer100G) }} g</dd></dl>
            </details><details><summary>技术说明与原始记录</summary><p>数据置信度：{{ confidence[r.c.Confidence] || '未声明' }}。未声明值不能当作零。</p><p>物品代码：{{ r.c.Codes.join('、') }}</p><pre>{{ JSON.stringify(r.c,null,2) }}</pre></details></td>
          </tr></tbody>
        </table>
        <table v-else><thead><tr><th>食物与所属模组</th><th>营养类别</th><th>原版饱食度</th><th>健康值</th><th>适用条件</th></tr></thead>
          <tbody><tr v-for="(r,index) in rows" :key="[r.mod,r.condition,r.code,page,index].join(':')">
            <td>{{ names(r) }}<br><small>{{ r.modName }}</small></td><td>{{ categories[r.category] || r.category }}</td><td>{{ fmt(r.satiety) }}</td><td>{{ fmt(r.health) }}</td>
            <td><details><summary>适用条件与技术说明</summary><p>代码：{{ r.codes.join('、') || r.code }}</p><p>营养适用字段：<code>{{ r.condition }}</code></p><p v-if="r.liquidUnits!=null">每升物品数：{{ fmt(r.liquidUnits) }}</p><p>匹配到 {{ r.calibrations.length }} 条 Seraph 校准；可切换至校准表按代码搜索。未匹配不表示零营养。</p><pre>{{ JSON.stringify(r.nutrition,null,2) }}</pre><p v-if="r.unresolvedVariants.length">尚未展开的变体：</p><pre v-if="r.unresolvedVariants.length">{{ JSON.stringify(r.unresolvedVariants,null,2) }}</pre></details></td>
          </tr></tbody>
        </table>
      </div>
      <p v-if="!rows.length">没有符合条件的记录。尝试完整物品代码，或取消来源筛选。</p>
      <div class="pagination"><button :disabled="page<=1" @click="page--">上一页</button><span>{{ page }} / {{ pages }}</span><button :disabled="page>=pages" @click="page++">下一页</button></div>
    </template>
  </div>
</template>

<style scoped>
.filters { display:flex; flex-wrap:wrap; gap:12px; }
label { display:flex; flex:1 1 180px; flex-direction:column; gap:5px; font-size:14px; }
input,select { border:1px solid var(--vp-c-divider); border-radius:6px; padding:8px; background:var(--vp-c-bg); color:var(--vp-c-text-1); min-width:0; max-width:100%; }
.table-scroll { overflow:auto; max-width:100%; } .table-scroll table { display:table; min-width:740px; }
td:first-child { min-width:150px; } td { vertical-align:top; }
details { max-width:560px; } pre { white-space:pre-wrap; overflow-wrap:anywhere; font-size:12px; max-height:340px; overflow:auto; }
dl { display:grid; grid-template-columns:minmax(120px,1fr) auto; gap:3px 12px; } dd { margin:0; }
small { color:var(--vp-c-text-2); }
.pagination { display:flex; align-items:center; gap:18px; margin-top:16px; } button { border:1px solid var(--vp-c-divider); padding:5px 14px; border-radius:6px; } button:disabled { opacity:.4; }
</style>
