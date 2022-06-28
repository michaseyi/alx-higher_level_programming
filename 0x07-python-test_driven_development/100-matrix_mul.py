#!/usr/bin/python3
"""This module defins a function matrix_mul that takes in
   two 2-d lists and returns the mathematical multiplication
   of both lists
"""


def matrix_mul(m_a, m_b):
    """
    matrix_mul finds the mathematical multiplication of two matrixes and
    returns the result

    :param m_a([list]): is a matrix to be multiplied
    :param m_b([list]): is a matrix to be multiplied
    :return ([list]): is the mathematical multiplication of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(j, int) or isinstance(j, float) for j in i)
               for i in m_a):
        raise TypeError('m_a should contain only integers or floats')
    if not all(all(isinstance(j, int) or isinstance(j, float) for j in i)
               for i in m_b):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = []
    for i in range(len(m_a)):
        temp = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_a[i])):
                sum += m_a[i][k] * m_b[k][j]
            temp.append(sum)
        res.append(temp)
    return res
