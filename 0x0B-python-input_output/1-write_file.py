#!/usr/bin/python3
"""module for write_file function"""


def write_file(filename="", text=""):
    """function for writing to a file"""
    with open(filename, "w", encoding="utf8") as f:
        return f.write(text)
