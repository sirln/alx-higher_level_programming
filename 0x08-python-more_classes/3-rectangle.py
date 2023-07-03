#!/usr/bin/python3

'''
Rectangle class module
'''


class Rectangle:
    '''
    Rectangle class
    '''
    def __init__(self, width=0, height=0):
        '''
        Rectangle instance initialization

        Arguments
        ---------
        width : int
            width of the Rectangle
        height : int
            height of the Rectangle

        Methods
        -------
        width()
            get rectangle width
        width(value)
            set rectangle width
        height()
            get rectangle height
        height(value)
            set rectangle height
        area()
            calculate the area of a rectangle
        perimeter()
            calculate the perimater of a rectangle

        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        gets the width of the rectangle

        Returns
        -------
        int
            rectangle width
        '''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''
        sets the rectangle width

        Arguments
        -------
        value : int
            rectangle width

        Raises
        ------
        TypeError
            if argument(value) is not an integer.

        ValueError
            if argument(value) is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''
        gets the width of the rectangle

        Returns
        -------
        int
            rectangle width
        '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''
        sets the rectangle height

        Arguments
        -------
        value : int
            rectangle height

        Raises
        ------
        TypeError
            if argument(value) is not an integer.

        ValueError
            if argument(value) is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''
        calculates and returns the area of a rectangle

        Returns
        -------
        int
            area of a rectangle
        '''
        return (self.width * self.height)

    def perimeter(self):
        '''
        calculates and returns the perimeter of a rectangle

        Returns
        -------
        int
            perimeter of a rectangle
        '''
        if not self.width or not self.height:
            return (0)
        return (self.width + self.height) * 2

    def __str__(self):
        '''
        print the rectangle with the character #
        '''
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for x in range(0, self.height):
            for y in range(0, self.width):
                rectangle += "#"
            if x < self.height - 1:
                rectangle += "\n"
        return rectangle
