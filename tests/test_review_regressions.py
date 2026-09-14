"""Offline guards for the documentation and theme regressions found in PR review."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReviewRegressionTests(unittest.TestCase):
    def test_advanced_explains_mapping_not_installation(self):
        text = (ROOT / 'docs/advanced.md').read_text(encoding='utf-8')
        self.assertNotIn('Builds that offer note-type installation', text)
        self.assertIn('Manabitan maps fields for existing models; it does not install note types.', text)

    def test_resources_explains_mapping_not_installation(self):
        text = (ROOT / 'docs/tools-resources.md').read_text(encoding='utf-8')
        self.assertNotIn("Manabitan's built-in note-type installation", text)
        self.assertIn('Install or import the note type in Anki first', text)

    def test_dark_sample_hide_rule_outranks_shared_image_rule(self):
        css = (ROOT / 'overrides/styles.css').read_text(encoding='utf-8')
        # Three classes must outrank the shared two-class + img display:block rule.
        # Browser verification additionally exercises default -> slate -> default.
        self.assertRegex(css, re.escape('.manabitan-home .home-media .theme-sample--dark')
                         + r'\s*\{\s*display:\s*none;\s*\}')
        self.assertIn('[data-md-color-scheme="slate"] .manabitan-home .home-media .theme-sample--dark { display: block; }', css)
        self.assertIn('[data-md-color-scheme="slate"] .manabitan-home .home-media .theme-sample--light { display: none; }', css)


if __name__ == '__main__':
    unittest.main()
