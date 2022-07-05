#!/usr/bin/python3
"""
Defines a function that returns the dictionary description for JSON
serialzation
of an object
"""


def class_to_json(obj):
    """
    class_to_json returns the json representation of an object
    """
    return obj.__dict__
