#!/usr/bin/python3
"""
Defines a function that saves a Json string to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file save the json representation of an object
    to a file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
