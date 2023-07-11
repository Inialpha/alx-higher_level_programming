#!/usr/bin/python3
"""module contains pascal_triangle(n) function"""


def pascal_triangle(n):
    """returns thw pascsl triangle of n"""
    my_list = [[1]]
    if n <= 0:
        return my_list
    n_list = []
    n -= 1
    while (n):
        new_list = []
        new_list.append(1)
        for i in range(len(n_list)):
            if i < len(n_list) - 1:
                new_list.append(n_list[i] + n_list[i + 1])
        new_list.append(1)
        n_list = list(new_list)
        my_list.append(new_list)
        n -= 1
    return my_list
