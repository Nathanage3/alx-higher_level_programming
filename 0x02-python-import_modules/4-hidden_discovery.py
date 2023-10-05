#!/usr/bin/python3
import importlib.util


def print_names_from_module(filename):
    spec = importlib.util.spec_from_file_location('hidden_module', filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for name in dir(module):
        if not name.startswith('__'):
            print(name)


if __name__ == '__main__':
    print_names_from_module('hidden_4.pyc')
