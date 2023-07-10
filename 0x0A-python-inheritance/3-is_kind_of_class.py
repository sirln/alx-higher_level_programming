#!/usr/bin/python3

'''
is_kind_of_class function module
'''


def is_kind_of_class(obj, a_class):
    '''
    checks if object is an instance of a given class
    or
    if the object is an instance of a class that inherited from,
    the given class.

    Arguments
    ---------
    obj : object
        object to check
    a_class : class
        class to compare against

    Returns
    -------
    bool
        True if obj is an instance of specified class
        or
        if the obj is an instance of a class that inherited from,
        the given class;

        Otherwise False
    '''
    return (isinstance(obj, a_class))
