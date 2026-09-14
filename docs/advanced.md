---
title: Advanced features
description: Scanning, appearance, audio, MeCab, and optional integrations in Manabitan.
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

### Custom audio sources and Forvo

Custom URLs can use `{term}`, `{reading}`, and `{language}` replacement patterns. Only send lookup data to services you trust. See [Privacy and permissions](privacy.md).

[Local Audio Server for Yomichan](https://github.com/yomidevs/local-audio-yomichan) remains the preferred documented route for local Forvo audio. Despite the historical name, it is used as a custom audio source; follow its current setup instructions and point Manabitan at the local URL it provides.

[Yomichan Forvo Server](https://github.com/jamesmaa/yomitan-forvo-server) is another Anki add-on option and is also available from [AnkiWeb](https://ankiweb.net/shared/info/580654285). Its documented custom JSON endpoint is `http://localhost:8770/?term={term}&reading={reading}` with optional language parameters. The current upstream Yomitan wiki flags this option as not working, while the add-on repository still documents installation and fixes. Keep it as a compatibility option, not the default recommendation, and check its current status before diagnosing Manabitan itself.

## Anki customization

Use **Anki → Configure Anki card format…** to choose formats, fields, and note types. Install or import the note type in Anki first. Manabitan maps fields for existing models; it does not install note types. Review the resulting field values before changing an existing setup. Test a single note after changing a format.

Additional formats can be used for sentence-only or audio-focused notes. Custom Handlebars templates are a separate advanced feature: export your settings first, keep your previous template, and preview the result. See [Anki integration](anki.md).

## MeCab

MeCab remains an optional Japanese native integration. [Yomitan MeCab Installer](https://github.com/yomidevs/yomitan-mecab-installer) is the upstream installer and supports adding custom extension IDs, which is the part that matters for Manabitan compatibility.

Install MeCab and the upstream installer as described in its README, but **do not use an upstream Yomitan store ID for Manabitan**. Add the actual Manabitan extension origin/ID when the installer asks for additional IDs:

- Chrome/Chromium/Edge: open Manabitan's Settings page and copy the extension origin before `settings.html` (for Edge, use the `chrome-extension://` form expected by the installer).
- Firefox: open `about:debugging`, find Manabitan, and copy the displayed extension ID, including braces when present.

Then enable **Text Parsing → Parse sentences using MeCab** and use its **Test** control. The installer and MeCab are separate projects, and browser/native-host registration can change across installs, so repeat the ID registration when the extension ID changes. The built-in parser remains available if you do not need MeCab.

## External API

The optional external API can allow local tools to request lookup data. Enable it only for a tool you intend to use, and verify that tool's extension discovery and API compatibility. Keep any sanitization bypass disabled unless you understand the complete downstream handling of the returned content.
