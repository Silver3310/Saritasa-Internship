"""SelfSet class

This module demonstrates the SelfSet class which represents the set class
and can work with it. The SelfSet supports all methods that the set class has.
SeltSet and set objects are compatible with each other

Example:
    a = {1, 2, 3, 4}
    b = SelfSet([3, 4, 5, 6])

    a.union(b)
        {1, 2, 3, 4, 5, 6}


"""

from random import choice


class SelfSet:
    """The class that represents the set class"""

    def __init__(self, sequence):
        """The constructor that creates a set based on a given list"""

        self.data = list()

        for each in sequence:
            if each not in self.data:
                self.data.append(each)

        self.i = 0

    def __iter__(self):
        """The method that is used to make SelfSet iterable"""
        return self

    def __next__(self):
        """The method that is used to make SelfSet iterable"""
        n = len(self)
        if self.i < n:
            i = self.i
            self.i += 1
            return self.data[i]
        else:
            self.i = 0
            raise StopIteration

    def __len__(self):
        """The length of the SelfSet"""
        return len(self.data)

    def __repr__(self):
        """The method that represents values"""
        # Here we read each value from data as a string
        result_str = [str(each) for each in self.data]
        # and connect them
        return '{' + ', '.join(result_str) + '}'

    def __contains__(self, item):
        """The method that represent 'in' operator"""
        return item in self.data

    def __eq__(self, another_set):
        """The method that allows to compare two sets regardless of
        their order
        """
        return self.issubset(another_set) and another_set.issubset(self)

    def add(self, item):
        """Add element elem to the set."""
        if item not in self.data:
            self.data.append(item)

    def remove(self, item):
        """Remove element elem from the set.

        Raises KeyError if elem is not contained in the set.
        """
        if item in self.data:
            self.data.remove(item)
        else:
            raise KeyError

    def discard(self, item):
        """Remove element elem from the set if it is present."""
        if item in self.data:
            self.data.remove(item)

    def pop(self):
        """Remove and return an arbitrary element from the set.

        Raises KeyError if the set is empty."""
        if self.data:
            to_del = choice(self.data)
            self.data.remove(to_del)
            return to_del
        else:
            raise KeyError

    def clear(self):
        """Remove all elements from the set."""
        self.data.clear()

    def update(self, another_set):
        """Update the set, adding elements from all others."""
        for each in another_set:
            if each not in self:
                self.data.append(each)

    def intersection_update(self, another_set):
        """Update the set, keeping only elements found in it and all others."""
        self.data = [
            each for each in another_set
            if each in self.data
        ]
        return self

    def difference_update(self, another_set):
        """Update the set, removing elements found in others."""
        for each in another_set:
            if each in self.data:
                self.data.remove(each)
        return self

    def symmetric_difference_update(self, another_set):
        """Update the set, keeping only elements found in either set,
         but not in both.
         """
        self.data = self.union(
            another_set
        ).difference_update(
            self.intersection(
                another_set
            )
        ).data
        return self

    def union(self, another_set):
        """Return a new set with elements from the set and all others."""
        new_list = list()
        for each in self.data:
            new_list.append(each)
        for each in another_set:
            new_list.append(each)
        return SelfSet(new_list)

    def intersection(self, another_set):
        """Return a new set with elements common to the set and all others."""
        new_list = [
            each for each in another_set
            if each in self.data
        ]
        return SelfSet(new_list)

    def difference(self, another_set):
        """Return a new set with elements in the set that are not in the
        others.
        """
        new_list = [
            each for each in self.data
            if each not in another_set
        ]
        return SelfSet(new_list)

    def symmetric_difference(self, another_set):
        """Return a new set with elements in either the set or other but not
        both.
        """
        new_list = self.union(
            another_set
        ).difference_update(
            self.intersection(
                another_set
            )
        ).data
        return SelfSet(new_list)

    def issubset(self, another_set):
        """Test whether every element in the set is in other."""
        for each in self.data:
            if each not in another_set:
                return False
        return True

    def issuperset(self, another_set):
        """Test whether every element in other is in the set."""
        for each in another_set:
            if each not in self.data:
                return False
        return True

    def copy(self):
        """Return a new set with a shallow copy of set."""
        return SelfSet(self.data)

    # Equivalent operators

    def __ge__(self, other):
        """Test whether every element in other is in the set."""
        return self.issuperset(other)

    def __le__(self, other):
        """Test whether every element in the set is in other."""
        return self.issubset(other)

    def __or__(self, other):
        """Return a new set with elements from the set and all others."""
        return self.union(other)

    def __and__(self, other):
        """Return a new set with elements common to the set and all others."""
        return self.intersection(other)

    def __sub__(self, other):
        """Return a new set with elements in the set that are not in the
        others.
        """
        return self.difference(other)

    def __xor__(self, other):
        """Return a new set with elements in either the set or other but not
        both.
        """
        return self.symmetric_difference(other)

    def __ior__(self, other):
        """Update the set, adding elements from all others."""
        self.update(other)
        return self

    def __iand__(self, other):
        """Update the set, keeping only elements found in it and all others."""

        self.intersection_update(other)
        return self

    def __isub__(self, other):
        """Update the set, removing elements found in others."""
        self.difference_update(other)
        return self

    def __ixor__(self, other):
        """Update the set, keeping only elements found in either set,
        but not in both.
        """
        self.symmetric_difference_update(other)
        return self


def main():
    pass


if __name__ == '__main__':
    main()
