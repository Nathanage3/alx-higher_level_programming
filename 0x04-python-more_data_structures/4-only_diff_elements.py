#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_set = set_1.symmetric_difference(set_2)
    return diff_set
