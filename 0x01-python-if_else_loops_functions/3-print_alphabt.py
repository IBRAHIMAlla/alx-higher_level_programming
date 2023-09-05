#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if alphabet != ord('q') and alphabet!= ord('e'):
        print("{}".format(chr(alphabet)), end="")
