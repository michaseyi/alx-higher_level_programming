#!/usr/bin/python3
"""This modules lists all cities from the database"""
import sys
import MySQLdb
if __name__ == "__main__":

    host = "localhost"
    port = 3306
    username = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    db = MySQLdb.connect(host=host, user=username,
                         passwd=passwd, db=dbname)

    cur = db.cursor()

    cur.execute(
        "SELECT cities.id , cities.name , states.name FROM states\
JOIN cities ON states.id = cities.state_id")

    for row in cur.fetchall():
        print(row)
