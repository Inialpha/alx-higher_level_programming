#!/usr/bin/python3
"""module contains function that returns True if
the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """function returns True if the object is
    exactly an instance of the specified class otherwise False.
    Args:
        obj(object): an object
        a_class(class): a class

    Return: True or False"""

    if type(obj) is a_class:
        return True
    else:
        return False
