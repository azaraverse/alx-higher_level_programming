#!/usr/bin/python3
'''a python script that takes in a URL from command line
sends a request to the URL and displays the value of the
variable X-Request-ID in the response header.
'''

import requests
import sys

if __name__ == '__main__':
    url_link = sys.argv[1]
    r = requests.get(url_link)
    if 'X-Request-ID' in r.headers:
        print(r.headers['X-Request-ID'])
