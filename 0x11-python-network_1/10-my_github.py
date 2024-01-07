#!/usr/bin/python3
"""
Script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    u = 'https://api.github.com/user'
    us = sys.argv[1]
    pas = sys.argv[2]
    m = get(u, auth=auth.HTTPBasicAuth(us, pas))
    print(m.json().get('id'))
