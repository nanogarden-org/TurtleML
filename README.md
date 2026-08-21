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

## First falsification target

Three logical nodes are enough:

- **Observer** — senses or simulates a condition and emits a claim
- **Controller** — can request an action
- **Policy boundary** — decides whether that action is authorized

The architecture passes its first test only if claims can move between nodes, knowledge does not imply permission, denied actions remain denied, granted authority is scoped and expires, actions can be traced back to claims and decisions, and a node can disappear without collapsing the whole simulation.

## Project status

`0.1.0-alpha` — executable architecture skeleton.

The current implementation is deliberately boring Python. That is a feature: the project is proving semantics before hardware, RF links, LLMs, or optimization.

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -e ".[dev]"
pytest
python examples/pump_demo.py
```

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

## License

MIT License. See `LICENSE`.
