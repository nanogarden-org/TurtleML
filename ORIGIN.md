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

Git history identifies artifact versions and recorded dates. Commit dates and retained snapshots alone do not establish when an artifact became publicly accessible. Public-availability claims require a separately recorded publication or archival anchor. This packet does not establish a verified first-publication date. Neither repository chronology nor publication evidence establishes universal novelty, exclusive ownership of abstract ideas, or derivation by later work.

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

## Evidence and challenge scope

Revocation of already-issued grants is not demonstrated by the current grant model. Capability truthfulness, hostile transport, and recursive authority safety remain architecture challenges. This is not a production distributed security system.

[Authority tests](tests/test_authority.py) · [Pump-policy demo](examples/pump_demo.py)

## Submit a useful challenge

[Open an issue](https://github.com/nanogarden-org/TurtleML/issues/new) with the version or commit SHA, invariant challenged, minimal synthetic input, commands or reasoning steps, expected versus observed behavior, and any relevant related-work link. Identify whether the challenge concerns implemented behavior or proposed architecture. Exclude private or unlicensed source material.
