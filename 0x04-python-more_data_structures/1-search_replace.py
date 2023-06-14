#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return ([replace if search == item else item for item in my_list])
