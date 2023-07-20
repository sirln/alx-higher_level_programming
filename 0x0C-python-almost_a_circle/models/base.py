#!/usr/bin/python3
'''
Base Class Module
'''
import json
import csv
import turtle

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
            return ("[]")
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

        except IOError:
            return (instance_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Serialize instances to CSV and save them to a file.

        Parameters
        ----------
        list_objs : list
            list of instancesto be serialized and saved
        '''
        filename = f'{cls.__name__}.csv'
        if list_objs is None or not list_objs:
            return

        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise TypeError("Unsupported class for CSV serialization.")
                csv_writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        '''
        Deserialize instances from a CSV file.

        Returns
        -------
        list
            List of instances loaded from the file
        '''

        filename = f'{cls.__name__}.csv'
        try:
            with open(filename, 'r', newline='') as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    errormsg = "Unsupported class for CSV deserialization."
                    raise TypeError(errormsg)
                list_dicts = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        canvas = turtle.Screen()
        canvas.title(" Let's draw it")
        canvas.bgcolor('#001a33')
        #canvas.bgpic('d.gif')

        surtle = turtle.Turtle()
        surtle.speed(1)
        surtle.hideturtle()

        colors = {
                  1: '#006635',
                  2: '#660066',
                  3: '#001a33',
                  4: '#660033',
                  5: '#B399FF',
                  6: '#006635',
                  7: '#cccc00',
                  8: '#00e6e6'
            }
        for c, r in enumerate(list_rectangles, 1):
            surtle.pen(pensize=3, pencolor='#F5DEB3', fillcolor=colors[c])
            surtle.begin_fill()
            surtle.up()
            surtle.setpos(r.x, r.y)
            surtle.down()
            for num_angles in range(2):
                surtle.fd(r.width)
                surtle.left(90)
                surtle.fd(r.height)
                surtle.left(90)
            surtle.end_fill()

        for c, s in enumerate(list_squares, 4):
            surtle.pen(pensize=3, pencolor='#cccc00', fillcolor=colors[c])
            surtle.begin_fill()
            surtle.up()
            surtle.setpos(s.x, s.y)
            surtle.down()
            for num_angles in range(2):
                surtle.fd(s.width)
                surtle.left(90)
                surtle.fd(s.height)
                surtle.left(90)
            surtle.end_fill()

        canvas.exitonclick()
