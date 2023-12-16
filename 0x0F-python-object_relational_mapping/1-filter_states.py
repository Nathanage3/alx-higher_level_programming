#!/usr/bin/python3
"""
A python module that lists states from db
"""

import MySQLdb
from sys import argv
import re

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)
    db = MySQLdb.connect(host="localhost",
                        user=argv[1], password=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY states.id")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
