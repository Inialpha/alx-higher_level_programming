#!/usr/bin/python3
"""module for append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """appends new_string after search_string"""
    with open(filename, "r", encoding="UTF-8") as f:
        new = []
        while True:
            line = f.readline()
            if line == "":
                break
            new.append(line)
            if search_string in line:
                new.append(new_string)

    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(new)
