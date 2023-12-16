#!/usr/bin/python3
"""
Script to retrieve and display cities of a state from a MySQL database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
    )

    cursor = db.cursor()

    # Create the SQL
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s ORDER BY cities.id ASC"""

    # Execute the query.
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    cities = [row[0] for row in results]
    print(", ".join(cities))

    cursor.close()
    db.close()
