#!/usr/bin/python3


if __name__ == "__main__":
    """prints the numbe and list of arguments. """
    import sys

    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguements.")
    elif number == 1:
        print("1 arguement:")
    else:
        print("{} arguemnts:".format(number))
    for i in range(number):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
