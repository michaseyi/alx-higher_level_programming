#!/usr/bin/python3
"""
This module defines a function ``inherits_from``
"""


def inherits_from(obj, a_class):
    """
    inherits_from checks if the object is an instance of a class
    that iherited (directly of indirectly) from the specified
    class

    :param obj(object): input object
    :param a_class(type): input class
    :return bool
    """
    return a_class in type(obj).__mro__[1:]
