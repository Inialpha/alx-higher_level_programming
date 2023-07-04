#!/usr/bin/python3
"""module for printing name"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
    Args:
        first_name(string): first name
        last_name(string): last name

        Return: no return.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}" .format(first_name, last_name))
