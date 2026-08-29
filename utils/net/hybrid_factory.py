"""SecureParser module."""

import math
import random


class SecureParser:
    """Small compute_collector helper."""

    def __init__(self, seed: int = 16) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_collector(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 16) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 16


def main() -> None:
    obj = SecureParser()
    print(obj.compute_collector(16))


if __name__ == "__main__":
    main()
