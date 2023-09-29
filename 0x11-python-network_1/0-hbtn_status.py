#!/usr/bin/python3
'''
module to fetch content from a url
'''
from urllib.request import urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        output = response.read()
        print('Body response:')
        print(f'\t- type: {type(output)}')
        print(f'\t- content: {output}')
        print(f'\t- utf8 content: {output.decode("utf-8")}')
