"""This Chain module

This module represents the generator and class that concatenate
different sequences so that they're in one list

Example:
    a = [‘a’, ‘b’, ‘c’]
    b = (i ** 2 for i in range(5))
    c = range(10)

    # func implementation
    d = chain(a, b, c)
    # class implementation
    d = Chain(a, b, c)
    print(list(d))
    ['a', 'b', 'c', 0, 1, 4, 9, 16, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


"""


class Chain:
    def __init__(self, *args):
        self.i = 0
        self.args = args

    def __iter__(self):
        for i in range(len(self.args)):
            yield from chain_gen(self.args[i])


def chain_gen(*args):
    for iter_ in args:
        for i in iter_:
            yield i


def main():
    pass


if __name__ == '__main__':
    main()
