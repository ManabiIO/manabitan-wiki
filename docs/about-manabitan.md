---
title: Why Manabitan is a fork
description: Why Manabitan's foundational storage and query rewrite is being developed and released separately from Yomitan.
---

# Why Manabitan is a fork

This page is about the project structure: why Manabitan is being built and released separately rather than landing the whole project inside Yomitan. For the user-facing reasons to choose it, see [Why use Manabitan?](why-manabitan.md).

Manabitan is based on [Yomitan](https://github.com/yomidevs/yomitan), which continues the work started by Yomichan. Manabitan preserves that lineage and the familiar user workflow, but its dictionary storage and query engines are a substantial departure from upstream.

Yomitan's primary maintainers have supported releasing this work as a separate fork, offered guidance, and reviewed our release preparations. Manabitan is maintained and released independently. That support is important context for why this project exists where it does; it is not a claim that Yomitan formally endorses every Manabitan release or has audited Manabitan's code.

## The change is foundational

This is not a small optimization patch. Manabitan replaces dictionary storage and much of the query path, with related changes to imports, updates, compression, caching, migration, compatibility, tests, and performance work.

Those pieces have to work together before much of the value appears. A fork gives the implementation room to become coherent and testable as a whole rather than forcing the project to live indefinitely as a sequence of intermediate states.

## Why not upstream it incrementally?

Contributors have tried bringing foundational parts of this work upstream. A change this large reasonably has to be divided into smaller, reviewable pull requests. The practical problem is that some intermediate steps add implementation, review, and maintenance work without producing much immediate value for Yomitan users on their own.

Completing the transition upstream therefore requires sustained work on both sides: preparing each incremental change and having enough reviewer capacity to understand and accept a major internal transition over time. There has not been enough sustained capacity to carry the entire rewrite through that process.

That is a practical constraint, not a criticism of Yomitan. If every Manabitan step had to be accepted upstream before the next step could be developed, this implementation would not exist in its current form.

## Why not migrate Yomitan's users now?

A storage rewrite is also a data-migration responsibility. Yomitan has users with years of dictionaries, profiles, settings, custom Anki templates, browser-specific state, and integrations. Better internals are not enough reason to put all of those installations through a major migration before the migration itself has been proven.

We are not taking responsibility yet for moving Yomitan's entire installed base onto these internals. Manabitan is a separate installation and an explicit choice. That lets us stabilize the architecture and migration paths with users who deliberately choose it rather than turning the work into an involuntary upstream upgrade.

It may make sense to revisit broader upstreaming later, including the less glamorous work of safely migrating everybody's data. We are not promising that outcome. First the implementation has to prove itself in normal use. One step at a time.

## Why the rewrite is worth maintaining separately

The user-facing gains are broader than one speed number. The new architecture supports faster imports and lookups, dramatically smaller installed dictionary footprints, keeping installed dictionaries available while new data is prepared, and making scheduled dictionary updates much easier to live with.

Manabitan also has room to improve onboarding and integrations around that foundation—for example automatic Anki field mapping today, with broader AnkiConnect performance and capability work on the roadmap—without changing the familiar core workflow just to justify being a fork.

Those benefits are described in [Why use Manabitan?](why-manabitan.md). The [roadmap](why-manabitan.md#roadmap) also makes the intended direction explicit: continue tracking Yomitan, keep improving performance and efficiency, improve onboarding and integrations, and avoid dramatic changes to the product's familiar behavior.

## The work can still go back upstream

A fork does not close the door in either direction. Manabitan remains open source under the same GPL-3.0-or-later licensing lineage as Yomitan, with upstream authorship and applicable third-party notices preserved.

Anyone can study the implementation and bring useful ideas or code back to Yomitan under those terms. We also intend to keep contributing changes upstream when they make sense independently of Manabitan's larger architecture.

Yomitan itself is part of a longer history of open-source stewardship through Yomichan and later maintainers. Manabitan is another branch of that history, not an attempt to erase or delegitimize it.

See [Credits](credits.md) for attribution and licensing details.
