#!/usr/bin/python3
"""Use requests package to make a get request to given URL
"""
import requests


if __name__ == "__main__":
    m = requests.get('https://alx-intranet.hbtn.io/status')
    y = m.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(y), y))
