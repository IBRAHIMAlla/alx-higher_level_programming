#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as rs:
        ct = rs.read()
        print("Body response:")
        print("\t- type: {}".format(type(ct)))
        print("\t- content: {}".format(ct))
        print("\t- utf8 content: {}".format(ct.decode('utf-8')))
