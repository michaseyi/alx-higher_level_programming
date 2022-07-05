#!/usr/bin/python3
"""Defines a function that returns tha JSON representation of
   an object
"""
import json


def to_json_string(my_obj):
    """
    to_json_string returns the json represntation of an objects
    """
    return json.dumps(my_obj)
