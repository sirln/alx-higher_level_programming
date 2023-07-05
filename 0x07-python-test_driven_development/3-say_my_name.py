#!/usr/bin/python3
'''
Name Printing Module
'''


def say_my_name(first_name, last_name=""):
    '''
    Prints "My name is <first name> <last name>".

    Arguments
    -------
    first_name : str
        The first name.
    last_name : str, optional
        The last name. Defaults to an empty string.

    Raises
    ------
    TypeError
        If first_name or last_name is not a string.

    '''
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f"My name is {first_name} {last_name}")
