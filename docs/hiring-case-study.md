# TurtleML — engineering case study

## Problem

An AI system can confuse information it receives with permission to act, especially when several nodes exchange claims.

## Contribution

Designed an executable architecture skeleton with explicit claims, scoped authority grants, role policy, audit events, and a pump-policy demonstration. This is an author-owned portfolio account of the work; repository history and attribution records provide the inspectable contribution trail. It does not imply independent external validation.

## Constraints

Keep observations and shared claims useful without letting their arrival create authority; expose semantics before adding hardware or networking.

## Decision

Separate Claim, ActionRequest, AuthorityGrant, and policy decision objects; bind grants to actor, action, target, and lifetime.

## Working result and verification

0.1.0-alpha Python reference model demonstrates role-policy decisions, actor/action/target scoping, grant expiry, and simulated node communication.

[Authority tests](tests/test_authority.py) · [Pump-policy demo](examples/pump_demo.py)

The README records a prior 6/6-test checkpoint. Inspect the tests and rerun the quick-start commands to assess the present checkout; this pass does not refresh that result.

## Limits

Revocation of already-issued grants is not demonstrated by the current grant model. Capability truthfulness, hostile transport, and recursive authority safety remain architecture challenges. This is not a production distributed security system.

## Business application

AI permission boundaries, policy contracts, distributed workflow design, and failure-case analysis. These are relevant applications of the demonstrated design skills, not claims of deployed client outcomes or measured savings.

## Review path

Read the [project summary](../README.md), inspect the evidence above, then use the [challenge instructions](../ORIGIN.md#submit-a-useful-challenge).
