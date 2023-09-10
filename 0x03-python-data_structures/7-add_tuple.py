#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    sum_1 = a[0] + b[0]
    sum_2 = a[1] + b[1]
    result = tuple(sum_1, sum_2)
    return (result)
