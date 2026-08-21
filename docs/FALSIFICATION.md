# TurtleML Falsification and Failure Criteria

TurtleML is intended to be an architecture that can be tested, not merely a metaphor that is declared successful after the fact. This document records conditions under which specific TurtleML claims should be considered weakened, inapplicable, or false.

## Claim 1: Boundaries reduce unnecessary coupling

**Claim:** Explicit turtle boundaries and exchange contracts allow internal implementations to change with less downstream disruption than tightly coupled designs.

**Evidence against:** Across comparable implementations, changes inside turtles routinely require equal or greater unrelated downstream changes despite stable contracts.

## Claim 2: Recursive composition remains useful across scales

**Claim:** The bounded-unit/exchange/composition model remains useful at more than one architectural scale.

**Evidence against:** The model becomes incoherent, purely metaphorical, or operationally useless when moved between component, workflow, subsystem, and system-of-systems scales.

## Claim 3: Heterogeneous implementations can interoperate through contracts

**Claim:** Turtles can use different internal technologies while interoperating through compatible exchange contracts.

**Evidence against:** Meaningful interoperability repeatedly requires shared hidden implementation assumptions that cannot be represented at the boundary.

## Claim 4: Boundary legibility improves traceability

**Claim:** Making important cross-boundary exchanges explicit can improve debugging, provenance, testing, policy enforcement, authority tracking, or system comprehension.

**Evidence against:** In representative systems, explicit boundary instrumentation produces no useful increase in traceability or produces costs that systematically exceed the benefit.

## Claim 5: Local autonomy can coexist with nested coordination

**Claim:** Smaller turtles can retain meaningful local behavior while larger turtles coordinate or constrain them.

**Evidence against:** Useful coordination consistently requires either complete central control or effectively unconstrained local behavior, making the proposed middle structure unstable or unnecessary.

## Claim 6: Contract compatibility enables practical replacement

**Claim:** A meaningful subset of turtles can be replaced by alternate implementations without rewriting the surrounding system when the relevant contract is preserved.

**Evidence against:** Replacement consistently fails because behavior essential to the surrounding system cannot be captured or constrained by the stated contract.

## Claim 7: The exchange-contract abstraction is sufficiently expressive

**Claim:** Important cross-boundary dependencies can be represented explicitly enough to support composition without exposing the complete internal implementation.

The current working schema is:

```text
R = (I, O, C, S, P)
```

for Inputs, Outputs, Capabilities, Exposed State, and Policy.

**Evidence against:** Representative TurtleML systems repeatedly require essential boundary properties that cannot be captured without either collapsing the boundary or expanding the contract model beyond practical usefulness.

A failure of the five-field schema does not automatically falsify the broader TurtleML boundary concept. It may instead require revision of the schema. Such revisions must be recorded rather than retroactively treated as though they were always present.

## Claim 8: Operational recursion adds useful information beyond structural recursion

**Claim:** Distinguishing recursively composed operational systems from recursively generated structure provides useful architectural guidance.

**Evidence against:** Across representative cases, the distinction adds no predictive, design, interoperability, control, failure-isolation, or explanatory value beyond existing structural-recursion or ordinary modular-composition models.

## Failure modes that do not automatically falsify TurtleML

The following can indicate a bad implementation without disproving the architecture itself:

- poorly specified interfaces;
- interfaces so broad that boundaries become meaningless;
- excessive nesting that adds ceremony without isolation;
- hidden shared state across supposed boundaries;
- global assumptions masquerading as local contracts;
- tracing that records data without preserving useful provenance;
- treating every object, function, or process as a turtle regardless of whether a meaningful operational boundary exists;
- treating simple recursive structure as sufficient evidence of TurtleML; or
- forcing the provisional `R = (I, O, C, S, P)` schema onto cases where a different contract representation is demonstrably better.

## Comparative testing

Where possible, TurtleML claims should be evaluated against alternative architectures using measurable criteria such as:

- change propagation after internal modification;
- number of components affected by replacement;
- boundary contract complexity;
- cross-component failure propagation;
- debugging time;
- provenance completeness;
- interoperability across heterogeneous implementations;
- coordination overhead;
- hidden shared assumptions discovered during integration;
- amount of internal disclosure required for successful composition; and
- performance or latency introduced by boundary mediation.

Comparisons with related work should distinguish the property being tested. For example, a structural-recursion system may be an appropriate comparator for graph growth while a distributed or component architecture may be a better comparator for operational composition.

## Revision rule

A failed claim should not be protected by redefining TurtleML after the result is known. Instead:

1. record the test and result;
2. identify which invariant or claim failed;
3. determine whether the failure is implementation-specific, schema-specific, or architectural;
4. revise the architecture transparently if warranted; and
5. preserve the earlier claim and revision in repository history.

Negative results are part of the TurtleML lineage, not something to erase from it.
