#!/usr/bin/python3


import io
import sys
from unittest.mock import patch
from models.square import Square
import unittest


class TestSquareInitilization(unittest.TestCase):

    def test_size(self):
        a = Square(10)
        b = Square(10)
        self.assertEqual(a.size, b.size)

    def test_size_less_than_or_equals_to_zero(self):
        with self.assertRaises(ValueError) as e:
            a = Square(0)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_size_string(self):
        with self.assertRaises(TypeError) as e:
            Square('1')
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_size_float(self):
        with self.assertRaises(TypeError) as e:
            Square(1.2)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_size_list(self):
        with self.assertRaises(TypeError) as e:
            Square([1, 1])
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_size_tuple(self):
        with self.assertRaises(TypeError) as e:
            Square((1, ))
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_size_complex(self):
        with self.assertRaises(TypeError) as e:
            Square(complex(real=1, imag=3))
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_size_very_large_number(self):
        with self.assertRaises(TypeError) as e:
            Square(float('inf'))
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_size_None_value(self):
        with self.assertRaises(TypeError) as e:
            Square(None)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_size_bool(self):
        with self.assertRaises(TypeError) as e:
            Square(True)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_id(self):
        a = Square(10, 1, 1)
        b = Square(10, 1, 1)
        self.assertEqual(a.id, b.id - 1)

    def test_id_less_than_zero(self):
        self.assertEqual(-1, Square(10, 1, 2, -1).id)

    def test_id_string(self):
        self.assertEqual('1', Square(10, 1, 1,  '1').id)

    def test_id_float(self):
        self.assertEqual(1.1,  Square(10, 1, 1, 1.1).id)

    def test_id_list(self):
        self.assertEqual([1],  Square(10, 1, 1, [1]).id)

    def test_id_tuple(self):
        self.assertEqual((1,),  Square(10, 1, 1, (1,)).id)

    def test_id_complex(self):
        self.assertEqual(complex(real=1.2, imag=2),
                         Square(10, 10, 10,
                                complex(real=1.2, imag=2)).id)

    def test_id_very_large_number(self):
        self.assertEqual(float('inf'),  Square(
            10, 1, 1, float('inf')).id)

    def test_id_None_value(self):
        a = Square(10, 1, 1, None)
        b = Square(10, 1, 1, None)
        self.assertEqual(a.id + 1,  b.id)

    def test_id_bool(self):
        self.assertEqual(
            False,  Square(10, 1, 1, False).id)

    def test_x(self):
        a = Square(10, 1, 1)
        b = Square(10, 1, 1)
        self.assertEqual(a.x, b.x)

    def test_x_less_than_zero(self):
        with self.assertRaises(ValueError) as e:
            Square(10, -1)
        self.assertEqual(str(e.exception), 'x must be >= 0')

    def test_x_string(self):
        with self.assertRaises(TypeError) as e:
            Square(10, '1')
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_x_float(self):
        with self.assertRaises(TypeError) as e:
            Square(10, 1.2)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_x_list(self):
        with self.assertRaises(TypeError) as e:
            Square(10, [1])
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_x_tuple(self):
        with self.assertRaises(TypeError) as e:
            Square(10, (1, ))
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_x_None_value(self):
        with self.assertRaises(TypeError) as e:
            Square(10, None)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_x_bool(self):
        with self.assertRaises(TypeError) as e:
            Square(10, True)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_y(self):
        a = Square(10, 1, 1)
        b = Square(10, 1, 1)
        self.assertEqual(a.y, b.y)

    def test_y_less_than_zero(self):
        with self.assertRaises(ValueError) as e:
            Square(10, 10, -1)
        self.assertEqual(str(e.exception), 'y must be >= 0')

    def test_y_string(self):
        with self.assertRaises(TypeError) as e:
            Square(10, 10, '1')
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_y_float(self):
        with self.assertRaises(TypeError) as e:
            Square(10, 10, 1.2)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_y_list(self):
        with self.assertRaises(TypeError) as e:
            Square(10, 10, [1])
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_y_tuple(self):
        with self.assertRaises(TypeError) as e:
            Square(10, 10, (1, ))
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_y_None_value(self):
        with self.assertRaises(TypeError) as e:
            Square(10, 10, None)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_y_bool(self):
        with self.assertRaises(TypeError) as e:
            Square(10, 10, True)
        self.assertEqual(str(e.exception), 'y must be an integer')


class TestSquareArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(25, Square(5).area())

    def test_area_large_values(self):
        a = 99999999999999999999999999999999
        self.assertEqual(a ** 2, Square(a).area())


# class TestSquareDisplay(unittest.TestCase):
#     @staticmethod
#     def get_stdout_val(obj, shouldPrint=False):
#         """
#         get_stdout_val temporarily sets the sys stdout to an io stream,
#         captures the value, sets the sys stdout back to the default outut
#         stream with fd of 1 and returns the value.

#         This works since the print function prints by default to sys.stdout.

#         :param obj(Base) is the object to captured
#         :param shouldPrint(bool) tell whether to call the display method
#         on the object or to just print it out
#         :return (str) the valued captured from the stdout
#         """
#         temp = sys.stdout
#         sys.stdout = io.StringIO()
#         print(obj) if shouldPrint else obj.display()
#         data = sys.stdout.getvalue()
#         sys.stdout = temp
#         return data

#     def test_diplay(self):
#         display = """\
# ######
# ######
# ######
# ######
# ######
# ######
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(Square(6, 6)))

#     def test_diplay_with_small_values(self):
#         display = """\
# ##
# ##
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(Square(2, 2)))

#     def test_diplay_with_vertical_padding(self):
#         display = """\


# ##
# ##
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(Square(2, 2, y=3)))

#     def test_diplay_with_large_vertical_padding(self):
#         display = """\


# ##
# ##
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(Square(2, 2, y=10)))

#     def test_diplay_with_zero_vertical_padding(self):
#         display = """\
# ##
# ##
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(Square(2, 2, y=0)))

#     def test_diplay_with_horizontal_padding(self):
#         display = """\
#    ##
#    ##
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(Square(2, 2, x=3)))

#     def test_diplay_with_large_horizontal_padding(self):
#         display = """\
#           ##
#           ##
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(Square(2, 2, x=10)))

#     @patch('sys.stdout', io.StringIO())
#     def test_diplay_with_zero_horizontal_padding(self):
#         display = """\
# ##
# ##
# """
#         Square(2, 2, x=0).display()
#         self.assertEqual(display, sys.stdout.getvalue())

#     def test_diplay_with_both_horizontal_and_vertical_padding(self):
#         display = """\


#           #####
#           #####
#           #####
#           #####
#           #####
# """
#         self.assertEqual(
#             display, TestSquareDisplay.
# get_stdout_val(Square(5, 5, x=10, y=5)))

#     def test_diplay_with_both_horizontal_and_vertical_padding(self):
#         display = """\


#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
#                               ############################
# """
#         self.assertEqual(
#             display, TestSquareDisplay.get_stdout_val(
#                 Square(28, 16, x=30, y=15)))


# class TestSquareStrRepresentation(unittest.TestCase):

#     @patch('sys.stdout', io.StringIO())
#     def test_str_rep(self):
#         print(Square(10, 20, 5, 10, 100), end="")
#         str_rep = "[Square] (100) 5/10 - 10/20"
#         self.assertEqual(str_rep, sys.stdout.getvalue())

#     @patch('sys.stdout', io.StringIO())
#     def test_str_rep_with_x_as_zero(self):
#         print(Square(10, 20, 0, 10, 100), end="")
#         str_rep = "[Square] (100) 0/10 - 10/20"
#         self.assertEqual(str_rep, sys.stdout.getvalue())

#     @patch('sys.stdout', io.StringIO())
#     def test_str_rep_with_y_as_zero(self):
#         print(Square(10, 20, 5, 0, 100), end="")
#         str_rep = "[Square] (100) 5/0 - 10/20"
#         self.assertEqual(str_rep, sys.stdout.getvalue())

#     @patch('sys.stdout', io.StringIO())
#     def test_str_rep_with_only_width_and_height(self):
#         print(Square(10, 20), end="")
#         str_rep = "[Square] ({}) 0/0 - 10/20".format(Square(100, 100).id - 1)
#         self.assertEqual(str_rep, sys.stdout.getvalue())


