---
title: Moving from Yomichan
description: Preserve a Yomichan setup while moving to a separate Manabitan installation.
---

# Moving from Yomichan

Keep Yomichan installed while you test Manabitan. Export settings from Yomichan's **Backup** section, and keep the original dictionary packages or their download locations. Then follow the separate-installation and verification steps in [Moving from Yomitan](yomitan-migration.md).

Yomichan's [community data exporter](https://github.com/yomidevs/yomichan-data-exporter) can preserve legacy data, but its whole-database JSON output is not a Manabitan SQLite backup. Do not promise or assume direct database interchange. Reimport compatible dictionary packages instead.

## Custom Anki templates

Yomitan's transition away from Yomichan included changes to Handlebars helpers. These are inherited compatibility changes, not fixes newly invented by Manabitan. When carrying old custom templates forward, check these forms:

| Helper | Older block form | Corrected form |
| --- | --- | --- |
| `formatGlossary` | `{{#formatGlossary ../dictionary}}{{{.}}}{{/formatGlossary}}` | `{{formatGlossary ../dictionary .}}` |
| `furigana` | `{{#furigana}}{{{definition}}}{{/furigana}}` | `{{furigana definition}}` |
| `furiganaPlain` | `{{~#furiganaPlain}}{{{.}}}{{/furiganaPlain~}}` | `{{~furiganaPlain .~}}` |
| `dumpObject` | `{{#dumpObject}}{{{.}}}{{/dumpObject}}` | `{{dumpObject .}}` |

Prefer current default templates unless you need a customization. Preview the result and create a test note; a successful settings import does not establish that every custom template still works. See [Anki](anki.md) for setup and the full developer template reference.
