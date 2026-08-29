"""StreamResolver module."""

import math
import random


class StreamResolver:
    """Small dispatch_worker helper."""

    def __init__(self, seed: int = 90) -> None:
        self._state = seed
        self._items: list[int] = []

    def dispatch_worker(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 90) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 90


def main() -> None:
    obj = StreamResolver()
    print(obj.dispatch_worker(90))


if __name__ == "__main__":
    main()
