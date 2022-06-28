#!/usr/bin/python3
"""This modules defines a function say_my_name that prints out
   My name is <first_name> <last_name>

   Sample:
   >>> say_my_name('Michael', 'Adewole')
   My name is Michael Adewole

   >>> say_my_name('Michael')
   My name is Michael
"""


def say_my_name(first_name, last_name=""):
    """
    Prints out My name is <first_name> <last_name>

    Raises an error if an none string value is passed as an argument

    Will work fine with one argument as the last_name by default is set to an
    empty string

    usage
    -

    >>> say_my_name('Michael', 'Adewole')
    My name is Michael Adewole

    >>> say_my_name('Michael')
    My name is Michael
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
