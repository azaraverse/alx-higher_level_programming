#!/usr/bin/python3
'''a Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
'''

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ''

    url_link = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    r = requests.post(url_link, data=data)
    try:
        json_r = r.json()
        if json_r:
            print(f'[{json_r["id"]}] {json_r["name"]}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
