from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class CapabilityType(str, Enum):
    SENSE = "sense"
    COMPUTE = "compute"
    STORE = "store"
    COMMUNICATE = "communicate"
    ACTUATE = "actuate"


@dataclass(frozen=True, slots=True)
class Capability:
    name: str
    type: CapabilityType
    description: str = ""


@dataclass(frozen=True, slots=True)
class NodeIdentity:
    node_id: str
    name: str
    role: str


@dataclass(frozen=True, slots=True)
class Claim:
    source_node: str
    subject: str
    assertion: str
    confidence: float
    provenance: dict[str, Any] = field(default_factory=dict)
    claim_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=utcnow)

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")


@dataclass(frozen=True, slots=True)
class ActionRequest:
    requesting_node: str
    target: str
    action: str
    reason_claim_id: str | None = None
    requested_duration_seconds: int = 30
    request_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self) -> None:
        if self.requested_duration_seconds <= 0:
            raise ValueError("requested_duration_seconds must be positive")


@dataclass(frozen=True, slots=True)
class AuthorityGrant:
    actor: str
    action: str
    scope: str
    issued_at: datetime
    expires_at: datetime
    grant_id: str = field(default_factory=lambda: str(uuid4()))

    def valid_at(self, moment: datetime | None = None) -> bool:
        moment = moment or utcnow()
        return self.issued_at <= moment < self.expires_at

    def authorizes(self, actor: str, action: str, scope: str, moment: datetime | None = None) -> bool:
        return self.actor == actor and self.action == action and self.scope == scope and self.valid_at(moment)


@dataclass(frozen=True, slots=True)
class AuditEvent:
    node_id: str
    event_type: str
    details: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=utcnow)
