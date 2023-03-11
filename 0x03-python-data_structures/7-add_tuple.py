#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    a = a[:2]
    b = b[:2]
    result = ()
    for i in range(len(a)):
        result += (a[i] + b[i],)
    return result
