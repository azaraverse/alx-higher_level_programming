#!/usr/bin/python3
'''a Python script that takes in a URL, sends a request
to the URL and displays the body of the response, an error
in this instance
'''

import requests
import sys


if __name__ == '__main__':
    url_link = sys.argv[1]

    r = requests.get(url_link)
    if r.status_code >= 400:
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
