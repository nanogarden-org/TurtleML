from __future__ import annotations

from typing import Any

from turtleml.abci.models import AuditEvent, AuthorityGrant, Capability, Claim, NodeIdentity


class TurtleNode:
    def __init__(self, identity: NodeIdentity, capabilities: list[Capability] | None = None) -> None:
        self.identity = identity
        self.capabilities = list(capabilities or [])
        self.claims: list[Claim] = []
        self.grants: list[AuthorityGrant] = []
        self.audit_log: list[AuditEvent] = []

    def emit_claim(self, *, subject: str, assertion: str, confidence: float, provenance: dict[str, Any] | None = None) -> Claim:
        claim = Claim(source_node=self.identity.node_id, subject=subject, assertion=assertion, confidence=confidence, provenance=provenance or {})
        self.claims.append(claim)
        self.audit("claim_created", claim_id=claim.claim_id)
        return claim

    def receive_claim(self, claim: Claim) -> None:
        self.claims.append(claim)
        self.audit("claim_received", claim_id=claim.claim_id, source=claim.source_node)

    def add_grant(self, grant: AuthorityGrant) -> None:
        self.grants.append(grant)
        self.audit("authority_granted", grant_id=grant.grant_id)

    def is_authorized(self, action: str, scope: str) -> bool:
        return any(grant.authorizes(self.identity.node_id, action, scope) for grant in self.grants)

    def audit(self, event_type: str, **details: Any) -> AuditEvent:
        event = AuditEvent(node_id=self.identity.node_id, event_type=event_type, details=details)
        self.audit_log.append(event)
        return event
