# TurtleML Architecture

TurtleML is a recursive systems architecture for composing independently meaningful operational units through explicit exchange boundaries.

The central unit is a **turtle**: a bounded system that has an internal implementation, an external contract, and a position within a larger composition. A turtle may contain other turtles and may itself be contained by a larger turtle.

The architecture is therefore not defined merely by recursion or nesting. It is defined by **recursive composition across operational boundaries**.

## 1. Turtle model

A turtle can be represented abstractly as:

```text
T = (B, X, R)
```

where:

- `B` is the turtle boundary;
- `X` is the internal implementation or internal world; and
- `R` is the externally legible exchange contract.

The internal implementation `X` is intentionally heterogeneous. It may be software, hardware, a model, a workflow, a human-operated process, a physical machine, a simulation, a database, another TurtleML graph, or a composition of many smaller turtles.

External participants should not need unrestricted knowledge of `X` to interact with the turtle. They interact through `R`.

## 2. Exchange-contract model

A useful initial model for a turtle boundary contract is:

```text
R = (I, O, C, S, P)
```

where:

- **I — Inputs:** data, signals, materials, requests, events, or resources accepted by the turtle;
- **O — Outputs:** data, signals, materials, events, decisions, or resources produced by the turtle;
- **C — Capabilities:** operations or services the turtle advertises across its boundary;
- **S — Exposed State:** state intentionally made observable or addressable outside the turtle;
- **P — Policy:** permissions, constraints, authority, safety rules, provenance requirements, timing rules, or other conditions governing exchange.

This tuple is a **working architectural schema**, not a claim that all future TurtleML interfaces must use exactly five fields. Implementations may encode contracts differently while preserving the underlying requirement that meaningful boundary exchange be explicit and inspectable.

## 3. Composition law

Two turtles may compose when their relevant boundary contracts are compatible enough for an intended exchange.

Conceptually:

```text
T_a --R_ab--> T_b
```

or bidirectionally:

```text
T_a <==R_ab==> T_b
```

Compatibility does not require identical internals. It requires sufficient agreement at the boundary.

A larger turtle may therefore be formed from smaller turtles:

```text
             T_parent
        ┌─────────────────┐
        │                 │
        │  T1 <--> T2     │
        │   \      /      │
        │    \    /       │
        │      T3          │
        │                 │
        └─────────────────┘
```

The parent has its own boundary and exchange contract even though its internal world contains an entire network of turtles.

This produces the recursive relation:

```text
T := bounded operational system
   | composition(T1, T2, ... Tn)
```

subject to explicit boundary contracts.

In the project's deliberately informal shorthand: **turtles all the way down — and back up.**

## 4. Recursive operational composition

TurtleML distinguishes **structural recursion** from **operational recursion**.

Structural recursion can repeatedly generate or rewrite shapes, graphs, trees, circuits, or other structures.

TurtleML's principal concern is different: a recursively composed unit should remain meaningful as an operational system at its own scale. A turtle may possess local state, behavior, control, responsibilities, policy, capabilities, or failure modes while also participating inside a larger system.

The recursive element is therefore not only:

```text
structure contains structure
```

but:

```text
operational system contains and coordinates operational systems
```

## 5. Heterogeneity behind the boundary

The same TurtleML composition may connect turtles implemented using very different substrates.

For example:

```text
[Python service]
       |
       v
[LLM agent] <--> [PLC / robot]
       |
       v
[human operator]
       |
       v
[simulation]
```

Each may be modeled as a turtle when it presents a meaningful operational boundary and explicit exchange contract.

TurtleML does not require every participant to share a programming language, runtime, model family, ontology, processor, or physical substrate.

## 6. Local autonomy and nested control

A turtle need not be fully autonomous. Autonomy is scale-relative.

A smaller turtle may be constrained, supervised, scheduled, powered, queried, stopped, or reconfigured by a parent while still retaining meaningful local behavior behind its boundary.

This allows nested control structures without requiring a single omniscient global controller.

## 7. Boundary legibility

Boundary events should be legible enough for the needs of the system. Depending on the application this may include:

- provenance;
- audit trails;
- debugging;
- permissions;
- resource accounting;
- timing;
- failure isolation;
- version compatibility;
- human review; or
- safety constraints.

Legibility does not mean that every turtle must reveal its internals. TurtleML separates **boundary transparency** from **implementation disclosure**.

## 8. Replacement and adaptation

When two turtles satisfy the relevant exchange contract, one may in some contexts substitute for the other without requiring the surrounding system to know how each works internally.

This is conditional rather than absolute. Contracts may include semantic, temporal, physical, safety, trust, or policy properties that make superficial input/output equivalence insufficient.

## 9. Scale

The turtle relation may be useful at scales such as:

```text
function or component
        ↓
service or tool
        ↓
agent or machine
        ↓
workflow or subsystem
        ↓
application or department
        ↓
system-of-systems
        ↓
ecosystem
```

Not every object at every scale is automatically a turtle. The boundary must carry operational meaning.

## 10. What TurtleML is not

TurtleML is not, by itself:

- a claim to have invented recursion;
- an L-system;
- a hardware description language;
- ordinary graph rewriting;
- a requirement for object-oriented programming;
- a universal ontology;
- a mandate for microservices;
- a requirement that every component expose its internals; or
- a claim that every nested system is TurtleML.

TurtleML is specifically concerned with **recursive system composition through explicit, interoperable operational boundaries**.

## 11. A useful implementation question

When deciding whether something should be treated as a turtle, ask:

> Can this thing be reasoned about as a bounded operational unit, can its important exchanges be expressed at its boundary, and can it participate in a larger composition without requiring the larger system to absorb all of its internal implementation details?

If the answer is yes, the turtle abstraction may be useful.

If the only reason to call something a turtle is that it is nested inside something else, the abstraction is probably too weak.
