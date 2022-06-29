#!/usr/bin/python3
"""This Module 2-matrix_divided defines a function matrix_divided
   that divides all the element int the matrix by the div param

   matrix_divided
   -
    >>> matrix = [
    ... [3, 5, 2],
    ... [5, 3, 6]
    ... ]

    >>> matrix_divided(matrix, 1) #doctest: +NORMALIZE_WHITESPACE
    [[3.0, 5.0, 2.0],
    [5.0, 3.0, 6.0]]

"""


def matrix_divided(matrix, div):
    """Returns a matrix with all cells divided by the div param

      Usage
      -
      -
      The matrix param should be a list of lists of integers or floats
      -
      The div param can be an integer of float but must not be zero
      -
      Raises a TypeError or ZeroDivisionError if the above condition are not
      followed

       >>> matrix = [
       ... [3, 5, 2],
       ... [5, 3, 6]
       ... ]

       >>> matrix_divided(matrix, 1) #doctest: +NORMALIZE_WHITESPACE
       [[3.0, 5.0, 2.0],
       [5.0, 3.0, 6.0]]

       >>> matrix_divided(matrix, 0) #doctest: +NORMALIZE_WHITESPACE
       Traceback (most recent call last):
       ZeroDivisionError: division by zero

       >>> matrix[0].append(1)
       >>> matrix_divided(matrix, 1)
       Traceback (most recent call last):
       TypeError: Each row of the matrix must have the same size

       >>> matrix[0] = ['2', 1, 3]
       >>> matrix_divided(matrix, 1)
       Traceback (most recent call last):
       TypeError: matrix must be a matrix (list of lists) of integers/floats

    """
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    size = None
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        if size is None:
            size = len(i)
        elif len(i) != size:
            raise TypeError('Each row of the matrix must have the same size')
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise \
                    TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    return [[float("{:.2f}".format(j/div)) for j in i] for i in matrix]
