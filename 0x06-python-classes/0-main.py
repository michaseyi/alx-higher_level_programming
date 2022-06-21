#!/usr/bin/python3
Square = __import__('0-square').Square
print(__import__('0-square').__doc__)
my_square = Square()
print(my_square.__doc__)
print(type(my_square))
print(my_square.__dict__)
