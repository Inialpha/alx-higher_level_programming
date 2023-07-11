#!/usr/bin/python3
"""module for append_write function"""


def append_write(filename="", text=""):
    """for appending to a file"""

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
