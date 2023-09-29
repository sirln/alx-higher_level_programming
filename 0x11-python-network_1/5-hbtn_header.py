#!/usr/bin/python3
'''
module that takes in a URL,
sends a request to the URL
and displays the value of the variable
X-Request-Id in the response header
'''
from sys import argv
from requests import get


if __name__ == '__main__':
    url = argv[1]
    response = get(url)
    print(response.headers.get('X-Request-Id'))
