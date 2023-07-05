#!/usr/bin/python3
'''
Text Indentation Module
'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after each
    occurrence of '.', '?', and ':'.

    Arguments
    -------
    text : str
        input text

    Raises
    ------
    TypeError
        If text is not string

    '''
    if type(text) is not str:
        raise TypeError('text must be a string')

    text = text.strip(' ')
    punctuation_marks = [".", "?", ":"]
    t = 0

    while (t < len(text) and text[t] == ' '):
        t += 1

    while t < len(text):
        print(text[t], end='')
        if text[t] in punctuation_marks:
            print('\n')
            while t < len(text) - 1 and text[t + 1] == ' ':
                t += 1
        t += 1
