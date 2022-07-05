#!/usr/bin/python3
"""Defines a function that loads json from a file"""

import json


def load_from_json_file(filename):
    """
    load_from_json_file load a json String from a file and
    returns it
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
