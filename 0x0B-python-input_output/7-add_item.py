#!/usr/bin/python3
""" adds all arguments to a Python
    list, and then save them to a file:
"""
import sys
import os
save_to_json = __import__("5-save_to_json_file").save_to_json_file
load_from_json = __import__("6-load_from_json_file").load_from_json_file


def add_item(args, filename):
    if (os.path.exists(filename)):
        content = load_from_json(filename)
    else:
        content = []
    content.extend(args)
    save_to_json(content, filename)
