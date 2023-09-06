#!/usr/bin/python3
alphabet = 0
for ch in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ch - alphabet)), end="")
    alphabet = 32 if alphabet == 0 else 0
