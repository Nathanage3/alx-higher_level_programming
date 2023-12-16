#!/usr/bin/python3
import MySQLdb
from sys import argv
import re

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY states.id")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
