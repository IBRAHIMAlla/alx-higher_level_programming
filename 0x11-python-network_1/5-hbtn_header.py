#!/usr/bin/python3
"""
Sends request to given URL and display
the value of `X-Request-Id` in response header.
"""
import sys
import requests

if __name__ == "__main__":
    u = sys.argv[1]
    m = requests.get(u)
    print(m.headers.get('x-request-id'))
