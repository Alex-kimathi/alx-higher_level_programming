#!/usr/bin/python3
""" function prints all int in reverse order """


def print_reversed_list_integer(my_list=[]):
    for num in reversed(my_list):
        print("{:d}".format(num))
