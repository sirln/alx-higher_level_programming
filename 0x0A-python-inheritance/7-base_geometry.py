#!/usr/bin/python3

'''
BaseGeometry class module
'''


class BaseGeometry():
    '''
    BaseGeometry class.

    An empty class.
    '''

    def __init__(self):
        '''
        Initializing BaseGeometry class objects
        '''
        pass

    def area(self):
        '''
        calculates the area of the geometry

        Raises
        ------
        Exception
            method should be implemented in derived class
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Arguments
        ---------
        name : str
            The name of the value.
        value : int
            The value to be validated.

        Raises
        ------
        TypeError
            If the value is not an integer.
        ValueError
            If the value is less than or equal to 0.

        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
