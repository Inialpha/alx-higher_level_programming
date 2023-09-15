#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT DISTINCT cities.name FROM cities, states \
            WHERE cities.state_id IN \
            (SELECT DISTINCT id FROM states WHERE name = %s)", (state,))
    state_row = cur.fetchall()
    res = ""
    print(", ".join(row[0] for row in state_row))
