#!/usr/bin/python3
"""
Script that takes GitHub credentials
and uses the GitHub API to display the user id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    a = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    m = requests.get("https://api.github.com/user", a=a)
    print(m.json().get("id"))
