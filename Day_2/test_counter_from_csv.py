import unittest
from counter_from_csv import list_counter as func


class TestListCounter(unittest.TestCase):

    def test_fields(self):
        sample_input = [{'a': '1', 'b': '2'},
                        {'a': '1', 'b': '3'}]
        sample_output = [{'key': 'b', 'value': '2', 'counter': 1},
                         {'key': 'b', 'value': '3', 'counter': 1},
                         {'key': 'a', 'value': '1', 'counter': 2}]
        # assertCountEqual(a, b) - a and b have the same elements in the same
        #  number, regardless of their order
        self.assertCountEqual(func(sample_input), sample_output)

        diff_types_input = [{'a': True, 'b': 1, 'c': 'str'},
                            {'a': False, 'b': 1, 'c': 'trs'},
                            {'a': True, 'b': 3, 'c': 'str'}]
        diff_types_output = [{'key': 'a', 'value': False, 'counter': 1},
                             {'key': 'a', 'value': True, 'counter': 2},
                             {'key': 'c', 'value': 'str', 'counter': 2},
                             {'key': 'c', 'value': 'trs', 'counter': 1},
                             {'key': 'b', 'value': 1, 'counter': 2},
                             {'key': 'b', 'value': 3, 'counter': 1}]
        self.assertCountEqual(func(diff_types_input), diff_types_output)

        diff_values_input = [{'a': True, 'b': 1, 'c': 'str'},
                             {'a': 1, 'b': False, 'c': 'trs'},
                             {'a': True, 'b': 3, 'c': 4}]
        diff_values_output = [{'key': 'a', 'value': True, 'counter': 3},
                              {'key': 'c', 'value': 4, 'counter': 1},
                              {'key': 'c', 'value': 'str', 'counter': 1},
                              {'key': 'c', 'value': 'trs', 'counter': 1},
                              {'key': 'b', 'value': False, 'counter': 1},
                              {'key': 'b', 'value': 1, 'counter': 1},
                              {'key': 'b', 'value': 3, 'counter': 1}]

        self.assertCountEqual(func(diff_values_input), diff_values_output)

        diff_fields_input = [{'a': '1', 'b': '2'},
                             {'a': '1', 'c': '3'}]
        self.assertRaises(KeyError, func, diff_fields_input)

    def test_types(self):
        self.assertRaises(TypeError, func, 'string')
        self.assertRaises(TypeError, func, True)
        self.assertRaises(TypeError, func, 123)
        self.assertRaises(TypeError, func, 123.45)
        self.assertRaises(TypeError, func, (2 + 3j))
        self.assertRaises(TypeError, func)


if __name__ == '__main__':
    unittest.main()
