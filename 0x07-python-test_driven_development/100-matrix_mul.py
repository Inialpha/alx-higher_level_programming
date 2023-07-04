#!/usr/bin/python3

"""module contains function for multiplying matrix"""


def matrix_mul(m_a, m_b):
    """function multiliess matrix
    Args:
        m_a(int, float)first matrix
        m_b(int, float)second matrix

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    """validste m_a"""
    for row_a in m_a:
        if not isinstance(row_a, list):
            raise TypeError("m_a must be a list of lists")
        for n in row_a:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_a must be of the same size")

    """validate m_b"""
    for row_b in m_b:
        if not isinstance(row_b, list):
            raise TypeError("m_b must be a list of lists")
        for n in row_b:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    i = 0
    for row_a in m_a:
        c_b = 0
        row_list = []
        while c_b < len(m_b):
            l_b = 0
            sm = 0
            for col_a in row_a:
                sm += (col_a * m_b[l_b][c_b])
                l_b += 1
            row_list.append(sm)
            c_b += 1
        new_matrix.append(row_list)

    return new_matrix
