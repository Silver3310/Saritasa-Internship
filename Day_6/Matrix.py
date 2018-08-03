""" Matrix

This modules represents the module class that can do the following:

    - summing or substructions
    - multiplication of two matrix
    - multiplication of matrix and a number
    - matrix transposing
    - inplace operations
    - dimensions check


"""


class Matrix:

    def __init__(self, init_list):
        """The constructor that takes a list as an inut

        Example:
            Matrix([[1,2],[3,4]])

        """

        self.__matrix_list = init_list

        self.__size = (
            len(init_list[0]),
            len(init_list)
        )

    @property
    def size(self):
        return self.__size

    @property
    def matrix_list(self):
        return self.__matrix_list

    def __add__(self, other):
        """Add two matrices"""

        if self.size != other.size:
            raise ValueError("Matrices aren't equal by size!")

        new_matrix = list()
        for i in range(self.size[1]):
            new_matrix.append(list())
            for j in range(self.size[0]):
                new_matrix[i].append(
                    self.matrix_list[i][j] + other.matrix_list[i][j]
                )
        
        return Matrix(new_matrix)

    def __iadd__(self, other):
        """in-place implementation for add"""
        return self.__add__(other)

    def __mul__(self, other):
        """Multiply two matrices"""

        new_matrix = list()

        # if we have an integer
        if isinstance(other, int):

            for i in range(self.size[1]):
                new_matrix.append(list())
                for j in range(self.size[0]):
                    new_matrix[i].append(
                        self.matrix_list[i][j] * other
                    )

        # if we have a matrix
        if isinstance(other, Matrix):

            for i in range(self.size[1]):
                new_matrix.append(list())
                for j in range(self.size[0]):
                    new_matrix[i].append(0)
                    for k in range(self.size[1]):
                        new_matrix[i][j] += \
                            self.matrix_list[i][k] * other.matrix_list[k][j]

        return Matrix(new_matrix)

    def __imul__(self, other):
        """in-place implementation for multiplying"""
        return self.__mul__(other)

    def __neg__(self):
        """Make a matrix negative"""

        new_matrix = list()
        for i in range(self.size[1]):
            new_matrix.append(list())
            for j in range(self.size[0]):
                new_matrix[i].append(
                    -self.matrix_list[i][j]
                )

        return Matrix(new_matrix)

    def T(self):
        """Transpose a matrix"""
        return Matrix([list(i) for i in zip(*self.matrix_list)])

    def __pow__(self, power):
        """Raise a matrix by power"""

        new_matrix = self

        for _ in range(power - 1):
            new_matrix = new_matrix * self

        return new_matrix


def main():
    pass


if __name__ == '__main__':
    main()
