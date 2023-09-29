#!/usr/bin/python3
'''
find_peak module
'''

def find_peak(list_of_integers):
    '''
     finds a peak in a list of unsorted integers
    '''
    if not list_of_integers:
        return None

    list_of_integers.sort()
    return list_of_integers[-1]
