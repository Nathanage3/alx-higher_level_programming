#!/usr/bin/python3
"""
A module that lists all states from the db.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host = "localhost",
        port=3306,
        user=username,
        password = password,
        db=database
    )

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id")

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
db.close()