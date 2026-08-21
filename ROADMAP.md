# TurtleML Roadmap

## 0.1 — Executable semantics

Goal: prove the architecture without hardware.

- ABCI envelope model
- identities and roles
- capability manifests
- claims and provenance
- action requests
- policy evaluation
- scoped/expiring authority
- audit events
- recursive TurtleRegion
- in-memory transport
- pump demo
- invariant tests

## 0.2 — Networked turtles

Goal: separate process boundaries.

- async message bus abstraction
- MQTT adapter
- WebSocket or HTTP adapter
- node discovery
- replay protection
- envelope signing interface
- persistent audit log
- failure/rejoin simulation

## 0.3 — Burger King hardware proof

Goal: heterogeneous off-the-shelf nodes.

Suggested minimum:

- Node A: PC/SBC running Python
- Node B: ESP32 or equivalent sensor node
- Node C: relay/actuator simulator or safe low-voltage actuator

Tests: capability discovery, claim exchange, policy denial, policy grant, grant expiration, node loss, and transport substitution.

## 0.4 — Edge intelligence adapters

- TinyML classifier adapter
- ONNX Runtime adapter
- local SLM/LLM tool adapter
- audio/wake-word adapter
- vision claim producer
- confidence/calibration metadata

## 0.5 — Resilient transports

- BLE adapter
- LoRa/Meshtastic gateway
- store-and-forward queue
- degraded-mode policies
- transport trust explicitly separated from identity trust

## 0.6 — Recursive federation

- room turtle
- building turtle
- property turtle
- capability aggregation
- delegated authority
- cross-region policy
- revocation propagation
- conflicting-claim handling

## Later questions

- signed claims and hardware-rooted identities
- capability negotiation
- semantic versioning for ABCI
- graph-based provenance
- Byzantine or malicious nodes
- policy language
- human override
- safety cases
- formal verification of critical invariants
- Rust reference router
