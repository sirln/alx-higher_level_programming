#!/usr/bin/python3
'''
Rectangle Class Module
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class

    A subclass of Base clase
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializing private instance attributes

        Arguments
        ---------
        width : int
            Rectacngle width
        height : int
            Rectacngle height
        x : int (optional)
            x-coordinate value. Default value is 0
        y : int (optional)
            y-coordinate value. Default value is 0
        id: int (optional)
            Rectangle id. Default is None.

        Methods
        -------
        width()
            get rectangle width
        width(v)
            set rectangle width
        height()
            get rectangle height
        height(v)
            set rectangle height
        x()
            get value of x-coordinate
        x(v)
            set value of x-coordinate
        y()
            get value of y-coordinate
        y(v)
            set value of y-coordinate
        area()
            calculate the area of a rectangle
        display()
            prints rectangle instance to stdout using `#`
        __str__()
            overriding the __str__ method
        update(*args, **kwargs)
            assigns a key/value argument to attributes
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Get width

        Returns
        -------
        int
            rectangle width
        '''
        return (self.__width)

    @width.setter
    def width(self, v):
        '''
        Set width

        Arguments
        -------
        v : int
            rectangle width

        Raises
        ------
        TypeError
            if argument(v) is not an integer.

        ValueError
            if argument(v) is less or equal to 0.
        '''
        if not isinstance(v, int):
            raise TypeError("width must be an integer")
        elif v <= 0:
            raise ValueError("width must be > 0")
        self.__width = v

    @property
    def height(self):
        '''
        Get height

        Returns
        -------
        int
            rectangle height
        '''
        return (self.__height)

    @height.setter
    def height(self, v):
        '''
        Set height

        Arguments
        -------
        v : int
            rectangle height

        Raises
        ------
        TypeError
            if argument(v) is not an integer.

        ValueError
            if argument(v) is less or equal to 0.
        '''
        if not isinstance(v, int):
            raise TypeError("height must be an integer")
        elif v <= 0:
            raise ValueError("height must be > 0")
        self.__height = v

    @property
    def x(self):
        '''
        Get x-coordinate

        Returns
        -------
        int
            value of x-coordinate
        '''
        return (self.__x)

    @x.setter
    def x(self, v):
        '''
        Set x-coordinate

        Arguments
        -------
        v : int
            value of x-coordinate

        Raises
        ------
        TypeError
            if argument(v) is not an integer.

        ValueError
            if argument(v) is less than 0.
        '''
        if not isinstance(v, int):
            raise TypeError("x must be an integer")
        elif v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        '''
        Get y-coordinate

        Returns
        -------
        int
            value of y-coordinate
        '''
        return (self.__y)

    @y.setter
    def y(self, v):
        '''
        Set y-coordinate

        Arguments
        -------
        v : int
            value of y-coordinate

        Raises
        ------
        TypeError
            if argument(v) is not an integer.

        ValueError
            if argument(v) is less than 0.
        '''
        if not isinstance(v, int):
            raise TypeError("y must be an integer")
        elif v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v

    def area(self):
        '''
        Calculate are of a rectangle

        Returns
        -------
        int
            area of a rectangle
        '''
        return (self.width * self.height)

    def display(self):
        '''
        Prints in stdout the Rectangle instance
        with the character #
        '''
        for _ in range(self.y):
            print("")
        for h in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        '''
        overriding the __str__ method

        Returns
        -------
        str
            String representation of the Rectangle object
            in the format:
                [Rectangle] (<id>) <x>/<y> - <width>/<height>
        '''
        return (
            f"[Rectangle] ({self.id}), {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        '''
        Assigning an argument to each attribute
        '''
        if args:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i, a in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], a)
                else:
                    break
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of a Rectangle

        Returns
        -------
        dict
            Dictionary representation of the Rectangle object
            containing the attribute values.
        '''
        dictionary = {'id': self.id, 'width': self.width,
                      'height': self.height, 'x': self.x,
                      'y': self.y}
        return (dictionary)
