#!/usr/bin/python3
"""7-add_item.py"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# load existing list
try:
    rslt = load_from_json_file(filename)
except Exception:
    rslt = []

rslt += sys.argv[1:]

# write new list
save_to_json_file(rslt, filename)
