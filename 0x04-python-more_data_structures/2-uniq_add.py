#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    total = 0
    for item in my_list:
        if item not in uniq:
            uniq.append(item)
            total += item
    return total
