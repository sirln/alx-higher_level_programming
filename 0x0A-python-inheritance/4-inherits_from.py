#!/usr/bin/python3

'''
inherits_from function module
'''


def inherits_from(obj, a_class):
    '''
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Arguments
    ---------
    obj : object
        object to check
    a_class : class
        class to compare against

    Returns
    -------
    bool
        True if obj is an instance of a class
        that inherited (directly or indirectly)
        from the specified class;

        Otherwise False
    '''
    if (type(obj) is a_class):
        return (False)

    return (issubclass(type(obj), a_class))
