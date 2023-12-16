#!/usr/bin/python3
""" takes in an argument and displays all values"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
             host='localhost', user=username,
             passwd=password, db=database, port=3306
             )

    cursor = db.cursor()

    # execute the query
    query = """SELECT * FROM states
                WHERE states.name LIKE BINARY '{:s}'
                ORDER BY states.id
            """.format(sys.argv[4])
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
