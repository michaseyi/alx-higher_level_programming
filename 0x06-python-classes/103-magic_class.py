#!/usr/bin/python3
"""Contains a MagicClass class"""
from math import pi


class MagicClass:
    """Defines a MagicClass"""

    def __init__(self, radius=0):
        """Initializes a MagicClass object"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass_radius = radius

    def area(self):
        """Gets the area of the object"""
        return self._MagicClass_radius ** 2 * pi

    def circumference(self):
        """Gets the circumference of the object"""
        return 2 * pi * self._MagicClass_radius
