#!/usr/bin/python3
"""module contains class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list:"""

    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
