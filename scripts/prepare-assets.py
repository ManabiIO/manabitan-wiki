#!/usr/bin/env python3
"""Prepare pinned branding and reference data; never fetch a floating branch."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import shutil
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def blob_hash(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def read_source(spec: dict, entry: dict, cache: Path, source_dir: Path | None = None) -> bytes:
    expected = entry['blob']
    if not re.fullmatch(r'[0-9a-f]{40}', expected):
        raise ValueError('Invalid pinned blob hash')
    cached = cache / expected
    if source_dir is not None:
        data = (source_dir / entry['path']).read_bytes()
    elif cached.is_file() and blob_hash(cached.read_bytes()) == expected:
        return cached.read_bytes()
    else:
        revision = spec['revision']
        if not re.fullmatch(r'[0-9a-f]{40}', revision):
            raise ValueError('An immutable source revision is required')
        url = f"https://raw.githubusercontent.com/{spec['repository']}/{revision}/{entry['path']}"
        with urlopen(Request(url, headers={'User-Agent': 'manabitan-wiki-build'}), timeout=30) as response:
            data = response.read(10 * 1024 * 1024 + 1)
        if len(data) > 10 * 1024 * 1024:
            raise ValueError('Unexpectedly large source asset')
    if blob_hash(data) != expected:
        raise ValueError(f"Source hash mismatch: {entry['path']}")
    cache.mkdir(parents=True, exist_ok=True)
    temporary = cached.with_suffix('.tmp')
    temporary.write_bytes(data)
    temporary.replace(cached)
    return data


def language_table(source: str) -> str:
    entries = re.findall(r"iso: '([^']+)',\s+iso639_3: '[^']+',\s+name: '([^']+)'", source)
    if not entries or len({code for code, _ in entries}) != len(entries):
        raise ValueError('Language descriptor format changed or contains duplicate codes')
    rows = ['| Language | Code |', '| --- | --- |']
    for code, name in sorted(entries, key=lambda row: row[1].casefold()):
        if not re.fullmatch(r'[a-z0-9-]+', code) or any(c in name for c in '|\r\n'):
            raise ValueError('Invalid language-table cell')
        rows.append(f'| {escape(name)} | `{code}` |')
    return '\n'.join(rows) + '\n'


def make_pdf(root: Path) -> None:
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

    viewer = root / 'docs/manabitan-pdf-viewer'
    text = (root / 'scripts/pdf-introduction.txt').read_text(encoding='utf-8')
    paragraphs = text.strip().split('\n\n')
    styles = getSampleStyleSheet()
    styles['BodyText'].fontSize = 12
    styles['BodyText'].leading = 18
    content = [Paragraph(escape(paragraphs[0]), styles['Title']), Spacer(1, 20)]
    for paragraph in paragraphs[1:]:
        content.extend([Paragraph(escape(paragraph), styles['BodyText']), Spacer(1, 14)])
    path = viewer / 'manabitan-pdf-viewer.pdf'
    SimpleDocTemplate(str(path), title='Manabitan PDF Viewer', author='Manabitan contributors',
                      subject='Opening PDFs and looking up selectable text', invariant=1).build(content)
    shutil.copyfile(path, viewer / 'web/manabitan-pdf-viewer.pdf')
    index = viewer / 'web/index.html'
    html = index.read_text(encoding='utf-8-sig')
    if '<title>PDF.js viewer</title>' in html:
        html = html.replace('<title>PDF.js viewer</title>', '<title>Manabitan PDF Viewer</title>\n<link rel="icon" href="../../assets/icon/manabitan-icon64.png">', 1)
    elif '<title>Manabitan PDF Viewer</title>' not in html:
        raise ValueError('Review the changed PDF.js HTML title before building')
    index.write_text(html, encoding='utf-8')
    if 'manabitan-pdf-viewer.pdf' not in (viewer / 'web/viewer.mjs').read_text(encoding='utf-8'):
        raise ValueError('PDF.js does not point at the generated introduction')


def prepare(root: Path = ROOT, source_dir: Path | None = None) -> None:
    from PIL import Image, ImageDraw, ImageFont

    spec = json.loads((root / 'scripts/asset-sources.json').read_text())
    data = {name: read_source(spec, entry, root / '.cache/source-assets', source_dir)
            for name, entry in spec['files'].items()}
    icons = root / 'docs/assets/icon'
    icons.mkdir(parents=True, exist_ok=True)
    for size in (16, 64, 128):
        image = Image.open(io.BytesIO(data[f'icon{size}']))
        if image.size != (size, size) or image.format != 'PNG':
            raise ValueError('Pinned icon has unexpected dimensions or format')
        (icons / f'manabitan-icon{size}.png').write_bytes(data[f'icon{size}'])
    image = Image.open(io.BytesIO(data['icon128'])).convert('RGBA')
    image.save(root / 'docs/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    social = root / 'docs/assets/social'
    social.mkdir(parents=True, exist_ok=True)
    card = Image.new('RGB', (1200, 630), '#f5f4f0')
    card.paste(image.resize((192, 192)), (72, 72), image.resize((192, 192)))
    draw = ImageDraw.Draw(card)
    draw.text((72, 315), 'Manabitan', font=ImageFont.load_default(size=76), fill='#1c1c1c')
    draw.text((72, 420), 'Your dictionaries, with less waiting.', font=ImageFont.load_default(size=40), fill='#303030')
    card.save(social / 'manabitan.png')
    generated = root / '_generated'
    generated.mkdir(exist_ok=True)
    table = language_table(data['languages'].decode('utf-8'))
    if table.count('\n') < 36:
        raise ValueError('Language extraction unexpectedly lost entries')
    (generated / 'languages.md').write_text(table, encoding='utf-8')
    make_pdf(root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', type=Path, help='Optional local checkout matching the pinned asset hashes')
    prepare(source_dir=parser.parse_args().source_dir)
