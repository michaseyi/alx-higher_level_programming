#!/usr/bin/python3
"""Module Doc"""


class Node:
    """Class Doc"""

    def __init__(self, data, next_node=None):
        """Function Doc"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Function Doc"""
        return self.__data

    @property
    def next_node(self):
        """Function Doc"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Function Doc"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Function Doc"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class Doc"""

    def __init__(self):
        """Function Doc"""
        self.__head = None

    def __str__(self):
        """Function Doc"""
        ret = []
        current = self.__head
        while current is not None:
            ret.append(str(current.data))
            current = current.next_node
        return "\n".join(ret)

    def sorted_insert(self, value):
        """Function Doc"""
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
