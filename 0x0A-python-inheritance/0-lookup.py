#!/usr/bin/python3
"""
This module define a function ``lookup`` that returns a
list of available attributes and methods of an object
"""


def lookup(obj):
    """
    lookup returns a list of available attributes and methods
    of an object

    :param obj(object): is the object to be looked up
    :return List[str]: is a list of strings
    """
    return dir(obj)
