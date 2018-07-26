import unittest
from transliteration import make_transl, is_rus


class TestMakeTransl(unittest.TestCase):

    def test_en_to_ru(self):
        self.assertEqual(make_transl('privet'), 'привет')
        self.assertEqual(make_transl('Klassno!'), 'Классно!')
        self.assertEqual(make_transl('1 Privet mir)))  1'),
                         '1 Привет мир)))  1')
        self.assertEqual(make_transl('&^%^&(*&'), '&^%^&(*&')

    def test_ru_to_en(self):
        self.assertEqual(make_transl('привет'), 'privet')
        self.assertEqual(make_transl('Классно!'), 'Klassno!')
        self.assertEqual(make_transl('1 Привет мир)))  1'),
                         '1 Privet mir)))  1')

    def test_types(self):
        self.assertRaises(TypeError, make_transl, 423)
        self.assertRaises(TypeError, make_transl, 234.23)
        self.assertRaises(TypeError, make_transl, (2 + 5j))
        self.assertRaises(TypeError, make_transl, True)
        self.assertRaises(TypeError, make_transl)

    def test_is_rus(self):
        self.assertEqual(is_rus('Строка на русском'), True)
        self.assertEqual(is_rus('Вроде бы я на русском, almost :)'), True)
        self.assertEqual(is_rus('A string in English'), False)
        self.assertEqual(is_rus('абвgnm'), False)
        self.assertEqual(is_rus('12345'), False)

    def test_is_rus_types(self):
        self.assertRaises(TypeError, is_rus, 423)
        self.assertRaises(TypeError, is_rus, 234.23)
        self.assertRaises(TypeError, is_rus, (2 + 5j))
        self.assertRaises(TypeError, is_rus, True)
        self.assertRaises(TypeError, is_rus)


if __name__ == '__main__':
    unittest.main()
