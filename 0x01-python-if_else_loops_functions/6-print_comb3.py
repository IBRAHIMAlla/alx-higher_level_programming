#!/usr/bin/python3
for count1 in range(0, 10):
    for count2 in range(count1 + 1, 10):
        if count1 == 8 and count2 == 9:
            print("{}{}".format(count1, count2))
        else:
            print("{}{}".format(count1, count2), end=", ")
