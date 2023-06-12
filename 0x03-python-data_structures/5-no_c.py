#!/usr/bin/python3

def no_c(my_string):
    for letter in my_string:
        if (letter in "cC"):
            my_string = my_string.replace(letter, "")
    return (my_string)
