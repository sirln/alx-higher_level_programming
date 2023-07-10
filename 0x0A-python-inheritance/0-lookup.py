#!/usr/bin/python3

'''
lookup function module
'''


def lookup(obj):
    '''
    get list of available attributes and methods of an object

    Arguments
    ---------
    obj : object
        class object from which we are get the list

    Returns
    -------
    list
        the list of available attributes and methods of an object
    '''
    attributes = dir(obj)
    return (attributes)
