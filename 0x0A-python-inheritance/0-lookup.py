#!/usr/bin/python3
"""module contains function that return the list of available attributes and methods of an object"""

def lookup(obj):
    """function that returns the list of available attributes and methods of an object
    Args: obj(object)

    Return: the list of available attributes and methods of an object"""

    return dir(obj);
