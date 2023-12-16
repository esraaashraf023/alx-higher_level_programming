#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
             host='localhost', user=username,
             passwd=password, db=database, port=3306
             )

    cursor = db.cursor()

    # execute the query to select states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows..
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
