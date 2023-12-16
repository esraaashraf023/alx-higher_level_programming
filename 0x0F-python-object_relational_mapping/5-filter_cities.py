#!/usr/bin/python3
"""that takes in the name of a state as an argument and lists all cities"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
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

    query = """SELECT cities.name FROM cities
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 ORDER BY cities.id ASC"""
    # Execute the query..
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    cities = [row[0] for row in results]
    print(", ".join(cities))

    cursor.close()
    db.close()
