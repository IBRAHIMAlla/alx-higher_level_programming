#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the variable X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]

    m = requests.get(u)
    print(m.headers.get("X-Request-Id"))
