#!/usr/bin/python3
'''a python script that fetches from given url'''
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(
        'https://alx-intranet.hbtn.io/status'
    ) as response:
        html = response.read()
        print('Body Response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("utf-8")}')
