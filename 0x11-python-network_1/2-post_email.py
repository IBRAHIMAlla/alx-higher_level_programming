#!/usr/bin/python3
"""
Send POST request, and display body of response
decoded in utf-8
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    val = {'email': sys.argv[2]}
    d = parse.urlencode(val)
    d = d.encode('ascii')
    re = request.Request(sys.argv[1], data)
    with request.urlopen(re) as resp:
        b = resp.read()
        print(b.decode('utf-8'))
