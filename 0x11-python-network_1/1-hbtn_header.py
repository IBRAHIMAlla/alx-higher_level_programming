#!/usr/bin/python3
"""Send request to URL and display value of `X-Request-Id`"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        h = resp.info()
        print(h.get('X-Request-Id'))
