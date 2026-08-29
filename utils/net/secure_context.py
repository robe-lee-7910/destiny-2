"""AsyncEngine module."""

import math
import random


class AsyncEngine:
    """Small run_buffer helper."""

    def __init__(self, seed: int = 87) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_buffer(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 87) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 87


def main() -> None:
    obj = AsyncEngine()
    print(obj.run_buffer(87))


if __name__ == "__main__":
    main()
