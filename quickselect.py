"""Quickselect

Get the k smallest items from a list.
The pivot is the last element of the selected range.
"""


def select(items: list, k: int, key=lambda x: x):
    _recursive_select(items, k, 0, len(items) - 1, key)
    return items[:k]


def _recursive_select(items, k, begin, end, key):
    if begin >= end:
        return

    partition = _partition(items, begin, end, key)
    if partition > k - 1:
        _recursive_select(items, k, begin, partition - 1, key)
    if partition < k - 1:
        _recursive_select(items, k, partition + 1, end, key)


def _partition(items, begin, end, key) -> int:
    i = begin
    for j in range(begin, end + 1):
        if key(items[j]) <= key(items[end]):
            _swap(items, i, j)
            i += 1
    return i - 1


def _swap(items, idx_1, idx_2):
    tmp = items[idx_1]
    items[idx_1] = items[idx_2]
    items[idx_2] = tmp
