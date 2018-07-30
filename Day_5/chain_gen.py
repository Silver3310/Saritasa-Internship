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
        self.common_list = []
        # here we put all the elements from args into our common list
        for iter_ in args:
            for i in iter_:
                self.common_list.append(i)
        # get the size of the created list
        self.size = len(self.common_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.size:
            i = self.i
            self.i += 1
            return self.common_list[i]
        else:
            raise StopIteration


def chain_gen(*args):
    for iter_ in args:
        for i in iter_:
            yield i


def main():
    a = ['a', 'b', 'c']
    b = (i ** 2 for i in range(5))
    c = range(10)
    d = chain_gen(a, b, c)
    print(list(d))

    # recreating a dictionary (since it was exhausted above)
    b = (i ** 2 for i in range(5))
    e = Chain(a, b, c)
    print(list(e))


if __name__ == '__main__':
    main()
