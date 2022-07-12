#!/usr/bin/python3


import io
import sys

from unittest.mock import patch
from models.rectangle import Rectangle
import unittest


class TestRectangleInitilization(unittest.TestCase):

    def test_height(self):
        a = Rectangle(10, 10, 1, 1)
        b = Rectangle(10, 10, 1, 1)
        self.assertEqual(a.height, b.height)

    def test_no_param(self):
        with self.assertRaises(TypeError) as e:
            Rectangle()
        self.assertEqual(str(e.exception), "__init__() missing 2 \
required positional arguments: 'width' and 'height'")

    def test_one_param(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10)
        self.assertEqual(str(e.exception), "__init__() missing 1 \
required positional argument: 'height'")

    def test_height_less_than_or_equals_to_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
        self.assertEqual(e.exception.args[0], 'height must be > 0')

    def test_height_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, '1')
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_height_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 1.2)
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_height_list(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, [1])
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_height_tuple(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, (1,))
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_height_complex(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, complex(real=1.2, imag=3))
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_height_very_large_number(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, float('inf'))
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_height_None_value(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, None)
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_height_bool(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, True)
        self.assertEqual(e.exception.args[0], 'height must be an integer')

    def test_width(self):
        a = Rectangle(10, 10, 1, 1)
        b = Rectangle(10, 10, 1, 1)
        self.assertEqual(a.width, b.width)

    def test_width_less_than_or_equals_to_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 10)
        self.assertEqual(e.exception.args[0], 'width must be > 0')

    def test_width_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle('1', 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_width_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1.3, 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_width_list(self):
        with self.assertRaises(TypeError) as e:
            Rectangle([1], 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_width_tuple(self):
        with self.assertRaises(TypeError) as e:
            Rectangle((1,), 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_width_complex(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(complex(real=1.2, imag=3.3), 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_width_very_large_number(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(float('inf'), 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_width_None_value(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(None, 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_width_bool(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(True, 10)
        self.assertEqual(e.exception.args[0], 'width must be an integer')

    def test_id(self):
        a = Rectangle(10, 10, 1, 1)
        b = Rectangle(10, 10, 1, 1)
        self.assertEqual(a.id, b.id - 1)

    def test_id_less_than_zero(self):
        self.assertEqual(-1, Rectangle(10, 10, 1, 2, -1).id)

    def test_id_string(self):
        self.assertEqual('1', Rectangle(10,  10, 1, 1,  '1').id)

    def test_id_float(self):
        self.assertEqual(1.1,  Rectangle(10, 10, 1, 1, 1.1).id)

    def test_id_list(self):
        self.assertEqual([1],  Rectangle(10, 10, 1, 1, [1]).id)

    def test_id_tuple(self):
        self.assertEqual((1,),  Rectangle(10, 10, 1, 1, (1,)).id)

    def test_id_complex(self):
        self.assertEqual(complex(real=1.2, imag=2),
                         Rectangle(10, 10, 10, 10,
                                   complex(real=1.2, imag=2)).id)

    def test_id_very_large_number(self):
        self.assertEqual(float('inf'),  Rectangle(
            10, 10, 1, 1, float('inf')).id)

    def test_id_None_value(self):
        a = Rectangle(10, 10, 1, 1, None)
        b = Rectangle(10, 10, 1, 1, None)
        self.assertEqual(a.id + 1,  b.id)

    def test_id_bool(self):
        self.assertEqual(
            False,  Rectangle(10, 10, 1, 1, False).id)

    def test_x(self):
        a = Rectangle(10, 10, 1, 1)
        b = Rectangle(10, 10, 1, 1)
        self.assertEqual(a.x, b.x)

    def test_x_less_than_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 10, -1, 1)
        self.assertEqual(e.exception.args[0], 'x must be >= 0')

    def test_x_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, '1', 1)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_x_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 1.1, 1)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_x_list(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, [1], 10)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_x_tuple(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, (1, ), 10)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_x_complex(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, complex(real=1.1, imag=1.3), 10)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_x_very_large_number(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, float('inf'), 10)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_x_None_value(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, None, 10)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_x_bool(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, True, 10)
        self.assertEqual(e.exception.args[0], 'x must be an integer')

    def test_y(self):
        a = Rectangle(10, 10, 1, 1)
        b = Rectangle(10, 10, 1, 1)
        self.assertEqual(a.y, b.y)

    def test_y_less_than_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 10, 10, -1)
        self.assertEqual(e.exception.args[0], 'y must be >= 0')

    def test_y_string(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, '1')
        self.assertEqual(e.exception.args[0], 'y must be an integer')

    def test_y_float(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, 1.3)
        self.assertEqual(e.exception.args[0], 'y must be an integer')

    def test_y_list(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, [1])
        self.assertEqual(e.exception.args[0], 'y must be an integer')

    def test_y_tuple(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, (1, ))
        self.assertEqual(e.exception.args[0], 'y must be an integer')

    def test_y_complex(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, complex(real=1.3, imag=33))
        self.assertEqual(e.exception.args[0], 'y must be an integer')

    def test_y_very_large_number(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, float('inf'))
        self.assertEqual(e.exception.args[0], 'y must be an integer')

    def test_y_None_value(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, None)
        self.assertEqual(e.exception.args[0], 'y must be an integer')
        self.assertRaises(TypeError, lambda: Rectangle(10, 10, 10, None))

    def test_y_bool(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 10, 10, True)
        self.assertEqual(e.exception.args[0], 'y must be an integer')


class TestRectangleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(10, Rectangle(2, 5).area())

    def test_area_same_width_and_height(self):
        self.assertEqual(100, Rectangle(10, 10).area())

    def test_area_large_values(self):
        a = 99999999999999999999999999999999
        self.assertEqual(a ** 2, Rectangle(a, a).area())

    def test_area_large_and_small_values(self):
        a = 999999999999999999999999999999999
        b = 10
        self.assertEqual(a * b, Rectangle(a, b).area())


class TestRectangleDisplay(unittest.TestCase):
    @staticmethod
    def get_stdout_val(obj, shouldPrint=False):
        """
        get_stdout_val temporarily sets the sys stdout to an io stream,
        captures the value, sets the sys stdout back to the default outut
        stream with fd of 1 and returns the value.

        This works since the print function prints by default to sys.stdout.

        :param obj(Base) is the object to captured
        :param shouldPrint(bool) tell whether to call the display method
        on the object or to just print it out
        :return (str) the valued captured from the stdout
        """
        temp = sys.stdout
        sys.stdout = io.StringIO()
        print(obj) if shouldPrint else obj.display()
        data = sys.stdout.getvalue()
        sys.stdout = temp
        return data

    def test_diplay(self):
        display = """\
######
######
######
######
######
######
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(6, 6)))

    def test_diplay_with_small_values(self):
        display = """\
##
##
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(2, 2)))

    def test_diplay_with_vertical_padding(self):
        display = """\



##
##
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(2, 2, y=3)))

    def test_diplay_with_large_vertical_padding(self):
        display = """\










##
##
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(2, 2, y=10)))

    def test_diplay_with_zero_vertical_padding(self):
        display = """\
##
##
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(2, 2, y=0)))

    def test_diplay_with_horizontal_padding(self):
        display = """\
   ##
   ##
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(2, 2, x=3)))

    def test_diplay_with_large_horizontal_padding(self):
        display = """\
          ##
          ##
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(2, 2, x=10)))

    @patch('sys.stdout', io.StringIO())
    def test_diplay_with_zero_horizontal_padding(self):
        display = """\
