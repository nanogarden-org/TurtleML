# TurtleML Provenance Record

## Canonical identity

- **Project:** TurtleML
- **Original author:** Robin Abigayle Bronson
- **Publisher / repository owner:** nanogarden-org
- **Canonical repository:** https://github.com/nanogarden-org/TurtleML
- **Initial public repository date:** 2026-08-21
- **Initial repository commit:** `7c255c3986bb7b6c33a01a81962fa2a46c5eefdd`

## Purpose of this record

This document records the public lineage of TurtleML so that the architecture may be reused, implemented, discussed, tested, criticized, and extended without erasing where this particular formulation came from.

TurtleML is intentionally not a black-box architecture. Its public documentation is meant to make the structure legible enough to implement and evaluate. The provenance goal is therefore not secrecy or forced disclosure of downstream proprietary systems. It is durable attribution of the TurtleML formulation and an auditable chronology of its development.

## Scope of the provenance claim

TurtleML does **not** claim invention or ownership of generic ideas such as:

- nesting
- recursion
- modularity
- encapsulation
- abstraction
- interface contracts
- hierarchical systems
- systems-of-systems
- graph composition
- layered control

Those concepts have extensive prior histories.

The TurtleML provenance claim concerns the identifiable project-level synthesis published here: the **TurtleML name**, turtle boundary metaphor, recursively composable bounded units, explicit interface-mediated exchange, independence of internal implementation from external contract, nested system-of-systems interpretation, accompanying terminology, diagrams, prose, executable reference material, invariants, falsification criteria, and their evolution as a coherent architecture.

A later architecture may legitimately resemble TurtleML through independent development or shared antecedents. This provenance record exists to make comparison possible rather than to presume copying.

## Initial architectural statement

A TurtleML "turtle" is a bounded operational unit that:

1. can be reasoned about as a unit at its own scale;
2. exposes explicit interfaces at its boundary;
3. may contain smaller turtles;
4. may itself participate inside a larger turtle;
5. can vary its internal implementation while preserving compatible external contracts; and
6. composes through interfaces rather than requiring global knowledge of every internal mechanism.

This creates a scale-recursive architecture in which similar reasoning can be applied across tool, component, workflow, subsystem, system, and system-of-systems levels.

See `docs/INVARIANTS.md` for the current structural fingerprint and `docs/FALSIFICATION.md` for testable limits.

## Licensing and attribution

Software source code in this repository is licensed under Apache-2.0 unless otherwise stated.

Documentation, architectural prose, diagrams, theory, and explanatory material authored for TurtleML are licensed under CC BY 4.0 unless otherwise stated.

Canonical citation metadata is provided in `CITATION.cff`.

## Chronology

### 2026-08-21 — Repository genesis

The public `nanogarden-org/TurtleML` repository was created with initial commit:

`7c255c3986bb7b6c33a01a81962fa2a46c5eefdd`

Initial description:

> Nested Turtle Concept demonstrating control layers through systems of systems

### 2026-08-21 — Provenance foundation

A dedicated provenance foundation branch was created immediately after the initial commit to establish:

- software licensing under Apache-2.0;
- documentation licensing under CC BY 4.0;
- a distributable NOTICE;
- machine-readable citation metadata;
- this provenance record;
- architectural invariants; and
- falsification criteria.

Future substantive releases should add entries here or in a linked changelog so that changes to the architecture remain traceable over time.

## Preferred attribution

A practical attribution is:

**TurtleML — Robin Abigayle Bronson, 2026, https://github.com/nanogarden-org/TurtleML**

When citing a specific implementation, paper, diagram, or release, include its version, tag, commit, DOI, or stable archive identifier when available.

## Provenance principle

Reuse is encouraged. Modification is encouraged. Commercial implementation is permitted under the applicable licenses. Proprietary internals do not need to be disclosed merely because TurtleML is used.

The request is simpler: **keep the tracks visible.**
