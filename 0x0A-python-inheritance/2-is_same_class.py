#!/usr/bin/python3

'''
is_same_class function module
'''


def is_same_class(obj, a_class):
    '''
    checks if object is an instance of a given class

    Arguments
    ---------
    obj : object
        object to check
    a_class : class
        class to compare against

    Returns
    -------
    bool
        True if obj is an instance of specified class;
        Otherwise False
    '''
    return (type(obj) is a_class)