##
##
"""
        Rectangle(2, 2, x=0).display()
        self.assertEqual(display, sys.stdout.getvalue())

    def test_diplay_with_both_horizontal_and_vertical_padding(self):
        display = """\





          #####
          #####
          #####
          #####
          #####
"""
        self.assertEqual(
            display, TestRectangleDisplay.
            get_stdout_val(Rectangle(5, 5, x=10, y=5)))

    def test_diplay_with_both_horizontal_and_vertical_padding(self):
        display = """\















                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
                              ############################
"""
        self.assertEqual(
            display, TestRectangleDisplay.get_stdout_val(
                Rectangle(28, 16, x=30, y=15)))


class TestRectangleStrRepresentation(unittest.TestCase):

    @patch('sys.stdout', io.StringIO())
    def test_str_rep(self):
        print(Rectangle(10, 20, 5, 10, 100), end="")
        str_rep = "[Rectangle] (100) 5/10 - 10/20"
        self.assertEqual(str_rep, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_str_rep_with_x_as_zero(self):
        print(Rectangle(10, 20, 0, 10, 100), end="")
        str_rep = "[Rectangle] (100) 0/10 - 10/20"
        self.assertEqual(str_rep, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_str_rep_with_y_as_zero(self):
        print(Rectangle(10, 20, 5, 0, 100), end="")
        str_rep = "[Rectangle] (100) 5/0 - 10/20"
        self.assertEqual(str_rep, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_str_rep_with_only_width_and_height(self):
        print(Rectangle(10, 20), end="")
        str_rep = "[Rectangle] ({}) 0/0 - 10/20"\
            .format(Rectangle(100, 100).id - 1)
        self.assertEqual(str_rep, sys.stdout.getvalue())


class TestRectangleUpdate(unittest.TestCase):

    def test_update_args_id(self):
        a = Rectangle(10, 10)
        a.update(11)
        self.assertEqual(a.id, 11)

    def test_update_args_width(self):
        a = Rectangle(10, 10)
        a.update(10, 20)
        self.assertEqual(a.width, 20)

    def test_update_args_height(self):
        a = Rectangle(10, 10)
        a.update(10, 10, 20)
        self.assertEqual(a.height, 20)

    def test_update_args_x(self):
        a = Rectangle(10, 10)
        a.update(10, 10, 10, 20)
        self.assertEqual(a.x, 20)

    def test_update_args_y(self):
        a = Rectangle(10, 10)
        a.update(10, 10, 10, 10, 20)
        self.assertEqual(a.y, 20)

    def test_update_kwargs_id(self):
        a = Rectangle(10, 10)
        a.update(id=20)
        self.assertEqual(a.id, 20)

    def test_update_kwargs_width(self):
        a = Rectangle(10, 10)
        a.update(width=20)
        self.assertEqual(a.width, 20)

    def test_update_kwargs_height(self):
        a = Rectangle(10, 10)
        a.update(height=20)
        self.assertEqual(a.height, 20)

    def test_update_kwargs_x(self):
        a = Rectangle(10, 10)
        a.update(x=20)
        self.assertEqual(a.x, 20)

    def test_update_kwargs_y(self):
        a = Rectangle(10, 10)
        a.update(y=20)
        self.assertEqual(a.y, 20)

    def test_update_precedence_id(self):
        a = Rectangle(10, 10)
        a.update(14, id=15)
        self.assertEqual(a.id, 14)

    def test_update_precedence_id_width(self):
        a = Rectangle(10, 10)
        a.update(14, 29, id=15, width=20)
        self.assertEqual(a.id, 14)
        self.assertEqual(a.width, 29)

    def test_update_precedence_id_width_height(self):
        a = Rectangle(10, 10)
        a.update(14, 29, 30, id=15, width=20, height=39)
        self.assertEqual(a.id, 14)
        self.assertEqual(a.width, 29)
        self.assertEqual(a.height, 30)

    def test_update_precedence_id_width_height_x(self):
        a = Rectangle(10, 10)
        a.update(11, 11, 11, 8, x=16)
        self.assertTrue(a.x == 8)

    def test_update_precedence_y(self):
        a = Rectangle(10, 10)
        a.update(11, 11, 11, 8, 39, x=16, y=23)
        self.assertTrue(a.x == 8 and a.y == 39)

    def test_update_no_params(self):
        a = Rectangle(10, 10)
        a.update()
        self.assertTrue(a.width == a.height == 10)

    def test_update_all_args(self):
        a = Rectangle(10, 10)
        a.update(11, 11, 11, 11, 11)
        self.assertTrue(a.id == a.width == a.height == a.x == a.y)

    def test_update_all_kwargs(self):
        a = Rectangle(10, 10)
        a.update(id=11, width=11, height=11, x=11, y=11)
        self.assertTrue(a.id == a.width == a.height == a.x == a.y)

    def test_update_all_args_and_kwargs(self):
        a = Rectangle(10, 10)
        a.update(12, 12, 12, 12, 12, id=11, width=11, height=11, x=11, y=11)
        self.assertTrue(a.id == a.width == a.height == a.x == a.y == 12)


class TestRectangleToDictionary(unittest.TestCase):

    def test_dict(self):
        a = Rectangle(10, 10)
        a_dict = a.to_dictionary()
        exp_dict = {"id": a.id, "width": 10, "height": 10,
                    "x": 0, "y": 0}
        self.assertTrue(a_dict == exp_dict)

    def test_dict_with_all_values_set(self):
        a = Rectangle(10, 10, 20, 20, 72)
        a_dict = a.to_dictionary()
        exp_dict = {"id": 72, "width": 10, "height": 10,
                    "x": 20, "y": 20}
        self.assertTrue(a_dict == exp_dict)


class TestSaveRectangleToFile(unittest.TestCase):
    def test_no_param(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
        self.assertEqual(str(e.exception), "save_to_file() missing 1 \
required positional argument: 'list_objs'")

    def test_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_one_rectangle_object(self):
        Rectangle.save_to_file([Rectangle(10, 10, id=10)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[{"x": 0, "y": 0, "id": 10, \
"height": 10, "width": 10}]')

    def test_multiple_rectangle_object(self):
        Rectangle.save_to_file([Rectangle(10, 10, id=10),
                               Rectangle(11, 11, id=11)])
        with open("Rectangle.json") as file:
            self.assertEqual(file.read(), '[{"x": 0, "y": 0, "id": 10, \
"height": 10, "width": 10}, {"x": 0, "y": 0, "id": 11, "height": 11, \
"width": 11}]')


class TestCreateRectangleObject(unittest.TestCase):

    def test_no_param(self):
        self.assertEqual(type(Rectangle.create()), Rectangle)
        self.assertEqual(Rectangle.create().width, 1)

    def test_width(self):
        self.assertEqual(Rectangle.create(width=10).width, 10)

    def test_height(self):
        self.assertEqual(Rectangle.create(height=10).height, 10)

    def test_id(self):
        self.assertEqual(Rectangle.create(id=10).id, 10)

    def test_x(self):
        self.assertEqual(Rectangle.create(x=10).x, 10)

    def test_y(self):
        self.assertEqual(Rectangle.create(y=10).y, 10)

    def test_all_param(self):
        a = Rectangle.create(width=10, height=10, id=10, x=10,
                             y=10)
        self.assertTrue(a.id == a.width == a.height == a.x ==
                        a.y == 10)

    def test_wrong_type_param(self):
        with self.assertRaises(TypeError) as e:
            Rectangle.create(width='10')
        self.assertEqual(str(e.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as e:
            Rectangle.create(height='10')
        self.assertEqual(str(e.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as e:
            Rectangle.create(x='10')
        self.assertEqual(str(e.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as e:
            Rectangle.create(y='10')
        self.assertEqual(str(e.exception), 'y must be an integer')


class TestLoadFromFile(unittest.TestCase):

    def test_load_single_object(self):
        Rectangle.save_to_file([Rectangle(10, 10, id=10)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 10)

    def test_load_multiple_objects(self):
        a = Rectangle(10, 11, id=10)
        b = Rectangle(10, 11, id=11)
        c = Rectangle(10, 11, id=12)
        Rectangle.save_to_file([a, b, c])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 3)
        self.assertTrue(objs[0].id == 10 and objs[1].id == 11 and
                        objs[2].id == 12)

    def test_load_empty_list(self):
        Rectangle.save_to_file([])
        objs = Rectangle.load_from_file()
        self.assertEqual(0, len(objs))

    def test_load_none(self):
        Rectangle.save_to_file(None)
        objs = Rectangle.load_from_file()
        self.assertEqual(0, len(objs))


if __name__ == "__main__":
    unittest.main()
