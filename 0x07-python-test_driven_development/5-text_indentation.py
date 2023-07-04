#!/usr/bin/python3
"""module contaians function for indenting text"""


def text_indentation(text):
    """ a function that prints a text with 2 new
    lines after each of these characters: ., ? and :

    Args:
        text(string): text to be indented.

    Return: noting
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    space = 0
    for c in text:
        if space == 0 and c == " ":
            continue
        space = 1
        print("{}".format(c), end="")
        if c in ".?:":
            print("\n")
            space = 0
