#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """defines unit tests for max integer function"""

    def test_ascending_list(self):
        """Test an ordered list of ascending integers."""
        ascending = [1, 2, 3, 4]
        self.assertEqual(max_integer(ascending), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [3, 2, 4, 1]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_string(self):
        """Test a string."""
        string = "Barbeque"
        self.assertEqual(max_integer(string), 'u')

    def test_single_element_list(self):
        """Test a list with a single element."""
        single_element = [50]
        self.assertEqual(max_integer(single_element), 50)

    def test_floats(self):
        """Test a list of floats."""
        floats = [22.1, 2.03, 99.9, 305.5]
        self.assertEqual(max_integer(floats), 305.5)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)
