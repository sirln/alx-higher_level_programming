#!/usr/bin/python3

'''
Square class module
'''


class Square:
    '''
    Square class
    '''
    def __init__(self, size=0):
        '''
        private square instance initialization

        Arguments
        ---------
        size : int
            size of the square

        Raises
        ------
        TypeError:
            if argument(size) is not an integer.

        ValueError:
            if argument(size) is less than 0.
        '''
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
