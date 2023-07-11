#!/usr/bin/python3

'''
Module to write a string to a text file
'''


def write_file(filename="", text=""):
    '''
    Method to write a string to a UTF8 txt file
    and returns the number of character written.

    Arguments
    ---------
    filename : file
        Name of the file to write to
    text : str
        String to write into the file

    Return
    ------
    int
        number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return (num_chars)
