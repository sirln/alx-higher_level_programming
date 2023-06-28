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
        if not isinstance(size, int):
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
        return (self.size ** 2)

    def __eq__(self, other_area):
        '''
        compare square instance to answer to `==` comparator

        Arguments
        ---------
        other_area : square
            The other square instance to compare

        Returns
        -------
        bool
            True if the areas are equal, False otherwise
        '''
        return (self.area() == other_area.area())

    def __ne__(self, other_area):
        '''
        compare square instance to answer to `!=` comparator

        Arguments
        ---------
        other_area : square
            The other square instance to compare

        Returns
        -------
        bool
            True if the areas are not equal, False otherwise.
        '''
        return (self.area() != other_area.area())

    def __gt__(self, other_area):
        '''
        compare square instance to answer to `>` comparator

        Arguments
        ---------
        other_area : square
            The other square instance to compare

        Returns
        -------
        bool
            True if the first square's area is greater, False otherwise.
        '''
        return (self.area() > other_area.area())

    def __ge__(self, other_area):
        '''
        compare square instance to answer to `>=` comparator

        Arguments
        ---------
        other_area : square
            The other square instance to compare

        Returns
        -------
        bool
            True if the first square's area is greater than
            or equal, False otherwise.
        '''
        return (self.area() >= other_area.area())

    def __lt__(self, other_area):
        '''
        compare square instance to answer to `<` comparator

        Arguments
        ---------
        other_area : square
            The other square instance to compare

        Returns
        -------
        bool
            True if the first square's area is less, False otherwise.
        '''
        return (self.area() < other_area.area())

    def __le__(self, other_area):
        '''
        compare square instance to answer to `<=` comparator

        Arguments
        ---------
        other_area : square
            The other square instance to compare

        Returns
        -------
        bool
            True if the first square's area is less than
            or equal, False otherwise.
        '''
        return (self.area() <= other_area.area())
