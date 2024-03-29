#!/usr/bin/python3
'''
fetches 10 commits from recent to oldest from a github repo
'''

import requests
import sys

if __name__ == '__main__':
    url_link = ('https://api.github.com/repos/'
                + sys.argv[2] + '/' + sys.argv[1]
                + '/commits')
    r = requests.get(url_link)

    recent_commits = r.json()
    for commit in recent_commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f'{sha}: {author_name}')
