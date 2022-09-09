#!/usr/bin/python3
"""This modules takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb
if __name__ == "__main__":

    host = "localhost"
    port = 3306
    username = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    user_input = sys.argv[4]
    db = MySQLdb.connect(host=host, user=username,
                         passwd=passwd, db=dbname)

    cur = db.cursor()

    cur.execute(
        """SELECT * FROM states WHERE BINARY\
 name = "{}" """.format(user_input))

    for row in cur.fetchall():
        print(row)
