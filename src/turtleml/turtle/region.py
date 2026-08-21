from __future__ import annotations

from turtleml.abci.models import Capability, NodeIdentity
from .node import TurtleNode


class TurtleRegion(TurtleNode):
    def __init__(self, identity: NodeIdentity, capabilities: list[Capability] | None = None, children: list[TurtleNode] | None = None) -> None:
        super().__init__(identity, capabilities)
        self.children = list(children or [])

    def add_child(self, node: TurtleNode) -> None:
        self.children.append(node)
        self.audit("child_added", child_node_id=node.identity.node_id)

    def discover_capabilities(self) -> dict[str, list[Capability]]:
        return {child.identity.node_id: list(child.capabilities) for child in self.children}
