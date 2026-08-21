# TurtleML

**TurtleML** is a recursive systems architecture for composing independently meaningful operational units into larger systems-of-systems through explicit exchange boundaries.

The central metaphor is a turtle: a bounded unit that can operate meaningfully at its own scale, expose a defined exchange contract, contain other turtles, and participate as a component inside a larger turtle. The implementation behind a boundary may vary while the external contract remains legible.

A concise working definition is:

> **TurtleML is recursive operational composition through explicit, interoperable boundaries.**

The architecture is not defined merely by nesting. A turtle may carry local state, behavior, control, capabilities, policy, responsibilities, or failure modes while participating inside a larger system.

## Exchange contracts

A useful initial model for a turtle boundary is:

```text
R = (I, O, C, S, P)
```

where:

- **I** — accepted inputs;
- **O** — produced outputs;
- **C** — externally advertised capabilities;
- **S** — intentionally exposed state; and
- **P** — policy, permissions, constraints, provenance, authority, or other rules governing exchange.

This five-part tuple is a working schema rather than a mandatory wire format. Implementations may encode contracts differently while preserving the architectural requirement that important cross-boundary exchange be explicit and inspectable.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the current model.

## Heterogeneous turtles

A turtle's internal implementation may be radically different from its neighbors. A TurtleML composition can potentially connect units implemented as:

- software services;
- LLM or other AI agents;
- databases;
- PLCs and industrial controllers;
- robots and physical machines;
- simulations;
- human-operated processes;
- hardware circuits; or
- other TurtleML graphs containing many additional turtles.

The surrounding system should interact through the boundary contract rather than requiring every turtle to share one language, runtime, model, ontology, or substrate.

## Project status

TurtleML is an early-stage architecture and reference implementation. This repository intentionally publishes the architecture, terminology, invariants, provenance, related work, and falsification criteria alongside the code so that reuse can remain open while lineage remains visible.

## Related work

TurtleML does **not** claim authorship of recursion, nesting, modularity, abstraction, graph composition, interface contracts, hierarchical control, or systems-of-systems.

Adjacent work is documented explicitly in [`docs/RELATED_WORK.md`](docs/RELATED_WORK.md).

One current comparison is **MorphoHDL**, an experimental hardware-description language and graph-rewrite system for growing circuits through structural recursion. MorphoHDL and TurtleML occupy overlapping recursive-computation territory, but their principal questions differ:

```text
MorphoHDL: How can computational structure grow recursively?

TurtleML:  How can operational systems recursively contain,
           coordinate, and exchange with other operational systems?
```

The two approaches can also compose: a TurtleML turtle could contain a recursively generated circuit while exposing a TurtleML exchange contract to the larger system.

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
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — turtle model and exchange-contract architecture
- [`docs/INVARIANTS.md`](docs/INVARIANTS.md) — structural features that identify the architecture
- [`docs/FALSIFICATION.md`](docs/FALSIFICATION.md) — claims that can be tested or shown inadequate
- [`docs/RELATED_WORK.md`](docs/RELATED_WORK.md) — adjacent prior art and comparison space

The provenance claim concerns the specific TurtleML project: its named architecture, turtle-boundary model, recursive operational composition, particular combination and expression of structural invariants, terminology, documentation, reference implementations, and published lineage.

## Canonical project

Repository: `nanogarden-org/TurtleML`

Original author: **Robin Abigayle Bronson**

First public repository publication: **2026-08-21**

---

**Build with the turtles. Keep the tracks visible.**
