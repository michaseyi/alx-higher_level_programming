#!/usr/bin/python3
"""
Defines add_attribute function
"""


def add_attribute(obj, name, value):
    """
    add_attribute tries to add an attribute to an object and if
    it is not possible it raises a TypeError

    :param obj(object): object to add new attribute to
    :param name(str): name of the attribute
    :param value(object): value of the attribute
    """
    if getattr(obj, '__dict__', None) is None:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
