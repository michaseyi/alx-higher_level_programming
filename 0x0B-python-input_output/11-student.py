#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Defines a student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student object with the first_name
           last_name and age parameters
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json returns a dictionary representation of the Student
        object
        """
        if type(attrs) == list and all([isinstance(item, str) for item
                                        in attrs]):
            return {key: self.__dict__[key] for key in attrs if key in
                    self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        reload_from_json updates all the student public attribute
        in the json dictionary
        """
        for key, val in json.items():
            setattr(self, key, val)
