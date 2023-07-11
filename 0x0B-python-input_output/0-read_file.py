#!/usr/bin/python3
"""module for read_file function"""


def read_file(filename=""):
    """function for reading and printing a file content"""

    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
