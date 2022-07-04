#!/usr/bin/python3
"""
Defines a base geometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        area raises an exception saying area() in not
        implemented
        """
        raise Exception("area() is not implemented")
