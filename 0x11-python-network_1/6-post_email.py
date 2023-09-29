#!/usr/bin/python3
"""post request"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    res = requests.post(url, data=email)
    print(res.text)
