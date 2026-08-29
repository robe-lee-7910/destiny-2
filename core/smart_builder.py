"""HybridCollector module."""

import math
import random


class HybridCollector:
    """Small parse_manager helper."""

    def __init__(self, seed: int = 35) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_manager(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 35) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 35


def main() -> None:
    obj = HybridCollector()
    print(obj.parse_manager(35))


if __name__ == "__main__":
    main()
