#!/usr/bin/python3

'''
save_to_json_file module
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Write an Objectto a text file using JSON representation

    Arguments
    ---------
    my_obj : object
        Object to be written in to a file
    filename : file
        File to write the object into

    '''
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
