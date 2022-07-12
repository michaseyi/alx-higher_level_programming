#!/usr/bin/python3
"""Unittest for models/base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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


class TestToJsonString(unittest.TestCase):

    def test_no_param(self):
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertEqual(str(e.exception), "to_json_string() missing 1 \
required positional argument: 'list_dictionaries'")

    def test_no_param(self):
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertEqual(str(e.exception), "to_json_string() missing 1 \
required positional argument: 'list_dictionaries'")

    def test_none_param(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_rectangle_object_dict(self):
        a = Rectangle(10, 10, id=10).to_dictionary()
        self.assertEqual(Base.to_json_string([a]), '[{"x": 0, "y": 0,\
 "id": 10, "height": 10, "width": 10}]')

    def test_square_object_dict(self):
        a = Square(10, id=11).to_dictionary()
        self.assertEqual(Base.to_json_string([a]), '[{"id": 11,\
 "x": 0, "size": 10, "y": 0}]')

    def test_square_and_rectangle_object(self):
        a = Square(10, id=11).to_dictionary()
        b = Rectangle(10, 10, id=12).to_dictionary()
        self.assertEqual(Base.to_json_string([a, b]), '[{"id": 11,\
 "x": 0, "size": 10, "y": 0}, {"x": 0, "y": 0,\
 "id": 12, "height": 10, "width": 10}]')


class TestFromJsonString(unittest.TestCase):

    def test_no_param(self):
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        self.assertEqual(str(e.exception), "from_json_string() missing 1 \
required positional argument: 'json_string'")

    def test_json_string_for_rectangle(self):
        a = '[{"x": 0, "y": 0, "id": 10, "height": 10, "width": 10}]'
        exp_list = [{"x": 0, "y": 0, "id": 10, "height": 10, "width": 10}]
        self.assertEqual(Base.from_json_string(a), exp_list)

    def test_json_string_for_square(self):
        a = '[{"x": 0, "y": 0, "id": 10, "size": 10}]'
        exp_list = [{"x": 0, "y": 0, "id": 10, "size": 10}]
        self.assertEqual(Base.from_json_string(a), exp_list)

    def test_json_string_for_square_and_rectangle(self):
        a = '[{"x": 0, "y": 0, "id": 10, "height": 10, "width": 10}, \
{"x": 0, "y": 0, "id": 10, "size": 10}]'
        exp_list = [{"x": 0, "y": 0, "id": 10, "height": 10,
                     "width": 10}, {"x": 0, "y": 0, "id": 10, "size": 10}]
        self.assertEqual(Base.from_json_string(a), exp_list)


if __name__ == "__main__":
    unittest.main()
