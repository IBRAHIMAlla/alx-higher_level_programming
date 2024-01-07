#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
or error code if error.
"""
import sys
import requests

if __name__ == "__main__":
    u = sys.argv[1]
    m = requests.get(u)
    try:
        m.raise_for_status()
        print(m.text)
    except Exception as e:
        print("Error code: {}".format(m.status_code))
