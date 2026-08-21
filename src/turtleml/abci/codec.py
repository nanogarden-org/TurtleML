from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from typing import Any

from .models import Claim, NodeIdentity

PROTOCOL = "TurtleML-ABCI"
PROTOCOL_VERSION = "0.1"


def _json_default(value: Any) -> str:
    if isinstance(value, datetime):
        return value.isoformat()
    raise TypeError(f"cannot encode {type(value)!r}")


def claim_envelope(identity: NodeIdentity, claim: Claim, scope: dict[str, str] | None = None) -> dict[str, Any]:
    return {
        "protocol": PROTOCOL,
        "version": PROTOCOL_VERSION,
        "message_type": "claim",
        "message_id": claim.claim_id,
        "source": asdict(identity),
        "subject": claim.subject,
        "payload": {"assertion": claim.assertion, "confidence": claim.confidence},
        "provenance": claim.provenance,
        "scope": scope or {},
        "authority": None,
        "timestamp": claim.timestamp.isoformat(),
    }


def dumps(envelope: dict[str, Any]) -> str:
    return json.dumps(envelope, default=_json_default, sort_keys=True)
