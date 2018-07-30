"""Reverse an iterable object

This module represents a function that reverses all elements in a sequence

Example:
    it = reverse_iter([1, 2, 3, 4, 5, 18, 20, 50, 8])
    print(it)

    [8, 50, 20, 18, 5, 4, 3, 2, 1]

"""


def reverse_gen(items_list):
    """The generator that defines what to send and when to stop"""
    i = 0
    size = len(items_list)
    while i < size:
        i += 1
        yield items_list[size - i]
    raise StopIteration


def reverse_iter(items_list):
    """The function that turns the reverse_gen into a list

    This function is necessary to access all the elements at once

    """
    return list(reverse_gen(items_list))


def main():
    it = reverse_iter([1, 2, 3, 4, 5, 18, 20, 50, 8])
    print(it)


if __name__ == '__main__':
    main()
