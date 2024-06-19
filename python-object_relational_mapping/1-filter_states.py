#!/usr/bin/python3

"""SQL query - retrieves all rows from states table

limited to to names beginning with N
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
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' "
        "ORDER BY states.id"
    )

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()


if __name__ == "__main__":
    main()
