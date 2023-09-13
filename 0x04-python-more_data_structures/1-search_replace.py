#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for item in my_list:
        if item == search:
            new.append(replace)
        else:
            new.append(item)
    return new
