#!/usr/bin/python3

"""SQL query - retrieves all rows from states table"""

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

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
