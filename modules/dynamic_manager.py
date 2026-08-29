"""SimpleService module."""

import math
import random


class SimpleService:
    """Small fetch_worker helper."""

    def __init__(self, seed: int = 3) -> None:
        self._state = seed
        self._items: list[int] = []

    def fetch_worker(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 3) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 3


def main() -> None:
    obj = SimpleService()
    print(obj.fetch_worker(3))


if __name__ == "__main__":
    main()
