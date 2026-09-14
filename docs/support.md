---
title: Tech support
description: Manabitan support, compatibility status, and safe troubleshooting for permissions and dictionary storage.
---

# Tech support

For Manabitan-specific questions and reproducible bug reports, use the [Manabi Discord](https://discord.gg/gvxzS93C3w). The public repositories currently have Issues disabled; this guide does not send you to a nonworking issue form. Do not file fork-specific bugs against Yomitan. Documentation fixes can be submitted as pull requests to [manabitan-wiki](https://github.com/ManabiIO/manabitan-wiki/pulls).

## Reporting a problem

Include the Manabitan version and installation method, browser/version, operating system and device, dictionary title/revision/format/size, steps to reproduce, expected result, and the actual error. State whether the problem is an initial import, update, lookup, or backup restore.

Recent builds expose diagnostics in Settings. Inspect a diagnostic export before sharing it: error messages, URLs, dictionary names, settings, and copied text may contain information you do not want to publish. Share a minimal example and redact private material, API keys, local paths, and personal page content. Never upload proprietary dictionary contents as a public reproducer.

## Browser and device support

This is a distribution/qualification matrix, not a list inferred from browser branding. The [release notes](https://github.com/ManabiIO/manabitan/releases) for the exact package take precedence.

| Platform | Distribution path | What still needs checking |
| --- | --- | --- |
| Desktop Chrome/Chromium | Manabitan Chrome package, loaded unpacked unless a Manabitan store listing is provided | Minimum browser version, imports, lookups, persistence, and updates on the installed build |
| Desktop Edge | Manabitan Edge package | The same checks; not an upstream Yomitan store install |
| Desktop Firefox | Signed package when explicitly provided; otherwise temporary development testing | Signing, host permission, storage behavior, restart persistence, and the specific update channel |
| Android Firefox | Package-specific testing | Availability of a persistent install, touch scanning, storage, audio, and AnkiDroid integration |
| Android Edge/other extension-capable browsers, including Elixir | Unverified until a release documents a tested combination | Do not infer support from desktop compatibility; e-readers need their own tests |
| iOS/Safari | No supported installation documented here | Source/build variants alone do not establish an available supported release |

## Frequently asked questions

### Nothing happens when I scan

Check that Manabitan is enabled, at least one definition dictionary is enabled in the active profile, and the scanning language/input matches your setup. Grant access to the website and reload the page. In Firefox, inspect the recommended host permissions on the welcome page. Test ordinary selectable webpage text before diagnosing a protected page or PDF viewer.

Disable another dictionary extension's scanning while testing. Browser settings pages, add-on store pages, image-only text, or pages without permission can be unavailable.

### A dictionary import or update fails

Record the exact error and check available disk space. Dictionary storage in Manabitan uses a different implementation from upstream Yomitan, including SQLite and origin-private file storage where supported. The old IndexedDB-only explanation and generic cookie/history fixes are not a reliable diagnosis for every Manabitan error.

Try one small known-compatible dictionary in a separate browser profile. Check whether the package downloaded completely and whether it is a dictionary package rather than a settings or database backup. Keep the original packages, settings export, and working installation.

Do not begin with Refresh Firefox, purging the database, or reinstalling the extension. Those can destroy the only copy of a working setup. Back up first; use destructive recovery only after identifying what will be lost.

### An automatic update did not run at the scheduled time

A dictionary needs a working update source, and the extension needs network access and an opportunity to run. Browser/device suspension can delay scheduled checks. Inspect the dictionary's update configuration and result. Do not delete the existing dictionary merely to retry an update.

### Can I scan local files and PDFs?

Enable file-URL access for local HTML in Chrome/Edge. Open PDFs in the [Manabitan PDF Viewer](manabitan-pdf-viewer/index.html). The PDF needs a selectable text layer; image-only scans need OCR elsewhere first.

### Is deleting a dictionary always slow?

No blanket timing applies to every storage backend, dictionary, and device. Let the operation finish and report prolonged stalls with the dictionary size and diagnostics. The inherited claim that deletion necessarily blocks the browser for about as long as import is not a verified description of the current implementation.

### Does Manabitan use online dictionaries for lookups?

Normal dictionary lookups use installed data. Downloading dictionary updates, fetching pronunciation audio, and the optional external API are different features. See [Privacy and permissions](privacy.md). This describes current behavior rather than promising that an online lookup feature can never be added.