# class TestSquareUpdate(unittest.TestCase):

#     def test_update_args_id(self):
#         a = Square(10, 10)
#         a.update(11)
#         self.assertEqual(a.id, 11)

#     def test_update_args_width(self):
#         a = Square(10, 10)
#         a.update(10, 20)
#         self.assertEqual(a.width, 20)

#     def test_update_args_height(self):
#         a = Square(10, 10)
#         a.update(10, 10, 20)
#         self.assertEqual(a.height, 20)

#     def test_update_args_x(self):
#         a = Square(10, 10)
#         a.update(10, 10, 10, 20)
#         self.assertEqual(a.x, 20)

#     def test_update_args_y(self):
#         a = Square(10, 10)
#         a.update(10, 10, 10, 10, 20)
#         self.assertEqual(a.y, 20)

#     def test_update_kwargs_id(self):
#         a = Square(10, 10)
#         a.update(id=20)
#         self.assertEqual(a.id, 20)

#     def test_update_kwargs_width(self):
#         a = Square(10, 10)
#         a.update(width=20)
#         self.assertEqual(a.width, 20)

#     def test_update_kwargs_height(self):
#         a = Square(10, 10)
#         a.update(height=20)
#         self.assertEqual(a.height, 20)

#     def test_update_kwargs_x(self):
#         a = Square(10, 10)
#         a.update(x=20)
#         self.assertEqual(a.x, 20)

#     def test_update_kwargs_y(self):
#         a = Square(10, 10)
#         a.update(y=20)
#         self.assertEqual(a.y, 20)

#     def test_update_precedence_id(self):
#         a = Square(10, 10)
#         a.update(14, id=15)
#         self.assertEqual(a.id, 14)

#     def test_update_precedence_id_width(self):
#         a = Square(10, 10)
#         a.update(14, 29, id=15, width=20)
#         self.assertEqual(a.id, 14)
#         self.assertEqual(a.width, 29)

#     def test_update_precedence_id_width_height(self):
#         a = Square(10, 10)
#         a.update(14, 29, 30, id=15, width=20, height=39)
#         self.assertEqual(a.id, 14)
#         self.assertEqual(a.width, 29)
#         self.assertEqual(a.height, 30)

#     def test_update_precedence_id_width_height_x(self):
#         a = Square(10, 10)
#         a.update(11, 11, 11, 8, x=16)
#         self.assertTrue(a.x == 8)

#     def test_update_precedence_y(self):
#         a = Square(10, 10)
#         a.update(11, 11, 11, 8, 39, x=16, y=23)
#         self.assertTrue(a.x == 8 and a.y == 39)

#     def test_update_no_params(self):
#         a = Square(10, 10)
#         a.update()
#         self.assertTrue(a.width == a.height == 10)

#     def test_update_all_args(self):
#         a = Square(10, 10)
#         a.update(11, 11, 11, 11, 11)
#         self.assertTrue(a.id == a.width == a.height == a.x == a.y)

#     def test_update_all_kwargs(self):
#         a = Square(10, 10)
#         a.update(id=11, width=11, height=11, x=11, y=11)
#         self.assertTrue(a.id == a.width == a.height == a.x == a.y)

#     def test_update_all_args_and_kwargs(self):
#         a = Square(10, 10)
#         a.update(12, 12, 12, 12, 12, id=11, width=11, height=11, x=11, y=11)
#         self.assertTrue(a.id == a.width == a.height == a.x == a.y == 12)


# class TestSquareToDictionary(unittest.TestCase):

#     def test_dict(self):
#         a = Square(10, 10)
#         a_dict = a.to_dictionary()
#         exp_dict = {"id": a.id, "width": 10, "height": 10,
#                     "x": 0, "y": 0}
#         self.assertTrue(a_dict == exp_dict)

#     def test_dict_with_all_values_set(self):
#         a = Square(10, 10, 20, 20, 72)
#         a_dict = a.to_dictionary()
#         exp_dict = {"id": 72, "width": 10, "height": 10,
#                     "x": 20, "y": 20}
#         self.assertTrue(a_dict == exp_dict)
