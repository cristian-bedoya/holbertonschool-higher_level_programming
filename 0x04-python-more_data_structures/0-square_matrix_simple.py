#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def pow_2(x):
        return x ** 2
    n_matrix = matrix.copy()
    for i in range(len(matrix)):
        n_matrix[i] = list(map(pow_2, n_matrix[i]))
    return n_matrix
