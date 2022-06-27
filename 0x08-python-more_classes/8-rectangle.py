#!/usr/bin/python3
"""This module defines a Rectangle class"""


class Rectangle:
    """Defines a Rectangle object with be width and height
       private instance attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        __init__  Initializes a Rectangle object

        :param width (int): describes the width of the rectangle
        :param height (int): describes the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        width gets the width private attribute of the rectangle object

        :return (int): the width attribute of the rectangle object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width sets the width private attrubute of the rectangle object

        :param value (int): is an integer value to be set as the width of the
         object
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        height gets the height private attribute of the rectangle object

        :return (int): the height attribute of the rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height sets the height private attrubute of the rectangle object

        :param value (int): is an integer value to be set as the height of the
         object
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def perimeter(self):
        """
        perimeter finds the perimeter of the rectangle object using the formula
        2(width + height)

        :return (int): the perimeter of the rectangle
        """
        if self.width * self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def area(self):
        """
        area finds the area of the rectangle object using the formula
        (width * height)

        :return (int): the area of the rectangle
        """
        return self.width * self.height

    def __str__(self):
        """
        __str__ produces a string of the characters #

        :return (str): a string representing the rectangle object
        """
        if self.width * self.height == 0:
            return ""
        rect = [str(self.print_symbol)*self.width for i in range(self.height)]
        return "\n".join(rect)

    def __repr__(self):
        """
        __repr__ produces a string representation of the rectangle that is
        able to create a new instance by using eval()

        :return (str): a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        __del__ prints the message 'Bye rectangle...' when this object is
        deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal checks rect_1 and rect_2 Rectangle objects and returns
        the one with the largest area

        :param rect_1(Rectangle): Rectangle object to be compared
        :param rect_2(Rectangle): Rectangle object to be compared
        :return (Rectangle): The Rectangle object with the largest area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
