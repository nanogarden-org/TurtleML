# TurtleML Architectural Invariants

These invariants describe the current structural fingerprint of TurtleML. They are not claims that each individual concept is novel; the identifiable architecture is the particular combination, terminology, and behavior described by the project as a whole.

## 1. Bounded operational unit

A turtle is treated as a bounded unit with an inside and an outside. Its boundary is meaningful: external participants should not need unrestricted knowledge of internal implementation to interact with it.

## 2. Explicit interface mediation

Exchange across a turtle boundary occurs through explicit interfaces or contracts. Interfaces should identify what may cross the boundary, in what form, and under what expectations.

## 3. Recursive composability

A turtle may contain smaller turtles and may itself be contained by a larger turtle. The same architectural reasoning can therefore recur across multiple scales.

## 4. Scale-relative autonomy

A turtle should be intelligible as an operational unit at its own scale. It does not need to be globally independent, but it should have locally meaningful responsibilities, state, behavior, or control.

## 5. Internal implementation freedom

Internal mechanisms may change without forcing changes on every external participant, provided the exposed interface remains compatible. This permits heterogeneous implementations behind stable boundaries.

## 6. Interface-first composition

Larger systems are composed by connecting turtle interfaces rather than by requiring every component to share one implementation, language, runtime, model, or internal ontology.

## 7. Nested control without mandatory global control

Control may exist at several nested levels. A larger turtle may coordinate or constrain smaller turtles, while smaller turtles retain local behavior behind their boundaries. TurtleML does not require a single omniscient controller.

## 8. Legible boundary crossings

Important exchanges between turtles should be inspectable enough to support debugging, provenance, policy, or testing. The architecture favors legible boundary events over invisible coupling.

## 9. Replaceability through contract compatibility

Where practical, one turtle can be replaced by another that satisfies the relevant contract. Replaceability is a consequence of meaningful boundaries, not a requirement that all turtles be interchangeable.

## 10. Cross-scale structural similarity

The turtle relation should remain useful when reasoning across scales such as component → service → workflow → subsystem → organization-level system-of-systems. The implementation details may differ while the bounded-unit/interface/composition pattern remains recognizable.

## Recognition test

An implementation is strongly TurtleML-like when most of the following are true:

- operational units are explicitly bounded;
- boundary crossings are mediated by defined interfaces;
- units can recursively contain or compose other units;
- internal implementations can differ behind compatible contracts;
- control can occur at multiple nested scales;
- boundary interactions are intentionally legible; and
- the same compositional reasoning is applied across more than one scale.

A system containing only generic nesting or only a conventional module hierarchy should not automatically be labeled TurtleML.

## Evolution

These invariants may be refined as the architecture is implemented and tested. Material changes should be documented in repository history, release notes, and `PROVENANCE.md` so that the evolution remains attributable and auditable.
