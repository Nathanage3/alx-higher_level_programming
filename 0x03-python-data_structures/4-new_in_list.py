#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > len(my_list)):
        my_list.copy()
        return (my_list)
    else:
        for i in range(len(my_list)):
            if (i == idx):
                my_list[idx] = element
                print("{:d}".format(my_list[i]))

