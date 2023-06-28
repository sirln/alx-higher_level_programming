#!/usr/bin/python3

'''
Square class module
'''


class Square:
    '''
    Square class
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        private square instance initialization

        Arguments
        ---------
        size : int, optional
            size of the square (default is 0)
        position : tuple, optional
            tuple of 2 positive integers (default is (0, 0))

        Raises
        ------
        TypeError
            if argument(size) is not an integer.
            if argument(position) is not a tuple of 2 positive integers.

        ValueError
            if argument(size) is less than 0.

        Methods
        -------
        size(value)
            set the size of the square
        size()
            retrives the size of the square
        area()
            returns the current square area
        my_print()
            prints the area of a square using the '#'
            character in stdout
        position()
            get square position
        position(value)
            set square position
        '''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        elif (
              not isinstance(position, tuple)
              or len(position) != 2
              or not all(isinstance(p, int) and p >= 0 for p in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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
            if argument(value) is not an integer

        ValueError
            if argument(value) is less than 0
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

    @property
    def position(self):
        '''
        gets the positin of the square

        Returns
        -------
        tuple
            the position of the square
        '''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''
        setting square position

        Arguments
        ---------
        value : tuple
            position of the square

        Raises
        ------
        TypeError
            If the value is not a tuple of 2 positive integers
        '''
        if (
              not isinstance(value, tuple)
              or len(value) != 2
              or not all(isinstance(v, int) and v >= 0 for v in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        '''
        prints the current area of a square using the '#'
        character in stdout

        if size is equal to 0, print an empty line
        '''
        if self.__size == 0:
            print()
        else:
            for p in range(self.__position[1]):
                print()
            for s in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)

    def __str__(self):
        '''
        returns a string representation of the square

        Returns
        -------
        str
            string representation of the square
        '''
        square_lines = []
        if self.__size == 0:
            return ("")

        for p in range(self.__position[1]):
            square_lines.append("\n")
        for s in range(self.__size):
            square_lines.append(" " * self.__position[0] + '#' * self.__size)
        return ("\n".join(square_lines))
