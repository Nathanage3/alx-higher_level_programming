#!/usr/bin/python3
"""
A script that takes in arguments and display all values from db.
But this time mysql injection comes to work.  
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(username=argv[1],
                         passwd=argv[2], db=argv[3])
    state_name = argv[4]
    cur = db.cursor()
    query = "SELECT * FROM states WHERE states.name = %s ORDER BY states.id ASC"
    cur.execute(query, (argv[4], ))
    states = cur.fetchall()
    for r in states:
        print(r)
    cur.close()
    db.close()