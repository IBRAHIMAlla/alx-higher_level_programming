#!/usr/bin/python3
"""
Module for log parsing scripts.
"""


import sys


if __name__ == "__main__":
    size = [0]
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(ln):
        '''Checks for match in line.'''
        try:
            ln = ln[:-1]
            w = ln.split(" ")
            size[0] += int(w[-1])
            c = int(w[-2])
            if c in codes:
                codes[c] += 1
        except ValueError:
            pass

    def print_stats():
        '''accumulated statistics.'''
        print("File size: {}".format(size[0]))
        for y in sorted(codes.keys()):
            if codes[y]:
                print("{}: {}".format(y, codes[y]))
    m = 1
    try:
        for ln in sys.stdin:
            check_match(ln)
            if m % 10 == 0:
                print_stats()
            m += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
