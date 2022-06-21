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
        """Sets the size of the square object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints out a square matrix of size size with
           the '#' character
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print("#"*self.size)
