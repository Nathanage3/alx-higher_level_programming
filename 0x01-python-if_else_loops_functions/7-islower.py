#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
