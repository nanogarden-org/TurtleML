from turtleml.abci.models import Capability, CapabilityType, NodeIdentity
from turtleml.turtle.node import TurtleNode
from turtleml.turtle.region import TurtleRegion


def test_region_discovers_child_capabilities_without_internal_details() -> None:
    sensor = TurtleNode(NodeIdentity("sensor-1", "Sensor", "observer"), [Capability("temperature", CapabilityType.SENSE)])
    controller = TurtleNode(NodeIdentity("controller-1", "Controller", "controller"), [Capability("relay", CapabilityType.ACTUATE)])
    room = TurtleRegion(NodeIdentity("room-1", "Mechanical Room", "region"), children=[sensor, controller])
    discovered = room.discover_capabilities()
    assert discovered["sensor-1"][0].name == "temperature"
    assert discovered["controller-1"][0].name == "relay"
