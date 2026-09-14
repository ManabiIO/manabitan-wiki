#!/usr/bin/env python3
"""Check the built tree at its real subpath, including HTML/CSS/search/sitemap URLs."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

BASE = 'https://manabi.io/manabitan/'


class Page(HTMLParser):
    def __init__(self, source: str):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.canonical: list[str] = []
        self.styles: list[str] = []
        self.in_style = False
        self.titles = 0
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('name'):
            self.ids.add(attrs['name'])
        for key in ('href', 'src', 'poster'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if attrs.get('style'):
            self.styles.append(attrs['style'])
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs.get('href', ''))
        if tag == 'title':
            self.titles += 1
        if tag == 'style':
            self.in_style = True

    def handle_endtag(self, tag):
        if tag == 'style':
            self.in_style = False

    def handle_data(self, data):
        if self.in_style:
            self.styles.append(data)


def css_urls(source: str) -> list[str]:
    return [match.strip(' \t\r\n\"\'') for match in re.findall(r'url\(([^)]+)\)', source)]


def page_url(path: Path, root: Path) -> str:
    relative = path.relative_to(root).as_posix()
    if relative.endswith('index.html'):
        relative = relative[:-len('index.html')]
    return BASE + relative


def check_reference(root: Path, origin: str, reference: str, pages: dict[Path, Page]) -> str | None:
    if reference.startswith(('data:', 'mailto:', 'tel:', 'javascript:')) or reference in ('', '#'):
        return None
    url = urlsplit(urljoin(origin, reference))
    if url.hostname != 'manabi.io':
        if url.hostname == 'manabitan.manabi.io':
            return f'Obsolete hostname: {reference}'
        return None
    if not unquote(url.path).startswith('/manabitan/'):
        return f'Escapes /manabitan/: {reference} from {origin}'
    relative = unquote(url.path)[len('/manabitan/'):]
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        return f'Escapes site directory: {reference}'
    if path.is_dir():
        path = path / 'index.html'
    if not path.is_file():
        return f'Missing file: {reference} from {origin}'
    if url.fragment and path.suffix == '.html' and path in pages:
        fragment = unquote(url.fragment)
        if fragment not in pages[path].ids:
            return f'Missing anchor #{fragment}: {reference} from {origin}'
    return None


def check(root: Path) -> list[str]:
    root = root.resolve()
    required = ['index.html', 'about-manabitan/index.html', 'yomitan-migration/index.html',
                'search/search_index.json', 'sitemap.xml', '404.html', 'assets/social/manabitan.png',
                'assets/icon/manabitan-icon128.png', 'assets/icon/manabitan-icon64.png',
                'manabitan-pdf-viewer/web/manabitan-pdf-viewer.pdf']
    errors = [f'Missing required output: {name}' for name in required if not (root / name).is_file()]
    pages = {path: Page(path.read_text(encoding='utf-8-sig')) for path in root.rglob('*.html')}
    for path, page in pages.items():
        origin = page_url(path, root)
        if page.titles != 1:
            errors.append(f'Expected one title: {path.relative_to(root)}')
        for canonical in page.canonical:
            if canonical != origin:
                errors.append(f'Incorrect canonical: {canonical}; expected {origin}')
        if 'manabitan-pdf-viewer' not in path.parts and path.name != '404.html' and not page.canonical:
            errors.append(f'Missing canonical: {path.relative_to(root)}')
        links = page.links + [url for style in page.styles for url in css_urls(style)]
        for reference in links:
            error = check_reference(root, origin, reference, pages)
            if error:
                errors.append(error)
    for path in root.rglob('*.css'):
        for reference in css_urls(path.read_text(encoding='utf-8')):
            error = check_reference(root, page_url(path, root), reference, pages)
            if error:
                errors.append(error)
    search = root / 'search/search_index.json'
    if search.is_file():
        for entry in json.loads(search.read_text())['docs']:
            error = check_reference(root, BASE, entry['location'], pages)
            if error:
                errors.append(error)
    sitemap = root / 'sitemap.xml'
    if sitemap.is_file():
        for location in ET.parse(sitemap).iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
            url = location.text or ''
            if not url.startswith(BASE):
                errors.append(f'Incorrect sitemap URL: {url}')
            else:
                error = check_reference(root, BASE, url, pages)
                if error:
                    errors.append(error)
    for prohibited in ('CNAME',):
        if (root / prohibited).exists():
            errors.append(f'Obsolete deployment artifact: {prohibited}')
    return sorted(set(errors))


if __name__ == '__main__':
    failures = check(Path(sys.argv[1] if len(sys.argv) > 1 else 'site'))
    if failures:
        print('\n'.join(failures), file=sys.stderr)
        raise SystemExit(1)
    print('Built-site links, assets, canonical URLs, search, and sitemap passed.')
