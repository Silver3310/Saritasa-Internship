"""The endless yrange

This module represents a usual iterable yrnage object that starts counting from
the initial element when reaching the end of its sequence, i.e.
1,2,3,4,1,2,3,4,1,2,3,4 etc.
The yrange is implemented through a generator and a class

"""


class YrangeIter:
    """The implementation through a class"""
    def __init__(self, n):
        if n < 0:
            raise AttributeError("N must be positive")

        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
        else:
            i = self.i = 0
        self.i += 1
        return i


def yrange_gen(n):
    """The implementation through a generator"""
    if n < 0:
        raise AttributeError("N must be positive")

    i = 0
    while i < n:
        yield i
        i += 1
    yield from yrange_gen(n)


def yrange_gen_test(n, amount):
    if amount < 0:
        raise AttributeError("Amount must be positive")

    """The function for testing the generator"""
    print("Yrange generator:")
    yrange_g = yrange_gen(n)
    result = list()
    for _ in range(amount):
        result.append(next(yrange_g))
    return result


def yrange_iter_test(n, amount):
    if amount < 0:
        raise AttributeError("Amount must be positive")

    """The function for testing the iterator"""
    print("Yrange iterator:")
    yrange_iter = YrangeIter(n)
    result = list()
    for _ in range(amount):
        result.append(next(yrange_iter))
    return result


def main():
    pass


if __name__ == '__main__':
    main()
