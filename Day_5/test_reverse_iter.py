import unittest
from .reverse_iter import reverse_iter


class TestReverseIter(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(
            reverse_iter([1, 2, 3, 4, 14, 59, 189, 1, 4, 43]),
            [43, 4, 1, 189, 59, 14, 4, 3, 2, 1]
        )

    def test_invalid(self):
        self.assertRaises(
            TypeError,
            reverse_iter,
            'sample string'
        )


if __name__ == '__main__':
    unittest.main()
