#!/usr/bin/python3

'''
MagicClass class module
'''
import math


class MagicClass:
    '''
    Square class
    '''
    def __init__(self, radius=None):
        '''
        private MagicClass instance initialization

        Arguments
        ---------
        radius : int/float
            size of a circle (default radius value is None)

        Raises
        ------
        TypeError
            if argument(radius) is not an integer.
            if argument(radius) is not a float.

        ValueError
            if argument(size) is less than 0.

        Methods
        -------
        area()
            returns the area of a circle
        circumference()
            returns the circumference/perimeter of a circle
        '''
        if type(radius) is not int:
            raise TypeError('radius must be a number')
        elif type(radius) is not float:
            raise ValueError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        '''
        calculates and returns the current area of a circle

        Returns
        -------
        int/float
            area of a circle
        '''
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        '''
        calculates and returns the current area of a circle

        Returns
        -------
        int/float
            circumference of a circle
        '''
        return (math.pi * self.__radius * 2)
