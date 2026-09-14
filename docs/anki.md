---
title: Anki integration
description: Connect Manabitan to Anki, automatically map popular note types, understand tested versions, and check note creation.
---

# Anki integration

Manabitan sends notes to [Anki](https://apps.ankiweb.net/) through [AnkiConnect](https://ankiweb.net/shared/info/2055492159). Install AnkiConnect in desktop Anki and restart Anki when required. Keep Anki running while using the integration.

## Flashcard configuration

Enable **Anki integration** in Manabitan Settings. Open **Configure Anki card format…**, choose the format, deck, and note type, and inspect its field mapping. Labels can differ in older releases; do not look for the obsolete separate “Anki Options” page shown in old screenshots.

For a minimal term card, put `{expression}` in the headword field, `{reading}` in a reading field, and `{glossary}` in the definition field. Add `{sentence}` and `{audio}` where appropriate. Use `{character}` as the identifier for a kanji card. A first field containing only a reading can make distinct words with the same reading appear to be duplicates.

## Automatic field mapping

Manabitan reduces one of the more tedious parts of Anki setup: wiring note-type fields to dictionary information and sentence context.

The note type must already exist in Anki. Manabitan does **not** install Kiku, Lapis, Senren, or Crop Theft Vocab. When you select an existing model, Manabitan asks AnkiConnect for its field names and builds the mapping for the selected card format. This configures future note creation; it does not populate or migrate existing Anki notes.

### Recognized note types

The following upstream packages were downloaded and their complete field schemas inspected on **September 14, 2026**. They were the latest published stable packages at that check; Crop Theft distributes its package directly from its repository rather than through numbered releases.

| Note type | Reviewed package | Fields | Important mapping detail |
| --- | --- | --- | --- |
| **Kiku** | [v2.1.0](https://github.com/youyoumu/kiku/releases/tag/v2.1.0) | 24 | `ExpressionFurigana` uses `{furigana-plain}`; `SentenceFurigana` uses `{sentence-furigana-plain}`. |
| **Lapis** | [1.7.0](https://github.com/donkuri/lapis/releases/tag/1.7.0) | 22 | `ExpressionFurigana` uses `{furigana-plain}`, but `SentenceFurigana` is deliberately blank. |
| **Senren** / **Senren 洗練** | [v5.1.0](https://github.com/BrenoAqua/Senren/releases/tag/v5.1.0) | 22 | Sentence fields retain Senren's grouping/highlight markup; `hint` is explicitly blank. |
| **Crop Theft Vocab** | [Package at revision 88865e6](https://github.com/Kuuuube/crop-theft/blob/88865e6209251b1baaaca7219be0dd6073e74cb8/crop_theft_vocab/Crop%20Theft%20Vocab.apkg) | 9 | `Definition` uses `{glossary-brief}`, `Example Target` uses `{search-query}`, and `Frequency` uses `{frequency-harmonic-rank}`. |

Presets map the expression/reading, available word audio, definitions, sentence context, pitch, frequency, and source fields appropriate to each note type. Optional media, translations, hints, and card-mode switches are intentionally left blank where no automatic source is specified. Automatic mapping is not automatic creation of missing recordings, images, translations, or pitch data.

For Kiku, Lapis, and Senren, the main-definition field uses the **first available dictionary-specific `single-glossary-*` marker** supplied by the enabled dictionary configuration. It is not a guarantee that this is your preferred dictionary. Review that choice. If no eligible marker is available, including when dictionary information cannot be loaded during setup, that field stays blank; select a marker from the dropdown afterwards. The separate glossary field still has its own mapping.

### Differences that matter

**Kiku and Lapis are not interchangeable.** [Kiku's current instructions](https://kiku.youyoumu.my.id/installation.html) use plain sentence furigana; Kiku 2.1 can transfer the target-word emphasis from the sentence field. [Lapis's instructions](https://github.com/donkuri/lapis#how-to-use-lapis) still recommend leaving its sentence-furigana field empty. Both use a sentence with the target surrounded by `<b>` tags. Kiku's `RelatedExpression` and `SentenceTranslation` fields remain blank for manual or external population.

AnkiConnect exposes the model name and fields here, not a reliable community-template release version. A model called `Kiku` is therefore not proof that it is Kiku 2.1. Use the reviewed version for the current defaults; with an older Kiku template, upgrade it or keep `SentenceFurigana` blank until you have checked its rendering. Existing saved Manabitan mappings are not silently rewritten by this preset change. To adopt the correction on an existing Kiku format, set `SentenceFurigana` to `{sentence-furigana-plain}` explicitly and inspect a test note.

**Senren keeps its scene-grouping structure.** Its sentence contains an outer `group` span and a `highlight` span around the target, while sentence furigana is wrapped in a `group` span. The actual v5.1.0 package also contains `hint`, even though the upstream field-setup table omits that row; Manabitan leaves it blank rather than inventing a source. For a multi-dictionary glossary, enable **Group term-reading pairs** or **Group related terms** as described in the [Senren setup guide](https://brenoaqua.github.io/Senren/yomitan/). Review `miscInfo` when using other mining tools that supply their own source information.

**Crop Theft Vocab uses its own nine-field layout.** Its [publisher's field table](https://github.com/Kuuuube/crop-theft#field-setup) is the basis for the mapping. `Notes` remains blank.

### Customization and other note types

Model-name recognition tolerates case, spacing, and punctuation differences, including `Senren・洗練`. It does not treat every name containing “Kiku” or “Lapis” as that preset. Preset field names are exact and case-sensitive. A renamed model or customized field layout may need manual configuration.

Selecting a recognized preset applies its defaults, including intentionally blank fields and blank unknown extra fields. Back up customized settings before changing note types. Newly generated mappings use the `coalesce` overwrite mode; inspect overwrite controls along with the field values.

Unrecognized models retain best-effort mapping from common field names and aliases: for example `Word`, `Term`, or `Phrase`; `Definition` or `Meaning`; `Sound` or `Audio`; and familiar sentence, pitch, frequency, dictionary, URL, title, and selection-text names. Existing values for the same-named fields can be reused, but overwrite modes are still initialized to `coalesce`. Otherwise the first field defaults to `{expression}` for a term card or `{character}` for a kanji card. Community presets apply to term formats, not kanji formats.

### Compatibility checks

The extension repository has three complementary checks: offline tests using field schemas captured from real APKGs, downloads of checksum-pinned reviewed packages, and downloads of the latest stable upstream packages. Crop Theft's latest check resolves the repository's current default branch to a commit before downloading its package.

The checks compare every field—including intentional blanks—with independently reviewed expected mappings, verify that the output uses available markers, and check the identifying first field. Added, removed, renamed, or duplicate fields fail the contract check. Missing downloads, ambiguous packages, and missing models fail rather than being reported as compatible. Fixtures are not automatically rewritten to accept drift.

The workflow runs on relevant pull requests and, once present on the default branch, weekly and by manual dispatch. Reports record package revisions, hashes, and extracted schemas. They do not import anything into your Anki collection, execute downloaded card templates, or retain package media.

These are **field-contract checks**, not complete Anki rendering or browser-integration tests. A template can change behavior without renaming its fields. New releases, custom templates, available dictionary data, audio sources, and device-specific behavior still require a real test note. See the [compatibility maintenance guide](https://github.com/ManabiIO/manabitan/blob/main/docs/development/anki-note-type-compatibility.md), [production mapper](https://github.com/ManabiIO/manabitan/blob/main/ext/js/data/anki-note-type-field-util.js), and [original mapper tests](https://github.com/ManabiIO/manabitan/blob/main/test/anki-note-type-field-util.test.js).

## Field markers

Use the field selector in **your installed build** as the authoritative list of available markers. The [template documentation in the Manabitan repository](https://github.com/ManabiIO/manabitan/blob/main/docs/templates.md) covers helpers and customization. Do not rename a marker because it contains an upstream name or a dictionary title.

| Information | Common markers |
| --- | --- |
| Headword and reading | `{expression}`, `{reading}`, `{furigana}`, `{furigana-plain}` |
| Definitions | `{glossary}`, `{glossary-brief}`, `{glossary-no-dictionary}`, `{glossary-plain}`, `{glossary-first}` |
| Sentence context | `{sentence}`, `{sentence-furigana}`, `{sentence-furigana-plain}`, `{cloze-prefix}`, `{cloze-body}`, `{cloze-body-kana}`, `{cloze-suffix}` |
| Source | `{url}`, `{document-title}`, `{search-query}`, `{popup-selection-text}` |
| Dictionary metadata | `{dictionary}`, `{dictionary-alias}`, `{tags}`, `{part-of-speech}`, `{conjugation}` |
| Audio and images | `{audio}`, `{screenshot}`, `{clipboard-image}`, `{clipboard-text}` |
| Frequency | `{frequencies}`, `{frequency-harmonic-rank}`, `{frequency-harmonic-occurrence}`, `{frequency-average-rank}`, `{frequency-average-occurrence}` |
| Pronunciation | `{phonetic-transcriptions}`, `{pitch-accents}`, `{pitch-accent-graphs}`, `{pitch-accent-graphs-jj}`, `{pitch-accent-positions}`, `{pitch-accent-categories}` |
| Kanji | `{character}`, `{kunyomi}`, `{onyomi}`, `{onyomi-hiragana}`, `{stroke-count}` |

Availability depends on the entry, dictionary, display mode, and permissions. Dictionary-specific markers should be selected from the dropdown rather than assembled by guessing an internal dictionary name. A template marker is not a promise that the requested data exists.

## Flashcard creation

Start with one test entry. Use the expression, reading, or kanji add control corresponding to the format you configured. Open the note in Anki and inspect its fields, audio, and formatting.

Check the duplicate settings deliberately. Depending on the configuration, a matching note can show a browse/book control, disable adding, or allow another note. The deck scope, note type, and identifying field matter; “same reading” is not always “same word.”

If controls are absent, confirm integration is enabled. If they are disabled or fail, check that Anki and AnkiConnect are running, the endpoint is correct, and a valid deck/note type/field mapping is selected. Do not expose AnkiConnect to the public internet to solve a local connection problem.

## Anki note generation

**Generate Anki Notes (Experimental)…** accepts a newline-separated list of terms. Test a short list before a large export. Confirm the deck and card format before using **Send to Anki**.

**Add media to notes** can include available recordings and images and can substantially increase work. Duplicate prevention checks the configured scope; it does not necessarily deduplicate the input list. Back up Anki and do not assume Manabitan provides a batch rollback.

**Export to File** produces the supported text-note export for later Anki import; it is not a packaged Anki collection and does not include media in that mode. Browser TTS is not downloadable audio; see [Audio](advanced.md#audio).

## Android

[AnkiDroid](https://ankidroid.org/) and [AnkiConnectAndroid](https://github.com/KamWithK/AnkiconnectAndroid) are separate third-party projects. The latter requires its own installation and permissions. Treat this as a compatibility path to test with a specific browser/build, not desktop AnkiConnect running unchanged on Android. See [device support](support.md#browser-and-device-support).

## Custom templates

Export your settings before editing Handlebars. Prefer the current default template unless a customization is needed. Old Yomichan helpers can require migration; see [Yomichan migration](yomichan-migration.md#custom-anki-templates).

The previous upstream-derived marker table is retained in the repository's `archive/anki-upstream.md` for attribution and historical comparison. It is not a supported-version contract.
