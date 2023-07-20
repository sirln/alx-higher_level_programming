#!/usr/bin/python3

'''
Square class module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class, a subclass of the Rectangle class
    that inherits from Base class

    Attributes
    ----------
        Attributes inherrited from Rectangle class:
        id : int
            id number of the square.
        width : int
            Width of the square.
        height : int
            Height of the square.
        x : int
            x-coordinate of the square's position.
        y : int
            y-coordinate of the square's position.
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a Square object instance.

        Arguments
        ---------
        size : int
            Size of quare
        x : int (optional)
            x-coordinate value. Default value is 0
        y : int (optional)
            y-coordinate value. Default value is 0
        id: int (optional)
            Square id. Default is None.

        Raises
        ------
        TypeError
            if size, x, y or id is not an integer.

        ValueError
            if size is less or equal to 0.
            if x or y is less than 0.
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        Get square size

        Returns
        -------
        int
            square size
        '''
        return (self.width)

    @size.setter
    def size(self, v):
        '''
        Set square size

        Arguments
        -------
        v : int
            New square size
        '''
        self.width = v
        self.height = v

    def __str__(self):
        '''
        overloading the __str__ method

        Returns
        -------
        str
            String representation of the Square object
            in the format:
                [Square] (<id>) <x>/<y> - <width>
        '''
        return (f"[Square] ({self.id}), {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        '''
        Assigning an argument to each attribute
        '''
        if args:
            attr = ['id', 'size', 'x', 'y']
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
        Returns the dictionary representation of a Square

        Returns
        -------
        dict
            Dictionary representation of the Square object
            containing the attribute values.
        '''
        dictionary = {'id': self.id, 'size': self.width,
                      'x': self.x, 'y': self.y}
        return (dictionary)
