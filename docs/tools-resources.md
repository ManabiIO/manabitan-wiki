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

[JP Mining Note](https://arbyste.github.io/jp-mining-note/), [Senren](https://brenoaqua.github.io/Senren/), and [Basic Mining Deck](https://github.com/friedrich-de/Basic-Mining-Deck) are community note types. Manabitan's built-in note-type installation is described in [Anki integration](anki.md). Do not assume every third-party template supports every language or every Manabitan change.

[Textractor](https://github.com/Artikash/Textractor) is a separate Windows text-extraction tool. A [community visual-novel guide](https://animecards.site/visualnovels/) can help connect its output to a dictionary workflow; enable clipboard access only when you need it.

[Backfill Anki Yomitan](https://ankiweb.net/shared/info/1184164376) and [Generate Batch Audio](https://ankiweb.net/shared/info/1156270186) retain their upstream add-on identities. Check API compatibility and back up Anki before bulk changes. Calling an add-on “Manabitan” does not make it discover or support this fork automatically.

[Local Audio Server for Yomichan](https://github.com/yomidevs/local-audio-yomichan) is an upstream local-audio option. The older Yomichan Forvo Server is not a current recommendation here; follow [audio configuration](advanced.md#audio) and verify the service rather than relying on inherited claims about availability.

## Themes

Try Manabitan's built-in themes in **Appearance** first. For third-party CSS, enable **Advanced**, open **Appearance → Configure Custom CSS…**, and keep a copy of your existing CSS before replacing it. Check the result in both light and dark modes.

[Yomichan Dictionary CSS](https://github.com/yomidevs/yomichan-dict-css) colors dictionary output by name. [Bint's Yomitan CSS](https://github.com/yomidevs/yomitan-featured-css/tree/main/bint's%20yomitan%20css) and [Nelan's Yomitan CSS](https://github.com/yomidevs/yomitan-featured-css/tree/main/nelan's%20yomitan%20css) are community themes. Their original names and authorship are preserved; these are not Manabitan-specific releases.

Some themes depend on dictionary titles, external resources, or fonts you do not have. Use resources you are licensed to use and adapt references to your own setup. Do not redistribute proprietary fonts with a theme or documentation screenshot.
