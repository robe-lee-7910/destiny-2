"""HybridResolver module."""

import math
import random


class HybridResolver:
    """Small flush_session helper."""

    def __init__(self, seed: int = 10) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_session(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 10) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 10


def main() -> None:
    obj = HybridResolver()
    print(obj.flush_session(10))


if __name__ == "__main__":
    main()
