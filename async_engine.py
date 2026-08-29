"""SimpleHandler module."""

import math
import random


class SimpleHandler:
    """Small render_registry helper."""

    def __init__(self, seed: int = 17) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_registry(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 17) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 17


def main() -> None:
    obj = SimpleHandler()
    print(obj.render_registry(17))


if __name__ == "__main__":
    main()
