#!/usr/bin/python3
"""Contains class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the square object with the size param"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
