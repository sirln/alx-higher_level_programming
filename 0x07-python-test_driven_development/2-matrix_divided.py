#!/usr/bin/python3
'''
Matrix Division Module
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix by a given number and returns a new matrix.

    Arguments
    -------
    matrix : list of lists
        matrix containing integers or floats.
    div : int or float
        number to divide the matrix elements by.

    Raises
    ------
    TypeError
        If matrix is not a list of lists of integers or floats
        If each row of the matrix doesn't have the same size
        If div is not a number (integer or float)
    ZeroDivisionError
        If div is equal to zero.

    Returns
    -------
    list of lists
        returns new matrix with elements divided by div.
    '''
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
