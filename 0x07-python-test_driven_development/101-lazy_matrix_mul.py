#!/usr/bin/python3
"""This module defins a function matrix_mul that takes int 2-d lists
   and returns the mathematical multiplication of both lists
"""


def lazy_matrix_mul(m_a, m_b):
    """
    matrix_mul finds the mathematical multiplication of two matrixes and
    returns the result

    :param m_a([list]): is a matrix to be multiplied
    :param m_b([list]): is a matrix to be multiplied
    :return ([list]): is the mathematical multiplication of m_a and m_b
    """
    import numpy as np
    return np.matmul(m_a, m_b)
