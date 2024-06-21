#!/usr/bin/python3
"""
Return matching states
parameters given to script: username, password, database, state to match
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Ensure correct number of command-line arguments
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state name>".format(argv[0]))
        exit(1)

    # Connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Create cursor to execute queries using SQL
    cursor = db.cursor()
    try:
        # Use parameterized query to avoid SQL injection
        sql_cmd = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(sql_cmd, (argv[4],))

        # Fetch and print matching rows
        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()
