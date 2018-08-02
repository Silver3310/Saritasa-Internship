from itertools import chain


class Matrix:

    def __init__(self, init_list):

        self.matrix_list = init_list

        self.size = (
            len(init_list[0]),
            len(init_list)
        )

    def __add__(self, other):
        self_flatten = [item for items in self.matrix_list for item in items]
        other_flatten = [item for items in other.matrix_list for item in items]
        
        return Matrix([x + y for x, y in zip(self_flatten, other_flatten)])

    def __iadd__(self, other):
        self.__add__(other)
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            self.matrix_list = [
                self.matrix_list[i][j] * other
                for i in range(self.size[0])
                for j in range(self.size[1])
            ]


def main():
    x = Matrix(
        [
            [0, 1],
            [1, 2],
            [5, 6]
        ]
    )

    print(x.size)

    y = Matrix(
        [
            [0, 1],
            [2, 3]
        ]
    )

    z = Matrix(
        [
            [5, 6],
            [7, 8]
        ]
    )

    t = y + z

    print()
    print(t.matrix_list)
    print()
    print(y.matrix_list)
    print()
    print(z.matrix_list)

    t += z

    print()
    print(t)
    print()
    print(z)




if __name__ == '__main__':
    main()
