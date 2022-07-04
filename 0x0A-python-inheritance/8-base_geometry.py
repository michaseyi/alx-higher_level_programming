#!/usr/bin/python3
"""
Defines a base Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a rectangle object
    """

    def __init__(self, width, height):
        """
        __init__ initializes the rectangle object

        :param width(int): input width
        :param height(int): input height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
