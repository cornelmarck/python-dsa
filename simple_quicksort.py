"""Simple quicksort with non-random partioning"""


def sort(items: list, key=lambda x: x):
    _recursive_sort(items, 0, len(items) - 1, key)


def _recursive_sort(items, begin, end, key):
    if begin >= end:
        return

    partition = _partition(items, begin, end, key)
    _recursive_sort(items, begin, partition - 1, key)
    _recursive_sort(items, partition + 1, end, key)


def _partition(items, begin, end, key) -> int:
    i = begin
    for j in range(begin, end):
        if key(items[j]) <= key(items[end]):
            _swap(items, i, j)
            i += 1
    return i - 1


def _swap(items, idx_1, idx_2):
    tmp = items[idx_1]
    items[idx_1] = items[idx_2]
    items[idx_2] = tmp
