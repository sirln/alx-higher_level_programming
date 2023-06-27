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
        TypeError
            if argument(size) is not an integer.

        ValueError
            if argument(size) is less than 0.

        Methods
        -------
        area()
            returns the current square area
        '''
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        '''
        gets the value of the square size

        Returns
        -------
        int
            size of the square
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''
        sets the value of the square size

        Arguments
        -------
        value : int
            size of the square

        Raises
        ------
        TypeError
            if argument(value) is not an integer.

        ValueError
            if argument(value) is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''
        calculates and returns the current area of a square

        Returns
        -------
        int
            area of the square
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''
        prints the current area of a square using the '#'
        character in stdout

        if size is equal to 0, print an empty line
        '''
        if self.__size == 0:
            print()
        else:
            for s in range(self.__size):
                print('#' * self.__size)
