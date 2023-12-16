#!/usr/bin/python3
"""Module to retrieve and display cities from a MySQL database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL..
    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
    )

    cur = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states s ON c.state_id = s.id
        ORDER BY cities.id ASC.
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
