#!/usr/bin/python3
'''a python script that fetches from given url'''

import urllib.request


if __name__ == '__main__':
    url_link = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url_link) as response:
        html = response.read()
        print('Body response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("utf-8")}')
