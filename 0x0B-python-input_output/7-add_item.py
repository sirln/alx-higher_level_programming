#!/usr/bin/python3

'''
script module  that adds all arguments to a Python list,
and then save them to a file
'''
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    pylist = load_from_json_file(filename)
except FileNotFoundError:
    pylist = []
finally:
    for a in argv[1:]:
        pylist.append(a)
    save_to_json_file(pylist, filename)
