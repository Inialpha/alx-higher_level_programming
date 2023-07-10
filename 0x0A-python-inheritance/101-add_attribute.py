#!/usr/bin/python3
"""module contain setattribue function"""


def add_attribute(obj, name, value):
    """add a new atrribute to obj"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
