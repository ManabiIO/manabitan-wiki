---
title: Privacy and permissions
description: Local dictionary data, optional network features, and browser permissions used by Manabitan.
---

# Privacy and permissions

Manabitan stores dictionaries and settings locally in the browser's extension storage. Normal dictionary lookup uses installed data. Local storage is not a backup: removing an extension or browser profile can remove its data.

## Network and optional features

Dictionary installation and update checks contact the configured dictionary publishers or download hosts. Scheduled updates can make those requests without a fresh click when enabled. The destination receives the request and normal network metadata, including an IP address; custom URLs can contain account-specific information.

Audio requests can send the term, reading, and language to configured sources such as JapanesePod101/LanguagePod101, Jisho, Lingua Libre/Wikimedia, Wiktionary/Wikimedia, or a custom service. Autoplay settings can trigger audio without pressing the speaker for each entry. Browser TTS follows the browser and selected voice provider's behavior; do not assume every voice is processed locally.

With Anki enabled, Manabitan communicates with the configured AnkiConnect endpoint. Depending on the configured fields and actions, this can include dictionary data, sentence text, the page URL/title, screenshots, clipboard contents, and settings needed to create/check notes. The usual endpoint is local, but a user-configured remote endpoint changes where that information goes. Anki's own synchronization is a separate service.

The optional external API allows other applications to request data when enabled. Optional MeCab/native messaging can send text to a separately installed local helper. Enable these only for integrations you intend to use; an integration's own network behavior is not controlled by this wiki.

## Browser permissions

| Permission | Why it is used |
| --- | --- |
| Website access / `<all_urls>` | Scan permitted webpages, show the popup, and make configured dictionary/audio/integration requests. Browser approval rules differ. |
| `storage`, `unlimitedStorage` | Store settings and dictionary data and reduce browser storage eviction risk; physical disk space still matters. |
| `alarms` | Schedule background work, including dictionary update checks. Browser suspension can delay it. |
| `declarativeNetRequest` | Apply request/header rules needed by supported network operations. |
| `scripting` | Inject extension scripts and styles on permitted pages. |
| `contextMenus` | Offer lookup actions for selected text. |
| `offscreen` (Chromium variants, including Edge) | Let the background service worker use a document for operations requiring DOM APIs. |
| `clipboardWrite` | Copy supported lookup/output content to the clipboard. |
| `clipboardRead` (optional) | Read clipboard content for enabled clipboard-search or note-field features. |
| `nativeMessaging` (optional, platform-dependent) | Communicate with an explicitly installed native helper such as MeCab. |

File-URL and private-window access are separate browser controls. The exact permissions are defined by the distributed package; the [manifest variants](https://github.com/ManabiIO/manabitan/blob/main/dev/data/manifest-variants.json) document the source configuration.

## Diagnostics and backups

Review settings/diagnostic exports before sharing. URLs, dictionary names, error text, custom templates, and local paths can reveal private information. Do not post credentials, private page content, or licensed dictionary data. Keep backups somewhere you control and check the [format limitations](dictionaries.md#backups-and-settings).

## This website

The documentation site is separate from the extension. Its server and any configured delivery proxy receive normal web requests. This homepage does not automatically embed YouTube demonstrations or load Google Fonts; it uses local assets and system fonts. Following an external project, community, store, or audio link subjects that visit to the destination's own practices.

The [extension privacy policy](https://github.com/ManabiIO/manabitan/blob/main/PRIVACY-POLICY.md) describes the corresponding app behavior. Neither page is a promise that third-party services receive no identifying network metadata.
