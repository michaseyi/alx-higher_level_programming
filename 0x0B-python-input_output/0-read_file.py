#!/usr/bin/python3
"""Defines a function that reads text files"""


def read_file(filename=""):
    """Prints the contents of a file to the stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
