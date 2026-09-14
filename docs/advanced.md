---
title: Advanced features
description: Scanning, appearance, audio, and optional integrations in Manabitan.
---

# Advanced features

Enable the **Advanced** toggle in Settings to reveal additional controls. Use the control's label rather than assuming a fixed screen position; the layout changes with viewport size and build.

## Keyboard shortcuts

The default global shortcuts are **Alt+Insert** for the search page and **Alt+Delete** to toggle scanning. A browser or operating system can reserve or override them; inspect the browser's extension shortcut settings when one does not work.

Search-result shortcuts are configurable in Manabitan's **Shortcuts** section. The inherited defaults include Esc to cancel, Alt+Up/Down to move between results, Alt+PageUp/PageDown to move by pages, Alt+Home/End for first/last, Alt+B to return to the source, Alt+P for audio, and Alt+E/R/K for Anki expression/reading/kanji actions. Check the bindings in your installed build, especially on keyboards without those keys.

## Scanning

The default input is Shift plus pointer movement. Configure a different modifier, no-key scanning, delays, or advanced inputs in Settings. No-key scanning and wildcard scanning can increase background work; change one setting at a time when diagnosing latency.

Manabitan's scan bounds are derived from dictionary information rather than requiring you to choose a fixed character limit for ordinary use. This does not make every browser surface scannable. Browser internal pages, protected viewers, images without text, and pages without permission can still prevent lookup.

For local HTML, enable the browser's file-URL permission. For local PDFs, open the [Manabitan PDF Viewer](manabitan-pdf-viewer/index.html). It needs selectable PDF text; it does not add OCR to scanned pages.

Private-window access is a separate browser permission. Private browsing can impose storage restrictions, so verify dictionary availability before relying on it and do not use a temporary/private installation as your backup.

## Appearance and recall

Choose a built-in popup theme in **Appearance** before adding custom CSS. Keep a copy of custom CSS and test it after a theme or dictionary-name change. Third-party themes retain their own project names and may depend on particular dictionary titles or fonts; see [Tools and resources](tools-resources.md#themes).

**Popup Behavior → Blur popup by frequency** can hide the first term entry until you choose to reveal it. Select the frequency dictionary and threshold in its controls. Rank-based and occurrence-based dictionaries use opposite numerical directions, so check the mode rather than assuming a smaller number always means a rarer word. This is a recall aid on popup results, not a measurement of whether you know a word.

## Audio

### Default audio sources

Available sources depend on the selected language. The inherited Japanese sources include JapanesePod101 and Jisho; other language configurations can use Lingua Libre, Wiktionary, and LanguagePod101. A configured source is not a guarantee that a recording exists for every entry.

Open **Audio → Configure audio playback sources…** to reorder or add sources. Right-click the popup's speaker control to choose a source when supported. If a recording is absent or a source fails, try another source and inspect the error before assuming the dictionary is broken.

### Text-to-speech

Browser text-to-speech can fill gaps in recorded audio. Voices and availability vary by browser, operating system, and installed voices. Japanese readings and pitch can be ambiguous, so do not treat synthesized audio as a reference recording.

Browser SpeechSynthesis audio cannot be exported to Anki through the normal audio-download path. The [upstream discussion](https://github.com/yomidevs/yomitan/issues/864) documents that limitation. A browser TTS voice and a downloadable custom audio URL are different source types.

### Custom audio sources

Custom URLs can use `{term}`, `{reading}`, and `{language}` replacement patterns. Only send lookup data to services you trust. See [Privacy and permissions](privacy.md).

[Local Audio Server for Yomichan](https://github.com/yomidevs/local-audio-yomichan) is an upstream tool that can provide local audio. Follow its actual installation instructions and check compatibility with your Manabitan build. The old Yomichan Forvo Server add-on is not a maintained recommendation here: third-party scraping/services can stop working, and the previous wiki contradicted itself about its status.

## Anki customization

Use **Anki → Configure Anki card format…** to choose formats, fields, and note types. Builds that offer note-type installation can set up supported community note types; review what will be installed before changing an existing setup. Test a single note after changing a format.

Additional formats can be used for sentence-only or audio-focused notes. Custom Handlebars templates are a separate advanced feature: export your settings first, keep your previous template, and preview the result. See [Anki integration](anki.md).

## MeCab and the external API

MeCab is an optional native integration, not part of the default installation. Its helper must authorize the actual Manabitan extension origin/ID. The previous link to a ManabiIO MeCab installer did not resolve; there is no verified Manabitan-specific installation guide to substitute yet. Do not reuse another extension's registration or rename its native-messaging protocol blindly. Use the built-in parser unless you have a tested helper configuration.

The optional external API can allow local tools to request lookup data. Enable it only for a tool you intend to use, and verify that tool's extension discovery and API compatibility. Keep any sanitization bypass disabled unless you understand the complete downstream handling of the returned content.
