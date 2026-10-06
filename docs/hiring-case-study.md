# TurtleML — engineering case study

## Problem

An AI system can confuse information it receives with permission to act, especially when several nodes exchange claims.

## What I built

I designed an executable architecture skeleton with explicit claims, scoped authority grants, role policy, audit events, and a pump-policy demonstration.

## Constraints

Keep observations and shared claims useful without letting their arrival create authority; expose semantics before adding hardware or networking.

## Decision

Separate Claim, ActionRequest, AuthorityGrant, and policy decision objects; bind grants to actor, action, target, and lifetime.

## Working result and verification

0.1.0-alpha Python reference model demonstrates role-policy decisions, actor/action/target scoping, grant expiry, and simulated node communication.

[Authority tests](../tests/test_authority.py) · [Pump-policy demo](../examples/pump_demo.py)

Recorded 0.1.0-alpha checkpoint: 6/6 tests passed. Run `pytest` and `python examples/pump_demo.py` using the README setup instructions.

## Limits

The current grant model checks scope and expiry; it has no issued-grant revocation mechanism. Capability truthfulness, hostile transport, and recursive authority safety remain architecture challenges. This is not a production distributed security system.

## Applications

AI permission boundaries, policy contracts, distributed workflow design, and failure-case analysis.

## Further reading

Read the [project summary](../README.md), inspect the evidence above, then use the [challenge instructions](../ORIGIN.md#submit-a-useful-challenge).
