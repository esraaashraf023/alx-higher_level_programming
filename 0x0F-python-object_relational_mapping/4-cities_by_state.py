#!/usr/bin/python3
"""Module to retrieve and display cities from a MySQL database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost', user=username,
        passwd=password, db=database, port=3306
    )

    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    # Execute the query..
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
