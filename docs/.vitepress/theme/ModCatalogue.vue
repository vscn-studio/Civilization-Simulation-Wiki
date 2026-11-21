<script setup>
import { ref, computed, onMounted } from 'vue'
import { withBase } from 'vitepress'
const entries = ref([]), query = ref(''), category = ref(''), error = ref('')
onMounted(async () => {
  try { const r = await fetch(withBase('/data/mod-catalogue.json')); if (!r.ok) throw new Error(String(r.status)); entries.value = await r.json() }
  catch { error.value = '模组目录暂时无法加载，请查看下方的完整清单。' }
})
const groups = computed(() => [...new Set(entries.value.map(x => x.category))])
const rows = computed(() => entries.value.filter(x => (!category.value || x.category === category.value) && [x.name,x.title,x.id,x.category].join(' ').toLowerCase().includes(query.value.trim().toLowerCase())))
</script>
<template>
  <div class="mod-catalogue">
    <div class="filters"><label>搜索名称或模组代码<input v-model="query" type="search" placeholder="例如：采石、stonequarry" /></label><label>玩法分类<select v-model="category"><option value="">全部分类</option><option v-for="g in groups" :key="g">{{ g }}</option></select></label></div>
    <p v-if="error" role="alert">{{ error }}</p><p v-else aria-live="polite">{{ rows.length }} 个模组</p>
    <table><thead><tr><th>模组</th><th>分类</th><th>版本</th></tr></thead><tbody><tr v-for="r in rows" :key="r.slug"><td><a :href="withBase('/mods/entries/'+r.slug+'.html')">{{ r.title }}</a><br><small>{{ r.name }} · {{ r.id }}</small></td><td>{{ r.category }}</td><td>{{ r.version }}</td></tr></tbody></table>
  </div>
</template>
<style scoped>
.filters { display:flex; flex-wrap:wrap; gap:12px; } label { display:flex; flex:1 1 180px; flex-direction:column; gap:5px; } input,select { border:1px solid var(--vp-c-divider); border-radius:6px; padding:8px; background:var(--vp-c-bg); color:var(--vp-c-text-1); min-width:0; } small { color:var(--vp-c-text-2); overflow-wrap:anywhere; }
</style>
