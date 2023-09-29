#!/usr/bin/python3
'''
module that takes your GitHub credentials(username and password)
and uses the GitHub API to display your id
'''
from sys import argv
from requests import get


if __name__ == '__main__':
    username = argv[1]
    token = argv[2]
    url = 'https://api.github.com/user'
    try:
        response = get(url, auth=(username, token))
        print(response.json().get('id'))
    except Exception:
        print('None')
