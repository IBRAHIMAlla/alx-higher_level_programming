#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    res = 0
    for m in range(len(sys.argv) - 1):
        res += int(sys.argv[m + 1])
    print("{}".format(res))
