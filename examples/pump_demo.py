from turtleml.abci.models import ActionRequest, Capability, CapabilityType, NodeIdentity
from turtleml.abci.policy import PolicyEngine
from turtleml.turtle.node import TurtleNode

observer = TurtleNode(NodeIdentity("basement-01", "Basement Observer", "environmental_observer"), [Capability("vibration", CapabilityType.SENSE, "Pump vibration sensor"), Capability("anomaly_model", CapabilityType.COMPUTE, "Local anomaly classifier")])
controller = TurtleNode(NodeIdentity("pump-control-01", "Pump Controller", "pump_controller"), [Capability("pump_speed_control", CapabilityType.ACTUATE, "Variable-speed control")])

claim = observer.emit_claim(subject="pump-03", assertion="possible_cavitation", confidence=0.87, provenance={"sensor": "vibration-01", "model": "pump-anomaly-v3"})
controller.receive_claim(claim)

print(f"Received claim: {claim.assertion} ({claim.confidence:.0%})")
print("Authorized before policy decision:", controller.is_authorized("reduce_speed", "pump-03"))

request = ActionRequest(requesting_node=controller.identity.node_id, target="pump-03", action="reduce_speed", reason_claim_id=claim.claim_id, requested_duration_seconds=30)
policy = PolicyEngine(role_permissions={"pump_controller": {"reduce_speed"}})
decision = policy.evaluate(controller.identity, request)
print("Policy decision:", "ALLOW" if decision.allowed else "DENY", "-", decision.reason)

if decision.grant is not None:
    controller.add_grant(decision.grant)

print("Authorized after policy decision:", controller.is_authorized("reduce_speed", "pump-03"))
