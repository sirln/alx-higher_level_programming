#!/usr/bin/python3

'''
Module convert object to JSON
'''
import json


def to_json_string(my_obj):
    '''
    Converts object to its JSON representation

    Arguments
    ---------
    my_obj : object
        Object to be converted

    Return
    ------
    str
        JSON representation of the object
    '''
    return (json.dumps(my_obj))
