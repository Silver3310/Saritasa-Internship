import unittest
from .Matrix import Matrix


class TestMatrx(unittest.TestCase):

    x = Matrix([[0, 1], [1, 2]])

    z = Matrix([[2, 3], [4, 5]])

    def test_size(self):

        self.assertEqual(
            self.x.size,
            (2, 2)
        )

    def test_sum(self):

        y = self.x + self.z

        self.assertEqual(
            y,
            [[2, 4], [5, 7]]
        )



