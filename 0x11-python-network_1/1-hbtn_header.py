#!/usr/bin/python3
'''a python script that displays the
value of X-Request-ID var from header of given url'''

import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print(response.getheader('X-Request-ID'))
