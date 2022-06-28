#!/usr/bin/python3
"""
   Module 0-add_integer defines a function add_integer that returns the sum
   of two numbers
   Raises a TypeError if the input parameters are not of type int or float.
   For example,

   >>> add_integer(100, 200)
   300
   >>> add_integer('aa', 33)
   Traceback (most recent call last):
   ...
   TypeError: a must be an integer

"""


def add_integer(a, b=98):
    """Returns the sum of a, b

        >>> add_integer(2, 4) #doctest: +NORMALIZE_WHITESPACE
        6
        >>> add_integer(100)
        198
        >>> add_integer('1', '2')
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
