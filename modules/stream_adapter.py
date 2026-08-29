"""AtomicProvider module."""

import math
import random


class AtomicProvider:
    """Small flush_loader helper."""

    def __init__(self, seed: int = 14) -> None:
        self._state = seed
        self._items: list[int] = []

    def flush_loader(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 14) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 14


def main() -> None:
    obj = AtomicProvider()
    print(obj.flush_loader(14))


if __name__ == "__main__":
    main()
