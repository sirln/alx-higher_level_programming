#!/usr/bin/python3

'''
Square class module
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Square class inheriting from Rectangle class
    that inherits from BaseGeometry class
    '''
    def __init__(self, size):
        '''
        Initializing a Square object instance.

        Arguments
        ---------
        size : int
            size of a square

        '''
        self.integer_validator('size', size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        '''
        Returns the area of a square

        Returns
        -------
        int
            Area of a Square
        '''
        return (self.__size * self.__size)

    def __str__(self):
        '''
        prints the rectangle description
        '''
        return (f"[Square] {self.__size:d}/{self.__size:d}")
