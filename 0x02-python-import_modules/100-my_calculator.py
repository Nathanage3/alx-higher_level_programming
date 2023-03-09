#!/usr/bin/python3
if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    blt_op = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(blt_op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, blt_op[sys.argv[2]](a, b)))

