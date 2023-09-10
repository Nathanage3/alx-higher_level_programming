#!/usr/bin/python3
def element_at(my_list, idx):
    for arr in range(len(my_list)):
        if ((idx < 0) or (idx > len(my_list))):
            return (None)
        elif (idx == arr):
            return (my_list[arr])
