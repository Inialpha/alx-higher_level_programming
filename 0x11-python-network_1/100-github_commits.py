#!/usr/bin/python3
"""view commits with github api"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    req = requests.get("https://api.github.com/repos/{}/{}/commits".format(
                      owner, repo))

    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get('sha'), commits[i].get(
                  'commit').get('author').get('name')))
    except IndexError:
        pass
