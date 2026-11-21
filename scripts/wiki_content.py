"""Only replace marked generated regions. Unmarked editorial pages receive drafts."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
START = '<!-- generated:start -->'
END = '<!-- generated:end -->'

def write_generated(path, content):
    path = Path(path)
    text = content.rstrip() + '\n'
    block = START + '\n' + text + END + '\n'
    if path.exists():
        old = path.read_text(encoding='utf-8')
        if START not in old:
            relative = path.relative_to(ROOT / 'docs')
            draft = ROOT / 'scripts/generated' / relative
            draft.parent.mkdir(parents=True, exist_ok=True)
            draft.write_text(text, encoding='utf-8')
            return
        if old.count(START) != 1 or old.count(END) != 1:
            raise ValueError(f'Ambiguous generated region: {path}')
        text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', lambda _: block, old, flags=re.S)
    else:
        text = block
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

def adopt(path):
    """Explicit one-time migration, never called by routine generation."""
    path = Path(path)
    if path.exists():
        text = path.read_text(encoding='utf-8')
        if START not in text:
            path.write_text(START + '\n' + text.rstrip() + '\n' + END + '\n', encoding='utf-8')
