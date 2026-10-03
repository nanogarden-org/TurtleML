# TurtleML — Origin, Chronology, and Challenge Notes

## Problem observed

Distributed AI/ML and automation systems can collapse distinct stages of cognition and authority into one operational path: a signal becomes an inference, an inference becomes a claim, and a claim becomes action without a sufficiently explicit boundary.

TurtleML was developed around a narrower architectural question:

> Can heterogeneous nodes exchange observations and learned experience while keeping authority separately scoped, revocable, expiring, and auditable?

## Specific architectural treatment

The current public formulation centers on:

- `signal != feature != inference != claim != authorized action`;
- knowledge propagation that does not imply permission propagation;
- truthful capability declaration;
- stable contracts across heterogeneous implementations;
- recursive composition in which a bounded region may itself act as a node.

These are this repository's design choices and formulation. The project does not claim ownership of distributed systems, capability security, authorization, provenance, actor models, policy engines, or edge AI as general fields.

## Public chronology

Repository history documents when particular TurtleML artifacts and formulations were public.

Use that history as evidence of this repository's chronology, not as proof that no earlier related work exists or that later similar work was derived from TurtleML.

## Why the model is intentionally a toy

The small Python implementation is an executable architectural argument. It is meant to expose semantics before adding hardware, networking stacks, LLMs, or production infrastructure.

If the invariant cannot survive the toy model, scaling it up is not progress.

## Break it

A meaningful counterexample is more useful than agreement. Try to produce a case where:

1. information propagation silently expands authority;
2. a revoked or expired grant remains effective;
3. recursion creates an authority escalation;
4. a node's declared capability and actual capability diverge;
5. transport preserves a message but changes its meaning;
6. node loss creates an unsafe fallback.

Open an issue with the smallest reproducible failure or a related-work reference that materially changes the framing.
