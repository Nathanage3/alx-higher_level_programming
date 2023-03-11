#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = my_list[0]
    if len(my_list) == 0:
        return None
    else:
        for number in my_list:
            if number > _max:
                _max = number
        return _max

