#!/usr/bin/python3
from math import pi


class MagicClass:
    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass_radius = radius

    def area(self):
        return self._MagicClass_radius ** 2 * pi

    def circumference(self):
        return 2 * pi * self._MagicClass_radius
