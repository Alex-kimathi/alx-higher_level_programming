#!/usr/bin/python3
""" Replaces an element of a list at a specific position """


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    if idx >= len(my_list):
        return my_list.copy()

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
