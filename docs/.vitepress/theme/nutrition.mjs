import { nutrients, categories } from './terms.mjs'
export const preparations = { raw:'生食／未加热', cooked:'熟制', baked:'烤熟', smoked:'烟熏', dried:'干燥', dry:'干制', cured:'盐腌', liquid:'液体', fermented:'发酵', roasted:'烤制', partbaked:'半熟', charred:'烤焦', juice:'果汁', dough:'面团', pickled:'腌渍', milled:'磨粉', ground:'研磨', aged:'熟成', 'as-served':'即食', churned:'搅制乳品', rendered:'熬制油脂', prepared:'混合制作', salt:'食盐', salted:'加盐', soaked:'浸泡', distilled:'蒸馏', syrup:'糖浆', unknown:'类别估算' }
export const kinds = { food:'食材与成品', liquid:'液体（每升）', pie:'馅饼配方（每片）' }
export const coverage = { reference:'具体成分校准', recipe:'配方计算', substitution:'替代食材校准', fallback:'类别估算' }
export const metrics = { energy:['能量','kJ'], water:['水分','g'], ...nutrients, sodium:['钠','mg'], potassium:['钾','mg'], electrolytes:['电解质','点'], alcohol:['酒精','g'] }
export const basisNames = { item:'每个', litre:'每升', slice:'每片（¼ 派）' }
export const normalize = text => String(text ?? '').normalize('NFKC').toLocaleLowerCase().replace(/\s+/g,' ').trim()
export const scaleDose = (dose, factor) => ({ mass:dose.mass*factor, values:Object.fromEntries(Object.entries(dose.values).map(([k,v])=>[k,v*factor])) })
export function combineDoses(doses) {
  if (!doses.length) return null
  return { mass:doses.reduce((s,d)=>s+d.mass,0), values:Object.fromEntries(Object.keys(doses[0].values).filter(k=>doses.every(d=>d.values[k]!=null)).map(k=>[k,doses.reduce((s,d)=>s+d.values[k],0)])) }
}
export function expandCatalogue(data) {
  const rows = [...data.rows]
  for (const [ci,fi,covered,level] of data.pieVariants) {
    const crust=data.rows[ci], filling=data.rows[fi], preparation=['raw','partbaked','baked','charred'][level]
    const dough=scaleDose(level>=2?crust.cookedDose:crust.dose,covered?4:2)
    const fill=scaleDose(level>=2?filling.cookedDose:filling.dose,8)
    if (level) {
      const dry=Math.max(0,dough.mass-dough.values.water), limit=[0,.5,.327,.2][level]
      dough.values.water=Math.min(dough.values.water,dry*limit/(1-limit)); dough.mass=dry+dough.values.water
    }
    rows.push({ id:`pie:${crust.code}:${filling.code}:${covered}:${preparation}`, code:`game:pie-${level===2?'perfect':preparation}`,
      name:`${filling.name} · ${crust.name} · ${covered?'带顶皮':'敞口'}${['生派','半熟派','烤熟派','烤焦派'][level]}`,
      mod:'game', modName:'原版', ingredientMods:[...new Set([crust.mod,filling.mod])], category:filling.category,
      kind:'pie', preparation, coverage:'recipe', basis:'slice', edible:level>0, perishable:true,
      dose:scaleDose(combineDoses([dough,fill]),.25),
      ingredients:[{id:crust.id,code:crust.code,name:crust.name,quantity:covered?4:2},{id:filling.id,code:filling.code,name:filling.name,quantity:8}],
      note:'配料数量为整派用量；营养按四分之一派显示。' })
  }
  return rows.map(row=>({...row, search:normalize([row.name,row.code,row.mod,row.modName,preparations[row.preparation],kinds[row.kind],categories[row.category],coverage[row.coverage],...(row.ingredients||[]).flatMap(i=>[i.name,i.code])].join(' '))}))
}
export function searchMatches(row, query) {
  return normalize(query).split(/\s+/).filter(Boolean).every(token=>row.search.includes(token))
}
export function displayedDose(row, {basis='portion',quantity=1,spoilage=0,process='current',pieces=6}={}) {
  const dose=process==='cooked' && row.kind!=='pie' ? row.cookedDose || row.dose : row.dose
  let factor=basis==='100' ? 100/dose.mass : Math.max(0,Number(quantity)||0)
  if (basis!=='100' && row.code.startsWith('rusticcookery:meatslab-')) factor*=Math.max(1,Math.min(6,Number(pieces)||6))/6
  const result=scaleDose(dose,factor), retained=1-Math.max(0,Math.min(100,Number(spoilage)||0))/100
  for (const key of Object.keys(result.values)) if (!['water','alcohol','sodium','potassium'].includes(key)) result.values[key]*=retained
  return result
}
export function csvText(rows, options) {
  const cell=value=>`"${String(value??'').replace(/^[=+\-@]/,"'$&").replaceAll('"','""')}"`
  return '\uFEFF'+[['名称','物品代码','模组','加工状态','计量','质量（g）',...Object.values(metrics).map(([n,u])=>`${n}（${u}）`)],
    ...rows.map(r=>{const d=displayedDose(r,options);return [r.name,r.code,r.modName,preparations[r.preparation],options.basis==='100'?'每100克':`${options.quantity} × ${basisNames[r.basis]}`,d.mass,...Object.keys(metrics).map(k=>d.values[k]??'未声明')]})]
    .map(row=>row.map(cell).join(',')).join('\r\n')
}

export function assignMeal(recipe, selected) {
  const inputs=selected.filter(Boolean), counts=recipe.roles.map(()=>0), assignment=[]
  function visit(index) {
    if(index===inputs.length)return recipe.roles.every((role,i)=>counts[i]>=role.min)
    for(let i=0;i<recipe.roles.length;i++) {
      const role=recipe.roles[i], option=role.options.find(o=>o.id===inputs[index])
      if(!option||counts[i]>=role.max)continue
      counts[i]++;assignment.push(option)
      if(visit(index+1))return true
      counts[i]--;assignment.pop()
    }
    return false
  }
  return visit(0)?assignment:null
}
export function pieDose(crust, fillings, covered, level) {
  if(!crust||fillings.length!==4||fillings.some(f=>!f))return null
  const same=fillings.every(f=>f.id===fillings[0].id)
  const category=fillings.every(f=>f.pie.category===fillings[0].pie.category)
  const codes=fillings[0].pie.mixingCodes.filter(code=>fillings.every(f=>f.pie.mixingCodes.includes(code)))
  if(!same&&(!fillings.every(f=>f.pie.mixing)||(!category&&!codes.length)))return null
  const dough=scaleDose(level>=2?crust.cookedDose:crust.dose,covered?4:2)
  if(level){const dry=Math.max(0,dough.mass-dough.values.water),limit=[0,.5,.327,.2][level];dough.values.water=Math.min(dough.values.water,dry*limit/(1-limit));dough.mass=dry+dough.values.water}
  return combineDoses([dough,...fillings.map(f=>scaleDose(level>=2?f.cookedDose:f.dose,2))])
}
