#!/usr/bin/python3
"""Defines is_same_class"""


def is_same_class(obj, a_class):
    """
    is_same_class check whether an object is an instance of
    a class

    :obj (object): input object
    :a_class (type): input class
    :return (bool)
    """
    return isinstance(obj, a_class)
