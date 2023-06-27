#!/usr/bin/python3

""" a class Square that defines a square"""


class Square:
    """A class Square that defines a square"""
    def __init__(self, size=0):
        """initializes class"""
        self.size = size

    @property
    def size(self):
        """retives the value of size"""
        return self.__size

    @size.setter
    def size(self, value):

        """set the value of size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value

            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """defines the area of a square"""
        return self.__size ** 2
