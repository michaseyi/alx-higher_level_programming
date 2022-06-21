#!/usr/bin/python3
"""Module Doc"""


class Square:
    """Class Doc"""

    def __init__(self, size=0):
        """Function Doc"""
        self.size = size

    def area(self):
        """Function Doc"""
        return self.__size ** 2

    @property
    def size(self):
        """Function Doc"""
        return self.__size

    @size.setter
    def size(self, value):
        """Function Doc"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __ne__(self, other):
        """Function Doc"""
        return self.area() != other.area()

    def __eq__(self, other):
        """Function Doc"""
        return self.area() == other.area()

    def __lt__(self, other):
        """Function Doc"""
        return self.area() < other.area()

    def __le__(self, other):
        """Function Doc"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Function Doc"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Function Doc"""
        return self.area() >= other.area()
