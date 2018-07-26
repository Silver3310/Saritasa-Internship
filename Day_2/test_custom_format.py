import unittest
from custom_format import check_and_insert as func


class TestCheckAndInsert(unittest.TestCase):

    example = {
        'age': 18,
        'name': 'Alice',
        'city': 'Ufa',
        'email': 'al@m.ru'
    }

    def test_order(self):
        self.assertEqual(func('{name} is {age}, {city}, {email}',
                              self.example), 'Alice is 18, Ufa, al@m.ru')
        self.assertEqual(func('{name} is {age}, {email}, {city}',
                              self.example), 'Alice is 18, al@m.ru, Ufa')
        self.assertEqual(func('{email} - {name} (age: {age}) [{city}]',
                              self.example), 'al@m.ru - Alice (age: 18) [Ufa]')

    def test_fields(self):
        self.assertEqual(func('{imya} is {age}, {gorod}, {pochta}',
                              self.example), '{imya} is 18, {gorod}, {pochta}')
        self.assertEqual(func('{I} {believe} {I} {can} {fly}',
                              self.example), '{I} {believe} {I} {can} {fly}')
        self.assertEqual(func('{mail} - {name} (age: {age}) [{city}]',
                              self.example), '{mail} - Alice (age: 18) [Ufa]')
        self.assertEqual(func('a string without fields', self.example),
                         'a string without fields')

    def test_braces(self):
        self.assertEqual(func('{name} is {age}, }city{, {email}',
                              self.example), 'Alice is 18, }city{, al@m.ru')
        self.assertEqual(func('{name} is {age{ {age}, {city}, {email}',
                              self.example), 'Alice is {age{ 18, Ufa, al@m.ru')
        self.assertRaises(Exception, func, '{name} is {age{, {city}, {email}',
                          self.example)

    def test_types(self):
        self.assertRaises(TypeError, func, True, self.example)
        self.assertRaises(TypeError, func, 123, self.example)
        self.assertRaises(TypeError, func, 123.45, self.example)
        self.assertRaises(TypeError, func, (2 + 3j), self.example)
        self.assertRaises(TypeError, func, self.example)


if __name__ == '__main__':
    unittest.main()
