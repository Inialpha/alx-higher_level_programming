#!/usr/bin/python3

"""module that adds two integer"""

def add_integer(a, b=98):
    """ adds two integars
    Args:
        a(int, float): first argument
        b(int, float): second argument

    Return: a + b
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
