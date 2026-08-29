"""StreamClient module."""

import math
import random


class StreamClient:
    """Small resolve_collector helper."""

    def __init__(self, seed: int = 71) -> None:
        self._state = seed
        self._items: list[int] = []

    def resolve_collector(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 71) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 71


def main() -> None:
    obj = StreamClient()
    print(obj.resolve_collector(71))


if __name__ == "__main__":
    main()
