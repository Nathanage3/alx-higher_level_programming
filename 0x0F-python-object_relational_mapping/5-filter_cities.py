#!/usr/bin/python3

"""
A script that join cities with its states from db.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
            """
    cur.execute(query, (argv[4], ))

    rows = cur.fetchall()
    cities = []
    for city in rows:
        city = cities.append(city[0])
    print(", ".join(cities))
    cur.close()
    db.close()
