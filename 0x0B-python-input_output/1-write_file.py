#!/usr/bin/python3
"""Defines a function that write to a file"""


def write_file(filename="", text=""):
    """
    write_file write the text to the given filename and
    returns the length of the content written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
