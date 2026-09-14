---
title: Moving from Yomitan
description: Keep backups, distinguish dictionary packages from database backups, and test a separate Manabitan installation.
---

# Moving from Yomitan

Manabitan is a separate extension with a different dictionary storage implementation. It does not upgrade Yomitan in place. Dictionary-format compatibility does not imply that the two applications' whole-database backups are interchangeable.

## Before changing anything

Export Yomitan's settings from **Settings → Backup**. Keep the original dictionary ZIPs or download locations as well. Retain your Yomitan installation and its data until you have checked the Manabitan setup. Back up Anki separately; an extension settings export does not back up your Anki collection.

Check the notes for the Manabitan build you plan to install. These instructions describe the separate-installation path, not an automatic migration of Yomitan's internal database.

## Set up the separate installation

Install [Manabitan](getting-started.md#installation). Disable Yomitan's text scanning while testing so two extensions do not compete for the same modifier key or show duplicate popups. Do not uninstall Yomitan just to disable scanning.

In Manabitan, try importing the exported settings through **Backup → Import Settings**. Read validation and sanitization warnings. Custom audio URLs, remote Anki endpoints, and custom templates can require confirmation or manual reconfiguration. Rejecting an incompatible settings file is not a reason to edit its version field or force an import; configure the new installation manually and report the incompatibility instead.

Import your original Yomitan-format dictionary ZIPs, or install the current recommended dictionaries. Do not feed a Yomitan/Dexie JSON database export into a Manabitan SQLite collection restore. A settings file is also not a dictionary database.

## Check the result

Verify the active profile, enabled dictionaries and their order, language, scanning inputs, and website permissions. Try a term lookup, an inflected word, available audio, and one test Anki note. Check the note's fields and duplicate detection before relying on it for normal mining.

Recheck custom CSS and templates, especially if they depend on dictionary titles. External tools may require the new extension's origin/ID, native-host registration, or API setting. Do not change protocol identifiers just to make them say Manabitan.

Large imports and background updates should also be tested on the device you actually read on. See [backups](dictionaries.md#backups-and-settings) before trying a newer build.

## Rollback

Disable Manabitan scanning and re-enable Yomitan. Because Yomitan was left installed, you can return to its existing setup. Changes made only in Manabitan are not automatically copied back. Keep separate backups and do not assume that a Manabitan database can be restored into Yomitan.

[Why Manabitan is a fork](about-manabitan.md) explains why migrating Yomitan's entire installed base is a separate responsibility.
