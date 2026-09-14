---
title: Dictionaries
description: Install Yomitan-format and MDX dictionaries, configure updates, and keep compatible backups.
---

# Dictionaries

Manabitan uses dictionaries installed in the extension's local storage. Install a definition dictionary before adding frequency, pronunciation, or pitch-accent data. Select the language and active profile before deciding which dictionaries to enable.

## Recommended dictionaries

Start in **Settings → Dictionaries → Get recommended dictionaries…**. Recommendations can be installed together. Availability and licensing belong to each publisher; an entry in this list is not a license to redistribute the dictionary.

For Japanese, [Jitendex](https://github.com/stephenmk/Jitendex) provides a JMdict-based definition dictionary. [JMdict, JMnedict, and KANJIDIC builds](https://github.com/yomidevs/jmdict-yomitan) provide definitions, proper names, and kanji information. Frequency dictionaries such as [BCCWJ and JPDB builds](https://github.com/Kuuuube/yomitan-dictionaries) supplement definitions.

For other languages, see [Wiktionary-to-Yomitan](https://yomidevs.github.io/wiktionary-to-yomitan/download/), [Wikipedia Yomitan](https://github.com/MarvNC/wikipedia-yomitan), [Korean dictionary builds](https://github.com/Lyroxide/yomitan-ko-dic/releases), [CC-CEDICT Yomitan](https://github.com/MarvNC/cc-cedict-yomitan), and [words.hk Yomitan](https://github.com/MarvNC/wordshk-yomitan). These retain their real upstream names and formats; they are not Manabitan-owned projects.

Coverage varies by dictionary and translation language. An English glossary is not necessarily a substitute for a dictionary in the language you need. See [language support](supported-languages.md).

## Importing packages

Open **Configure installed and enabled dictionaries…**, then **Import**. Keep a Yomitan-format dictionary as its ZIP package. Enable the imported dictionary in the active profile and adjust its order. Dictionaries may be installed once but enabled differently across profiles.

Manabitan also supports MDX import. Select the `.mdx` dictionary and include any companion `.mdd` resource files required by that dictionary through the import flow supported by your build. Check a few entries with images, sound, and formatting afterwards. MDX packages vary, and a successful text lookup does not prove every resource or publisher-specific feature works. Keep the source files and use the release notes for version-specific restrictions.

EPWING is a conversion workflow: use [Yomitan Import](https://github.com/yomidevs/yomitan-import) to make a compatible package, then import that package. It is not a claim that Manabitan directly imports arbitrary EPWING files. Obtain proprietary dictionaries legitimately.

## Managing dictionaries

Use the installed-dictionary dialog to enable, disable, reorder, update, delete, or edit the metadata supported by the current build. Changing a dictionary's name can affect custom CSS, Anki markers, and other settings that refer to that name. Test those integrations afterwards.

Deletion and import time depend on the build, storage backend, dictionary size, and device. Do not close the browser in the middle of an operation. A failure should be investigated before repeatedly deleting data or reinstalling the extension.

## Automatic updates

Automatic updates require the dictionary to provide a usable web update source. A file imported from disk does not acquire an update URL just because Manabitan can read it.

In the dictionary's update controls, choose the available update schedule; supported intervals include hourly, daily, weekly, and monthly. The dictionary-management controls also provide bulk update actions. Review the source before enabling automatic downloads, particularly on metered connections or small devices.

Schedules depend on the browser being able to run the extension. Closing the browser, suspending the device, or loss of network access can delay a check. They are not an exact wall-clock delivery guarantee.

The update path prepares new data while installed dictionaries can remain available. A first-time import has no previous version to use. Errors or interruptions still need to be handled: inspect the result and retry after resolving the cause rather than deleting the working dictionary first. Consult [support](support.md) when an update fails repeatedly.

## Backups and settings

There are three different things to keep:

| Data | Purpose | Compatibility |
| --- | --- | --- |
| Original dictionary ZIP or MDX/MDD files | Install an individual dictionary again | Depends on the format and importer |
| Settings JSON | Profiles, preferences, custom configuration | Import validates the settings version and can warn or sanitize values |
| Dictionary collection backup | Restore an application's database | Specific to the storage implementation and supported build |

Use the **Backup** section for settings and collection export/import. In the source reviewed for this documentation, settings export is named `yomitan-settings-…json`, and collection export is named `yomitan-dictionaries-…sqlite3`. The inherited `yomitan-` filename prefix is not evidence that a SQLite backup works in Yomitan. Do not rename `.sqlite3` to `.json` or use the old wiki's `manabitan-dictionaries-…json` example.

Keep the release/build version with a backup. Do not assume a whole-database backup includes every external resource used by a newer storage layout, or that it can be restored across arbitrary builds. Keep the original packages as the recovery path and test restoration in a separate browser profile before relying on a collection backup alone.

A settings export does not contain the dictionary contents or back up Anki. After restoring settings, check custom templates, non-localhost audio/Anki URLs, profile selection, and enabled dictionaries. See [migration](yomitan-migration.md).
