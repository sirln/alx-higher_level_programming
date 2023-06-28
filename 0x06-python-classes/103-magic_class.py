#!/usr/bin/python3

'''
MagicClass class module
'''
import math


class MagicClass:
    '''
    MagicClass class
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

        Methods
        -------
        area()
            returns the area of a circle
        circumference()
            returns the circumference/perimeter of a circle
        '''
        if not (type(radius) is int or type(radius) is float):
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        '''
        calculates and returns the current area of a circle

        Returns
        -------
        float
            area of a circle
        '''
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        '''
        calculates and returns the current area of a circle

        Returns
        -------
        float
            circumference of a circle
        '''
        return (math.pi * self.__radius * 2)
