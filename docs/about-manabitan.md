---
title: Why Manabitan exists
description: Why Manabitan rewrites Yomitan's storage and query engines, and why that work is being released as a fork.
---

# Why Manabitan exists

Manabitan is a fork of [Yomitan](https://github.com/yomidevs/yomitan) with rewritten dictionary storage and query engines. The point is to spend less time importing dictionaries and waiting for lookups, without giving up the extension that makes those dictionaries useful.

Yomitan's primary maintainers have supported releasing this work as a separate fork, offered guidance, and reviewed our release preparations. Manabitan is maintained and released independently. Their help has made it easier to take this route responsibly.

## A different implementation, not a different idea of Yomitan

This is a substantial departure from Yomitan's internals. It replaces the storage and query engines and changes how dictionaries are imported, updated, compressed, and accessed. Getting that to work quickly adds complexity. We take on that maintenance work in Manabitan rather than asking the upstream project to inherit it all at once.

What we want to preserve is the useful part of the experience: looking up a word where you're reading, choosing your dictionaries, hearing its pronunciation, and making an Anki card. We also want to smooth out onboarding and dictionary management. We aren't trying to make people relearn Yomitan just to use a faster implementation.

## Why a fork instead of upstream contributions?

Contributors have already tried bringing foundational pieces of this work to Yomitan. A change of this size needs to be split into smaller, reviewable changes. That's sensible, but some of those intermediate steps add work and complexity without delivering an immediate improvement on their own. Much of the value only appears once the pieces work together.

Preparing and reviewing that transition is a substantial project in its own right. There hasn't been enough sustained contributor and reviewer capacity to carry the whole thing through that way. That is a constraint on the work, not a judgment about either project's maintainers.

If developing Manabitan also required completing that upstream transition, this project wouldn't exist. A fork lets us build and test the implementation together, release it to people who choose to try it, and find out what holds up in everyday use.

## Why not move Yomitan's users over now?

A storage rewrite also means taking responsibility for a data migration. Yomitan users have existing dictionaries, profiles, settings, and custom Anki templates, across different browsers and devices. Faster code is not enough reason to put all of those installations through a major upgrade.

We aren't ready to take on that migration for Yomitan's whole user base. For now, Manabitan is a separate installation and an explicit choice. Keep backups, follow the [migration guide](yomitan-migration.md), and check the release notes for the package you're installing.

It may make sense to revisit broader upstreaming later, including the work and responsibility of safely moving existing users' data. We're not promising that outcome. First we need to make this implementation reliable for the people using it. One step at a time.

## Why speed matters

The first thing a new Yomitan user does is often import dictionaries and wait before they can start reading. It's worth the wait, but we'd like to make that first experience better. Large dictionaries make the problem harder; on older devices and e-ink readers, import times can become a serious obstacle.

Manabitan addresses both the amount of work and how it is scheduled. Imports are optimized, and the storage architecture is designed to keep installed dictionaries available while new data is imported. A dictionary being installed for the first time still needs to finish before it can be used. Availability during an import doesn't mean that background work has no cost, especially on a small device.

This also makes automatic updates practical. Manually starting an update is easy to put off, particularly when it interrupts reading. For dictionaries that provide a web update source, Manabitan can check for and install updates on a schedule. Dictionaries without that information still need a manually obtained update. See [dictionary updates](dictionaries.md#automatic-updates).

The query work improves ordinary lookups too. Waiting for a definition breaks the reading flow, and small delays are more noticeable on an e-reader. Reducing CPU and storage work should also help power consumption, but we haven't established a measured battery-life improvement. Performance varies with the device, dictionary collection, and build; benchmark results need that context.

## The work can go back upstream

Yomitan continues the work of Yomichan through successive open-source maintainers and communities. Manabitan is another branch of that history. The existing authorship and licenses stay with the work.

The extension remains GPL-3.0 licensed, with upstream notices and applicable third-party licenses preserved. Anyone can study it, adapt it, and contribute useful pieces back to Yomitan under those terms. Changes that stand on their own are still good candidates for upstream contributions; the fork doesn't close that door.

See [Credits](credits.md) for attribution and the distinction between the extension, documentation, and PDF viewer licenses.
