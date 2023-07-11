#!/usr/bin/python3

'''
add_attribute function module
'''


def add_attribute(obj, attr_name, attr_value):
    '''
    Adds a new attribute to an object if it's possible.

    Arguments
    ---------
    obj : object
        object to add the attribute to
    attr_name: str
        name of the attribute to be added
    attr_value:
        value of the attribute to be added

    Raises
    ------
    TypeError
        If the object cannot have a new attribute.

    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
