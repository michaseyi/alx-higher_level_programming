#!/usr/bin/python3
"""This modules connects the a mysql database using the
login details proivided in the commandline and fetches
rows in the states table"""
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

    cur.execute("SELECT * FROM states")

    for row in cur.fetchall():
        print(row)
