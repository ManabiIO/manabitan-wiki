---
title: Language support
description: Language selection, deinflection, and dictionary availability are distinct parts of Manabitan support.
---

# Language support

Choose the language in Settings and install appropriate dictionaries. A language appearing in the selector does not guarantee a particular dictionary, complete deinflection, pronunciation audio, or a translated interface.

The table below is generated from `language-descriptors.js` at the extension revision recorded in `scripts/asset-sources.json`. It replaces the stale hand-maintained list. Your installed build can differ; its language selector is authoritative for that build.

--8<-- "_generated/languages.md"

## What support means

Dictionary availability determines which words and definitions can be found. Language transforms determine which inflected or normalized forms lead to those entries. Audio is supplied separately and has its own coverage. These should not be conflated into a single claim of complete language support.

Use separate profiles for different languages when they need different dictionaries, scanning inputs, or settings. Recheck the active profile after importing settings.

For development, see [language features](https://github.com/ManabiIO/manabitan/blob/main/docs/development/language-features.md) and the [language descriptors](https://github.com/ManabiIO/manabitan/blob/main/ext/js/language/language-descriptors.js). New languages and improvements can often benefit the upstream ecosystem too.
