#!/usr/bin/python3
"""Contains a Node class and a SinglyLinkedList class"""


class Node:
    """Defines a Node object with a data and next_node
       attribute
    """

    def __init__(self, data, next_node=None):
        """Initializes a Node object with the data and next_node param"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns the value of the private data attribute"""
        return self.__data

    @property
    def next_node(self):
        """Returns the value of the private next_node attribute"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Sets the value of the private data attribute
           It will raise a TypeError if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Sets the value of the private next_node attribute
           It will raise a TypeError if value is not of type Node or
           None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines the singly linked list data structure"""

    def __init__(self):
        """Initializes the singly linked list object and sets the private
           head attribute to None
        """
        self.__head = None

    def __str__(self):
        """Returns a string representation of the singly linked list data
           structure
        """
        ret = []
        current = self.__head
        while current is not None:
            ret.append(str(current.data))
            current = current.next_node
        return "\n".join(ret)

    def sorted_insert(self, value):
        """Inserts item into the singly linked list in a sorted manner
           (increasing order)
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            current = self.__head
            prev = None
            while current is not None and value >= current.data:
                prev = current
                current = current.next_node
            new_node.next_node = current
            if prev is not None:
                prev.next_node = new_node
            else:
                self.__head = new_node
