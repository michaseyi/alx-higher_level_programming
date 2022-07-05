#!/usr/bin/python3
"""
Defines a function that inserts a line of text to a file, after
each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after inserts a line of text to a flie, after each line
    containing a specific string
    """
    content = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(content)
