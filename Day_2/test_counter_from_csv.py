import unittest
from counter_from_csv import list_counter


class TestListCounter(unittest.TestCase):

    def test_fields(self):

        sample_input = [
            {'a': '1', 'b': '2'},
            {'a': '1', 'b': '3'}
        ]
        sample_output = [
            {'key': 'b', 'value': '2', 'counter': 1},
            {'key': 'b', 'value': '3', 'counter': 1},
            {'key': 'a', 'value': '1', 'counter': 2}
        ]

        # assertCountEqual(a, b) - a and b have the same elements in the same
        #  number, regardless of their order
        self.assertCountEqual(list_counter(sample_input), sample_output)

        diff_fields_input = [
            {'a': '1', 'b': '2'},
            {'a': '1', 'c': '3'}
        ]

        self.assertRaises(KeyError, list_counter, diff_fields_input)


if __name__ == '__main__':
    unittest.main()
