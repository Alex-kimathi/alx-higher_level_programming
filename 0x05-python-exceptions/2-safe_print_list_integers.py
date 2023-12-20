#!/usr/bin/python3
"""
function interates through x elaments of a list
formats the values into intergers
prints the values that are only intergers
if the value is not an interger, it silently skips to the next element
"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            value = my_list[i]
            print("{:d}".format(value), end="")
            count += 1 if isinstance(value, int) else 0

    except (IndexError, ValueError):
        pass

    finally:
        print()
        return count
