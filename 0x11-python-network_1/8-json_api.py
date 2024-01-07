#!/usr/bin/python3
"""A script that:
-Takes in a letter
- Sends POST request to http://0.0.0.0:5000/search_user
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        g = sys.argv[1]
    else:
        g = ""
    p = {'q': g}
    u = "http://0.0.0.0:5000/search_user"
    m = requests.post(u, data=p)
    try:
        m.raise_for_status()
        j = m.json()
        if len(j) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(j['id'], j['name']))
    except Exception:
        print("Not a valid JSON")
