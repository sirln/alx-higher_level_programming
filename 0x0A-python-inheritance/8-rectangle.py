#!/usr/bin/python3

'''
Rectangle class module
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Rectangle class inheriting from BaseGeometry class
    '''
    def __init__(self, width, height):
        """
        Initializing a Rectangle instance.

        Arguments
        ---------
        width : int
            Rectangle width
        height : int
            Rectangle height

        Raises
        ------
        TypeError
            If width or height is not an integer.
        ValueError
            If width or height is less than or equal to 0.

        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
