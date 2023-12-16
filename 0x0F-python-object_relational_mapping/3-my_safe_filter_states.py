#!/usr/bin/python3
"""This script displays all values in the states table"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL.
    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
    )

    cursor = db.cursor()

    # Execute the query to select states matching the provided name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows..
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
