---
title: Tools and resources
description: Upstream and third-party tools that can complement Manabitan, with their original names and compatibility boundaries.
---

# Tools and resources

These are independent projects, not Manabitan products. Their names, licenses, support channels, and compatibility requirements remain their own. Check a tool against your installed Manabitan build before depending on it.

## Reading and subtitles

[asbplayer](https://github.com/killergerbah/asbplayer) can provide text-selectable subtitles on supported video sources. [Ttsu Reader](https://reader.ttsu.app/) and [Koodo Reader](https://web.koodoreader.com/) provide browser-based reading. The [AnimeCards MPV guide](https://animecards.site/minefromanime/) describes a separate media-player workflow. Availability on a particular mobile browser must be checked rather than assumed.

For PDFs, use the [Manabitan PDF Viewer](manabitan-pdf-viewer/index.html). It is based on Mozilla PDF.js. It does not turn an image-only PDF into selectable text.

## Anki and external applications

[JP Mining Note](https://arbyste.github.io/jp-mining-note/), [Senren](https://brenoaqua.github.io/Senren/), and [Basic Mining Deck](https://github.com/friedrich-de/Basic-Mining-Deck) are community note types. Install or import the note type in Anki first, then select it in Manabitan. Automatic field mapping for recognized models is described in [Anki integration](anki.md). Do not assume every third-party template supports every language or every Manabitan change.

[Textractor](https://github.com/Artikash/Textractor) is a separate Windows text-extraction tool. A [community visual-novel guide](https://animecards.site/visualnovels/) can help connect its output to a dictionary workflow; enable clipboard access only when you need it.

[Backfill Anki Yomitan](https://ankiweb.net/shared/info/1184164376) and [Generate Batch Audio](https://ankiweb.net/shared/info/1156270186) retain their upstream add-on identities. Check API compatibility and back up Anki before bulk changes. Calling an add-on “Manabitan” does not make it discover or support this fork automatically.

### Forvo and local audio

[Local Audio Server for Yomichan](https://github.com/yomidevs/local-audio-yomichan) is the preferred documented local Forvo path. Configure it as a custom Manabitan audio source using the URL/type described by that project.

[Yomichan Forvo Server](https://github.com/jamesmaa/yomitan-forvo-server) / [AnkiWeb 580654285](https://ankiweb.net/shared/info/580654285) is a second option that serves JSON from Anki, normally on port 8770. The upstream Yomitan wiki currently marks it as not working, so treat it as an optional compatibility route and verify the add-on's current status first rather than removing the documentation entirely.

### MeCab

[Yomitan MeCab Installer](https://github.com/yomidevs/yomitan-mecab-installer) can register custom extension IDs. For Manabitan, follow the installer but add Manabitan's actual extension origin/ID instead of assuming the Yomitan store ID. See [MeCab setup](advanced.md#mecab) for the Manabitan-specific step.

## Themes

Try Manabitan's built-in themes in **Appearance** first. For third-party CSS, enable **Advanced**, open **Appearance → Configure Custom CSS…**, and keep a copy of your existing CSS before replacing it. Check the result in both light and dark modes.

[Yomichan Dictionary CSS](https://github.com/yomidevs/yomichan-dict-css) colors dictionary output by name. [Bint's Yomitan CSS](https://github.com/yomidevs/yomitan-featured-css/tree/main/bint's%20yomitan%20css) and [Nelan's Yomitan CSS](https://github.com/yomidevs/yomitan-featured-css/tree/main/nelan's%20yomitan%20css) are community themes. Their original names and authorship are preserved; these are not Manabitan-specific releases.

Some themes depend on dictionary titles, external resources, or fonts you do not have. Use resources you are licensed to use and adapt references to your own setup. Do not redistribute proprietary fonts with a theme or documentation screenshot.
