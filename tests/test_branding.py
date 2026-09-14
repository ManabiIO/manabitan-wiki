"""Offline palette contracts; browser/rendered-site checks are complementary."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CSS = (ROOT / 'docs/stylesheets/brand.css').read_text(encoding='utf-8')


def declarations(selector):
    # The four token blocks deliberately contain only flat declarations.
    match = re.search(r'^' + re.escape(selector) + r'\s*\{([^{}]*)\}', CSS, re.M)
    if match is None:
        raise ValueError(f'Missing token block: {selector}')
    pairs = re.findall(r'(--[\w-]+)\s*:\s*([^;]+);', match[1])
    if len(dict(pairs)) != len(pairs):
        raise ValueError(f'Duplicate token in {selector}')
    return dict(pairs)


def tokens(scheme):
    result = declarations(':root')
    result.update(declarations(':root,\n[data-md-color-scheme="default"]'))
    if scheme == 'slate':
        result.update(declarations('[data-md-color-scheme="slate"]'))
    result.update(declarations(':root,\n[data-md-color-scheme]'))
    return result


def resolve(values, name, seen=()):
    if name in seen:
        raise ValueError(f'Cyclic token: {name}')
    return re.sub(r'var\((--[\w-]+)\)', lambda m: resolve(values, m[1], (*seen, name)), values[name])


def luminance(color):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', color):
        raise ValueError(f'Expected an opaque hex color: {color}')
    rgb = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    return sum(c * weight for c, weight in zip(linear, (.2126, .7152, .0722)))


def contrast(foreground, background):
    low, high = sorted((luminance(foreground), luminance(background)))
    return (high + .05) / (low + .05)


class BrandingTests(unittest.TestCase):
    def test_reader_brand_values(self):
        values = tokens('default')
        for name, expected in {'gold':'#d9b141', 'gold-hover':'#fcbd20', 'charcoal':'#1c1c1c',
                               'surface':'#222222', 'raised':'#323232', 'deep':'#0a0a0a'}.items():
            self.assertEqual(resolve(values, '--manabi-brand-' + name), expected)
        self.assertIn('661433220b3455770111415759effc908b1e135d', CSS)

    def test_all_token_aliases_resolve_in_both_schemes(self):
        for scheme in ('default', 'slate'):
            values = tokens(scheme)
            for name in values:
                with self.subTest(scheme=scheme, token=name):
                    self.assertNotIn('var(', resolve(values, name))

    def test_material_aliases_follow_theme(self):
        light, dark = tokens('default'), tokens('slate')
        self.assertEqual(resolve(light, '--md-default-bg-color'), '#faf8f3')
        self.assertEqual(resolve(dark, '--md-default-bg-color'), '#1c1c1c')
        self.assertEqual(resolve(light, '--md-typeset-a-color'), '#7a5b0a')
        self.assertEqual(resolve(dark, '--md-typeset-a-color'), '#d9b141')

    def test_text_and_link_contrast(self):
        for scheme in ('default', 'slate'):
            values = tokens(scheme)
            for foreground in ('text', 'muted', 'link', 'link-hover'):
                for background in ('background', 'surface', 'surface-subtle', 'accent-soft'):
                    with self.subTest(scheme=scheme, foreground=foreground, background=background):
                        ratio = contrast(resolve(values, '--manabi-' + foreground), resolve(values, '--manabi-' + background))
                        self.assertGreaterEqual(ratio, 4.5)

    def test_button_and_selection_contrast(self):
        for scheme in ('default', 'slate'):
            values = tokens(scheme)
            for background in ('brand-gold', 'brand-gold-hover', 'selection'):
                with self.subTest(scheme=scheme, background=background):
                    self.assertGreaterEqual(contrast(resolve(values, '--manabi-on-accent'), resolve(values, '--manabi-' + background)), 4.5)

    def test_controls_and_focus_contrast(self):
        for scheme in ('default', 'slate'):
            values = tokens(scheme)
            for foreground in ('border-strong', 'link'):
                for background in ('background', 'surface', 'surface-subtle'):
                    with self.subTest(scheme=scheme, foreground=foreground, background=background):
                        self.assertGreaterEqual(contrast(resolve(values, '--manabi-' + foreground), resolve(values, '--manabi-' + background)), 3)

    def test_chrome_contrast(self):
        values = tokens('default')
        for foreground in ('on-chrome', 'on-chrome-muted', 'brand-gold', 'brand-gold-hover'):
            for background in ('brand-charcoal', 'brand-deep'):
                self.assertGreaterEqual(contrast(resolve(values, '--manabi-' + foreground), resolve(values, '--manabi-' + background)), 4.5)

    def test_colors_are_not_duplicated_in_component_styles(self):
        for relative in ('docs/stylesheets/extra.css', 'overrides/styles.css'):
            source = (ROOT / relative).read_text(encoding='utf-8')
            self.assertNotRegex(source, r'#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(')
            for name in re.findall(r'var\((--manabi-[\w-]+)\)', source):
                self.assertIn(name, tokens('default'))

    def test_global_loading_and_system_fonts(self):
        config = (ROOT / 'mkdocs.yml').read_text(encoding='utf-8')
        self.assertIn('extra_css:\n  - stylesheets/brand.css\n  - stylesheets/extra.css', config)
        self.assertEqual(config.count('primary: custom'), 2)
        self.assertEqual(config.count('accent: custom'), 2)
        self.assertIn('font: false', config)
        self.assertIn('system-ui', resolve(tokens('default'), '--md-text-font-family'))
        self.assertIn('ui-monospace', resolve(tokens('slate'), '--md-code-font-family'))
        self.assertNotIn('@import', CSS)
        self.assertNotIn('@font-face', CSS)

    def test_user_accessibility_preferences_remain_available(self):
        self.assertIn('@media (forced-colors: active)', CSS)
        self.assertNotIn('forced-color-adjust: none', CSS)
        extra = (ROOT / 'docs/stylesheets/extra.css').read_text(encoding='utf-8')
        self.assertIn('@media (prefers-reduced-motion: reduce)', extra)
        self.assertNotIn('filter:', (ROOT / 'overrides/styles.css').read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
