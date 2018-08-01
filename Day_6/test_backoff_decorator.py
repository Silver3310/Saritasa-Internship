import unittest
from random import choice
from .backoff_decorator import backoff


class TestFunction(unittest.TestCase):

    def test_func_that_work_until_end(self):

        @backoff(
            exceptions=(KeyError, AttributeError, IndexError),
            max_retry_count=5,
            delay=1
        )
        def random_throw_error(name):
            print('hello {}!'.format(name))
            excepts = (KeyError, AttributeError, IndexError)
            raise choice(excepts)

        random_throw_error('alex')

    def test_func_that_work_properly(self):

        @backoff(
            exceptions=(KeyError, AttributeError, IndexError),
            max_retry_count=5,
            delay=0
        )
        def random_throw_error(name):
            print('hello {}!'.format(name))

        random_throw_error('john')

    def test_func_that_gonna_crush(self):

        @backoff(
            exceptions=(KeyError, AttributeError, IndexError),
            max_retry_count=5,
            delay=0
        )
        def random_throw_error(name):
            print('hello {}!'.format(name))
            raise ArithmeticError

        with self.assertRaises(ArithmeticError):
            random_throw_error('jake')


if __name__ == '__main__':
    unittest.main()