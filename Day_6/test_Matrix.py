import unittest
from .Matrix import Matrix


class TestMatrix(unittest.TestCase):

    x = Matrix(
        [
            [0, 1],
            [1, 2]
        ]
    )

    z = Matrix(
        [
            [2, 3],
            [4, 5]
        ]
    )

    def test_size(self):

        self.assertEqual(
            self.x.size,
            (2, 2)
        )

    def test_sum(self):

        y = self.x + self.z

        self.assertEqual(
            y.matrix_list,
            [
                [2, 4],
                [5, 7]
            ]
        )

    def test_iadd(self):

        self.x += self.x

        self.assertEqual(
            self.x.matrix_list,
            [
                [0, 2],
                [2, 4]
            ]
        )

    def test_multiplying(self):

        self.x * 4

        self.assertEqual(
            self.x.matrix_list,
            [
                [0, 8],
                [8, 64]
            ]
        )

    def test_prefix_minus(self):

        y = -self.x

        self.assertEqual(
            y,
            [
                [0, -2],
                [-2, -4]
            ]
        )

    def test_to_the_power_of(self):

        y = self.x ** 2

        self.assertEqual(
            y,
            [
                [4, 8],
                [8, 20]
            ]
        )

    def test_transposing(self):

        y = [
            [1, 2],
            [3, 4]
        ]

        self.assertEqual(
            y,
            [
                [1, 3],
                [2, 4]
            ]
        )