#!/usr/bin/python3
'''a python script that fetches from given url'''

import requests
import sys

if __name__ == '__main__':
    url_link = sys.argv[1]
    r = requests.get(url_link)
    if 'X-Request-ID' in r.headers:
        print(r.headers['X-Request-ID'])
