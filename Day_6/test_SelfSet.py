import unittest
from .SelfSet import SelfSet


class TestSelfSet(unittest.TestCase):

    def test_union(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        self.assertEqual(
            a.union(b),
            {1, 2, 3, 4, 5, 6}
        )

        self.assertEqual(
            b.union(a),
            SelfSet([1, 2, 3, 4, 5, 6])
        )

    def test_intersection(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        self.assertEqual(
            a.intersection(b),
            {3, 4}
        )

        self.assertEqual(
            b.intersection(a),
            SelfSet([3, 4])
        )

    def test_difference(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        self.assertEqual(
            a.difference(b),
            {1, 2}
        )

        self.assertEqual(
            b.difference(a),
            SelfSet([5, 6])
        )

    def test_symmetric_difference(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        self.assertEqual(
            a.symmetric_difference(b),
            {1, 2, 5, 6}
        )

        self.assertEqual(
            b.symmetric_difference(a),
            SelfSet([1, 2, 5, 6])
        )

    def test_update(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        b.update(a)

        self.assertEqual(
            b,
            SelfSet([1, 2, 3, 4, 5, 6])
        )

        # vice versa
        b = SelfSet([3, 4, 5, 6])
        a.update(b)

        self.assertEqual(
            a,
            {1, 2, 3, 4, 5, 6}
        )

    def test_intersection_update(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        b.intersection_update(a)

        self.assertEqual(
            b,
            SelfSet([3, 4])
        )

        # vice versa
        b = SelfSet([3, 4, 5, 6])
        a.intersection_update(b)

        self.assertEqual(
            a,
            {3, 4}
        )

    def test_difference_update(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        b.difference_update(a)

        self.assertEqual(
            b,
            SelfSet([5, 6])
        )

        # vice versa
        b = SelfSet([3, 4, 5, 6])
        a.difference_update(b)

        self.assertEqual(
            a,
            {1, 2}
        )

    def test_symmetric_difference_update(self):

        a = {1, 2, 3, 4}
        b = SelfSet([3, 4, 5, 6])

        b.symmetric_difference_update(a)

        self.assertEqual(
            b,
            SelfSet([1, 2, 5, 6])
        )

        # vice versa
        b = SelfSet([3, 4, 5, 6])
        a.symmetric_difference_update(b)

        self.assertEqual(
            a,
            {1, 2, 5, 6}
        )

    def test_issubset(self):

        a = {3, 4}
        b = SelfSet([1, 2, 3, 4])

        self.assertEqual(
            a.issubset(b),
            True
        )

        # vice versa
        a = {1, 2, 3, 4}
        b = SelfSet([3, 4])

        self.assertEqual(
            b.issubset(a),
            True
        )

    def test_issuperset(self):

        a = {3, 4}
        b = SelfSet([1, 2, 3, 4])

        self.assertEqual(
            b.issuperset(a),
            True
        )

        # vice versa
        a = {1, 2, 3, 4}
        b = SelfSet([3, 4])

        self.assertEqual(
            a.issuperset(b),
            True
        )

    def test_in_operator(self):

        a = SelfSet([1, 2, 3, 4])

        self.assertEqual(
            3 in a,
            True
        )

        self.assertEqual(
            5 not in a,
            True
        )

    def test_len_operator(self):

        a = SelfSet([1, 2, 3, 4, 5, 0])

        self.assertEqual(
            len(a),
            6
        )

    def test_add(self):

        a = SelfSet([1, 2, 3, 4])

        a.add(3)
        a.add(7)
        a.add('g')

        self.assertEqual(
            a,
            SelfSet([1, 2, 3, 4, 7, 'g'])
        )

    def test_copy(self):

        a = SelfSet([1, 2, 3, 4])
        b = a.copy()

        self.assertEqual(
            a is not b,
            True
        )

    def test_remove(self):

        a = SelfSet([1, 2, 3, 4])

        a.remove(3)

        self.assertEqual(
            a,
            SelfSet([1, 2, 4])
        )

        with self.assertRaises(KeyError):
            a.remove(6)

    def test_discard(self):

        a = SelfSet([1, 2, 3, 4])

        a.discard(3)

        self.assertEqual(
            a,
            SelfSet([1, 2, 4])
        )

        a.discard(6)

        self.assertEqual(
            a,
            SelfSet([1, 2, 4])
        )

    def test_pop(self):

        a = SelfSet([1, 2, 3, 4])
        b = a.copy()

        arbitrary_value = a.pop()
        a.add(arbitrary_value)

        self.assertEqual(
            a == b,
            True
        )

    def test_clear(self):

        a = SelfSet([1, 2, 3, 4])

        a.clear()

        self.assertEqual(
            a,
            SelfSet([])
        )

    # Next we'll check equivalent functions

    def test_greater_than_or_equal(self):

        a = {3, 4}
        b = SelfSet([1, 2, 3, 4])

        self.assertEqual(
            b >= a,
            True
        )

        # vice versa
        a = {1, 2, 3, 4}
        b = SelfSet([3, 4])

        self.assertEqual(
            a >= b,
            True
        )

    def test_less_than_or_equal(self):

        a = {3, 4}
        b = SelfSet([1, 2, 3, 4])

        self.assertEqual(
            a <= b,
            True
        )

        # vice versa
        a = {1, 2, 3, 4}
        b = SelfSet([3, 4])

        self.assertEqual(
            b <= a,
            True
        )

    def test_union_as_or(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        self.assertEqual(
            a | b,
            {1, 2, 3, 4, 5, 6}
        )

    def test_intersection_as_and(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        self.assertEqual(
            a & b,
            SelfSet([3, 4])
        )

    def test_difference_as_sub(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        self.assertEqual(
            a - b,
            SelfSet([1, 2])
        )

    def test_symmetric_difference_as_xor(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        self.assertEqual(
            a ^ b,
            SelfSet([1, 2, 5, 6])
        )

    def test_update_as_ior(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        a |= b

        self.assertEqual(
            a,
            SelfSet([1, 2, 3, 4, 5, 6])
        )

    def test_intersection_update_as_iand(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        a &= b

        self.assertEqual(
            a,
            SelfSet([3, 4])
        )

    def test_difference_update_as_isub(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        a -= b

        self.assertEqual(
            a,
            SelfSet([1, 2])
        )

    def test_symmetric_difference_update_as_ixor(self):

        a = SelfSet([1, 2, 3, 4])
        b = {3, 4, 5, 6}

        a ^= b

        self.assertEqual(
            a,
            SelfSet([1, 2, 5, 6])
        )


if __name__ == '__main__':
    unittest.main()
