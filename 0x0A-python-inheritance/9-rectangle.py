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
        '''
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

        '''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Returns the area of a rectangle

        Returns
        -------
        int
            Area of a rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        prints the rectangle description
        '''
        return (f"[Rectangle] {self.__width:d}/{self.__height:d}")
