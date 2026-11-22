import re, pathlib
roots={
'文明模拟':(pathlib.Path(__file__).resolve().parent.parent.parent/'Seraph Civilization Simulation'/'src'),
'文明补丁':(pathlib.Path(__file__).resolve().parent.parent.parent/'Seraph Civilization Patches'/'src'),
'生存模拟':(pathlib.Path(__file__).resolve().parent.parent.parent/'Seraph Living Survival Simulation'/'src')}
for n,root in roots.items():
 print('\n##',n)
 for p in sorted(root.rglob('*.cs')):
  if '\\obj\\' in str(p) or '\\bin\\' in str(p): continue
  t=p.read_text(encoding='utf-8-sig',errors='ignore')
  classes=re.findall(r'\b(?:public|internal|private|protected|sealed|static|partial|abstract|record|class|struct|interface|enum|file)\s+(?:sealed\s+|static\s+|partial\s+|abstract\s+)?(?:class|record|struct|interface|enum)?\s*([A-Za-z_][A-Za-z0-9_]*)',t)
  # simpler declarations
  decl=re.findall(r'\b(?:class|record|struct|interface|enum)\s+([A-Za-z_][A-Za-z0-9_]*)',t)
  print(f'- `{p.relative_to(root).as_posix()}`: '+', '.join(dict.fromkeys(decl))[:250])
