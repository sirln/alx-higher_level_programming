#!/usr/bin/python3
'''
module that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8).
'''
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print(f'Error code: {error.code}')
