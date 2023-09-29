#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status request"""
import requests

if __name__ == '__main__':
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- conent: {}".format(req.text))
