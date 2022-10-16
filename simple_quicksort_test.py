import unittest
import simple_quicksort as mod


class SimpleQuickSortTest(unittest.TestCase):
    def test_int(self):
        a = [4, 2, 1, 6, 3, 9, 5]
        mod.sort(a)
        self.assertListEqual(
            a,
            [1, 2, 3, 4, 5, 6, 9]
        )

    def test_equal_elem(self):
        a = [4, 2, 1, 3, 2, 3, 3]
        mod.sort(a)
        self.assertListEqual(
            a,
            [1, 2, 2, 3, 3, 3, 4]
        )


if __name__ == '__main__':
    unittest.main()
