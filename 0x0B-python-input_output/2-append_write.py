#!/usr/bin/python3

'''
Module to append a string at the end of a text file
'''


def append_write(filename="", text=""):
    '''
    Method to append a string at the end of a UTF8 text file
    and returns the number of character added.

    Arguments
    ---------
    filename : file
        Name of the file to append to
    text : str
        String to append at the end of a text file

    Return
    ------
    int
        number of characters added
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars = file.write(text)
    return (num_chars)
