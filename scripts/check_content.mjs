import fs from 'node:fs'
import path from 'node:path'
import assert from 'node:assert/strict'
import { nav, sidebar } from '../docs/.vitepress/navigation.mjs'
const read = p => fs.readFileSync(p,'utf8')
const resolvePage = link => {
  const raw=link.split('#')[0].replace(/^\//,'')
  return fs.existsSync('docs/'+raw+'.md') ? 'docs/'+raw+'.md' : 'docs/'+raw+(raw.endsWith('/')?'':'/')+'index.md'
}
for (const i of [...nav,...Object.values(sidebar).flatMap(groups=>groups.flatMap(g=>g.items))]) assert(fs.existsSync(resolvePage(i.link)),i.link)
for (const id of ['vsscsmod','vsscpmod','vsslssmod']) {
  assert(!read('docs/mods/entries/'+id+'.md').includes('| SHA-256 前 12 位 |'))
  assert(!fs.existsSync('docs/develop/sources/'+id+'.md'))
}
const data=JSON.parse(read('docs/public/data/food-catalogue.json'))
assert.equal(data.foods.length,352)
assert.equal(data.calibrations.length,414)
assert(!('patches' in data))
assert(data.foods.every(f=>!('file' in f)))
assert(data.calibrations.every(c=>!('Source' in c) && !('PortionBasis' in c)))
assert.equal(data.calibrationNames.length,data.calibrations.length)
assert.equal(data.foods.length,data.counts.foodRows)
assert(data.calibrationNames.some(n=>n.some(s=>s.includes('胡萝卜'))))
const mods=JSON.parse(read('docs/public/data/mod-catalogue.json'))
assert.equal(mods.length,JSON.parse(read('scripts/inventory-manifest.json')).length)
assert(mods.every(m=>m.title && m.category!=='待分类的新模组'))
assert.equal(new Set(mods.map(m=>m.id)).size,mods.length)
assert(mods.every(m=>Object.keys(m).sort().join(',')==='category,id,name,slug,title,version'))
assert(read('docs/develop/api.md').includes('1.0.3'))
assert(read('docs/develop/api.md').includes('RegisterFoodV1'))
// Public pages and downloads must not expose extraction paths or package evidence.
const publicFiles=[]
const walkPublic=dir=>{for(const e of fs.readdirSync(dir,{withFileTypes:true})) {
  if(e.name==='.vitepress') continue
  const p=path.join(dir,e.name)
  if(e.isDirectory()) walkPublic(p)
  else if(/\.(md|json)$/.test(p)) publicFiles.push(p)
}}
walkPublic('docs')
for(const file of publicFiles) {
  const text=read(file)
  assert(!/(?<![\w:/])[A-Za-z]:[\\/]/.test(text),file+': local drive path')
  assert(!/本机目录已省略|package-evidence:start|SHA-256|\/develop\/source-inventory|\/develop\/sources\/|\/develop\/maintenance/.test(text),file+': extraction provenance')
  assert(!/[\w/-]+\.cs(?::\d+|[<\x60])/.test(text),file+': source file citation')
}
const diseases=read('docs/guide/diseases.md')
assert.equal((diseases.match(/^### .*\{#/gm)||[]).length,21)
assert(diseases.includes('不是感染概率'))
// Validate internal links and fragments in rendered HTML, including old anchors.
const dist='docs/.vitepress/dist'
const base=process.env.WIKI_BASE || '/'
assert(base.startsWith('/') && base.endsWith('/'), 'WIKI_BASE must start and end with /')
if (fs.existsSync(dist)) {
  const files=[]
  const walk=dir=>{for(const e of fs.readdirSync(dir,{withFileTypes:true})) { const p=path.join(dir,e.name); if(e.isDirectory()) walk(p); else if(p.endsWith('.html')) files.push(p) }}
  walk(dist)
  const anchors=new Map(files.map(p=>[path.resolve(p),new Set([...read(p).matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]))]))
  const errors=[]
  for (const file of files) for (const [,raw] of read(file).matchAll(/\bhref="([^"\s]+)"/g)) {
    if (/^(https?:|mailto:|data:|javascript:|\/\/)/.test(raw)) continue
    const [url,hash]=raw.split('#')
    let clean=decodeURIComponent(url.split('?')[0])
    if (clean.startsWith('/') && base !== '/') {
      if (!clean.startsWith(base)) {
        errors.push(file+': link outside deployment base '+raw)
        continue
      }
      clean='/'+clean.slice(base.length)
    }
    let target=clean ? path.resolve(clean.startsWith('/')?dist:path.dirname(file),clean.replace(/^\//,'')) : path.resolve(file)
    if (fs.existsSync(target) && fs.statSync(target).isDirectory()) target=path.join(target,'index.html')
    if (!fs.existsSync(target) && !path.extname(target)) target+='.html'
    if (!fs.existsSync(target)) errors.push(file+': missing '+raw)
    else if (hash && anchors.has(target) && !anchors.get(target).has(decodeURIComponent(hash))) errors.push(file+': missing anchor '+raw)
  }
  assert.equal(errors.length,0,errors.slice(0,30).join('\n'))
  console.log('Checked rendered pages:',files.length)
}
console.log('Navigation, public metadata, current API, disease anchors and catalogue coverage OK')
