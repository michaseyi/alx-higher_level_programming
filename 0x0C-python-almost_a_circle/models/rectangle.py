#!/usr/bin/python3
"""Defines a Rectangle class"""
import sys
sys.path.append('models')
from base import Base


class Rectangle(Base):
    """Creates a rectangle object and inherits from the
       Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ initializes the rectangle object

        :param width: is the width of the rectangle
        :param height: is the height of the rectangle
        :param x(int): x
        :param y(int): y
        :param id: is the id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width is a property with both a getter and setter to the
        private __width attribute of the object
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        height is a property with both a getter and setter to the
        private __height attribute of the object
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        x is a property with both a getter and setter to the
        private __x attribute of the object
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        y is a property with both a getter and setter to the
        private __width attribute  of the object
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        area returns the area value of the Rectangle instance

        :return (number) the area of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        display prints in the stdout the Rectangle instance with the
        character #
        """
        print(('\n' * self.y) +
              ((((' ' * self.x)+("#" * self.width)) + '\n') * self.height),
              end="")

    def __str__(self):
        """
        __str__ returns a nicely formated representation of the Rectangle
         instance

        :return (str): a nicely formated representation of the Rectangle
         instance
        """
        return('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.x, self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """
        update updates the Rectangle instance

        :param args(tuple): is a tuple of all supplied parameters
        :param kwargs(dict): is a dict of key to be added to the instance
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]
            else:
                break
        if len(args) == 0:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        to_dictionary returns the dictionary representation of a Rectangle
        instance

        :return (dict): a dictionary representation of the Rectangle instance
        """
        ret = {}
        ret['x'] = self.x
        ret['y'] = self.y
        ret['id'] = self.id
        ret['height'] = self.height
        ret['width'] = self.width
        return ret

