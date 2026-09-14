---
hide:
  - navigation
  - footer
---

# Why Manabitan exists

Manabitan is a fork of [Yomitan](https://github.com/yomidevs/yomitan). It keeps the parts of Yomitan that make it such a useful language-learning tool, while replacing some of its deepest internals so dictionaries can import, update, and answer lookups much faster.

This isn't a split caused by a disagreement with Yomitan. The primary Yomitan maintainers have provided guidance and support around developing and releasing Manabitan as a fork, and have reviewed the steps taken to release it this way. We think a separate fork is the responsible place to prove changes of this scale before asking Yomitan's much larger user base to migrate to them.

Yomitan itself is part of a longer line of open-source stewardship. It continues the work of Yomichan, and Manabitan is another branch of that same family rather than an attempt to erase it. We intend to keep contributing useful work back where it makes sense.

## Why not make all of this a Yomitan pull request?

The short version is that the storage work is too large to land usefully one piece at a time.

Manabitan replaces Yomitan's dictionary storage and much of its query path. That work also includes migration, import and update machinery, compression, caching, compatibility code, tests, and performance work around the new architecture. It is not a small optimization that can be dropped into the existing database layer.

There have already been attempts to bring foundational pieces of this work upstream. The problem is practical: a change this large has to be split into incremental pull requests, while many of those intermediate pieces create review and maintenance work without delivering much immediate value to Yomitan users on their own. The complete change is useful; many of the steps required to get there are not especially useful in isolation.

Given the amount of implementation and review work involved, there has been limited appetite for doing the whole transition incrementally inside Yomitan. That's reasonable. It also means Manabitan would simply not exist if every part of it had to be accepted upstream before we could build the next part.

A fork lets us finish the architecture, test it as a whole, and take responsibility for the users who deliberately choose it.

## Why not migrate Yomitan itself now?

Because changing a database is easy compared with taking responsibility for everybody's data.

Yomitan has a large installed user base with years of dictionaries, settings, profiles, Anki templates, and browser-specific state. Manabitan changes the internal representation of a substantial part of that data. Even if the new architecture is better, we do not currently want to ask the Yomitan maintainers—or ourselves—to take on the risk of migrating every existing Yomitan installation in one upgrade.

For now, installing Manabitan is an explicit choice. That gives us room to stabilize the new internals and migration paths without turning an architectural experiment into an involuntary migration for existing Yomitan users.

Maybe that changes later. Once this has been proven in the wild, it may make sense to revisit upstreaming more of the architecture and doing the much less glamorous work of safely migrating everybody. One step at a time.

## Why speed matters

Waiting for a dictionary to import is not language learning.

Yomitan is worth waiting for, but its onboarding experience can be rough when the first thing a new user has to do is import dictionaries and wait. Large dictionaries make that more obvious. On older hardware and constrained devices such as e-ink readers, an import can take an overwhelming amount of time.

Manabitan attacks that problem in two ways. First, imports themselves are much faster. Second, the storage architecture is designed so an import does not have to make the rest of the extension useless while it runs. Existing dictionaries can remain available while new data is prepared and moved into place.

That changes what is practical. Dictionaries with a web-accessible update source can update automatically instead of making the user periodically notice an update, start it manually, and wait for the extension to become useful again. Faster imports are nice; making routine updates cheap enough to stop thinking about them is better.

The same work also improves normal lookups. That is especially noticeable on slow devices, but reducing the amount of CPU and I/O required for a lookup matters everywhere: less latency, less battery use, and less work between pointing at a word and seeing its definition.

## What Manabitan is not trying to change

Manabitan is not a redesign for the sake of being different. Yomitan already has an unusually capable feature set and a workflow that many language learners depend on.

We do want to smooth out rough edges—especially onboarding, dictionary management, updates, and performance—but the goal is to stay recognizably Yomitan-compatible rather than replace a mature product with a different opinion about how people should learn languages.

## Open source goes both ways

Manabitan remains open source under the same GPL family of licensing as Yomitan, and this documentation preserves the upstream wiki's CC BY licensing and attribution. The code is there to be studied, criticized, reused, and improved.

Nobody needs permission to take a useful idea or implementation from Manabitan and bring it back to Yomitan. We would be happy to see that happen. We will also continue contributing improvements upstream when a change makes sense independently of Manabitan's larger storage architecture.

See [Credits](credits.md) for the project's lineage and attribution.
