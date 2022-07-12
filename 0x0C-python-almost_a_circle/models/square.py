#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square object that has attributes  of a rectangle object"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ initializes the square object and the superclass

        :param size(int): is the size of the square
        :param x(int): left indentation
        :param y(int): top indentation
        :param id: is the id of the square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ returns a nicely formated representation of the Square instance

        :return (str): a nicely formated representation of the Square instance
        """
        return('[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.width))

    @property
    def size(self):
        """
        size is a property with both a getter and setter to the
        private __height and __width attribute of the object
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """
        update updates the Square instance

        :param args(tuple): is a tuple of all supplied parameters
        :param kwargs(dict): is a dict of key to be added to the instance
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.size = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]
            else:
                break
        if len(args) == 0:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        to_dictionary returns the dictionary representation of a Square
        instance

        :return (dict): a dictionary representation of the Square instance
        """
        ret = {}
        ret['id'] = self.id
        ret['x'] = self.x
        ret['size'] = self.width
        ret['y'] = self.y
        return ret
