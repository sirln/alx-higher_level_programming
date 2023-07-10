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
