#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        message = "Exception: {}\n".format(err.args[0])
        sys.stderr.write(message)
        return False
