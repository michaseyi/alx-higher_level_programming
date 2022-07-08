#!/usr/bin/python3
"""Defines a Base class"""
import json


class Base:
    """Creates a Base class object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ initializes the Base object

        :param id(int): is the id of the newly created Base object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string returns the JSON string representation of a list of 
        dictionaries

        :param list_dictionaries(List[dict]): is the list of dictionaies
        :return (str): the JSON string representation of the input parameter
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file write the JSON string representation of the param list_objs
        to a file

        :param list_objs(list[Base]): is a list of objects with types that inherited
        from the Base class
        """
        data = None
        for obj in list_objs:
            if data is None:
                data = []
            data.append(obj.to_dictionary())
        data = Base.to_json_string(data)
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string returns the list of JSON string representation json_string

        :param json_string(str): is a string representing a list of dictionaries
        """

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create returns an instance with all attributes already set

        :param dictionary: 
        """
        if cls == Base:
            return
        new_obj = cls(1, 1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """
        load_from_file returns a list of instances from <cls.__name__>.json

        :return (list[Base]): is a list of instances
        """
        try:
            with open("{}.json".format(cls.__name__), encoding="utf-8") as file:
                objs = file.read()
        except FileExistsError:
            objs = []

        objs = Base.from_json_string(objs)
        objs = map(lambda obj: cls.create(**obj), objs)
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        pass

    @classmethod
    def load_from_file_csv(cls):
        pass
