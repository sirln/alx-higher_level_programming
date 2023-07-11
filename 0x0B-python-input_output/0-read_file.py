#!/usr/bin/python3

'''
Module to read a file
'''


def read_file(filename=""):
    '''
    Method to read a UTF8 file and prints it to stdout

    Arguments
    -------
    filename : file
        Name of the file to read from

    '''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
