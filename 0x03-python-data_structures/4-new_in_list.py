#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > len(my_list) - 1):
        return (my_list)
    else:
        _copy = my_list.copy()
        _copy[idx] = element
        return (_copy)
