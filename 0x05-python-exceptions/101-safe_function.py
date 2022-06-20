#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as err:
        message = "Exception: {}\n".format(err.args[0])
        sys.stderr.write(message)
        return None
