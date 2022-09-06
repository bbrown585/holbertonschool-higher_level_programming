#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqmatrix = []
    for i in matrix[:]:
        sqmatrix.append(list(map(lambda a: a ** 2, sqmatrix)))
    return sqmatrix
