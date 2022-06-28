#!/usr/bin/python3
"""This module defies a class Locked that only the creation of a
   first_name instance attribute
"""


class LockedClass(object):
    """
    LockedClass is a class the prevents user from dyamically creating
    new instanc attribute, except if the new instance attribute is
    called first_name
    """

    __slots__ = ["first_name"]
