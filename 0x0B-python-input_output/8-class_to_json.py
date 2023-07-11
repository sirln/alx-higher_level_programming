#!/usr/bin/python3

'''
class_to_json module
'''
import json


def class_to_json(obj):
    '''
    Generates a dictionary description of an object
    with simple data structure for JSON serialization.

    Arguments
    ---------
    obj : object
       Object to be serialized

    Returns
    -------
    dict
        Dictionary description of the object
    '''
    return obj.__dict__
