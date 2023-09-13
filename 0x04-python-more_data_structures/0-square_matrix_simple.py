#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = matrix.copy()

    for m in range(len(matrix)):
        matrix_new[m] = list(map(lambda x: x**2, matrix[m]))

    return (matrix_new)
