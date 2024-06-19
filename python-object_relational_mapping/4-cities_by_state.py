#!/usr/bin/python3

"""SQL query - retrieves all cities with their states

from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def main():
    """creates SQL query"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    c = db.cursor()

    c.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id"
    )

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()


if __name__ == "__main__":
    main()
