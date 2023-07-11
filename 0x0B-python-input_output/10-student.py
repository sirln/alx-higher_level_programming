#!/usr/bin/python3

'''
Student class module
'''


class Student:
    '''
    Class that defines a student
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Student object instance initialization

        Arguments
        ----------
        first_name : str
            Student first name
        last_name : str
            Student last name
        age : int
            Student age

        Methods
        -------
        to_json()
            retrieves a dictionary representation of a Student instance
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        Get a dictionary representation of the Student instance

        Returns
        -------
        dict
            A dictionary containing the attribute names
            and their corresponding values.
        '''
        return (self.__dict__)

    def to_json(self, attrs=None):
        '''
        Gets a dictionary representation of a Student instance

        Arguments
        ---------
        attrs: (list, optional)
            list of attributes to get (default is None)

        Returns
        -------
        dict
            Attribute names if attrs is a list
            Otherwise, all attributes
        '''
        if attrs is None:
            return (self.__dict__)
        elif not isinstance(attrs, list):
            return (self.__dict__)
        else:
            return ({a: getattr(self, a) for a in attrs if hasattr(self, a)})
