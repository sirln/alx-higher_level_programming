#!/usr/bin/python3

# def square(a):
#    return (a * a)


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = [a * a for a in row]
        new_matrix.append(new_row)
    return new_matrix
