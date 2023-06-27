#!/usr/bin/python3

""" a class Square that defines a square"""


class Square:
    """A class Square that defines a square"""
    def __init__(self, size=0):
        if type(size) is int:
            if size >= 0:
                self.__size = size

            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """defines the area of a square"""
        return self.__size ** 2
