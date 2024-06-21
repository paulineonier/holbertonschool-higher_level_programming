#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Parameters: mysql username, mysql password, database name, and state name searched
"""

import MySQLdb
import sys import argv

if __name__ == "__main__":
   
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL; match arg given
    cursor = db.cursor()
    sql_cmd = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_cmd, (argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
