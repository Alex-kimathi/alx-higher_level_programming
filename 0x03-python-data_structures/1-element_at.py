#!/usr/bin/python3
""" Retrieves an element and prints the results """


def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None

    return my_list[idx]
