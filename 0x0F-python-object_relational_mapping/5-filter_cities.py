#!/usr/bin/python3
"""This modules takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb
if __name__ == "__main__":

    host = "localhost"
    port = 3306
    username = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host=host, user=username,
                         passwd=passwd, db=dbname)

    cur = db.cursor()

    cur.execute(
        "SELECT cities.name FROM states JOIN cities ON states.id\
= cities.state_id WHERE states.name = \"{}\"".format(state_name))
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    print(", ".join(data))
