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

        t = self.x * 8

        self.assertEqual(
            t.matrix_list,
            [
                [0, 8],
                [8, 16]
            ]
        )

    def test_prefix_minus(self):

        y = -self.x

        self.assertEqual(
            y.matrix_list,
            [
                [0, -1],
                [-1, -2]
            ]
        )

    def test_to_the_power_of(self):

        y = self.x ** 2

        self.assertEqual(
            y.matrix_list,
            [
                [1, 2],
                [2, 5]
            ]
        )

    def test_transposing(self):

        y = Matrix(
            [
                [1, 2],
                [3, 4]
            ]
        )

        y = y.T()

        self.assertEqual(
            y.matrix_list,
            [
                [1, 3],
                [2, 4]
            ]
        )

    def test_transposing_dif_sizes(self):

        y = Matrix(
            [
                [1, 2],
                [3, 4],
                [5, 6]
            ]
        )

        y = y.T()

        self.assertEqual(
            y.matrix_list,
            [
                [1, 3, 5],
                [2, 4, 6]
            ]
        )

    def test_multiplying_dif_sizes(self):

        t = Matrix(
            [
                [2, 3],
                [4, 8],
                [1, 2]
            ]
        )

        t = t * 2

        self.assertEqual(
            t.matrix_list,
            [
                [4, 6],
                [8, 16],
                [2, 4]
            ]
        )

    def test_multiplying_inplace(self):

        t = Matrix(
            [
                [0, 1],
                [1, 2]
            ]
        )

        t *= 8

        self.assertEqual(
            t.matrix_list,
            [
                [0, 8],
                [8, 16]
            ]
        )


if __name__ == '__main__':
    unittest.main()

