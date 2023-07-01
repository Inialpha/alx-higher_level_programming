#!/usr/bin/python3

"""module that divides a metrix"""

def matrix_divided(matrix, div):
    """divides every data in a mayrix by div
    Args:
        div(int, float): the divisor

    Return: a new metrix containing the divided data
    """
    mlen = len(matrix)
    for row in matrix:
        if type(matrix) != list or type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in range(mlen):
        if i != mlen - 1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for row in matrix:
        r_list = []
        for num in row:
            r_list.append(round(num / div, 2))
        new_list.append(r_list)

    return new_list

"""matrix = [
    [1, 2, 3],
    [5, 2, 3],
    [4, 5, 6]
]

print(matrix_divided(matrix, 3))
print(matrix)"""
