"""Heap

By default, this is a min-heap
"""
import abc
from typing import Callable, List, Optional, Self, TypeVar, Protocol


class Comparable(Protocol):
    def __lt__(self, other: 'Comparable') -> bool:
        pass

T = TypeVar('T')
K = TypeVar['C', Comparable]

class Heap:
    def __init__(
        self,
        items: Optional[List[T]] = None,
        key: Optional[Callable[[T], Comparable]] = None
    ) -> None:
        self.items = items if items else list()
        self.key = key if key else lambda x: x

    def insert(self: Self, item: T) -> None:
        self.items.append(item)
        self._swim(len(self.items) - 1)

    def pop(self) -> T:
        self._swap(0, len(self.items) - 1)
        self._sink(0)
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def _swap(self: Self, i: int, j: int) -> None:
        tmp = self.items[i]
        self.items[i] = self.items[j]
        self.items[j] = tmp

    def _eval(self: Self, i: int):
        return self.key(self.items[i])

    def _swim(self: Self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self._eval(parent) < self._eval(i):
                break
            self._swap(parent, i)
            i = parent

    def _sink(self, i: int) -> None:
        while 2 * (i + 1) <= len(self.items):
            j = 2 * i + 1
            if (
                j + 1 < len(self.items)
                and self._eval(j + 1) < self._eval(j)
            ):
                j += 1
            if self._eval(j) < self._eval(i):
                break
            self._swap(i, j)
            i = j
