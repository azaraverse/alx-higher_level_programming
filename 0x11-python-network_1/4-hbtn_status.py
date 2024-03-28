#!/usr/bin/python3
'''a python script that fetches from given url'''

import requests


if __name__ == '__main__':
    url_link = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url_link)
    print('Body response:')
    print(f'\t- type: {type(r.text)}')
    print(f'\t- content: {r.text}')
