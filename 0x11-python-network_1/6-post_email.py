#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
and display body of response.
"""
import sys
import requests

if __name__ == "__main__":
    u = sys.argv[1]
    p = {'email': sys.argv[2]}
    m = requests.post(u, data=p)
    print(m.text)
