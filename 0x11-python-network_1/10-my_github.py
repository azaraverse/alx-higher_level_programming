#!/usr/bin/python3
'''a python script that takes in github credentials from command line
and uses the GithubAPI to display your id
'''

import requests
import sys

if __name__ == '__main__':
    url_link = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    auth = (username, token)

    r = requests.get(url_link, auth=auth)
    # check if reponse was successful (status code 200)
    if r.status_code == 200:
        print(r.json()['id'])
    else:
        print('None')
