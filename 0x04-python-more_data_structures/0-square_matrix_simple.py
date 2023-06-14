#!/usr/bin/python3

# def square(a):
#    return (a * a)


def square_matrix_simple(matrix=[]):
    return [[a * a for a in row] for row in matrix]
