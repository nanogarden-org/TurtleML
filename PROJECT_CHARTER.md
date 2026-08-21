# TurtleML Project Charter

## Purpose

Formalize and test a recursive local-first systems architecture in which heterogeneous AI/ML, embedded, sensor, and control nodes can cooperate without collapsing knowledge, trust, and authority into the same channel.

## Primary research question

Can heterogeneous nodes exchange observations and learned claims while preserving explicit, scoped, expiring authority boundaries?

## Architectural thesis

TurtleML treats each node or region as a bounded adaptive system ("turtle"). Internal implementation is allowed to evolve independently. Inter-node communication is constrained by stable contracts carrying identity, provenance, scope, claims, and authority state.

## Design principles

### P1 — Separate epistemics from control
A node's inference may be useful without being authoritative.

### P2 — Standardize seams, not boxes
Hardware, operating system, model, transport, and internal implementation may vary.

### P3 — Local-first operation
The reference system must continue functioning without an Internet connection.

### P4 — Recursive composition
A group of turtles may present a capability boundary as a higher-order turtle.

### P5 — Honest capability manifests
Nodes must declare what they can sense, compute, store, communicate, and actuate.

### P6 — Least authority
Authority is granted only for a specific actor, action, target/scope, and lifetime.

### P7 — Auditable transitions
Claims, decisions, grants, denials, and actions should be reconstructable.

## 0.1 Success criteria

- [ ] Node identities are explicit.
- [ ] Capabilities are machine-readable.
- [ ] Claims carry source, subject, assertion, confidence, timestamp, and provenance.
- [ ] Claims do not confer authority.
- [ ] Policy evaluation is separate from inference.
- [ ] Authority grants are scoped and expiring.
- [ ] Denials are first-class audit events.
- [ ] Turtle regions recursively expose child capabilities.
- [ ] Protocol envelopes serialize independently of internal node classes.
- [ ] Unit tests encode architectural invariants.
- [ ] A three-node pump-anomaly example demonstrates the full path.

## Falsification conditions

TurtleML's initial architecture should be considered failed or in need of redesign if any of the following becomes necessary:

1. every node must run the same hardware or runtime;
2. receiving a claim is enough to execute an actuator;
3. trust is derived from transport alone;
4. authority cannot be scoped or expired;
5. higher-order turtles require access to every child's internal implementation;
6. cloud availability is required for basic local operation.

## Near-term deliverable

An executable Python reference model, tests, a protocol schema, and one small demonstration. Hardware integration begins only after the semantic model passes.
