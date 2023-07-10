#!/usr/bin/python3

'''
MyList class module
'''


class MyList(list):
    '''
    MyList class.

    A subclass of the list class.
    '''

    def print_sorted(self):
        '''
        prints a list in ascending order
        '''
        sorted_list = sorted(self)
        print(sorted_list)
