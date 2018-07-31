import unittest
from .yrange import yrange_gen_test, yrange_iter_test


class TestYrange(unittest.TestCase):

    def test_gen_valid(self):
        self.assertEqual(
            yrange_gen_test(4, 10),
            [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
        )

    def test_iter_valid(self):
        self.assertEqual(
            yrange_iter_test(4, 10),
            [0, 1, 2, 3, 0, 1, 2, 3, 0, 1]
        )

    def test_gen_n_negative(self):
        self.assertRaises(
            AttributeError,
            yrange_gen_test,
            -3, 2
        )

    def test_gen_amount_negative(self):
        self.assertRaises(
            AttributeError,
            yrange_gen_test,
            3, -2
        )

    def test_iter_n_negative(self):
        self.assertRaises(
            AttributeError,
            yrange_iter_test,
            -3, 2
        )

    def test_iter_amount_negative(self):
        self.assertRaises(
            AttributeError,
            yrange_iter_test,
            3, -2
        )


if __name__ == '__main__':
    unittest.main()
