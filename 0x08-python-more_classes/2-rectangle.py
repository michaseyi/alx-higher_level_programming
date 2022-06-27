#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """Defines a Rectangle object with be width and height
       private instance attribute
    """

    def __init__(self, width=0, height=0):
        """
        __init__  Initializes a Rectangle object

        :param width (int): describes the width of the rectangle
        :param height (int): describes the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width gets the width private attribute of the rectangle object

        :return (int): the width attribute of the rectangle object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width sets the width private attrubute of the rectangle object

        :param value (int): is an integer value to be set as the width of the
         object
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        height gets the height private attribute of the rectangle object

        :return (int): the height attribute of the rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height sets the height private attrubute of the rectangle object

        :param value (int): is an integer value to be set as the height of the
         object
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def perimeter(self):
        """
        perimeter finds the perimeter of the rectangle object using the formula
        2(width + height)

        :return (int): the perimeter of the rectangle
        """
        if self.width * self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def area(self):
        """
        area finds the area of the rectangle object using the formula
        (width * height)

        :return (int): the area of the rectangle
        """
        return self.width * self.height
