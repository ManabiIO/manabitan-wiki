# Manabi branding

The wiki uses the palette from the Reader landing page at `https://reader.manabi.io/`.
The source is `lake-of-fire/manabi`, revision
`0699eabb6f8f6bf06122507457f23cc21c14759a`,
`manabi/static/reader/css/new-age.css` (blob
`661433220b3455770111415759effc908b1e135d`).
The corresponding `manabi/templates/reader/index.html` links to that stylesheet.

Reader's shared colors are gold `#D9B141`, hover gold `#FCBD20`, charcoal
`#1C1C1C`, surface `#222222`, raised gray `#323232`, and deep charcoal `#0A0A0A`.
The inline blue/orange word-learning examples on Reader's homepage are reading
states, not the site's primary branding palette.

## One palette, two themes

`docs/stylesheets/brand.css` is the single source of color variables for the
Manabitan site's authored CSS. It loads globally through `mkdocs.yml`, before
layout overrides, so the homepage and documentation use the same palette.

- `--manabi-brand-*` holds Reader's shared gold and charcoal colors.
- `--manabi-background`, `--manabi-surface`, `--manabi-surface-subtle`,
  `--manabi-text`, `--manabi-muted`, `--manabi-border`, and
  `--manabi-border-strong` describe their use in each theme.
- `--manabi-link`, `--manabi-link-hover`, `--manabi-accent-soft`, and
  `--manabi-selection` describe interactive and highlighted states.
- `--manabi-on-accent` and `--manabi-on-chrome` prevent white-on-gold buttons or
  light-theme text from becoming unreadable against the dark navigation.

The dark theme uses Reader's charcoal surfaces and exact gold links. The light
theme is an adaptation: warm off-white content, dark text, and a darker gold
link (`#7A5B0A`, hover `#5F4506`) to maintain contrast. Filled buttons retain the
original gold in both themes with dark labels. Header, navigation tabs, and
footer retain dark surfaces in both modes.

Material's `--md-*` variables map onto the semantic tokens. Define those aliases
on the element carrying `data-md-color-scheme`, not just `:root`: otherwise an
inherited alias can retain a light-mode computed value after a theme switch.
Both palettes declare `primary: custom` and `accent: custom` so the default
indigo/purple accents do not compete with the brand colors.

`extra.css` and `overrides/styles.css` contain layout/component styles, not a
second hardcoded palette. System UI fonts remain in use throughout the site,
with system monospace fonts for code and no remote font import. Existing media,
theme examples, videos, and their captions remain unchanged; the CSS does not
recolor screenshots or embedded third-party content. Semantic warning/success
colors and syntax highlighting retain their meaning instead of becoming gold.
The bundled PDF.js application's controls and user-opened PDFs are not recolored
by the documentation theme.

## Validation

Run `python -m unittest discover -s tests -p 'test_branding.py' -v` for the
network-independent palette checks. They cover the source colors, alias
resolution in both schemes, global loading, absence of duplicate component
colors, system fonts, and text/control contrast. These tests run with the
existing wiki unit-test discovery; no dependency or deployment workflow is added.

The tested text/link/label pairings must reach a contrast ratio of at least
4.5:1; controls and focus colors are checked at 3:1 against their surfaces.
Decorative media/card borders are not treated as text or control boundaries.

Before visual approval, build the site and inspect the homepage and a nested
document at desktop and mobile widths in both themes. Check primary and
secondary buttons (including hover/focus), search input/results, selection,
mobile navigation, captions, and footer. Also inspect forced-colors and
reduced-motion settings. Token tests are not a substitute for a full rendered
MkDocs or production-route check.
