#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
The results are sorted in ascending order by states.id.
"""

import sys
import MySQLdb


def list_states(username, password, database_name):
    """
    Connect to the MySQL server running on localhost at port 3306,
    retrieve all states from the specified database, and print them
    sorted in ascending order by states.id.
    
    Args:
        username (str): MySQL username
        password (str): MySQL password
        database_name (str): Database name
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    
    cur = db.cursor()
    
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()
