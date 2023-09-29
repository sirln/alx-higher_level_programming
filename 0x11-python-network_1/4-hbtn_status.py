#!/usr/bin/python3
'''
module that fetchs content from a url
'''
from requests import get


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = get(url)
    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
