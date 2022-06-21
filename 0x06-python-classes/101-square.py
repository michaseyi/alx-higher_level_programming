#!/usr/bin/python3
"""Module Doc"""


class Square:
    """Class Doc"""

    def __init__(self, size=0, position=(0, 0)):
        """Function Doc"""
        self.size = size
        self.position = position

    def area(self):
        """Function Doc"""
        return self.__size ** 2

    @property
    def size(self):
        """Function Doc"""
        return self.__size

    @property
    def position(self):
        """Function Doc"""
        return self.__position

    @size.setter
    def size(self, value):
        """Function Doc"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Function Doc"""
        if isinstance(value, tuple) and len(value) == 2\
                and isinstance(value[0], int) and isinstance(value[1], int)\
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Function Doc"""
        if self.size == 0:
            print("")
        else:
            print("\n"*self.position[1], end="")
            for i in range(self.size):
                print("{}{}".format(" "*self.position[0], "#"*self.size))

    def __str__(self):
        """Function Doc"""
        ret = []
        if self.size == 0:
            return ""
        else:
            ret = ["" for i in range(self.position[1])]
            for i in range(self.size):
                ret.append("{}{}".format(" "*self.position[0], "#"*self.size))
        return "\n".join(ret)
