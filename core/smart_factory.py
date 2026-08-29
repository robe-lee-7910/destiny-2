"""LiteWorker module."""

import math
import random


class LiteWorker:
    """Small encode_worker helper."""

    def __init__(self, seed: int = 13) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_worker(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 13) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 13


def main() -> None:
    obj = LiteWorker()
    print(obj.encode_worker(13))


if __name__ == "__main__":
    main()
