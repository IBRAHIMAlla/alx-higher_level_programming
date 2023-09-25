#!/usr/bin/python3
import sys


def safe_function(fct, *args):
	try:
		rslt = fct(*args)
	except Exception:
		rslt = None
		print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
	finally:
		return rslt
