#!/usr/bin/python3

"""
A script that display what is inside db.
This script takes in 3 arguments, username, passwd, and db.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC
            """
    cur.execute(query)
    for city in cur.fetchall():
        print(city)
    cur.close()
    db.close