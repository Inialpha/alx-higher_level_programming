#!/usr/bin/python3
"""module contains lazy_matrix_mul(l function"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function multiplys two matrix
    Args:
        m_a(int, float)matrix 1
        m_b(int, fliat)matrix 2

    Return: a new matrix(m_a * m_b)
    """

    return np.matmul(m_a, m_b)
