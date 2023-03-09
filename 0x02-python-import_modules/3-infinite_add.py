#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = sys.argv[1:]
    sum = 0
    for i in num:
        sum += int(i)
print(sum)
