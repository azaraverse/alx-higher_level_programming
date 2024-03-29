#!/usr/bin/python3
'''a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
'''

import urllib.parse
import urllib.request
import sys


if __name__ == '__main__':
    url_link = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url_link, data) as response:
        print(response.read().decode('utf-8'))
