# TurtleML Architectural Invariants

These invariants describe the current structural fingerprint of TurtleML. They are not claims that each individual concept is novel; the identifiable architecture is the particular combination, terminology, and behavior described by the project as a whole.

## 1. Bounded operational unit

A turtle is treated as a bounded unit with an inside and an outside. Its boundary is meaningful: external participants should not need unrestricted knowledge of internal implementation to interact with it.

## 2. Explicit exchange contracts

Exchange across a turtle boundary occurs through explicit interfaces or contracts. A useful working schema is:

```text
R = (I, O, C, S, P)
```

representing Inputs, Outputs, Capabilities, Exposed State, and Policy.

This tuple is not a mandatory encoding. The invariant is that important boundary exchanges are defined rather than left as invisible coupling.

## 3. Recursive composability

A turtle may contain smaller turtles and may itself be contained by a larger turtle. The same architectural reasoning can therefore recur across multiple scales.

## 4. Operational meaning at each scale

A turtle should be intelligible as an operational unit at its own scale. It may possess locally meaningful responsibilities, state, behavior, control, policy, capabilities, or failure modes.

Generic nesting alone is insufficient.

## 5. Internal implementation freedom

Internal mechanisms may change without forcing changes on every external participant, provided the exposed contract remains compatible. This permits heterogeneous implementations behind stable boundaries.

## 6. Interface-first composition

Larger systems are composed by connecting turtle exchange contracts rather than by requiring every component to share one implementation, language, runtime, model, ontology, or physical substrate.

## 7. Nested control without mandatory global control

Control may exist at several nested levels. A larger turtle may coordinate or constrain smaller turtles, while smaller turtles retain local behavior behind their boundaries. TurtleML does not require a single omniscient controller.

## 8. Legible boundary crossings

Important exchanges between turtles should be inspectable enough to support debugging, provenance, policy, testing, safety, authority, accounting, or other system needs. The architecture favors legible boundary events over invisible coupling.

## 9. Boundary transparency without mandatory internal disclosure

A turtle may expose enough information to make its exchanges understandable without revealing every internal mechanism. TurtleML distinguishes legible boundaries from forced implementation transparency.

## 10. Replaceability through contract compatibility

Where practical, one turtle can be replaced by another that satisfies the relevant contract. Replaceability is a consequence of meaningful boundaries, not a requirement that all turtles be interchangeable.

Compatibility may include semantic, temporal, physical, trust, policy, or safety conditions beyond superficial input/output shape.

## 11. Cross-scale structural similarity

The turtle relation should remain useful when reasoning across scales such as component → service → workflow → subsystem → organization-level system-of-systems. The implementation details may differ while the bounded-unit/exchange/composition pattern remains recognizable.

## 12. Structural recursion is not sufficient

A recursively generated tree, graph, circuit, geometry, or module hierarchy is not automatically TurtleML.

TurtleML's recursive unit is intended to remain operationally meaningful at its own scale and participate in larger compositions through explicit exchange boundaries.

## Recognition test

An implementation is strongly TurtleML-like when most of the following are true:

- operational units are explicitly bounded;
- boundary crossings are mediated by defined exchange contracts;
- units can recursively contain or compose other units;
- recursively composed units retain operational meaning at their own scale;
- internal implementations can differ behind compatible contracts;
- control can occur at multiple nested scales;
- boundary interactions are intentionally legible;
- boundary legibility does not require unrestricted internal disclosure; and
- the same compositional reasoning is applied across more than one scale.

A system containing only generic nesting, only recursive structural rewriting, or only a conventional module hierarchy should not automatically be labeled TurtleML.

## Evolution

These invariants may be refined as the architecture is implemented and tested. Material changes should be documented in repository history, release notes, and `PROVENANCE.md` so that the evolution remains attributable and auditable.
