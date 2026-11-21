"""Summarize declared recipe fields; never invent defaults or runtime availability."""
import html, re

def safe(value):
    return html.escape(str(value),quote=False).replace('|','&#124;').replace('`','&#96;').replace('{{','&#123;&#123;').replace('\n','<br>')

def display_name(code,domain,langs,kind='item'):
    if not isinstance(code,str): return '未声明物品名称'
    dom,key=code.split(':',1) if ':' in code else (domain,code)
    for typ in [kind,'block' if kind=='item' else 'item']:
        value=langs.get((dom,typ+'-'+key)) or langs.get((dom,dom+':'+typ+'-'+key))
        if value and re.search('[\u4e00-\u9fff]',value): return re.sub('<[^>]*>','',value)
    return '变体材料（按代码匹配）' if '*' in code or '{' in code else '名称未汉化（见物品代码）'

def recipe_summary(data,domain,langs):
    out=[]
    recipes=data if isinstance(data,list) else [data]
    for i,r in enumerate(recipes):
        if not isinstance(r,dict): continue
        out += [f'**方案 {i+1}**',''] if len(recipes)>1 else []
        ingredients=r.get('ingredients',{})
        rows=[]
        def collect(obj,label):
            if isinstance(obj,list):
                for j,v in enumerate(obj): collect(v,f'{label} {j+1}')
            elif isinstance(obj,dict):
                if 'code' in obj:
                    code=obj['code']; name=display_name(code,domain,langs,obj.get('type','item'))
                    quantity=obj.get('quantity',obj.get('stacksize',obj.get('stackSize','未声明；按配方类型判定')))
                    if 'litres' in obj: quantity=f'{obj["litres"]} 升'
                    notes=[]
                    if obj.get('isTool'): notes.append('工具')
                    for k,cn in [('toolDurabilityCost','耐久消耗'),('consumeQuantity','实际消耗量'),('allowedVariants','允许变体'),('skipVariants','排除变体'),('minQuantity','最少数量'),('maxQuantity','最多数量')]:
                        if k in obj: notes.append(cn+'：'+str(obj[k]))
                    rows.append(f'| {safe(label)} | {safe(name)}<br><code>{safe(code)}</code> | {safe(quantity)} | {safe("；".join(notes) or "未声明附加限制")} |')
                else:
                    for k,v in obj.items():
                        if isinstance(v,(list,dict)): collect(v,f'{label} {k}')
        collect(ingredients,'投入')
        collect(r.get('output',{}),'产物')
        if rows:
            out += ['| 用途／格位符号 | 材料或产物 | 数量 | 工具与变体限制 |','| --- | --- | --- | --- |',*rows,'']
        conditions=[]
        labels={'enabled':'配方开关','requiresTrait':'所需特性','sealHours':'密封时间（游戏小时）','cookingTime':'烹饪时间（原字段单位）','meltingPoint':'熔点','meltingDuration':'熔化时长（原字段单位）','width':'网格宽度','height':'网格高度','minTemp':'最低温度','maxTemp':'最高温度'}
        for key,cn in labels.items():
            if key in r: conditions.append(cn+'：'+safe(r[key]))
        if conditions: out += ['**加工条件：** '+'；'.join(conditions)+'。','']
        pattern=r.get('ingredientPattern')
        if isinstance(pattern,str):
            out += ['**摆放步骤：** 将上表格位符号对应的材料按下列网格放置；逗号分隔行，空白或下划线表示空位。工具按配方标注保留或消耗耐久。','', '```text', pattern.replace(',','\n'),'```','']
        elif rows:
            out += ['**操作顺序：** 准备上表投入，核对所属加工设备及条件，再检查产物。此文件未提供通用工作台摆放图；锻造、陶塑或特殊加工的形状见原始定义。','']
        else:
            out += ['此配方采用特殊结构，尚未生成材料摘要；请展开原始定义核对，不能把缺失摘要当作无材料配方。','']
    return out
