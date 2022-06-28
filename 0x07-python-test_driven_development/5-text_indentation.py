#!/usr/bin/python3
"""This module defines a function text_indentation that prints a text
   with 2 new lines after each of these characters: ., ? and ;

   usage
   -
   >>> text_indentation("hi.go.well.")
   hi.
   <BLANKLINE>
   go.
   <BLANKLINE>
   well.
   <BLANKLINE>

   >>> text_indentation(1)
   Traceback (most recent call last):
   TypeError: text must be a string

"""


from cgi import test


def text_indentation(text):
    """
    usage
    -
    >>> text_indentation("hi.go.well.")
    hi.
    <BLANKLINE>
    go.
    <BLANKLINE>
    well.
    <BLANKLINE>

    >>> text_indentation(1)
    Traceback (most recent call last):
    TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    start = 0

    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[start: i + 1].strip(), end="\n\n")
            start = i + 1
    print(text[start:].strip(), end="")
