#!/usr/bin/python3
import MySQLdb
import re
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: <username> <password> <database>")
        exit(1)

    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        port=3306,
        password=password,
        db=database
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id".format(state_name)

    cur.execute(query)

    states = cur.fetchall()

    for r in states:
        print(r)

    cur.close()
    db.close()