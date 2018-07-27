import unittest
from custom_format import check_and_insert


class TestCheckAndInsert(unittest.TestCase):

    example = {
        'age': 18,
        'name': 'Alice',
        'city': 'Ufa',
        'email': 'al@m.ru'
    }

    def test_valid(self):

        self.assertEqual(
            check_and_insert(
                '{name} is {age}, {email}, {city}',
                self.example),
            'Alice is 18, al@m.ru, Ufa'
            )

    def test_invalid_placeholder(self):
        self.assertEqual(
            check_and_insert(
                '{imya} is {age}, {gorod}, {pochta}',
                self.example),
            'Your template is invalid')

    def test_invalid_braces(self):
        self.assertEqual(
            check_and_insert(
                '{name} is {email{',
                self.example),
            'Your template is invalid')


if __name__ == '__main__':
    unittest.main()
