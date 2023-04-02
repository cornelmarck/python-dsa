import unittest
from heap import Heap

class HeapTest(unittest.TestCase):
    def test_insert(self):
        heap = Heap()
        for i in [3, 1, 5, 4, 7]:
            heap.insert(i)
        self.assertEqual(
            [1, 3, 4, 5, 7],
            heap.items
        )
    
    def test_pop(self):
        heap = Heap()
        for i in [3, 1, 5, 4, 7]:
            heap.insert(i)
        
        result = []
        while heap:
            result.append(heap.pop())
        self.assertEqual(
            [7, 5, 4, 3, 1],
            result
        )


if __name__ == "__main__":
    unittest.main()

