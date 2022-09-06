#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    qmatrix = []
    for i in matrix[:]:
        qmatrix.append(list(map(lambda x: x ** 2, i)))
    return qmatrix
