import unittest
from .dict_as_object import DictFactory


class TestDict(unittest.TestCase):

    # sample data
    ball_dict = {
        "color": "blue",
        "size": "big",
        "material":
            {
                "rubber": '1',
                "flash":
                    {
                        "first": '11',
                        "second": '22'
                    }
            }
    }

    def test_read_property_true(self):

        ball = DictFactory(
            self.ball_dict,
            read=True
        )

        self.assertEqual(
            str(ball.material.flash.first),
            '11'
        )

    def test_read_property_false(self):

        ball = DictFactory(
            self.ball_dict,
            read=False
        )

        with self.assertRaises(AttributeError):
            print(ball.material.flash.first)

    def test_delete_property_true(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            delete=True
        )

        del ball.material.flash.first

        with self.assertRaises(KeyError):
            print(ball.material.flash.first)

    def test_delete_property_false(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            delete=False
        )

        with self.assertRaises(AttributeError):
            del ball.material.flash.first

    def test_add_property_true(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            add=True
        )

        ball.key = '2'

        self.assertEqual(
            str(ball.key),
            '2'
        )

    def test_add_property_false(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            add=False
        )

        with self.assertRaises(AttributeError):
            ball.key = '2'

    def test_change_property_true(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            change=True
        )

        ball.material.flash.first = '30'

    def test_change_property_false(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            change=False
        )

        with self.assertRaises(AttributeError):
            ball.material.flash.first = '30'

    def test_print_several_values(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
        )

        self.assertEqual(
            str(ball.material),
            '|rubber, flash|'
        )

    def test_print_list(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            add=True
        )

        ball.key = ['attr1', 'attr2']

        self.assertEqual(
            str(ball.key),
            "['attr1', 'attr2']"
        )

    def test_print_default_with_keys(self):

        ball = DictFactory(
            self.ball_dict,
            read=True,
            add=True
        )

        ball.key = 2
        ball.key.new_key = 3

        self.assertEqual(
            str(ball.key),
            '|new_key, 2|'
        )


if __name__ == '__main__':
    unittest.main()