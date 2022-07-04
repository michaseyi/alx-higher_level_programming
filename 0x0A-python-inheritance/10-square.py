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
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area gets the area of the square object

        :return (int):
        """
        return self.__size ** 2
