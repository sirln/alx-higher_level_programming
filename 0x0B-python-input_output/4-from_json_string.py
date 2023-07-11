#!/usr/bin/python3

'''
Module convert object to JSON
'''
import json


def from_json_string(my_str):
    '''
    Converts JSON string to an object

    Arguments
    ---------
    my_str : str
        JSON string to be converted

    Returns
    -------
    object
        python object represented by the JSON string
    '''
    return (json.loads(my_str))
