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

    def __setattr__(self, name, value):
        """
        __setattr__ overides the default setattr function of this class
        to prevent the creation of instance attribute except if the 
        attribute is named first_name

        :param self(LockedClass): is the created instace object of this
        class
        :param name(str): is the name of the attribute to be set
        :param value(any): is the value of the attribute to be set
        """
        if name == "first_name":
            super.__setattr__(self, name, value)
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
