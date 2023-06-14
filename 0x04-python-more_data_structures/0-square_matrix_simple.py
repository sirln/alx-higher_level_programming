#!/usr/bin/python3

def square(a):
    return (a * a)


def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda row: list(map(square, row)), matrix))
    return (new_matrix)
