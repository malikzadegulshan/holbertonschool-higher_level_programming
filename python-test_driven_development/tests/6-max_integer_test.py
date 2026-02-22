#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    # --------------------------------------------------
    # Basic functionality
    # --------------------------------------------------

    def test_ordered_list(self):
        """Max is at the end of an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max is somewhere in the middle of an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max is the first element"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """List with one element returns that element"""
        self.assertEqual(max_integer([7]), 7)

    def test_all_same(self):
        """All elements are the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    # --------------------------------------------------
    # Edge cases
    # --------------------------------------------------

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Calling with no argument uses default empty list, returns None"""
        self.assertIsNone(max_integer())

    # --------------------------------------------------
    # Negative numbers
    # --------------------------------------------------

    def test_all_negative(self):
        """List of all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """List with both positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_negative_and_zero(self):
        """List with negative numbers and zero"""
        self.assertEqual(max_integer([-5, -1, 0]), 0)

    # --------------------------------------------------
    # Floats and mixed types
    # --------------------------------------------------

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_and_float(self):
        """List of mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 2, 3.9]), 3.9)

    # --------------------------------------------------
    # Larger lists
    # --------------------------------------------------

    def test_large_list(self):
        """Max in a large list"""
        self.assertEqual(max_integer(list(range(1000))), 999)

    def test_two_elements(self):
        """List with exactly two elements"""
        self.assertEqual(max_integer([10, 20]), 20)
        self.assertEqual(max_integer([20, 10]), 20)


if __name__ == '__main__':
    unittest.main()
