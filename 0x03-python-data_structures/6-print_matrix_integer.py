#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x in range(len(row)):
            if x == 0:
                print('{:d}'.format(row[x]), end='')
            else:
                print(' {:d}'.format(row[x]), end='')
        print()
