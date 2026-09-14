---
title: Why use Manabitan?
description: Faster imports and lookups, dramatically smaller installed dictionaries, easier Anki setup, and the directions guiding Manabitan's roadmap.
---

# Why use Manabitan?

If Yomitan already works for you, Manabitan should earn the switch. The point is not the new name. It is to keep the same basic lookup-and-Anki workflow while removing waiting, setup work, and some rough edges around dictionaries and mining.

The biggest difference is the rewritten storage and query architecture, but Manabitan is not only a speed-focused fork. It also dramatically reduces the space taken up by imported dictionaries and adds dictionary-management and Anki conveniences that are useful even on a fast computer.

## Less waiting

Dictionary imports and normal lookups are heavily optimized. The difference is most obvious with large dictionary collections, older hardware, and e-ink devices, but reducing storage and query work matters everywhere.

The storage design also lets already-installed dictionaries stay usable while new dictionary data is being prepared. A dictionary being installed for the first time still has to finish before you can use that dictionary, and background work still consumes resources.

Performance depends on the build, browser, dictionaries, and device. We benchmark the work, but this page does not turn one benchmark result into a universal speed ratio or a battery-life claim.

## Dramatically less disk space

Manabitan has dramatically reduced the disk space taken up by imported dictionaries compared with Yomitan. This is a reduction in the **installed dictionary footprint**, not merely the size of a downloaded ZIP. It makes large dictionary collections more practical, particularly on devices with limited storage.

The amount saved depends on the dictionaries and storage implementation in the build you use; there is no single percentage that describes every collection. Imports and updates can also need temporary working space, so a smaller installed footprint does not eliminate the need for free space during an operation. Our [benchmarking direction](#public-comparable-benchmarks) includes making storage comparisons reproducible alongside import and lookup measurements.

## Dictionary updates you do not have to babysit

For dictionaries that provide a usable web update source, Manabitan can check and update them on a schedule. Current controls support hourly, daily, weekly, and monthly schedules, along with bulk update actions.

That matters because manual updating is easy to neglect, especially when updating interrupts the thing you opened the extension to do. Making imports faster and keeping installed dictionaries available makes routine background updating practical instead of something you need to plan around.

See [Dictionaries](dictionaries.md#automatic-updates).

## Better dictionary management

Manabitan adds quality-of-life improvements around the same dictionary ecosystem: install recommended dictionaries together, import MDX dictionaries and supported companion MDD resources, edit supported metadata after import, and update dictionaries individually or in bulk.

The project still supports Yomitan-format dictionaries and familiar per-profile dictionary configuration. Third-party dictionary projects keep their existing names and licenses; Manabitan compatibility does not make them Manabitan-owned projects.

## Less Anki field setup

When an Anki note type already exists in Anki and you select it in Manabitan, Manabitan asks AnkiConnect for that model's field names and builds the field mapping automatically. Purpose-built presets cover **Kiku, Lapis, Senren / Senren 洗練, and Crop Theft Vocab**.

These mappings cover the word, reading, available audio, definitions, sentence context, pitch, frequency, and source fields appropriate to each type. They are not all interchangeable: current Kiku gets plain sentence furigana, Lapis deliberately leaves its sentence-furigana field blank, and Senren keeps its scene-grouping markup. Kiku, Lapis, and Senren can also use an available dictionary-specific `single-glossary-*` marker for their main definition.

The presets are reviewed against the publishers' instructions and actual downloadable note-type packages. Automated checks compare the production mapper with every field in pinned packages and the latest upstream packages, with additional offline regression tests. They flag schema drift rather than silently treating new fields as supported. See the [tested versions and scope](anki.md#compatibility-checks).

Other note types retain best-effort mapping from familiar field names and aliases such as `Word`, `Term`, `Phrase`, `Definition`, `Meaning`, `Sound`, and `Example Sentence`. Existing same-named mapping values can be reused for unrecognized models; this generic fallback is distinct from the purpose-built community presets.

**Manabitan does not install these note types into Anki.** Install or import the note type in Anki first, then select it in Manabitan. Selecting a recognized preset applies its defaults, including intentionally blank fields. Customized or renamed fields need review before normal mining.

See [Anki integration](anki.md#automatic-field-mapping) for setup, version-specific differences, and how to inspect the result.

## More reading-oriented quality of life

Manabitan also includes built-in popup themes and frequency-based recall blur. These are additions around the reading workflow that already works, not an attempt to turn Yomitan into a different product.

Familiar scanning, audio, custom CSS, AnkiConnect, custom templates, and installed-dictionary workflows remain central. MeCab, local audio, Forvo integrations, and other upstream/community tools remain available where their integration requirements are satisfied.

## Roadmap

Nothing here is set in stone. These are general directions, not a fixed feature list or a delivery schedule.

### Continued maintenance and upstream improvements

We intend to keep maintaining Manabitan and to continue bringing upstream Yomitan changes into it. Improvements from Yomitan remain important to this project; they need to be adapted and tested against Manabitan's different internals rather than copied blindly.

### A better welcome for new users

We will continue refining onboarding so more people can get started in the Yomitan/Manabitan ecosystem. Choosing dictionaries, importing them, understanding the popup, and setting up Anki should take less effort without taking away the flexibility experienced users rely on.

### Faster and more resource-efficient

We will continue making dictionary imports and lookups faster while reducing memory use and installed storage requirements. The aim is a more practical tool for everyday reading, including large collections and constrained devices—not just better numbers in an isolated benchmark.

### Public, comparable benchmarks

We are developing a robust benchmark suite to compare **dictionary imports, lookups, and storage requirements across tools compatible with Yomitan dictionaries**. We plan to make that suite public, with reproducible workloads and clear versions and test conditions. The suite and its publication are work in progress, not a finished comparison being announced here.

### Stay true to Yomitan

We have **no current plans for dramatic changes to Yomitan's general functionality, design, or familiar behaviors**. Manabitan intends to stay true to Yomitan's vision for how this tool works. Faster internals, a smaller footprint, and easier setup should improve the experience people already value, not require them to relearn it.

## Why not just make these changes in Yomitan?

That is a different question from whether the changes are useful. The storage rewrite is large enough that developing and safely migrating it upstream is a project in its own right. Manabitan is a fork because that is currently the practical way to build and prove the architecture without forcing Yomitan's existing users through a major migration.

Read [Why Manabitan is a fork](about-manabitan.md) for the longer explanation of the upstream relationship, migration responsibility, and why useful work can still flow back to Yomitan.
