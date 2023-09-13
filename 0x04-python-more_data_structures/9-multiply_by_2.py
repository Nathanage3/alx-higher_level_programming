#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    alpha_order = {}
    for key, value in a_dictionary.items():
        alpha_order[key] = value * 2
    return alpha_order
