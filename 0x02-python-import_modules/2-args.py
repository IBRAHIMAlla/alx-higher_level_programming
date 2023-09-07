#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    digit = len(sys.argv) - 1
    if digit == 0:
        print("0 arguments.")
    elif digit == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(digit))
    for m in range(digit):
        print("{}: {}".format(m + 1, sys.argv[m + 1]))
