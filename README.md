# TurtleML

**TurtleML** is a nested systems-architecture concept for composing independently operable units into larger systems-of-systems through explicit boundaries and interfaces.

The central metaphor is a turtle: a bounded unit that can operate on its own, expose a defined interface, contain other turtles, and participate as a component inside a larger turtle. The implementation behind a boundary may vary while the interface contract remains legible.

## Project status

TurtleML is an early-stage architecture and reference implementation. This repository is intentionally publishing the architecture, terminology, invariants, provenance, and falsification criteria alongside the code so that reuse can remain open while lineage remains visible.

## Licensing

TurtleML uses a split-license model:

- **Software source code** is licensed under the **Apache License 2.0**. See [`LICENSE`](LICENSE).
- **Documentation, architectural prose, diagrams, theory, and explanatory material authored for TurtleML** are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)** unless a file states otherwise. See [`LICENSE-DOCS`](LICENSE-DOCS).

These licenses permit commercial use, redistribution, and modification under their respective terms. They do not require downstream implementations to disclose proprietary internals merely because they implement or interoperate with TurtleML.

## Attribution and provenance

If you reuse or adapt TurtleML documentation, architectural material, diagrams, or substantial explanatory expression, please preserve attribution as required by CC BY 4.0 and identify TurtleML as the source.

For canonical citation and lineage information, see:

- [`CITATION.cff`](CITATION.cff) — machine-readable citation metadata
- [`NOTICE`](NOTICE) — attribution notice for distributed software
- [`PROVENANCE.md`](PROVENANCE.md) — origin, dates, scope of the priority claim, and lineage
- [`docs/INVARIANTS.md`](docs/INVARIANTS.md) — structural features that identify the architecture
- [`docs/FALSIFICATION.md`](docs/FALSIFICATION.md) — claims that can be tested or shown inadequate

TurtleML does **not** claim authorship of generic concepts such as nesting, modularity, recursion, abstraction, encapsulation, or systems-of-systems. The provenance claim concerns the specific TurtleML project: its named architecture, particular combination and expression of structural invariants, terminology, documentation, reference implementations, and published lineage.

## Canonical project

Repository: `nanogarden-org/TurtleML`

Original author: **Robin Abigayle Bronson**

First public repository publication: **2026-08-21**

---

Build with the turtles. Keep the tracks visible.
