import sys

def safe_function(fct, *args):
    try:
        rslt = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return rslt
