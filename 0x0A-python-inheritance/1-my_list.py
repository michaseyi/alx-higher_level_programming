#!/usr/bin/python3
"""
This module contains a class that inherits from the list class
with an added ``print_sorted`` function
"""


class MyList(list):
    """
    MyList inherits from the list class and adds a new
    print_sorted method
    """

    def print_sorted(self):
        """
        print_sorted prints out the list object in an sorted manner

        :return void
        """
        res = self.copy()
        res.sort()
        print(res)
