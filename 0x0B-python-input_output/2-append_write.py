#!/usr/bin/python3
"""Defines a function that write to a file"""


def append_file(filename="", text=""):
    """
    append_file appends the text to the given filename and
    returns the length of the content written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
