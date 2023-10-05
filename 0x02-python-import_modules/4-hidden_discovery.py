#!/usr/bin/python3
import dis
import sys


def print_names_from_module(filename):
    with open(filename, 'rb') as file:
        bytecode = file.read()
        code_obj = dis._unpack_code(bytecode)

        # Extract names from code object
        names = code_obj.co_names

        # Filter names starting with '__'
        valid_names = [name for name in names if not name.startswith('__')]

        # Print names in sorted order
        for name in sorted(valid_names):
            print(name)


if __name__ == '__main__':
    # Provide path to the compiled module as argument
    print_names_from_module('hidden_4.pyc')
