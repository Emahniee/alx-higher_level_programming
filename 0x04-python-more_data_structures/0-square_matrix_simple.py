#!/usr/bin/python34
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda int: int ** 2, row)))
    return new_matrix
