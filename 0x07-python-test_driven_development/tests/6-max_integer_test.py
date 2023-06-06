#!/usr/bin/python3
"""Unittest for Max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer([..])"""

    def test_at_beginning(self):
        """tests for max value at beginning of list"""
        begin = [4, 3, 2, 1]
        self.assertEqual(max_integer(begin), 4)

    def test_unordered_list(self):
        """tests an un sorted list"""
        unordered = [3, 1, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_sorted_list(self):
        """test for a sorted list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_empty_list(self):
        """tests for an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        """tests a list with only one element"""
        one_list = [10]
        self.assertEqual(max_integer(one_list), 10)

    def test_floats(self):
        """tests for a list of floats"""
        float_list = [2.56, -8.54, 10.55, 0.7, 25.98]
        self.assertEqual(max_integer(float_list), 25.98)

    def test_mixed(self):
        """tests a mixed list of ints and floats"""
        mixed = [10, 2.5, -9, 25.98, 4]
        self.assertEqual(max_integer(mixed), 25.98)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """tests an empty string"""
        self.assertEqual(max_integer(""), None)

    if __name__ == "__main__":
        unittest.main()
