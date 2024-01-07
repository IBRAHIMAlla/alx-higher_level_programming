#!/usr/bin/python3
"""
Send POST request, and display body of response
decoded in utf-8
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    val = {'email': sys.argv[2]}
    d = parse.urlencode(val)
    d = d.encode('utf-8')
    re = request.Request(sys.argv[1], d)
    with request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
