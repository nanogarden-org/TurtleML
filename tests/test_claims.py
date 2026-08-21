import pytest

from turtleml.abci.models import NodeIdentity
from turtleml.turtle.node import TurtleNode


def test_receiving_claim_does_not_create_authority() -> None:
    observer = TurtleNode(NodeIdentity("observer", "Observer", "observer"))
    controller = TurtleNode(NodeIdentity("controller", "Controller", "controller"))
    claim = observer.emit_claim(subject="pump-03", assertion="possible_cavitation", confidence=0.87)
    controller.receive_claim(claim)
    assert controller.claims[-1] == claim
    assert controller.grants == []
    assert not controller.is_authorized("stop", "pump-03")


def test_claim_confidence_is_bounded() -> None:
    node = TurtleNode(NodeIdentity("observer", "Observer", "observer"))
    with pytest.raises(ValueError):
        node.emit_claim(subject="x", assertion="y", confidence=1.1)
