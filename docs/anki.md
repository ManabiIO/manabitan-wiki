---
title: Anki integration
description: Connect Manabitan to Anki, configure note types and fields, and test note creation.
---

# Anki integration

Manabitan sends notes to [Anki](https://apps.ankiweb.net/) through [AnkiConnect](https://ankiweb.net/shared/info/2055492159). Install AnkiConnect in desktop Anki and restart Anki when required. Keep Anki running while using the integration.

## Flashcard configuration

Enable **Anki integration** in Manabitan Settings. Open **Configure Anki card format…**, choose the format, deck, and note type, and map its fields to the information you want. Labels can differ in older releases; do not look for the obsolete separate “Anki Options” page shown in old screenshots.

Manabitan builds with the note-type installer offer setup for supported community note types, including Kiku, Lapis, and Senren. This installs/configures a note type; it does not make all community templates equivalent. Read the selected type's requirements, protect any existing customization with an Anki backup, and check the mappings afterwards.

For a minimal term card, put `{expression}` in the headword field, `{reading}` in a reading field, and `{glossary}` in the definition field. Add `{sentence}` and `{audio}` where appropriate. Use `{character}` as the identifier for a kanji card. A first field containing only a reading can make distinct words with the same reading appear to be duplicates.

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

Availability depends on the entry, dictionary, display mode, and permissions. Dictionary-specific markers such as `single-glossary` and `single-frequency` should be selected from the dropdown rather than assembled by guessing an internal dictionary name. A template marker is not a promise that the requested data exists.

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
