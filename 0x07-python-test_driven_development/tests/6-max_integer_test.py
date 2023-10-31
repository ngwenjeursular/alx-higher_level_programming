#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Test that max_integer([]) returns None."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test that max_integer([1]) returns 1."""
        self.assertEqual(max_integer([1]), 1)

    def test_multiple_element_list(self):
        """Test that max_integer([1, 2, 3]) returns 3."""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_list_with_negative_numbers(self):
        """Test that max_integer([1, -2, 3]) returns 3."""
        self.assertEqual(max_integer([1, -2, 3]), 3)

    def test_list_with_floats(self):
        """Test that max_integer([1.0, 2.0, 3.0]) returns 3.0."""
        self.assertEqual(max_integer([1.0, 2.0, 3.0]), 3.0)

    def test_list_with_strings(self):
        """Test that max_integer([1, "a", 3]) raises a TypeError exception."""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

    def test_two_integers_that_are_the_same(self):
        self.assertEqual(max_integer([1, 1]), 1)

    def test_an_unmodified_list(self):
        list = [1, 2, 3]
        max_integer(list)
        self.assertEqual(list, [1, 2, 3])

    def test_a_sorted_list(self):
        list = [1, 2, 3]
        self.assertEqual(max_integer(list), 3)

    def test_with_the_max_number_in_the_middle(self):
        list = [1, 3, 2]
        self.assertEqual(max_integer(list), 3)


if __name__ == "__main__":
    unittest.main()
