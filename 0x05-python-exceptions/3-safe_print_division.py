#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        rslt = a / b
    except:
        rslt = None
    finally:
        print("Inside result: {}".format(rslt))
    return rslt
