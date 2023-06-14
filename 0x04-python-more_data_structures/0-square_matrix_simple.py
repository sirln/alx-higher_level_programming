#!/usr/bin/python3

# def square(a):
#    return (a * a)


def square_matrix_simple(matrix=[]):
    return list(map(lambda row: list(map(lambda a: a * a, row)), matrix))
