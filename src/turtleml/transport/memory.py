from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any

Handler = Callable[[dict[str, Any]], None]


class InMemoryBus:
    """Synchronous transport used only to test protocol behavior."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Handler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: Handler) -> None:
        self._subscribers[topic].append(handler)

    def publish(self, topic: str, envelope: dict[str, Any]) -> None:
        for handler in list(self._subscribers[topic]):
            handler(envelope)
