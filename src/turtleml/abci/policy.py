from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta

from .models import ActionRequest, AuthorityGrant, NodeIdentity, utcnow


@dataclass(frozen=True, slots=True)
class PolicyDecision:
    allowed: bool
    reason: str
    grant: AuthorityGrant | None = None


class PolicyEngine:
    """Explicit policy engine for the TurtleML 0.1 reference model."""

    def __init__(self, role_permissions: dict[str, set[str]] | None = None) -> None:
        self.role_permissions = role_permissions or {}

    def evaluate(self, identity: NodeIdentity, request: ActionRequest) -> PolicyDecision:
        allowed_actions = self.role_permissions.get(identity.role, set())

        if request.requesting_node != identity.node_id:
            return PolicyDecision(False, "requesting node does not match evaluated identity")

        if request.action not in allowed_actions:
            return PolicyDecision(False, f"role {identity.role!r} is not permitted to perform {request.action!r}")

        issued = utcnow()
        grant = AuthorityGrant(actor=identity.node_id, action=request.action, scope=request.target, issued_at=issued, expires_at=issued + timedelta(seconds=request.requested_duration_seconds))
        return PolicyDecision(True, "explicit role policy granted authority", grant)
