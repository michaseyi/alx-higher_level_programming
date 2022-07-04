#!/usr/bin/python3
"""
Defines a square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a Square object
    """

    def __init__(self, size):
        """
        Initializes a square object

        param size(int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area gets the area of the square object

        :return (int):
        """
        return self.__size ** 2

    def __str__(self):
        """
        __str__ returns a neat representation of the square
        object as a string

        :return (str):
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
