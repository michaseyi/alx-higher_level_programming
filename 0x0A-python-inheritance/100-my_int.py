#!/usr/bin/python3
"""
Defines MyInt class
"""


class MyInt(int):
    """
    Defines an integer but with the == and != operator
    inverted
    """

    def __eq__(self, other):
        """
        __eq__ inverts the == operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        __ne__ inverts the != operator
        """
        return super().__eq__(other)
