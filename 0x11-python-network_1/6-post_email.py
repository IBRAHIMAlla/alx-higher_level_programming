#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
and display body of response.
"""
import requests
import sys


if __name__ == "__main__":
    m = requests.post(sys.argv[1], d={'email': sys.argv[2]})
    print(m.text)
