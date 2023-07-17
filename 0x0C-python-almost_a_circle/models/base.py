#!/usr/bin/python3
'''
Base Class Module
'''
import json


class Base:
    '''
    Base class

    Attributes
    ----------
    __nb_objects : int
        number of Base class object instances
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializing Base object instances

        Parameters
        ----------
        id : int, optional
            unique identifier for the object, by default None
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Converts a list of dictionaries to a JSON string

        Parameters
        ----------
        list_dictionaries : list of dict
            list of dictionaries to be converted to JSON

        Returns
        -------
        str
            JSON string representation of `list_dictionaries`
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes the JSON string representation of list_objs to a file.

        Parameters
        ----------
        list_objs : list
            list of instances that inherit from Base class
        '''
        filename = f'{cls.__name__}.json'

        if list_objs is None:
            list_objs = []

        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)
        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def from_json_string(cls, json_string):
        '''
        Converts a JSON string representation
        to a list of dictionaries.

        Parameters
        ----------
        json_string : str
            JSON string representation to be converted

        Returns
        -------
        list
            List of dictionaries represented by the JSON string
        '''

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Create an instance with attributes set from
        the provided dictionary.

        Parameters
        ----------
        dictionary : dict
            Dictionary with attribute names
            and their corresponding values

        Returns
        -------
        Base
            An instance of the class with attributes
            set according to the dictionary
        '''
        if cls.__name__ == 'Rectangle':
            new_instance = cls(7, 7)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = cls()

        new_instance.update(**dictionary)
        return (new_instance)

    @classmethod
    def load_from_file(cls):
        '''
        Loads instances from a JSON file.

        Returns
        -------
        list
            List of instances loaded from the file
        '''

        filename = f'{cls.__name__}.json'
        instance_list = []
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionary_list = cls.from_json_string(json_string)

            for dictionary in dictionary_list:
                instance = cls.create(**dictionary)
                instance_list.append(instance)

            return (instance_list)

        except FileNotFoundError:
            return (instance_list)
