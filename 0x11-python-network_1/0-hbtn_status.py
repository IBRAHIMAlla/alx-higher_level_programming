#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        ct = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(ct)))
        print("\t- content: {}".format(ct))
        print("\t- utf8 content: {}".format(ct.decode('utf-8')))
