#!/usr/bin/python3
"""
Defines a function that generates the pascal triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle generate n number of lines of the pascal
    triangle
    """
    if n <= 0:
        return []
    res = [[]for i in range(n)]
    for line in range(1, n+1):
        c = 1
        for j in range(1, line+1):
            res[line - 1].append(c)
            c = c * (line - j) // j
    return res
