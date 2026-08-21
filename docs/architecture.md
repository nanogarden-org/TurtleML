# TurtleML Architecture

## 1. System model

TurtleML models a distributed environment as recursively composable bounded nodes.

```text
                 Turtle Region
                      |
           +----------+----------+
           |          |          |
        Turtle A   Turtle B   Turtle C
        observer   cognition   control
           |          |          |
        sensors     models    actuators
```

A region can itself expose a boundary and participate as a turtle in a larger region.

## 2. The semantic pipeline

The project deliberately refuses to collapse these stages:

```text
signal
  -> feature
  -> inference
  -> claim
  -> validation/policy
  -> authority grant
  -> action
  -> audit
```

A transition may stop at any stage.

## 3. ABCI-compatible boundary

For TurtleML, the initial ABCI-style envelope carries protocol/version, message type/ID, source identity, role, subject, payload, provenance, scope, authority reference if any, and timestamp. The boundary describes meaning, not implementation.

## 4. Claims

A Claim is an epistemic object. It can be stored, forwarded, challenged, combined, or ignored. It is not an actuator command.

## 5. Authority

An AuthorityGrant is a control object binding actor + action + scope + issue time + expiry time.

## 6. Recursive regions

A TurtleRegion aggregates children but does not require knowledge of each child's internal implementation. The parent may ask what capabilities are currently available instead of requiring exact hardware/model/runtime details.

## 7. Transports

Transport is deliberately below the trust semantics. The same conceptual envelope should eventually travel over Ethernet, Wi-Fi, MQTT, WebSocket, BLE, LoRa/Meshtastic gateways, or serial links. Reliable transport does not make a claim true, and authenticated transport does not by itself authorize an action.

## 8. Reference implementation boundary

Python is used to make the model cheap to change and easy to inspect. The protocol must not require Python.
