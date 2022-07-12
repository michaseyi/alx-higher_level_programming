#!/usr/bin/python3
"""Defines a Base class"""
import json
import turtle


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
        save_to_file write the JSON string representation of the param
         list_objs
        to a file

        :param list_objs(list[Base]): is a list of objects with types
         that inherited
        from the Base class
        """
        data = None
        for obj in list_objs:
            if data is None:
                data = []
            data.append(obj.to_dictionary())
        data = Base.to_json_string(data)
        with open("{}.json".format(cls.__name__), 'w',
                  encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string returns the list of JSON string representation
         json_string

        :param json_string(str): is a string representing a list of
         dictionaries
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
        load_from_file returns a list of instances from
        <cls.__name__>.json

        :return (list[Base]): is a list of instances
        """
        try:
            with open("{}.json".format(cls.__name__),
                      encoding="utf-8") as file:
                objs = file.read()
        except FileExistsError:
            return []

        objs = Base.from_json_string(objs)
        objs = list(map(lambda obj: cls.create(**obj), objs))
        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file serializes the list_objs to a CSV file

        :param list_objs(list[Base]): a list of object to be serialized
        to a CSV file
        """
        if cls == Base:
            return
        data = None
        for obj in list_objs:
            if data is None:
                data = []
            data.append(obj.to_dictionary())
        csv_string = ["id,width,height,x,y"] if cls.__name__ == "Rectangle"\
            else ["id,size,x,y"]

        if data is not None:
            for obj in data:
                temp_str = "{},{},{},{},{}".format(
                    obj['id'], obj['width'], obj['height'],
                    obj['x'], obj['y'])\
                    if cls.__name__ == "Rectangle"\
                    else "{},{},{},{}".format(
                    obj['id'], obj['size'], obj['x'], obj['y'])
                csv_string.append(temp_str)
        with open("{}.csv".format(cls.__name__), 'w',
                  encoding="utf-8") as file:
            file.write("\n".join(csv_string))

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv deserializes the CSV file of the class an returns
        a list
        of instances

        :return (list[Base]):
        """
        try:
            with open("{}.csv".format(cls.__name__),
                      encoding="utf-8") as file:
                head = None
                objs = []
                for line in file:
                    line = line.strip()
                    if head is None:
                        head = line.split(',')
                        continue
                    if len(line.split(',')) != len(head):
                        continue
                    obj = {k: int(v) for k, v in zip(head, line.split(','))}
                    objs.append(obj)
                objs = list(map(lambda obj: cls.create(**obj), objs))
                return objs
        except FileExistsError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw opens a window and draws the Rectngles and Squares

        :param list_rectangles(list[Rectangle]) is a list of Rectangle objects
        :param list_squares(list[Square]) is a list of Square objects
        """
        def draw_shape(shape):
            """
            draw_shape takes in a single shape object and draws it unto the
            screen

            :param shape(Base): is the object to be drawn to the screen
            """
            turtle.goto((shape.x, shape.y))
            turtle.clear()
            for i in range(4):
                if i % 2 == 0:
                    turtle.forward(shape.width)
                else:
                    turtle.forward(shape.height)
                turtle.left(90)
            turtle.clearscreen()
        for shape in list_rectangles:
            draw_shape(shape)
        for shape in list_squares:
            draw_shape(shape)
        turtle.exitonclick()
