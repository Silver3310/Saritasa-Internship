# -*- coding: utf-8 -*-
"""Generator that remembers where to continue

In this module the generator uses cache which is designed to store the data
for all variables. lru-cache from functools wasn't used it required
max_value

Example:

    i1 = integers()

    next(i1)
    1
    next(i1)
    2
    next(i1)
    3

    i2 = integers()

    next(i2)
    4

"""


def memorize(func):
    """The decorator that stores the values the function used"""
    cache = {}

    def memorized(*args):
        if args in cache:
            return cache[args]
        if args not in cache:
            result = func(*args)
            cache[args] = result
            return result
    return memorized


@memorize
def integers():
    """The simple function that increments the value"""
    i = 1
    while True:
        yield i
        i = i + 1


def main():
    i1 = integers()
    print(next(i1))
    print(next(i1))
    print(next(i1))

    i2 = integers()
    print(next(i2))
    print(next(i2))
    print(next(i2))
    print(next(i2))

    i3 = integers()
    print(next(i3))
    print(next(i3))
    print(next(i3))


if __name__ == '__main__':
    main()
