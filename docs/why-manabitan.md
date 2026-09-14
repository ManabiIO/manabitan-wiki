---
title: Why use Manabitan?
description: What Manabitan improves beyond Yomitan: faster storage and lookups, non-blocking updates, dictionary management, and automatic Anki field mapping.
---

# Why use Manabitan?

If Yomitan already works for you, Manabitan should earn the switch. The point is not the new name. It is to keep the same basic lookup-and-Anki workflow while removing waiting, setup work, and some rough edges around dictionaries and mining.

The biggest difference is the rewritten storage and query architecture, but Manabitan is not only a performance fork. It also adds dictionary-management and Anki conveniences that are useful even on a fast computer.

## Less waiting

Dictionary imports and normal lookups are heavily optimized. The difference is most obvious with large dictionary collections, older hardware, and e-ink devices, but reducing storage and query work matters everywhere.

The storage design also lets already-installed dictionaries stay usable while new dictionary data is being prepared. A dictionary being installed for the first time still has to finish before you can use that dictionary, and background work still consumes resources.

Performance depends on the build, browser, dictionaries, and device. We benchmark the work, but this page does not turn one benchmark result into a universal speed ratio or a battery-life claim.

## Dictionary updates you do not have to babysit

For dictionaries that provide a usable web update source, Manabitan can check and update them on a schedule. Current controls support hourly, daily, weekly, and monthly schedules, along with bulk update actions.

That matters because manual updating is easy to neglect, especially when updating interrupts the thing you opened the extension to do. Making imports faster and keeping installed dictionaries available makes routine background updating practical instead of something you need to plan around.

See [Dictionaries](dictionaries.md#automatic-updates).

## Better dictionary management

Manabitan adds quality-of-life improvements around the same dictionary ecosystem:

- install recommended dictionaries together instead of working through them one by one;
- import MDX dictionaries, including companion MDD resources where supported;
- edit supported dictionary metadata after import;
- update supported dictionaries individually or in bulk;
- keep separate profiles with different enabled dictionaries and ordering.

The project still supports Yomitan-format dictionaries. Third-party dictionary projects keep their existing names and licenses; Manabitan compatibility does not make them Manabitan-owned projects.

## Less Anki field setup

This is a Manabitan-specific improvement that is easy to miss.

When an Anki note type already exists in Anki and you select it in Manabitan, Manabitan asks AnkiConnect for that model's field names and builds the field mapping automatically. It has explicit presets for several popular Japanese mining note types:

- **Kiku**
- **Lapis**
- **Senren**, including the `Senren 洗練` name
- **Crop Theft Vocab**

For Kiku and Lapis, Manabitan maps fields such as expression, furigana, reading, audio, selection text, sentence/cloze context, glossary, pitch information, frequency, and document title. For the main definition it chooses an available dictionary-specific `single-glossary-*` marker when one exists.

Senren gets the same kind of purpose-built mapping for its word, reading, sentence, sentence-furigana, selection, definition, audio, pitch, frequency, and source fields. Crop Theft Vocab has its own mapping for word, reading, pitch pattern, audio, brief definition, example sentence/target, and frequency.

Other note types are not ignored. Manabitan has a generic mapper for familiar field names and aliases such as `Word`, `Term`, `Phrase`, `Definition`, `Meaning`, `Sound`, `Audio`, `Example Sentence`, and frequency/pitch fields. When possible it also preserves an existing mapping for a field with the same name.

**Manabitan does not install these note types into Anki.** Install or import the note type in Anki first, then select it in Manabitan. Selecting a recognized preset applies the preset mapping, and fields the preset does not know about can be left blank, so review the result before normal mining.

See [Anki integration](anki.md#automatic-field-mapping) for the exact behavior and [the implementation](https://github.com/ManabiIO/manabitan/blob/main/ext/js/data/anki-note-type-field-util.js) if you want to inspect the presets.

## More reading-oriented quality of life

Manabitan also includes built-in popup themes and frequency-based recall blur. The goal is not to redesign Yomitan into a different product; these are additions around the reading workflow that already works.

The extension remains compatible with the familiar scanning, audio, custom CSS, AnkiConnect, custom templates, and installed-dictionary workflow. MeCab, local audio, Forvo integrations, and other upstream/community tools remain available where their integration requirements are satisfied.

## Why not just make these changes in Yomitan?

That is a different question from whether the changes are useful. The storage rewrite is large enough that developing and safely migrating it upstream is a project in its own right. Manabitan is a fork because that is currently the practical way to build and prove the architecture without forcing Yomitan's existing users through a major migration.

Read [Why Manabitan is a fork](about-manabitan.md) for the longer explanation of the upstream relationship, migration responsibility, and why useful work can still flow back to Yomitan.
