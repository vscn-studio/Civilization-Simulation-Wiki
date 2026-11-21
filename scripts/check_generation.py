# -*- coding: utf-8 -*-
"""Refresh twice, prove generated outputs are stable and unmarked prose is protected."""
from pathlib import Path
import hashlib, subprocess, sys, tempfile
import wiki_content
ROOT=wiki_content.ROOT

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def files():
    return {p.relative_to(ROOT).as_posix():digest(p) for p in (ROOT/'docs').rglob('*') if p.is_file() and not any(x in ('dist','cache') for x in p.parts)}

def refresh():
    for script in ['source_details.py','source_feature_pages.py','site_catalogue.py','asset_catalogue.py']:
        subprocess.run([sys.executable,str(ROOT/'scripts'/script)],cwd=ROOT,check=True)

def main():
    protected={p:digest(p) for p in (ROOT/'docs').rglob('*.md') if '.vitepress' not in p.parts and wiki_content.START not in p.read_text(encoding='utf-8')}
    # Asset reference-link regions are separately owned; protect prose outside those regions.
    import re
    clean=lambda p:re.sub(r'\n<!-- reference-link:start -->.*?<!-- reference-link:end -->\n','\n',p.read_text(encoding='utf-8'),flags=re.S).strip()
    prose={p:clean(p) for p in protected}
    refresh(); first=files(); refresh(); second=files()
    changed=[p for p in set(first)|set(second) if first.get(p)!=second.get(p)]
    assert not changed,changed
    assert all(clean(p)==text for p,text in prose.items()),'Unmarked editorial text changed'
    with tempfile.TemporaryDirectory() as folder:
        wiki_content.ROOT=Path(folder)
        target=Path(folder)/'docs/example.md'; target.parent.mkdir()
        target.write_text('manual intro\n'+wiki_content.START+'\nold\n'+wiki_content.END+'\nmanual footer\n',encoding='utf-8')
        wiki_content.write_generated(target,'new data')
        text=target.read_text(encoding='utf-8')
        assert text.startswith('manual intro\n') and text.endswith('manual footer\n')
        wiki_content.write_generated(target,'new data'); assert target.read_text(encoding='utf-8')==text
        target.write_text('manual only',encoding='utf-8')
        wiki_content.write_generated(target,'draft')
        assert target.read_text(encoding='utf-8')=='manual only'
        assert (Path(folder)/'scripts/generated/example.md').read_text(encoding='utf-8')=='draft\n'
    wiki_content.ROOT=ROOT
    print(f'Idempotence and editorial protection OK: {len(second)} files')

if __name__=='__main__': main()
