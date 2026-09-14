#!/usr/bin/env python3
"""Update vendored PDF.js only to an explicit, checksum-verified release."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
LIMIT = 256 * 1024 * 1024


def stage_archive(archive: Path, stage: Path) -> None:
    total = 0
    with zipfile.ZipFile(archive) as bundle:
        for item in bundle.infolist():
            path = PurePosixPath(item.filename)
            if path.is_absolute() or '..' in path.parts or '\\' in item.filename:
                raise ValueError('Unsafe PDF.js archive path')
            if not path.parts or path.parts[0] not in ('build', 'web', 'LICENSE', 'NOTICE'):
                continue
            if (item.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError('PDF.js archive must not contain symlinks')
            total += item.file_size
            if total > LIMIT:
                raise ValueError('PDF.js archive exceeds size limit')
            target = stage.joinpath(*path.parts)
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with bundle.open(item) as source, target.open('xb') as output:
                    shutil.copyfileobj(source, output)
    for name in ('build/pdf.mjs', 'build/pdf.worker.mjs', 'web/viewer.html', 'web/viewer.mjs', 'web/viewer.css'):
        if not (stage / name).is_file():
            raise ValueError(f'Review changed PDF.js distribution: missing {name}')
    script = stage / 'web/viewer.mjs'
    text = script.read_text()
    needle = 'compressed.tracemonkey-pldi-09.pdf'
    if text.count(needle) != 1:
        raise ValueError('Review changed PDF.js default-document configuration')
    script.write_text(text.replace(needle, 'manabitan-pdf-viewer.pdf'))
    (stage / 'web/viewer.html').rename(stage / 'web/index.html')
    (stage / 'web/compressed.tracemonkey-pldi-09.pdf').unlink(missing_ok=True)


def update(version: str, expected: str) -> None:
    if not re.fullmatch(r'\d+\.\d+\.\d+', version) or not re.fullmatch(r'[0-9a-f]{64}', expected):
        raise ValueError('Specify a numeric PDF.js version and the independently verified SHA-256')
    viewer = ROOT / 'docs/manabitan-pdf-viewer'
    with tempfile.TemporaryDirectory(prefix='pdfjs-update-') as work:
        temporary = Path(work)
        archive = temporary / 'pdfjs.zip'
        url = f'https://github.com/mozilla/pdf.js/releases/download/v{version}/pdfjs-{version}-dist.zip'
        with urlopen(Request(url, headers={'User-Agent':'manabitan-wiki-maintenance'}), timeout=60) as response:
            data = response.read(LIMIT + 1)
        if len(data) > LIMIT or hashlib.sha256(data).hexdigest() != expected:
            raise ValueError('PDF.js release checksum mismatch or size limit exceeded')
        archive.write_bytes(data)
        stage = temporary / 'stage'
        stage.mkdir()
        stage_archive(archive, stage)
        # All archive/format validation has completed before touching the working tree.
        for name in ('build', 'web'):
            destination = viewer / name
            if destination.exists():
                shutil.rmtree(destination)
            shutil.copytree(stage / name, destination)
        for name in ('LICENSE', 'NOTICE'):
            if (stage / name).is_file():
                shutil.copyfile(stage / name, viewer / ('PDFJS-' + name))
        (ROOT / 'scripts/pdfjs-source.json').write_text(json.dumps({'version':version, 'sha256':expected, 'url':url}, indent=2) + '\n')
    print('PDF.js staged. Run prepare-assets.py, strict MkDocs build, check-site.py, and browser viewer tests before committing.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True)
    parser.add_argument('--sha256', required=True)
    args = parser.parse_args()
    update(args.version, args.sha256)
