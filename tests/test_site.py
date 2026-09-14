import hashlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


assets = load('prepare-assets')
site = load('check-site')


class SourceTests(unittest.TestCase):
    def test_git_blob_hash(self):
        self.assertEqual(assets.blob_hash(b''), 'e69de29bb2d1d6434b8b29ae775ad8c2e48c5391')

    def test_source_hash_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'icon.png').write_bytes(b'wrong')
            with self.assertRaisesRegex(ValueError, 'hash mismatch'):
                assets.read_source({}, {'path': 'icon.png', 'blob': 'a'*40}, root / 'cache', root)

    def test_valid_cache_needs_no_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = b'pinned bytes'
            sha = assets.blob_hash(data)
            (root / sha).write_bytes(data)
            with patch.object(assets, 'urlopen', side_effect=AssertionError('network')):
                self.assertEqual(assets.read_source({}, {'path': 'x', 'blob': sha}, root), data)

    def test_language_table(self):
        self.assertIn('| Japanese | `ja` |', assets.language_table("iso: 'ja', iso639_3: 'jpn', name: 'Japanese'"))

    def test_language_shape_change_fails(self):
        with self.assertRaises(ValueError):
            assets.language_table('changed format')

    def test_duplicate_language_fails(self):
        with self.assertRaises(ValueError):
            assets.language_table("iso: 'ja', iso639_3: 'jpn', name: 'Japanese'" * 2)

    def test_pdf_is_deterministic_and_branded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            web = root / 'docs/manabitan-pdf-viewer/web'
            web.mkdir(parents=True)
            (root / 'scripts').mkdir()
            (root / 'scripts/pdf-introduction.txt').write_text('Manabitan PDF Viewer\n\nRead a PDF with selectable text.\n')
            (web / 'index.html').write_text('<title>PDF.js viewer</title>')
            (web / 'viewer.mjs').write_text('"manabitan-pdf-viewer.pdf"')
            assets.make_pdf(root)
            first = (web / 'manabitan-pdf-viewer.pdf').read_bytes()
            assets.make_pdf(root)
            self.assertEqual(first, (web / 'manabitan-pdf-viewer.pdf').read_bytes())
            self.assertTrue(first.startswith(b'%PDF-'))
            self.assertEqual((web / 'index.html').read_text().count('rel="icon"'), 1)


class URLTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'assets').mkdir()
        (self.root / 'assets/logo.png').touch()
        (self.root / 'guide').mkdir()
        path = self.root / 'guide/index.html'
        path.write_text('<title>Guide</title><h2 id="setup">Setup</h2>')
        self.pages = {path: site.Page(path.read_text())}

    def test_good_relative_asset(self):
        self.assertIsNone(site.check_reference(self.root, site.BASE + 'guide/', '../assets/logo.png', self.pages))

    def test_root_relative_escape(self):
        self.assertIn('Escapes', site.check_reference(self.root, site.BASE, '/assets/logo.png', self.pages))

    def test_css_parent_escape(self):
        self.assertIn('Escapes', site.check_reference(self.root, site.BASE + 'styles.css', '../assets/logo.png', self.pages))

    def test_fragment(self):
        self.assertIsNone(site.check_reference(self.root, site.BASE, 'guide/#setup', self.pages))
        self.assertIn('Missing anchor', site.check_reference(self.root, site.BASE, 'guide/#missing', self.pages))

    def test_old_host(self):
        self.assertIn('Obsolete', site.check_reference(self.root, site.BASE, 'https://manabitan.manabi.io/guide/', self.pages))

    def test_encoded_traversal(self):
        self.assertIn('Escapes', site.check_reference(self.root, site.BASE, '%2e%2e/secret', self.pages))

    def test_external_and_inline_resources(self):
        self.assertIsNone(site.check_reference(self.root, site.BASE, 'https://github.com/yomidevs/yomitan', self.pages))
        self.assertIsNone(site.check_reference(self.root, site.BASE, 'data:image/svg+xml,abc', self.pages))

    def test_css_parser_and_titles(self):
        self.assertEqual(site.css_urls("a{background:url('assets/logo.png')}"), ['assets/logo.png'])
        self.assertEqual(site.Page('<title>A</title><title>B</title>').titles, 2)


if __name__ == '__main__':
    unittest.main()
