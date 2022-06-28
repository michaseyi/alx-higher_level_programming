#!/usr/bin/python3
"""This module defines a function print_square that takes in a size param

   usage
   -
   print square prints a square of size  size to the standard output with
   the character #

   print_square raises an error if size is not an integer or not greater
   than zero

   sample:

   >>> print_square(3)
   ###
   ###
   ###

   >>> print_square(-4)
   Traceback (most recent call last):
   ValueError: size must be >= 0
"""


def print_square(size):
    """
    Prints out a square with width and height size using the character # to
    the standard output

    This function will raise an error if the size param is not an integer
    greater than zero

    sample usage
    -
    >>> print_square(3)
    ###
    ###
    ###

    >>> print_square(-5)
    Traceback (most recent call last):
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#"*size)
