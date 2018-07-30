import unittest
from .transliteration import make_transl, is_rus


class TestMakeTransl(unittest.TestCase):

    def test_en_to_ru(self):
        self.assertEqual(
            make_transl('privet'),
            'привет',
        )
        self.assertEqual(
            make_transl('Klassno!'),
            'Классно!'
        )
        self.assertEqual(
            make_transl('1 Privet mir)))  1'),
            '1 Привет мир)))  1'
        )
        self.assertEqual(
            make_transl('&^%^&(*&'),
            '&^%^&(*&'
        )

    def test_ru_to_en(self):
        self.assertEqual(
            make_transl('приветь'),
            'privet'
        )
        self.assertEqual(
            make_transl('Классно!'),
            'Klassno!'
        )
        self.assertEqual(
            make_transl('1 Привет мир)))  1'),
            '1 Privet mir)))  1'
        )

    def test_is_rus(self):
        self.assertEqual(
            is_rus('Строка на русском'),
            True
        )
        self.assertEqual(
            is_rus('Вроде бы я на русском, almost :)'),
            True
        )
        self.assertEqual(
            is_rus('A string in English'),
            False
        )
        self.assertEqual(
            is_rus('абвgnm'),
            False
        )
        self.assertEqual(
            is_rus('12345'),
            False
        )


if __name__ == '__main__':
    unittest.main()
