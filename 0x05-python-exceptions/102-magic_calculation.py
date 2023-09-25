#!/usr/bin/python3
def magic_calculation(a, b):
    rslt = 0
    for m in range(1, 3):
        try:
            if m > a:
                raise Exception("Too far")
            rslt += (a ** b) / m
        except Exception:
            rslt = b + a
            break
    return rslt
