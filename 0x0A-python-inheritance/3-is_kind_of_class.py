#!/usr/bin/python3
"""module contain is_kind_of_class functoin"""


def is_kind_of_class(obj, a_class):
    """function  returns True if the object is
    an instance of, or if the object is an
    instance of a class that inherited from, the
    ispecified class otherwise False.
    Args:
        obj(oject)v an object
        a_class(class): a class

    Return: True or False
    """

    return isinstance(obj, a_class)
