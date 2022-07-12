#!/usr/bin/python3
"""Unittest for models/base.py"""
import unittest
from models.base import Base


class TestBaseInitilization(unittest.TestCase):
    """Unittest class for models/base.py"""

    def test_main(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, b3.id + 1)

    def test_no_params(self):
        self.assertEqual(Base, type(Base()))

    def test_id_no_params(self):
        self.assertEqual(Base().id, Base().id - 1)

    def test_id_int_param(self):
        self.assertEqual(10, Base(10).id)

    def test_string_param(self):
        self.assertEqual("1", Base("1").id)

    def test_float_param(self):
        self.assertEqual(1.9, Base(1.9).id)

    def test_largest_positive_number_param(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_positive_number_param(self):
        self.assertEqual(+10, Base(+10).id)

    def test_smallest_negative_number_param(self):
        self.assertEqual(float('-inf'), Base(float('-inf')).id)

    def test_negative_number_param(self):
        self.assertEqual(-10, Base(-10).id)

    def test_list_as_param(self):
        self.assertEqual([1, 2], Base([1, 2]).id)

    def test_list_as_param_2(self):
        self.assertEqual([], Base([]).id)

    def test_list_as_param_3(self):
        self.assertEqual(["1", "2"], Base(["1", "2"]).id)

    def test_list_as_param_4(self):
        self.assertEqual([-1, -2], Base([-1, -2]).id)

    def test_list_as_param_5(self):
        self.assertEqual([float('inf')], Base([float('inf')]).id)

    def test_list_as_param_6(self):
        self.assertEqual([1.1, 1.2], Base([1.1, 1.2]).id)

    def test_None_value_as_param(self):
        self.assertEqual(Base().id, Base().id - 1)

    def test_complex_value_as_param(self):
        self.assertEqual(complex(real=1, imag=2),
                         Base(complex(real=1, imag=2)).id)

    def test_bool_true_as_param(self):
        self.assertEqual(True, Base(True).id)

    def test_bool_false_as_param(self):
        self.assertEqual(False, Base(False).id)

    def test_int_type_as_param(self):
        self.assertEqual(int, Base(int).id)

    def test_str_type_as_param(self):
        self.assertEqual(str, Base(str).id)

    def test_bool_type_as_param(self):
        self.assertEqual(bool, Base(bool).id)

    def test_float_type_as_param(self):
        self.assertEqual(float, Base(float).id)

    def test_list_type_as_param(self):
        self.assertEqual(list, Base(list).id)
