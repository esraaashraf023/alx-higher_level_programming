#!/usr/bin/python3
"""that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to SQL database.
    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
        )

    cursor = db.cursor()

    # execute to select.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch all rows.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
