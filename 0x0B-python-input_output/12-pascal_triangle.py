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
    p = []

    if n <= 0:
        return p

    for l in range(n):
        num = 11 ** l
        s = [int(n) for n in str(num)]
        p.append(s)
    return (p)
