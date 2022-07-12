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

    def test_no_param(self):
        with self.assertRaises(TypeError) as e:
            Square()
        self.assertEqual(
            str(e.exception), "__init__() missing 1 \
required positional argument: 'size'")

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


class TestSquareDisplay(unittest.TestCase):

    @patch('sys.stdout', io.StringIO())
    def test_diplay(self):
        display = """\
######
######
######
######
######
######
"""
        Square(6).display()
        self.assertEqual(
            display, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_diplay_with_small_values(self):
        display = """\
##
##
"""
        Square(2).display()
        self.assertEqual(
            display, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_diplay_with_vertical_padding(self):
        display = """\


##
##
"""
        Square(2, y=2).display()
        self.assertEqual(display, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_diplay_with_horizontal_padding(self):
        display = """\
   ##
   ##
"""
        Square(2, x=3).display()
        self.assertEqual(display, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_diplay_with_both_horizontal_and_vertical_padding(self):
        display = """\


          #####
          #####
          #####
          #####
          #####
"""
        Square(5, 10, 2).display()
        self.assertEqual(display, sys.stdout.getvalue())


class TestSquareStrRepresentation(unittest.TestCase):

    @patch('sys.stdout', io.StringIO())
    def test_str_rep(self):
        print(Square(10, 5, 10, 100), end="")
        str_rep = "[Square] (100) 5/10 - 10"
        self.assertEqual(str_rep, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_str_rep_with_x_as_zero(self):
        print(Square(10, 0, 10, 100), end="")
        str_rep = "[Square] (100) 0/10 - 10"
        self.assertEqual(str_rep, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_str_rep_with_y_as_zero(self):
        print(Square(10, 5, 0, 100), end="")
        str_rep = "[Square] (100) 5/0 - 10"
        self.assertEqual(str_rep, sys.stdout.getvalue())

    @patch('sys.stdout', io.StringIO())
    def test_str_rep_with_only_width_and_height(self):
        print(Square(10), end="")
        str_rep = "[Square] ({}) 0/0 - 10".format(Square(100, 100).id - 1)
        self.assertEqual(str_rep, sys.stdout.getvalue())


class TestSquareUpdate(unittest.TestCase):

    def test_update_args_id(self):
        a = Square(10)
        a.update(11)
        self.assertEqual(a.id, 11)

    def test_update_args_size(self):
        a = Square(10)
        a.update(10, 20)
        self.assertEqual(a.size, 20)

    def test_update_args_x(self):
        a = Square(10)
        a.update(10, 10, 20)
        self.assertEqual(a.x, 20)

    def test_update_args_y(self):
        a = Square(10)
        a.update(10, 10, 10, 20)
        self.assertEqual(a.y, 20)

    def test_update_kwargs_id(self):
        a = Square(10)
        a.update(id=20)
        self.assertEqual(a.id, 20)

    def test_update_kwargs_size(self):
        a = Square(10)
        a.update(size=20)
        self.assertEqual(a.size, 20)

    def test_update_kwargs_x(self):
        a = Square(10)
        a.update(x=20)
        self.assertEqual(a.x, 20)

    def test_update_kwargs_y(self):
        a = Square(10)
        a.update(y=20)
        self.assertEqual(a.y, 20)

    def test_update_precedence_id(self):
        a = Square(10)
        a.update(14, id=15)
        self.assertEqual(a.id, 14)

    def test_update_precedence_id_size(self):
        a = Square(10)
        a.update(14, 29, id=15, size=20)
        self.assertEqual(a.id, 14)
        self.assertEqual(a.size, 29)

    def test_update_precedence_y(self):
        a = Square(10)
        a.update(11, 11, 8, 39, x=16, y=23)
        self.assertTrue(a.x == 8 and a.y == 39)

    def test_update_no_params(self):
        a = Square(10)
        a.update()
        self.assertTrue(a.size == 10)

    def test_update_all_args(self):
        a = Square(10)
        a.update(11, 11, 11, 11)
        self.assertTrue(a.id == a.size == a.x == a.y)

    def test_update_all_kwargs(self):
        a = Square(10)
        a.update(id=11, size=11, x=11, y=11)
        self.assertTrue(a.id == a.width == a.height == a.x == a.y)

    def test_update_all_args_and_kwargs(self):
        a = Square(10)
        a.update(12, 12, 12, 12, id=11, size=11, x=11, y=11)
        self.assertTrue(a.id == a.size == a.x == a.y == 12)


class TestSquareToDictionary(unittest.TestCase):

    def test_dict(self):
        a = Square(10)
        a_dict = a.to_dictionary()
        exp_dict = {"id": a.id, "size": 10,
                    "x": 0, "y": 0}
        self.assertTrue(a_dict == exp_dict)

    def test_dict_with_all_values_set(self):
        a = Square(10, 20, 20, 72)
        a_dict = a.to_dictionary()
        exp_dict = {"id": 72, "size": 10,
                    "x": 20, "y": 20}
        self.assertTrue(a_dict == exp_dict)


class TestSaveSquareToFile(unittest.TestCase):
    def test_no_param(self):
        with self.assertRaises(TypeError) as e:
            Square.save_to_file()
        self.assertEqual(str(e.exception), "save_to_file() missing 1 \
required positional argument: 'list_objs'")

    def test_empty_list(self):
        Square.save_to_file([])
        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")

    def test_one_rectangle_object(self):
        Square.save_to_file([Square(10, id=10)])
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[{"id": 10, "x": 0, "size": \
10, "y": 0}]')

    def test_multiple_rectangle_object(self):
        Square.save_to_file([Square(10, id=10),
                             Square(11, id=11)])
        with open("Square.json") as file:
            self.assertEqual(file.read(), '[{"id": 10, "x": 0, "size": \
10, "y": 0}, {"id": 11, "x": 0, "size": 11, "y": 0}]')


class TestCreateSquareObject(unittest.TestCase):

    def test_no_param(self):
        self.assertEqual(type(Square.create()), Square)
        self.assertEqual(Square.create().size, 1)

    def test_width(self):
        self.assertEqual(Square.create(size=10).size, 10)

    def test_id(self):
        self.assertEqual(Square.create(id=10).id, 10)

    def test_x(self):
        self.assertEqual(Square.create(x=10).x, 10)

    def test_y(self):
        self.assertEqual(Square.create(y=10).y, 10)

    def test_all_param(self):
        a = Square.create(size=10, id=10, x=10,
                          y=10)
        self.assertTrue(a.id == a.size == a.x ==
                        a.y == 10)

    def test_wrong_type_param(self):
        with self.assertRaises(TypeError) as e:
            Square.create(size='10')
        self.assertEqual(str(e.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as e:
            Square.create(x='10')
        self.assertEqual(str(e.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as e:
            Square.create(y='10')
        self.assertEqual(str(e.exception), 'y must be an integer')


class TestLoadFromFile(unittest.TestCase):

    def test_load_single_object(self):
        Square.save_to_file([Square(10, id=10)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 10)

    def test_load_multiple_objects(self):
        a = Square(10, id=10)
        b = Square(10, id=11)
        c = Square(10,  id=12)
        Square.save_to_file([a, b, c])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 3)
        self.assertTrue(objs[0].id == 10 and objs[1].id == 11 and
                        objs[2].id == 12)

    def test_load_empty_list(self):
        Square.save_to_file([])
        objs = Square.load_from_file()
        self.assertEqual(0, len(objs))

    def test_load_none(self):
        Square.save_to_file(None)
        objs = Square.load_from_file()
        self.assertEqual(0, len(objs))


if __name__ == "__main__":
    unittest.main()
