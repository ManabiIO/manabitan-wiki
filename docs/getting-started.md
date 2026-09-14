---
title: Getting started with Manabitan
description: Choose a browser package, install dictionaries, and make your first lookup.
---

# Getting started with Manabitan

Manabitan is installed separately from Yomitan. Existing users should first read [Moving from Yomitan](yomitan-migration.md) or [Moving from Yomichan](yomichan-migration.md).

## Installation

Get packages from [Manabitan's GitHub Releases](https://github.com/ManabiIO/manabitan/releases). Read the notes for the release you select. A package called `manabitan-chrome.zip` is a browser variant, not evidence that the release is stable. Releases marked **Pre-release** are development releases. Do not use the Playwright package for everyday reading.

### Chrome and Chromium-based desktop browsers

Download `manabitan-chrome.zip`, extract it to a permanent folder, and open `chrome://extensions`. Enable **Developer mode**, choose **Load unpacked**, and select the extracted folder containing `manifest.json`.

Do not delete or move that folder afterwards. To update an unpacked installation, back up your data, replace its files with the intended new release, then use **Reload** on the extension's card. Keep the same installation/folder rather than removing and reinstalling it. Unpacked installation is not Chrome Web Store installation and does not provide store-managed updates.

### Microsoft Edge on desktop

Use `manabitan-edge.zip` and the same procedure at `edge://extensions`. Choose the extracted folder containing `manifest.json`. The same backup and manual-update precautions apply.

### Firefox on desktop

Normal Firefox installation requires a Mozilla-signed package. Install a signed Manabitan package only when the release explicitly provides one, using **Add-ons and themes → Extensions → Install Add-on From File**. A GitHub ZIP is not automatically a signed installable add-on.

For development testing, extract `manabitan-firefox.zip`, open `about:debugging#/runtime/this-firefox`, select **Load Temporary Add-on**, and select `manifest.json`. Temporary add-ons are removed when Firefox restarts; this is not a persistent installation or an automatic-update channel. Do not use temporary storage as your only copy of a dictionary collection.

The source has a separate Firefox development variant with an update URL. Automatic updates depend on the exact signed package, its manifest, and a working update feed. They are not promised for arbitrary ZIPs, temporary add-ons, or every Firefox package. Do not disable signature checks as an installation shortcut.

### Mobile and e-readers

See [Browser and device support](support.md#browser-and-device-support). Android Firefox and extension-capable Android Chromium browsers need package-specific testing. Desktop availability does not establish mobile support. There is no supported iOS/Safari installation documented here; use only a platform package explicitly described in a release.

## Manabitan setup

Open the extension's toolbar icon, then **Settings**. The welcome page offers the same initial setup. Grant the website permissions your browser requests; in Firefox, check **Enable recommended permissions** on the welcome page when available. Reload an already-open webpage after installation or permission changes.

### Installing dictionaries

Choose your language, then open **Get recommended dictionaries…**. Start with a definition dictionary for that language. The recommended-dictionary dialog can install recommendations together; do not install every available dictionary just because it is listed.

To import a downloaded dictionary, open **Dictionaries → Configure installed and enabled dictionaries…**, then use **Import**. Wait for the new dictionary to finish, enable it in the profile you are using, and try a lookup. A frequency or pitch-accent dictionary adds information but does not replace a definition dictionary.

See [Dictionaries](dictionaries.md) for MDX packages, automatic updates, profiles, and backups.

## Basic usage

On a normal webpage with selectable text, hold **Shift** and move the pointer over a word. If a matching entry exists in an enabled dictionary, a definition popup appears. Scanning input can be changed in Settings. Browser settings pages, store pages, protected viewers, and image-only text may not allow scanning.

Use the speaker button for available pronunciation audio. Availability depends on the language and configured audio sources; not every entry has a recording. [Configure audio](advanced.md#audio).

[Set up Anki](anki.md) before using the add-card controls. Anki normally needs to be running with AnkiConnect installed. Do a test lookup and create one test note before importing or updating a large collection.

### Local files and PDFs

In Chrome or Edge, enable **Allow access to file URLs** on Manabitan's extension details page to scan local HTML. For PDFs, use the [Manabitan PDF Viewer](manabitan-pdf-viewer/index.html), then open or drop a file into it. Scanned image-only PDFs need a text layer before dictionary lookup can work.

## Need help?

Use [Tech support](support.md) for permission, storage, and import troubleshooting. For Manabitan-specific questions and reproducible reports, use the [Manabi Discord](https://discord.gg/gvxzS93C3w). Do not send fork-specific bugs to Yomitan's issue tracker.

Browser installation references: [Chrome's unpacked-extension instructions](https://developer.chrome.com/docs/extensions/get-started/tutorial/hello-world#load-unpacked) and [Mozilla's temporary-installation guide](https://extensionworkshop.com/documentation/develop/temporary-installation-in-firefox/).
