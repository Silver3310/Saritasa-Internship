import unittest
from .chain_gen import chain_gen, Chain


class TestChain(unittest.TestCase):

    def test_chain_gen_valid(self):

        a = ['a', 'b', 'c']
        b = (i ** 2 for i in range(5))
        c = range(10)

        self.assertEqual(
            list(chain_gen(a, b, c)),
            ['a', 'b', 'c', 0, 1, 4, 9, 16, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def test_chain_class_valid(self):

        a = ['a', 'b', 'c']
        b = (i ** 2 for i in range(5))
        c = range(10)

        self.assertEqual(
            list(Chain(a, b, c)),
            ['a', 'b', 'c', 0, 1, 4, 9, 16, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )


if __name__ == '__main__':
    unittest.main()
