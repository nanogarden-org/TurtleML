# TurtleML Falsification and Failure Criteria

TurtleML is intended to be an architecture that can be tested, not merely a metaphor that is declared successful after the fact. This document records conditions under which specific TurtleML claims should be considered weakened, inapplicable, or false.

## Claim 1: Boundaries reduce unnecessary coupling

**Claim:** Explicit turtle boundaries and interface contracts allow internal implementations to change with less downstream disruption than tightly coupled designs.

**Evidence against:** Across comparable implementations, changes inside turtles routinely require equal or greater unrelated downstream changes despite stable interfaces.

## Claim 2: Recursive composition remains useful across scales

**Claim:** The bounded-unit/interface/composition model remains useful at more than one architectural scale.

**Evidence against:** The model becomes incoherent, purely metaphorical, or operationally useless when moved between component, workflow, subsystem, and system-of-systems scales.

## Claim 3: Heterogeneous implementations can interoperate through contracts

**Claim:** Turtles can use different internal technologies while interoperating through compatible interfaces.

**Evidence against:** Meaningful interoperability repeatedly requires shared hidden implementation assumptions that cannot be represented at the interface boundary.

## Claim 4: Boundary legibility improves traceability

**Claim:** Making important cross-boundary exchanges explicit can improve debugging, provenance, testing, policy enforcement, or system comprehension.

**Evidence against:** In representative systems, explicit boundary instrumentation produces no useful increase in traceability or produces costs that systematically exceed the benefit.

## Claim 5: Local autonomy can coexist with nested coordination

**Claim:** Smaller turtles can retain meaningful local behavior while larger turtles coordinate or constrain them.

**Evidence against:** Useful coordination consistently requires either complete central control or effectively unconstrained local behavior, making the proposed middle structure unstable or unnecessary.

## Claim 6: Contract compatibility enables practical replacement

**Claim:** A meaningful subset of turtles can be replaced by alternate implementations without rewriting the surrounding system when the relevant contract is preserved.

**Evidence against:** Replacement consistently fails because behavior essential to the surrounding system cannot be captured or constrained by the stated contract.

## Failure modes that do not automatically falsify TurtleML

The following can indicate a bad implementation without disproving the architecture itself:

- poorly specified interfaces;
- interfaces so broad that boundaries become meaningless;
- excessive nesting that adds ceremony without isolation;
- hidden shared state across supposed boundaries;
- global assumptions masquerading as local contracts;
- tracing that records data without preserving useful provenance;
- treating every object, function, or process as a turtle regardless of whether a meaningful operational boundary exists.

## Comparative testing

Where possible, TurtleML claims should be evaluated against alternative architectures using measurable criteria such as:

- change propagation after internal modification;
- number of components affected by replacement;
- boundary contract complexity;
- cross-component failure propagation;
- debugging time;
- provenance completeness;
- interoperability across heterogeneous implementations;
- coordination overhead; and
- performance or latency introduced by boundary mediation.

## Revision rule

A failed claim should not be protected by redefining TurtleML after the result is known. Instead:

1. record the test and result;
2. identify which invariant or claim failed;
3. determine whether the failure is implementation-specific or architectural;
4. revise the architecture transparently if warranted; and
5. preserve the earlier claim and revision in repository history.

Negative results are part of the TurtleML lineage, not something to erase from it.
