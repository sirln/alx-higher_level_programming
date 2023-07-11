#!/usr/bin/python3

'''
MyInt class module
'''


class MyInt(int):
    '''
    MyInt class inheriting from int class
    And inverts == and != operators
    '''

    def __eq__(self, copy):
        '''
        Overrides operator (==) to invert it

        Arguments
        ---------
        copy : object
            object to compare against

        Returns
        -------
        bool
            True if the objects are not equal;
            False otherwise.
        '''
        return (super().__ne__(copy))

    def __ne__(self, copy):
        '''
        Overrides operator (==) to invert it

        Arguments
        ---------
        copy : object
            object to compare against

        Returns
        -------
        bool
            True if the objects are equal;
            False otherwise.
        '''
        return (super().__eq__(copy))
