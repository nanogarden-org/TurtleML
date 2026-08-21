# ADR 0001 — Python as the first reference implementation

## Status
Accepted for 0.1.

## Context
The first risk is semantic incoherence, not runtime performance.

## Decision
Use Python 3.11+ for the executable reference model.

## Consequences
Positive: fast iteration, broad ML/edge ecosystem, readable prototypes, easy testing.

Negative: not appropriate for every embedded target; not the final choice for all long-running infrastructure.

## Constraint
No protocol concept may depend on Python-specific serialization or object identity.
