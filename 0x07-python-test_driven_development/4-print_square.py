#!/usr/bin/python3
'''
Square Printing Module
'''


def print_square(size):
    '''
    Prints a square of a given size using the character '#'.

    Arguments
    -------
    size : int
        square length

    Raises
    ------
    TypeError
        If size is not an integer or a float (less than 0)
    ValueError
        If size is less than 0

    '''
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError("size must be >= 0")

    for s in range(size):
        print('#' * size)
