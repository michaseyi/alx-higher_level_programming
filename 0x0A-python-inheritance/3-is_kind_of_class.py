#!/usr/bin/python3
"""Defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class checks whether an object is an instance of
    or if the object is an instance of a class that inherited
    from the specified class

    :param obj(object): input object
    :param a_class(type): input class
    :return (bool): is true if the object is an instance of a
    class that inherits or is an instance of the a_class
    """
    return isinstance(obj, a_class)
