#!/usr/bin/python3
'''a Python script that takes in a URL, sends a request
to the URL and displays the body of the response, an error
in this instance
'''

from urllib.error import HTTPError
import urllib.request
import sys


if __name__ == '__main__':
    url_link = sys.argv[1]

    try:
        with urllib.request.urlopen(url_link) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
