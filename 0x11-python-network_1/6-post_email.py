#!/usr/bin/python3
'''
module that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''
from sys import argv
from requests import post


if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}
    response = post(url, email)
    print(response.text)
