#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        exefunc = fct(*args)
        return exefunc
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
