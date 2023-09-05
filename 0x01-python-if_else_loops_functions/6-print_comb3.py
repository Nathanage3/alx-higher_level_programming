#!/usr/bin/python3
for c in range(9):
    for a in range(1, 10):
        if (c > a or c == a):
            continue
        if (c != 8):
            print("{:d}{:d}".format(c, a), end=', ')
        else:
            print("{:d}{:d}".format(c, a))
