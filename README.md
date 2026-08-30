# TurtleML

**TurtleML** is a local-first reference architecture for recursive, heterogeneous AI/ML nodes that communicate through stable authority and provenance contracts.

> Ecological evolution inside; engineered contracts at the seams.

TurtleML is intentionally **not** a monolithic smart-home platform, agent framework, or model-training stack. Its first job is to prove a smaller claim:

> A node may observe, infer, and share knowledge without automatically gaining—or propagating—the authority to act.

## Core invariants

1. **Signal != feature != inference != claim != authorized action**
2. **Experience may propagate faster than authority**
3. **Heterogeneous internals; stable contracts**
4. **Cloud is augmentation, not dependency**
5. **Authority is scoped, expiring, revocable, and auditable**
6. **Every node truthfully declares capabilities**
7. **Recursive composition:** a region can itself behave as a turtle

## Current status

`0.1.0-alpha` — executable architecture skeleton on the default `main` branch.

The current implementation is deliberately dependency-light Python. It proves the authority and provenance semantics before hardware, RF links, LLMs, or optimization:

- observer claims can move between nodes;
- knowledge does not imply permission;
- policy can deny or grant a scoped action;
- authority can expire and be audited; and
- a node can disappear without collapsing the simulation.

At this checkpoint, the test suite passes **6/6 tests**, and the pump-policy example runs successfully. GitHub Actions runs the test suite and example on Python 3.11 and 3.12; the commands below are also the canonical local verification path.

## Quick start

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
source .venv/bin/activate

pip install -e ".[dev]"
pytest
python examples/pump_demo.py
```

## Repository map

- `src/turtleml/` — reference package for claims, authority, transport, and recursive regions.
- `schemas/abci-envelope.schema.json` — initial machine-readable exchange envelope.
- `examples/pump_demo.py` — end-to-end observer/controller/policy example.
- `tests/` — executable invariants and authority-boundary tests.
- `PROJECT_CHARTER.md`, `ROADMAP.md`, and `docs/` — scope, architecture, and decision records.

## Language strategy

Python is the **reference implementation**, not the architectural boundary. Future turtles may be written in Rust, C, C++, TypeScript, MicroPython, or something else. Interoperability belongs in the ABCI-compatible envelope/schema.

Likely evolution:

- Python — experimentation, ML, simulation, orchestration
- Rust — durable routers, policy services, edge daemons
- C/C++/Rust — constrained hardware and actuators
- JSON Schema initially; Protocol Buffers or CBOR later if justified

## Non-goals for 0.1

No MQTT, LoRa, Meshtastic, BLE, SDR, cameras, LLMs, Kubernetes, cloud control plane, or distributed database yet. Those are adapters. The authority semantics come first.

## Naming

A **Turtle** is a node or bounded region with identity, declared capabilities, local state, local implementation, and an engineered interface to other turtles. A turtle may contain other turtles.

## Related branch

The `provenance-foundation` branch contains the expanded provenance and research record. It is documentation-only and is intentionally not the default runnable branch.

## License

MIT License. See [LICENSE](./LICENSE).
