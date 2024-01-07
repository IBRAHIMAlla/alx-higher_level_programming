#!/usr/bin/python3
"""
Send a request to URL, and dispaly body of response decoded in
utf-8. Manage urllib's error exceptions.
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            b = resp.read()
            print(b.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
