#!/usr/bin/python3

"""
Formats the value entered in an ints and tries to
handle exceptions like ValueError and TypeError
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
