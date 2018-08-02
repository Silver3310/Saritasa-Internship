"""Backoff decorator

This module demonstrates a backoff decorator that allows you to retry the
particular function until it works without raising any given exception.
You also can specify a period of time between repeated calls and a maximum
amount or calls.
In this module, the backoff decorator is used in conjunction with the
random_throw_error function that welcomes and throws an exception randomly

"""


from time import sleep
from random import choice


def backoff(exceptions, max_retry_count=3, delay=0):
    """The decorator itself, it takes the decorator's attributes"""
    def parameters(func):
        """The function in which we specify the given function

        We already know the parameters we need

        """
        def retry_func(*args):
            """The function that retries the given function"""
            # for the specified amount of times
            for _ in range(max_retry_count):
                try:
                    func(*args)
                    print("the function didn't raise any given exception")
                    # so we can break the loop, we no longer need to go through
                    break
                except exceptions as e:
                    # notify a user of this problem
                    print(e)
                    # wait for a specified amount of time
                    sleep(delay)

        return retry_func

    return parameters


@backoff(
    exceptions=(KeyError, AttributeError, IndexError),
    max_retry_count=2,
    delay=2
)
def random_throw_error(name):
    """A random function, used to show how the backoff decorator works"""
    print('hello {}!'.format(name))
    excepts = (KeyError, AttributeError, IndexError)
    # throw any given exception randomly
    raise choice(excepts)


def main():
    random_throw_error('alex')


if __name__ == '__main__':
    main()
