#!/usr/bin/python3
"""Adds all argument to a python list and saves them
   to a file
"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(items):
    """
    add_items add the input python list to the add_item.json file
    """
    try:
        data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        data = []
    data.extend(items)
    save_to_json_file(data, 'add_item.json')


if __name__ == "__main__":
    add_item(sys.argv[1:])
