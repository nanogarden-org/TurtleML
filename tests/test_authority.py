from datetime import timedelta

from turtleml.abci.models import ActionRequest, NodeIdentity
from turtleml.abci.policy import PolicyEngine


def test_unpermitted_role_is_denied() -> None:
    identity = NodeIdentity("observer", "Observer", "observer")
    request = ActionRequest(requesting_node="observer", target="pump-03", action="stop")
    decision = PolicyEngine({"controller": {"stop"}}).evaluate(identity, request)
    assert not decision.allowed
    assert decision.grant is None


def test_grant_is_scoped_to_actor_action_and_target() -> None:
    identity = NodeIdentity("controller", "Controller", "controller")
    request = ActionRequest(requesting_node="controller", target="pump-03", action="reduce_speed")
    decision = PolicyEngine({"controller": {"reduce_speed"}}).evaluate(identity, request)
    assert decision.allowed
    grant = decision.grant
    assert grant is not None
    assert grant.authorizes("controller", "reduce_speed", "pump-03")
    assert not grant.authorizes("controller", "stop", "pump-03")
    assert not grant.authorizes("other-node", "reduce_speed", "pump-03")
    assert not grant.authorizes("controller", "reduce_speed", "pump-99")


def test_grant_expires() -> None:
    identity = NodeIdentity("controller", "Controller", "controller")
    request = ActionRequest(requesting_node="controller", target="pump-03", action="reduce_speed", requested_duration_seconds=1)
    grant = PolicyEngine({"controller": {"reduce_speed"}}).evaluate(identity, request).grant
    assert grant is not None
    after_expiry = grant.expires_at + timedelta(microseconds=1)
    assert not grant.valid_at(after_expiry)
