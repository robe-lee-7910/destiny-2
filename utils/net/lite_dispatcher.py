"""CoreController module."""

import math
import random


class CoreController:
    """Small render_loader helper."""

    def __init__(self, seed: int = 22) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_loader(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 22) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 22


def main() -> None:
    obj = CoreController()
    print(obj.render_loader(22))


if __name__ == "__main__":
    main()
