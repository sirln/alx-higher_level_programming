#!/usr/bin/python3

'''
Pascal Triangle Module
'''


def pascal_triangle(n):
    '''
    Generates Pascal's triangle up to the specified number of rows

    Arguments
    ---------
    n : int
        Number of rows in Pascal's triangle

    Return
    ------
    list
        A list of lists representing Pascal's triangle
    '''

    if n <= 0:
        return (pt)

    pt = [[1]]

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(pt[x - 1][y] + pt[x - 1][y-1])
        row.append(1)
        pt.append(row)
    return (pt)
