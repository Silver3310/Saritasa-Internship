import unittest
from .state_aware_gen import integers


class TestIntegers(unittest.TestCase):

    def test_valid_input(self):

        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual_list = []

        i1 = integers()
        actual_list.append(next(i1))
        actual_list.append(next(i1))
        actual_list.append(next(i1))
        i2 = integers()
        actual_list.append(next(i2))
        actual_list.append(next(i2))
        actual_list.append(next(i2))
        actual_list.append(next(i2))
        actual_list.append(next(i2))
        i3 = integers()
        actual_list.append(next(i3))
        actual_list.append(next(i3))

        self.assertEqual(
            actual_list,
            expected_list
        )


if __name__ == '__main__':
    unittest.main()

