#!/usr/bin/python3
for count in range(100):
    if count == 99:
        print("{}".format(count))
    else:
        print("{:02}".format(count), end=", ")
