#!/usr/bin/python3

# def square(a):
#    return (a * a)


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda a: a * a, row)))
    return new_matrix
