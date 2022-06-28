#!/usr/bin/python3
"""Unittest for max_integer([...])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for the max_integer function"""

    def test_max_integer(self):
        """Test max integer from a list of integers"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 5]), 5)
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_same_values(self):
        """Test a list of same integers"""
        self.assertAlmostEqual(max_integer([5, 5, 5]), 5)

    def test_negative_values(self):
        """Test a list of negative integers"""
        self.assertAlmostEqual(max_integer([-1, -22, -100]), -1)

    def test_float_values(self):
        """Test a list of floating point values"""
        self.assertAlmostEqual(max_integer([1.11, 1.2, 4, 4.001]), 4.001)

    def test_floats_and_int(self):
        """Test a list of mixed values int and floats"""
        self.assertAlmostEqual(max_integer([10.99, 11, 3, 9]), 11)

    def test_empty_list(self):
        """Tests an empty list"""
        self.assertAlmostEqual(max_integer(), None)

    def test_string(self):
        """Tests a list of strings"""
        self.assertAlmostEqual(max_integer(['1', '2', '9']), '9')
        self.assertAlmostEqual(max_integer(
            ["Michael", "Jacob", "Mikey"]), "Mikey")
