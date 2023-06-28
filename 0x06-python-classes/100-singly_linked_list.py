#!/usr/bin/python3
"""defines the property of a LL"""


class Node:
    """defines a node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """retreives next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the value of next_node"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """descibes a singly linked list"""

    def __init__(self):
        """initializes class instance"""
        self.__head = None

    def sorted_insert(self, value):
        """insert in a sorted list"""
        node = Node(value)

        if self.__head is None:
            node.next_node = None
            self.__head = node

        elif value < self.__head.data:
            node.next_node = self.__head
            self.__head = node

        else:
            temp = self.__head
            while temp.next_node and node.data > temp.next_node.data:
                temp = temp.next_node

            node.next_node = temp.next_node
            temp.next_node = node

    def __str__(self):
        """prints the Node class"""
        value = []
        temp = self.__head
        while temp:
            value.append(str(temp.data))
            temp = temp.next_node

        return '\n'.join(value)
