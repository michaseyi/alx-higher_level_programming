#!/usr/bin/python3
"""Defines is_same_class"""


def is_same_class(obj, a_class):
    """
    is_same_class check whether an object is an instance of
    a class

    :param obj (object): input object
    :param a_class (type): input class
    :return (bool)
    """
    if type(obj) == a_class:
        return True
    return False
