#!/usr/bin/python3
__import__("0-add")
from 0-add  import add
'''
Args:
    a: first integer
    b: second integer

    Returns:
  The return value.  a + b
'''
a = 1
b = 2
result_add = add(a, b)
print(f"{a} + {b} = {result_add}")
