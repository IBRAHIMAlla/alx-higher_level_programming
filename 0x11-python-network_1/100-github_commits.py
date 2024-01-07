#!/usr/bin/python3
"""Sends a request to the URL and
   displays the value of a variable in the response header
"""
import sys
import requests


if __name__ == "__main__":
    u = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    m = requests.get(u)
    c = m.json()
    try:
        for t in range(10):
            print("{}: {}".format(
                c[t].get("sha"),
                c[t].get("commit").get("author").get("name")))
    except IndexError:
        pass
