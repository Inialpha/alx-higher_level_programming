#!/usr/bin/python3
"""Post email"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    email = urllib.parse.urlencode(email)
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("{}".format(body.decode('utf-8')))
