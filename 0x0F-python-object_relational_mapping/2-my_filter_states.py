#!/usr/bin/python3
"""
Filter states by user input
It takes in an argument and displays all values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2], db=argv[3])
    query = "SELECT * FROM states\
             WHERE states.name LIKE BINARY '{}'\
             ORDER BY states.id ASC".format(argv[4])
    cursor = db.cursor()
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()