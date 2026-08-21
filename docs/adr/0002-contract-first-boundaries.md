# ADR 0002 — Contract-first boundaries

## Status
Accepted.

## Decision
TurtleML standardizes inter-node semantics before standardizing node internals.

## Rationale
The project assumes heterogeneous and scavenged hardware. Uniform internals would defeat that premise.

## Consequence
Any implementation is acceptable if it can truthfully express compatible identity, capability, claim, scope, authority, and audit information.
