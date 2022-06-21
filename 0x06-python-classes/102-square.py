#!/usr/bin/python3
"""Contains class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the square object with the size param"""
        self.size = size

    def area(self):
        """Gets the area of the square object"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the private size member of the object
           The value param must be of type int else a TypeError will be
           raised
           The value param must be a positive integer else a ValueError will
           be raised
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __ne__(self, other):
        """Handles != comparison"""
        return self.area() != other.area()

    def __eq__(self, other):
        """Handles == comparison"""
        return self.area() == other.area()

    def __lt__(self, other):
        """Handles < comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Handles <= comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Handles > comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Handles >= comparison"""
        return self.area() >= other.area()
