#!/usr/bin/python3
"""Containse class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square object with the size param and
           the position param
        """
        self.size = size
        self.position = position

    def area(self):
        """Gets the area of the square object"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square object"""
        return self.__size

    @property
    def position(self):
        """Returns the position of the square object"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Sets the value of the private position member of the object
           The value param must be a tuple of two positive integers else
           a TypeError will be raised
        """
        if isinstance(value, tuple) and len(value) == 2\
                and isinstance(value[0], int) and isinstance(value[1], int)\
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints out a square matirx of size size with the '#' scharacter"""
        if self.size == 0:
            print("")
        else:
            print("\n"*self.position[1], end="")
            for i in range(self.size):
                print("{}{}".format(" "*self.position[0], "#"*self.size))
