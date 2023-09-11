#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for co in r:
            print("{:d}".format(co), end=" " if co != r[-1] else "")
        print()
