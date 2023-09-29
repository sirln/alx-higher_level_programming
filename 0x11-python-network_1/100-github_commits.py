#!/usr/bin/python3
'''
module to solve a challenge
'''
from sys import argv
from requests import get


if __name__ == '__main__':
    repo_name = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits'
    try:
        response = get(url)
        commits = response.json()
        for commit in commits[:10]:
            print(f'{commit["sha"]}: {commit["commit"]["author"]["name"]}')
    except Exception as error:
        print('Error: ', error)
