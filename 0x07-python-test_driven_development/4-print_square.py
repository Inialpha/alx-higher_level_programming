#!/usr/bin/python3
"""module contains function for printing square"""


def print_square(size):
    """function that prints a square with the character #.
    Args:
        size(int, size >= 0): size of the square

    Return: noting
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")
