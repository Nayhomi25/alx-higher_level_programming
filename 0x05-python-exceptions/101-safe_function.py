#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as error:
        import sys
        print("Exceptionr {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
