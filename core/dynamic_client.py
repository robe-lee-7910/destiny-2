"""FastFactory module."""

import math
import random


class FastFactory:
    """Small handle_dispatcher helper."""

    def __init__(self, seed: int = 86) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_dispatcher(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 86) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 86


def main() -> None:
    obj = FastFactory()
    print(obj.handle_dispatcher(86))


if __name__ == "__main__":
    main()
