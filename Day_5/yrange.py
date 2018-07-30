"""The endless yrange

This module represents a usual iterable yrnage object that starts counting from
the initial element when reaching the end of its sequence, i.e.
1,2,3,4,1,2,3,4,1,2,3,4 etc.
The yrange is implemented through a generator and a class

"""


class YrangeIter:
    """The implementation through a class"""
    def __init__(self, n):
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
    i = 0
    while i < n:
        yield i
        i += 1
    yield from yrange_gen(n)


def main():
    print("Yrange iterator:")
    yrange_iter = YrangeIter(4)
    for _ in range(10):
        print(next(yrange_iter))

    print()

    print("Yrange generator:")
    yrange_g = yrange_gen(4)
    for _ in range(10):
        print(next(yrange_g))


if __name__ == '__main__':
    main()
