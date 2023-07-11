#!/usr/bin/python3

'''
load_from_json_file module
'''
import json


def load_from_json_file(filename):
    '''
    Create an Object from JSON file

    Arguments
    ---------
    filename : str
       JSON file to load the object from

    Returns
    -------
    object
        Object created from the JSON file
    '''
    with open(filename) as file:
        return (json.load(file))
