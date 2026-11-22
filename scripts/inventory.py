from local_inputs import required_dir, source_dir
import json, os, re, zipfile, hashlib, html
from pathlib import Path
from html.parser import HTMLParser
ROOT = Path(__file__).resolve().parent.parent
PACK = required_dir('SERAPH_MODS_DIR')
SURVIVAL = source_dir('SERAPH_SURVIVAL_SOURCE', 'Seraph Living Survival Simulation')
OUT = ROOT / 'docs' / 'mods' / 'entries'
OUT.mkdir(parents=True, exist_ok=True)

def clean(s):
    return re.sub(r'\s+', ' ', str('' if s is None else s)).strip()
def cell(s):
    return clean(s).replace('|', r'\|').replace('<', '&lt;').replace('>', '&gt;') or '未声明'
def parse(raw):
    try:
        text = raw.decode('utf-8-sig')
        try: return json.loads(text)
        except ValueError:
            # Some mod manifests permit trailing commas. Only remove commas outside strings.
            result=[]; quoted=False; escaped=False
            for i, ch in enumerate(text):
                if quoted:
                    result.append(ch)
                    if escaped: escaped=False
                    elif ch == chr(92): escaped=True
                    elif ch == chr(34): quoted=False
                elif ch == chr(34): quoted=True; result.append(ch)
                elif ch == ',' and text[i+1:].lstrip().startswith(('}', ']')): continue
                else: result.append(ch)
            return json.loads(''.join(result))
    except (ValueError, UnicodeError): return {}
def load_item(path):
    if path.is_dir():
        files = [p for p in path.rglob('*') if p.is_file()]
        metadata = next((p for p in files if p.name.lower() == 'modinfo.json'), None)
        data = parse(metadata.read_bytes()) if metadata else {}
        readme = next((p for p in files if re.match(r'^readme(?:[._-]|$)', p.name, re.I) and p.stat().st_size < 100000), None)
        note = readme.read_text(encoding='utf-8-sig', errors='replace') if readme else ''
    else:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()
            info = next((n for n in names if n.lower().strip('/') == 'modinfo.json'), None)
            data = parse(z.read(info)) if info else {}
            readme = next((n for n in names if '/' not in n.strip('/') and re.match(r'^readme(?:[._-]|$)', n, re.I) and z.getinfo(n).file_size < 100000), None)
            note = z.read(readme).decode('utf-8-sig', errors='replace') if readme else ''
    return {str(k).lower():v for k,v in data.items()}, note

def safe_text(s):
    s = s.replace('\x00', '')
    return s[:12000].strip()

entries=[]
for path in sorted(PACK.iterdir(), key=lambda x: x.name.casefold()):
    if not path.is_dir() and path.suffix.lower() != '.zip': continue
    try: d,note=load_item(path)
    except (OSError, zipfile.BadZipFile): d,note={},''
    ident=clean(d.get('modid')) or path.stem
    slug=re.sub(r'[^a-z0-9-]+','-',ident.lower()).strip('-') or hashlib.sha256(path.name.encode()).hexdigest()[:12]
    name=clean(d.get('name')) or path.stem
    entries.append({'slug':slug,'name':name,'id':ident,'version':clean(d.get('version')) or '未声明','file':path.name})
# A directory may contain outdated copies with the same mod ID. Publish only
# the highest declared version, keeping stable links keyed by that ID.
latest={}
for entry in entries:
    key=entry['id'].casefold()
    version=lambda e:tuple(int(n) for n in re.findall(r'\d+',e['version']))
    if key not in latest or version(entry)>version(latest[key]):
        latest[key]=entry
entries=list(latest.values())
index=['# 整合包模组图鉴','',f'本地快照共收录 **{len(entries)}** 个安装包或模组目录。每个条目记录包内声明，点击查看详细信息；清单不代表服务器当前运行状态。','', '| 名称 | 模组 ID | 版本 |', '| --- | --- | --- |']
for e in sorted(entries,key=lambda e:e['name'].casefold()): index.append('| [{}](/mods/entries/{}) | `{}` | {} |'.format(cell(e['name']),e['slug'],cell(e['id']),cell(e['version'])))
(ROOT/'scripts/inventory-manifest.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
from site_catalogue import main as refresh_catalogue
refresh_catalogue()

class TextHTML(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip_link=False
    def handle_starttag(self,tag,attrs):
        if tag=='br': self.parts.append('\n')
        elif tag in ('p','div'): self.parts.append('\n\n')
        elif tag=='strong': self.parts.append('**')
        elif tag=='a' and any(k=='href' and v and v.startswith('handbook://') for k,v in attrs): self.skip_link=True
    def handle_endtag(self,tag):
        if tag=='strong': self.parts.append('**')
        elif tag=='a': self.skip_link=False
        elif tag in ('p','div'): self.parts.append('\n\n')
    def handle_data(self,data):
        if not self.skip_link: self.parts.append(data)
langs=json.loads((SURVIVAL/'assets/vsslssmod/lang/zh-cn.json').read_text(encoding='utf-8-sig'))
chapters=['# 生存模拟游戏内手册','', '生存模拟 1.0.3 中文游戏内手册。游戏内可按 H 搜索并查看相关物品；数值会受配置影响。','']
for f in sorted((SURVIVAL/'assets/vsslssmod/config/handbook').glob('*.json')):
    d=json.loads(f.read_text(encoding='utf-8-sig')); title=langs.get(d['title'].split(':',1)[-1],d['title']); text=langs.get(d['text'].split(':',1)[-1],d['text']); parser=TextHTML(); parser.feed(text)
    body=re.sub(r'\n{3,}','\n\n',''.join(parser.parts)).strip().replace('<','&lt;')
    chapters += ['## '+title, '', body, '']
from wiki_content import write_generated
write_generated(ROOT/'docs/guide/handbook.md','\n'.join(chapters))
print('Indexed',len(entries),'packages and generated handbook')

