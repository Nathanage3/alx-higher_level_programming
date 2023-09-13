#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.keys())
    for item in sorted_dic:
        value = a_dictionary[item]
        print("{:s}: {}".format(item, value))
