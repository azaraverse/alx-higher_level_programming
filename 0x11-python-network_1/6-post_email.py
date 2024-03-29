#!/usr/bin/python3
'''a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
'''

import requests
import sys


if __name__ == '__main__':
    url_link = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    r = requests.post(url_link, data=data)
    print(r.text)
