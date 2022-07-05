#!/usr/bin/python3
"""Defines a function that converts a JSON string to a
   python object
"""
import json


def from_json_string(my_str):
    """
    from_json_string converts a JSON string to a python
    object
    """
    return json.loads(my_str)
