#!/usr/bin/python3
import sys


def safe_function(fct, *args):
	try:
		rslt = fct(*args)
	except BaseException as e:
		rslt = None
		print("Exception: {}".format(e), file=sys.stderr)
	finally:
		return rslt
