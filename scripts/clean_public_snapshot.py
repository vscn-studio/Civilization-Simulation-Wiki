# -*- coding: utf-8 -*-
"""Explicit migration of the previous public snapshot; normal refresh uses wiki_content."""
import json
from pathlib import Path
from public_content import public_markdown, public_food_data, RETIRED_PAGES
from site_catalogue import main, entry_content
from wiki_content import ROOT, START, END


def migrate():
    for relative in RETIRED_PAGES:
        page = ROOT/'docs'/relative
        if page.exists():
            page.unlink()
    for page in (ROOT/'docs').rglob('*.md'):
        if '.vitepress' in page.parts:
            continue
        text = page.read_text(encoding='utf-8')
        cleaned = public_markdown(text)
        if text != cleaned:
            page.write_text(cleaned, encoding='utf-8')
    datafile = ROOT/'docs/public/data/food-catalogue.json'
    data = public_food_data(json.loads(datafile.read_text(encoding='utf-8')))
    datafile.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    # Entry pages now contain catalogue metadata and tutorial links only.
    entries = json.loads((ROOT/'docs/public/data/mod-catalogue.json').read_text(encoding='utf-8'))
    for row in entries:
        (ROOT/'docs/mods/entries'/(row['slug']+'.md')).write_text(
            START+'\n'+entry_content(row)+END+'\n', encoding='utf-8')
    main()


if __name__ == '__main__':
    migrate()
