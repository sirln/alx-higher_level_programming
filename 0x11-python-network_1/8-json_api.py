#!/usr/bin/python3
'''

'''
from sys import argv
from requests import post, get


if __name__ == '__main__':
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    response = post(url, data)

    try:
        json_response = response.json()
        if json_response:
            print(f'[{json_response.get("id")}] {json_response.get("name")}')
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
