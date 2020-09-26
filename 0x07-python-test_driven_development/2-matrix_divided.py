#!/usr/bin/python3
""" Function that divide elements to a matrix"""


def matrix_divided(matrix, div):
    """ return new matrix with division """

    mess1 = "matrix must be a matrix (list of lists) of integers/floats"
    mess2 = "Each row of the matrix must have the same size"
    mess3 = "div must be a number"
    mess4 = "division by zero"
    if not (matrix or isinstance(matrix, list)):
        raise TypeError(mess1)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError(mess3)
    if (div == 0):
        raise ZeroDivisionError(mess4)
    for row in matrix:
        if (len(row) == 0):
            raise TypeError(mess1)
        if (len(row) != len(matrix[0])):
            raise TypeError(mess2)
        if not (row or isinstance(row, list)):
            raise TypeError(mess1)
        for col in row:
            if not (isinstance(col, int) or isinstance(col, float)):
                raise TypeError(mess1)
    new_matrix = [[round((col / div), 2) for col in row] for row in matrix]
    return (new_matrix)
