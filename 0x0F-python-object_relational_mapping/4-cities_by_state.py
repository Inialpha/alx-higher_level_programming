#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states \
                ON states.id = cities.state_id ORDER BY cities.id")
    state_row = cur.fetchall()
    for row in state_row:
        print(row)
