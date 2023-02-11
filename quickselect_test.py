import unittest
import quickselect as mod


class QuickSelectTest(unittest.TestCase):
    a = [4, 2, 1, 6, 3, 9, 5]

    def test_empty(self):
        self.assertEqual(
            set(mod.select(self.a, 3)),
            set([1, 2, 3])
        )


if __name__ == '__main__':
    unittest.main()
