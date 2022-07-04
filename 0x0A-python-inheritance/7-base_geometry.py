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

    def integer_validator(self, name, value):
        """
        integer_validator validates an integer

        :param name(str): name of the value
        :param value(int): value to be validated
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
