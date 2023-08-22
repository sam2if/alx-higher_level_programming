#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        return(fct(*args))
    except ZeroDivisionError:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
    except IndexError:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
